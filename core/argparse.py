import optparse
from config import config

def parse_argument():
    '''
    command line option parser
    '''

    option_parser = optparse.OptionParser()

    option_parser.usage = \
        """
        search_register.py -e [email] [options]
        search_register.py -c [cellphone] [options]"""

    option_parser.add_option('-u', '--url', dest='url', action='store', default=None)
    option_parser.add_option('-d', '--dictionary', dest='dictionary', action='store', default=None, help="list of dictionary name use comma to seperate")
    option_parser.add_option('-l', '--list-dictionary', dest='list', action='store', default=1, help="")
    option_parser.add_option('-t', '--threads', dest='threads', action='store', type='int',default=10, help="")
    option_parser.add_option('-v','--verbose',dest='verbose',action='store_true',help='output all the infomation')

    """
    parse options
    """
    (options, args) = option_parser.parse_args()



    """
    set thread
    """
    config.THREAD_NUM=options.threads


    """
    set webroot
    """
    if not (options.url[0:7]=='http://' or options.url[0:8]=='https://'):
        config.WEB_ROOT='http://' + options.url
    else:
        config.WEB_ROOT=options.url


    """
    set dictionary
    """
    if options.dictionary is not None:
        config.dictionary=options.dictionary.split(',')
        config.dictionary.extend(['ctf','common_location','common_directory'])
    else:
        config.dictionary=['ctf','common_location','common_directory']


    """
    set verbose
    """
    if options.verbose:
        config.verbose=True

