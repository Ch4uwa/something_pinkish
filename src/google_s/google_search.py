# Performing google search using Python code
import os
import time

from arg import use_args

try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' Found")


class Gsearch_python:
    def __init__(
            self, name_search: str,
            start: int, stop: int,
            pause: float, num: int, tld_search: str,
            output_file: bool):
        self.name = name_search
        self.tld = tld_search
        self.num = num
        self.start = start
        self.stop = stop
        self.pause = pause

        self.output_file = output_file
        self.date = time.strftime('%Y-%m-%d', time.localtime())
        self.filename = "-".join(self.name.split()) + "-" + self.date + '.csv'

    def Gsearch(self):
        """Perform the search query"""
        base_path = os.path.dirname(__file__)

        r = search(query=self.name, tld=self.tld, lang='en',
                   num=self.num, start=self.start, stop=self.stop,
                   pause=self.pause)

        count = 0
        if self.output_file:
            file_path = os.path.join(
                base_path, self.filename)
            print(f"writing file: {self.filename}")

            with open(file_path, 'w') as f:
                f.write(f'Search query: {self.name}\n')
                for x in r:
                    count += 1
                    f.write(f'{x}\n')
                print(f"Found: {count}")
        else:
            print(f"Searchin for {self.name}")
            for i in r:
                count += 1
                print(f"{count}: {i}")
            print(f"Found: {count}")


if __name__ == '__main__':
    args = use_args()
    gs = Gsearch_python(
        name_search=args.query,
        tld_search=args.tld,
        start=args.start,
        stop=args.stop,
        pause=args.pause,
        num=args.num,
        output_file=args.file
    )
    gs.Gsearch()
