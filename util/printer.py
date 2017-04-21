import sys
from config import config
class Printer:
    LINEBREAK_CHAR='\n'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    STATUS_MAP={
        200:'OK',
        302:'Found',
        301:'Move Permanently',
        400:'Bad Request',
        401:'Unauthorized',
        403:'Forbidden',
        404:'Not Found',
        500:'Internal Server Error',
        502:'Bad Gateway'
    }
    def __init__(self):
        self._output=sys.stdout.write

    def println_okgreen(self, content):
        self._output(self.OKGREEN + content + self.LINEBREAK_CHAR)

    def println_okblue(self, content):
        self._output(self.OKBLUE + content + self.LINEBREAK_CHAR)

    def println_header(self, content):
        self._output(self.HEADER + content + self.LINEBREAK_CHAR)

    def println_warning(self, content):
        self._output(self.WARNING + content + self.LINEBREAK_CHAR)

    def println_fail(self, content):
        self._output(self.FAIL + content + self.LINEBREAK_CHAR)

    def print_crab(self , path , status_code):


        if status_code == 200:
            STATUS_COLOR = self.OKGREEN
        elif status_code == 301 or status_code == 302:
            STATUS_COLOR = self.OKBLUE
        elif status_code in [401 , 403 , 500 ,502]:
            STATUS_COLOR = self.WARNING
        elif status_code== 404 :
            STATUS_COLOR = self.FAIL
        else:
            STATUS_COLOR = self.WARNING

        status = self.STATUS_MAP.get(status_code) or ''
        if  not config.verbose and status_code !=404:
            status_code = str(status_code)

            self._output(self.HEADER+path+STATUS_COLOR+'['+status_code+']'+status )


printer = Printer()

