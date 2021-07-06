from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash:
    def hashPwd(password):
        hashedPwd = pwd_cxt.hash(password)
        return hashedPwd

