class __colors__:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def __useColor__(s: str, color: __colors__) -> str:
    return '{}{}{}'.format(color, s, __colors__.END)

def green(s: str):
    return __useColor__(s, __colors__.GREEN)

def red(s: str):
    return __useColor__(s, __colors__.RED)

