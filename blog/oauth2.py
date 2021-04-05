
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .token import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credential",
        headers={'WWW-Authenticate': 'Bearer'}
    )

    verify_token(token, credential_exception)
