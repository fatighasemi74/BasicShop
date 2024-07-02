from pydantic import EmailStr
from typing import Optional
from schemas.enums import UserRole
from interfaces.iuser import IUser
from security.auth_utils import create_access_token, verify_token
from security.password_utils import hash_password, verify_password

class UserService(IUser):
    def __init__(self, db):
        self.db = db
        if 'users' not in self.db:
            self.db['users'] = {}

    async def create_user(self, first_name: str, last_name: str, email: EmailStr, role: UserRole, password: str, bio: Optional[str] = None):
        user_id = str(len(self.db['users']) + 1)
        hashed_password = hash_password(password)
        user_document = {
            'user_id': user_id,
            "first_name": first_name,
            "last_name": last_name,
            "password": hashed_password,
            "email": email,
            "email_verified": False,  
            "role": role.value,  
            "is_active": True, 
            "bio": bio
        }
        # print(create_access_token(user_document))
        self.db["users"][user_id] = user_document
        return user_id

    async def get_user_by_id(self, user_id):
        return self.db['users'].get(user_id)

    async def get_users(self):
        return list(self.db['users'].values())

    async def update_user_by_id(self, user_id, update_fields):
        if user_id in self.db['users']:
            self.db['users'][user_id].update(update_fields)
            return True
        return False

    async def delete_user_by_id(self, user_id):
        if user_id in self.db['users']:
            del self.db['users'][user_id]
            return True
        return False

    async def set_user_active_status(self, user_id, is_active: bool):
        if user_id in self.db['users']:
            self.db['users'][user_id]['is_active'] = is_active
            return True
        return False

    async def verify_user_email(self, user_id):
        if user_id in self.db['users']:
            self.db['users'][user_id]['email_verified'] = True
            return True
        return False
    
    async def authenticate_user(self, email: str, password: str):
        user = next((user for user in self.db['users'].values() if user['email'] == email) , None)
        if user and verify_password(password, user['password']):
            return user
        return None