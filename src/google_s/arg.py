import argparse


def use_args():
    """Commandline argument parser"""
    parser = argparse.ArgumentParser(description="Search for something")

    parser.add_argument("query", help="search query")

    parser.add_argument("--tld", default="com",
                        help="""top-level-domain 'com',
                                'co.in' default is 'com'""")
    parser.add_argument("--pause", type=int, default=2,
                        help="lapse to wait between HTTP requests")
    parser.add_argument("--num", type=int, default=10,
                        help="number of results per page")
    parser.add_argument("--start", type=int, default=0,
                        help="first result to retrieve")
    parser.add_argument("--stop", type=int,
                        help=("last result to retrieve."
                              "Use None to search forever"))
    parser.add_argument("-f", "--file", action='store_true', help="If Output should be to file")

    args = parser.parse_args()

    return args
