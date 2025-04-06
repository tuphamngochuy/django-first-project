import bcrypt

class SecurityUtils:
    @staticmethod
    def generate_salt(length: int = 8) -> str:
        return bcrypt.gensalt(length).decode('utf-8')

    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')