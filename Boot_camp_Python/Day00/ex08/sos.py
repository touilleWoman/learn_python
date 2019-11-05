import sys

def convert(str):
    str = str.upper()
    d = {
        'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-·· ', 'E': '·',
        'F':'··-·', 'G': '--·','H': '····', 'I': '··', 'J': '·---',
        'K': '-·- ', 'L': '·-··', 'M': '--', 'N': '-·', 'O': '---',
        'P': '·--·', 'Q': '--·-', 'R': '·-· ', 'S': '···', 'T': '-',
        'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--',
        'Z': '--··',
        '1': '·----', '2': '··---', '3': '···--', '4': '····-',
        '5': '·····', '6': '-····', '7':  '--···', '8': '---··',
        '9': '----·', '0': '-----'
    }
    for c in str:
        if c == ' ':
            print('/ ', end='')
        elif c in d:
            print(d[c]+' ', end='')


def check_arg():
    if len(sys.argv) >= 2:
        str = ' '.join(sys.argv[1:])
        for x in str:
            if not (x.isspace() or x.isalnum()):
                print("ERROR")
                exit()
        convert(str)


if __name__ == '__main__':
    check_arg()