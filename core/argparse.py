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

    option_parser.add_option('-e', '--email', dest='email', action='store', default=None)
    option_parser.add_option('-c', '--cellphone', dest='cellphone', action='store', default=None)
    option_parser.add_option('-t', '--thread', dest='thread', action='store', default=1, help="")

    """
    parse options
    """
    (options, args) = option_parser.parse_args()


    """
    specific the search type (email or cellphone)
    """

