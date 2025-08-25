from typing import Optional
from models import AuthRequest, AuthResponse
from .logging_service import LoggingService
from .person_service import PersonService
from .error_service import NetworkingExceptions as error
from .database_service import DatabaseService
from ..models.hax_models.pv_person import PVPerson
import logging

class AuthService:

    def __init__(self):
        self.person_service = PersonService()
        self.logging_service = LoggingService(logger=None)  # Pass actual logger if available

    #######################
    # Login Process
    #######################
    async def authenticate_user(self, auth_request: AuthRequest) -> AuthResponse:

    ##    #STEP 1 - Validate has required fields
        if not auth_request.email or not auth_request.password:
            if not auth_request.email:
                self.logging_service.log_no_username(auth_request)
            elif not auth_request.password:
                self.logging_service.log_no_password(auth_request)
            raise error.bad_credentials()
            #reCAPTCHA token - come back later for that
            #LOGGING_VALUE_CAPTCHA_FAIL

    ##    #STEP 2 - Get user from database
        matched_user_object = DatabaseService.get_user(with_email=auth_request.email)
        matched_person = PVPerson.fromUserModel(matched_user_object)
        logging.debug(f"matched_user_object: {matched_user_object}")
        logging.debug(f"matched_person: {matched_person}")
        logging.debug(f"matched_person.user_id(): {matched_person.user_id() if matched_person else None}")
        if not matched_person:
            self.logging_service.log_user_not_exist(auth_request)
            raise error.bad_credentials()
        
    ##    #STEP 3 - Validate user password and verified status
        if not matched_person.is_verified():
            self.logging_service.log_user_not_verified(auth_request, user_id=matched_person.user_id() if matched_person else None)
            raise error.account_not_verified()
        attempted_pw = auth_request.password
        hashed_pw = matched_user_object.password
        if not self.password_is_valid(attempted_pw, hashed_pw):
            self.logging_service.log_incorrect_password(auth_request, user_id=matched_person.user_id() if matched_person else None)
            raise error.bad_credentials()
        
    ##    #STEP 4 - Create JWT auth Token + increment session version
        from .jwt_service import JWTService as token_service
        new_token = await token_service.create_auth_token(matched_person.email(), expires_delta_seconds=3600)
        user_id = matched_person.user_id()
        if user_id is None:
            logging.error(f"User ID is None for matched_person: {matched_person}")
            raise error.bad_credentials()
        matched_person = DatabaseService.update_session_version_and_token(user_id=user_id, token=new_token)
        matched_person = PVPerson.fromUserModel(matched_person)
    ##    #STEP 5 - Log auth/login event
        self.logging_service.log_success(auth_request, user_id=matched_person.user_id() if matched_person else None)
        return AuthResponse(access_token=new_token, email=matched_person.email())  # Return the JWT token instead of the user object

    #######################
    # Helper Functions
    #######################
    def password_is_valid(self, plain_password: str, hashed_password_from_db: str) -> bool:
        import bcrypt
        #Verifies a plain password against a PHP bcrypt hash from the database.
        # bcrypt requires bytes
        if isinstance(plain_password, str):
            plain_password = plain_password.encode('utf-8')
        if isinstance(hashed_password_from_db, str):
            hashed_password_from_db = hashed_password_from_db.encode('utf-8')
        return bcrypt.checkpw(plain_password, hashed_password_from_db)


    #######################
    # NON-LOGIN FUNCTIONS
    #######################
    @staticmethod
    def validate_token_and_return_user(email: str, token: str) -> PVPerson:
        matched_user_object = DatabaseService.get_user(with_email=email)
        # Validates the JWT token and returns the user email (sub)
        from .jwt_service import JWTService
        if JWTService.verify_auth_token(token, expected_username=email):
            return PVPerson.fromUserModel(matched_user_object)
        else:
            raise error.invalid_token()

    def logout():
        #client calls this on logout 
        #bump session version?
        pass