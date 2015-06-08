class Config(object):
    SECRET_KEY = 'secret key'
    SPREADSHEET = '1ele3BSmZMKWpunF0f3L0_Eeye7ELqtbrb7W89vdtAdk'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False