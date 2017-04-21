import requests
import threadpool
from config import config
from util.printer import  printer

class Spider:

    WEB_ROOT=config.web_root



    def work(self,path):
        default_headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        }
        headers = config.headers or default_headers
        cookies = config.cookies

        web_root = config.web_root
        if web_root.strip()[-1] != '/':
            web_root=web_root.strip()+'/'

        task_list = config.target_list
        results = {}

        pool = threadpool.ThreadPool(config.THREAD_NUM)
        # reqs = pool.

    @staticmethod
    def crab(web_root,path,headers,cookies):
        url = web_root + path
        resp = requests.get(url=url,headers=headers,cookies=cookies)

        if not config.NO_PRINT:
            prine



