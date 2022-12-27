from fastapi import Depends, HTTPException
from starlette import status


from app.models import AuthToken, connect_db


def check_auth_token(token: str, db=Depends(connect_db)):
    auth_token = db.query(AuthToken).filter(AuthToken.token == token).one_or_none()
    if auth_token:
        return auth_token

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Auth is failed'
    )