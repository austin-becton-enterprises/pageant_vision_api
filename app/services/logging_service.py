LOGGING_VALUE_SUCCESS = "success"
LOGGING_VALUE_INCORRECT_PASSWORD = "password_incorrect_fail"
LOGGING_VALUE_USER_NOT_VERIFIED = "user_not_verified_fail"
LOGGING_VALUE_USER_NOT_EXIST = "user_not_exist_fail"
LOGGING_VALUE_CAPTCHA_FAIL = "captcha_fail"
LOGGING_VALUE_NO_USERNAME_FAIL = "no_username_fail"
LOGGING_VALUE_NO_PASSWORD_FAIL = "no_password_fail"

class LoggingService:

    def __init__(self, logger):
        self.logger = logger

    def login_attempt(self, auth_request, login_log: str, user_id: int = None):
        email = getattr(auth_request, "email", None)
        ip_address = getattr(auth_request, "ip_address", None)
        user_agent = getattr(auth_request, "user_agent", None)
        if self.logger:
            self.logger.info(f"Login attempt for {email}: {login_log}")
        else:
            print(f"Login attempt for {email}: {login_log}")
        from .database_service import DatabaseService
        DatabaseService.add_log(
            email=email,
            success=login_log,
            ip_address=ip_address,
            user_agent=user_agent,
            user_id=user_id
        )

    def log_success(self, auth_request, user_id: int = None):
        self.login_attempt(auth_request, LOGGING_VALUE_SUCCESS, user_id)

    def log_incorrect_password(self, auth_request, user_id: int = None):
        self.login_attempt(auth_request, LOGGING_VALUE_INCORRECT_PASSWORD, user_id)

    def log_user_not_verified(self, auth_request, user_id: int = None):
        self.login_attempt(auth_request, LOGGING_VALUE_USER_NOT_VERIFIED, user_id)

    def log_user_not_exist(self, auth_request):
        self.login_attempt(auth_request, LOGGING_VALUE_USER_NOT_EXIST, user_id=None)

    def log_no_username(self, auth_request):
        self.login_attempt(auth_request, LOGGING_VALUE_NO_USERNAME_FAIL, user_id=None)

    def log_no_password(self, auth_request):
        self.login_attempt(auth_request, LOGGING_VALUE_NO_PASSWORD_FAIL, user_id=None)

    def log_captcha_fail(self, auth_request):
        self.login_attempt(auth_request, LOGGING_VALUE_CAPTCHA_FAIL, user_id=None)