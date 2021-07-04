# Performing google search using Python code
import argparse
import os
import csv
try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' Found")


class Gsearch_python:
    def __init__(
            self, name_search: str, quiet: bool,
            start: int, stop: int,
            pause: int, num: int, tld_search: str,
            output_file: str):
        self.name = name_search
        self.tld = tld_search
        self.num = num
        self.start = start
        self.stop = stop
        self.pause = pause

        self.is_quiet = quiet
        self.output_file = output_file

    def Gsearch(self):
        """Perform the search query"""
        file_extension = '.csv'
        base_path = os.path.dirname(__file__)

        search_response = [_ for _ in search(
            query=self.name, tld=self.tld, lang='en',
            num=self.num, start=self.start, stop=self.stop, pause=self.pause)]

        if not self.is_quiet:
            print("---------------------------")
            print(f"Search word: {self.name}")
            print("---------------------------")
            for i in search_response:
                print(i)

        if self.output_file is not None:
            file_name = self.output_file + file_extension
            file_path = os.path.join(
                base_path, file_name)
            print(f"writing file: {file_name}")

            with open(file_path, 'a') as f:
                writer = csv.writer(
                    f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([self.name])
                writer.writerow(search_response)


def use_args():
    """Commandline argument parser"""
    parser = argparse.ArgumentParser(description="Search for something")

    parser.add_argument("query", help="search query")

    parser.add_argument("-q", "--quiet", action="store_true",
                        help="omit output to console")
    parser.add_argument("--tld", default="com",
                        help="top-level-domain 'com', 'co.in' default is 'com'")
    parser.add_argument("--pause", type=int, default=2,
                        help="lapse to wait between HTTP requests")
    parser.add_argument("--num", type=int, default=25,
                        help="number of results per page")
    parser.add_argument("--start", type=int, default=0,
                        help="first result to retrieve")
    parser.add_argument("--stop", type=int, default=10,
                        help=("last result to retrieve."
                              "Use None to search forever"))
    parser.add_argument("-f", "--file", help="filename")

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = use_args()
    gs = Gsearch_python(
        name_search=args.query,
        tld_search=args.tld,
        start=args.start,
        stop=args.stop,
        pause=args.pause,
        quiet=args.quiet,
        num=args.num,
        output_file=args.file
    )
    gs.Gsearch()
