import sys
import re

def unpack_files():
    marker = '::::::::::textpak=>(.*)'
    for line in sys.stdin:
        m = re.match(marker, line)
        if m:
            filename = m.group(1)
            print(f'Creating {filename}')
            with open(filename, 'w') as f:
                f.write(next(sys.stdin))
                for line in sys.stdin:
                    f.write(line)

if __name__ == '__main__':
    unpack_files()