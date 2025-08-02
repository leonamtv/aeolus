#!/usr/bin/python3

from argparser import parse_arguments
from matching import handle_matching
from linking import handle_linking


def main():
    args = parse_arguments()

    if args.matcher:
        handle_matching(args.matcher)

    if args.add_url:
        handle_linking(args.add_term, args.add_url)


if __name__ == "__main__" :
    main()