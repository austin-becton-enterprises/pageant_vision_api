from fastapi import APIRouter, HTTPException, status

class NetworkingExceptions:
    
    def bad_credentials() -> HTTPException:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    def account_not_verified() -> HTTPException:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account not verified: Please check your email for verification instructions.",
            headers={"WWW-Authenticate": "Bearer"},
        )