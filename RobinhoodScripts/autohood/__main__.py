import sys
from login import login

def main(args = None):
    args = sys.argv[1:]
    print('count of args ::{}'.format(len(args)))

    for arg in args:
        print('passed argument ::{}'.format(arg))

    if args[0] == 'login':
        username = args[1]
        password = args[2]
        login(username, password)

if __name__ == '__main__':
    main()