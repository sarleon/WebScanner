from core.argparse import parse_argument
from core.dictionary_reader import  parse_dict
from core.spider import Spider

def main():
    parse_argument()
    spider = Spider()
    parse_dict()
    spider.work()


if __name__ == '__main__':
    main()