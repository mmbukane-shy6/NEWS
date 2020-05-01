import os

class Config:
    '''
    General configuration class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    

class ProdConfig(Config):
    '''
    Production  configuration class
    '''   

    pass 

class DevConfig(Config):
    '''
    Development  configuration class
    '''    

    DEBUG = True

config_options = {
    'production' : ProdConfig,
    'development' : DevConfig
}