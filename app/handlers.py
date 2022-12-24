from fastapi import APIRouter, Body, Depends
import uuid


from app.forms import UserLoginForm
from app.models import connect_db, User, AuthToken
from app.utils import get_password_hash


router = APIRouter()


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), db=Depends(connect_db)):
    user = db.query(User).filter(User.email == user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {'error': 'Email/password invalid!'}

    auth_token = AuthToken(token=str(uuid.uuid4()), user_id=user.id)
    db.add(auth_token)
    db.commit()
    return {'status': 'OK'}


#def create_user(user: UserCreateForm = Body(..., embed=True), db=Depends(connect_db)):
