from passlib.hash import bcrypt


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)
    
    @classmethod
    def hashed_password(cls, password: str) -> str:
        return bcrypt.hash(password)
