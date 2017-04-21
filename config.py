import os

class Config:

    web_root=''
    verbose = False
    project_dir = os.path.dirname(os.path.abspath(__file__))
    dictionary_dir='dictionarys'




class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass