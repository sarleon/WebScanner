import requests
import threadpool
from config import config
from multiprocessing.pool import ThreadPool
from util.printer import  printer

class Spider:

    WEB_ROOT=config.web_root



    def work(self,path):
        default_headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        }
        config.headers = config.headers or default_headers

        if config.web_root.strip()[-1] != '/':
            config.web_root=config.web_root.strip()+'/'

        task_list = config.target_list


        pool = ThreadPool(config.THREAD_NUM)
        res = pool.map(self.crab,task_list)
        results = dict(zip(task_list,res))
        return results

    @staticmethod
    def crab(path):
        url = config.web_root + path
        resp = requests.get(url=url,headers=config.headers,cookies=config.cookies)

        if not config.NO_PRINT:
            printer.print_crab(path,resp.status_code)

        if resp.status_code == 404:
            return False
        else:
            return  True



