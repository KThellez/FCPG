import secrets
key = secrets.token_hex(16)


class Config:
    SECRET_KEY = key

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='pronosticos'

config={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
