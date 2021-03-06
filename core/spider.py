import requests
from config import config
from multiprocessing.pool import ThreadPool
from util.printer import  printer
from util.content import  parse_robots_txt,parse_res
import urllib3
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

class Spider:

    WEB_ROOT=config.WEB_ROOT




    def work(self):
        default_headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        }
        config.headers = config.headers or default_headers


        """
        add slash (dir seperator) to the url
        """
        if config.WEB_ROOT.strip()[-1] != config.DIR_SEPERATOR:
            config.WEB_ROOT=config.WEB_ROOT.strip()+config.DIR_SEPERATOR
        else:
            config.WEB_ROOT = config.WEB_ROOT.strip()
        task_list = config.target_list
        second_list = []

        """
        crab the robots.txt
        """
        robots_txt_content= self.crab("robots.txt",ret="content")
        robots_txt_content_list =  parse_robots_txt(robots_txt_content)

        if robots_txt_content_list :
            task_list = list(set(task_list+robots_txt_content_list))

        """
        do the first time  crab work
        """
        pool = ThreadPool(config.THREAD_NUM)
        res = pool.map(self.crab,task_list)
        res = filter(lambda x:x!=False,res)
        for i in map(parse_res,list(res)):
            second_list+=i

        res2 = pool.map(self.crab, second_list)
        results = dict(zip(task_list,res+res2))

        return results

    @staticmethod
    def crab(path,ret=None):
        url = config.WEB_ROOT + path
        resp = requests.get(url=url,headers=config.headers,cookies=config.cookies,verify=False)

        if not config.NO_PRINT:
            printer.print_crab(path+" [Size]:"+str(len(resp.text)),resp.status_code)



        if resp.status_code == 404:
            return False
        else:
            if ret == "content":
                return resp.content
            else:
                return  path



