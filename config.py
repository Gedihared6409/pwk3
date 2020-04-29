import os

class Config:
    '''
    General configuration parent class
    '''
    
    SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):

    pass


class DevConfig(Config):


    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}