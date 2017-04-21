import os




class Config:


    THREAD_NUM=20
    WEB_ROOT= ''
    target_list=[]
    cookies = {}
    headers = None
    verbose = False
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
    DICTIONARY_DIR= 'dictionarys'
    NO_PRINT = False
    dictionary= []
    DIR_SEPERATOR='/'



class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config=Config()