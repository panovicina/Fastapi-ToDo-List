from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import Token
from app.services.auth import create_access_token
from app.services.users import UserService

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
async def login(userdetails: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.get_by_username(userdetails.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The User Does not exist",
        )

    # if not utils.verify_password(userdetails.password, user.password):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="The Passwords do not match")

    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
