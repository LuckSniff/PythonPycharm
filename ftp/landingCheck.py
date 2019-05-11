import hashlib
import configparser
from ftp import FactoryLogging

logging = FactoryLogging.factoryLogging().getLogging()

def getConfigParser(filePath):
    config = configparser.ConfigParser()
    config.read(filePath)
    return config

def getPasswordMd5(password):
    md5 = hashlib.md5(bytes('salt', encoding='utf-8'))
    if ( not isinstance(password,bytes) ):
        password = bytes(password, encoding='utf-8')
    md5.update(password)
    return md5.hexdigest()

def passwordCheck(user,password):
    configparser = getConfigParser('password.conf')
    passwordMd5 = getPasswordMd5(password)
    try:
        userPassword = configparser.get(user,'password')
    except Exception:
        logging.debug('user is not correct')
        return False
    else:
        if( userPassword==passwordMd5):
            return True
        logging.debug('password is not correct')
        return False

if __name__ == '__main__':
    print(passwordCheck('zha','a'))




