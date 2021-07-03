# Performing google search using Python code
import sys


class Gsearch_python:
    def __init__(self, name_search,
                 start: int = None, stop: int = 10,
                 pause: int = 2, tld_search='co.in', num: int = 10):
        self.name = name_search
        self.tld = tld_search
        self.num = num
        self.start = start
        self.stop = stop
        self.pause = pause

    def Gsearch(self):
        count = 0
        try:
            from googlesearch import search
        except ImportError:
            print("No Module named 'google' Found")
        for i in search(query=self.name,
                        tld=self.tld, lang='en',
                        num=self.num, stop=self.stop, pause=self.pause):
            count += 1
            print(count)
            print(i + '\n')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        args = sys.argv[1:]
        gs = Gsearch_python(args[0])
        gs.Gsearch()
    else:
        print('Need a search query.')
