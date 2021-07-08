from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash():
    def bcrypt(password):
        hashedPwd = pwd_cxt.hash(password)
        return hashedPwd

    def verifyPwd(hashedPwd , plainPwd):
        return pwd_cxt.verify(plainPwd , hashedPwd)

