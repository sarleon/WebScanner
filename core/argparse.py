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
    option_parser.add_option('-d', '--dictionary', dest='thread', action='store', default=None, help="")
    option_parser.add_option('-l', '--list-dictionary', dest='thread', action='store', default=1, help="")
    option_parser.add_option('-t', '--threads', dest='threads', action='store', type='int',default=1, help="")

    """
    parse options
    """
    (options, args) = option_parser.parse_args()


    """
    specific the search type (email or cellphone)
    """

