import requests
import threadpool
from config import config


class Spider:

    WEB_ROOT=config.web_root



    def work(self,path):
        default_headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        }
        headers = config.headers or default_headers
        cookies = config.cookies

        url = config.web_root
        if url.strip()[-1] != '/':
            url=url.strip()+'/'

        task_list = config.target_list
        results = {}

        pool = threadpool.ThreadPool(config.THREAD_NUM)
        # reqs = pool.

    @staticmethod
    def crab(url,headers,cookies):
        resp = requests.get(url=url,headers=headers,cookies=cookies)



        if not config.NO_PRINT:



