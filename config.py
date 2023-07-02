import secrets
key = secrets.token_hex(16)


class Config:
    SECRET_KEY = key

class DevelopmentConfig(Config):
    DEBUG=True

config={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}