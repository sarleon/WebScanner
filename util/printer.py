import sys
class Printer:
    LINEBREAK_CHAR='\n'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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



