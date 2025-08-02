#!/usr/bin/python3

from os import path
from argparse import ArgumentParser
from linking import handle_linking
from config.config import BULK_LINKING_FILE_EXTENSION, BULK_LINKING_FILE_SEPARATOR


def parse_file(file_path):
    terms_and_urls = []
    with open(file_path, 'r') as file_to_parse:
        for line in file_to_parse.readlines():
            line_components = line \
                .replace(' ', '') \
                .replace('\n', '') \
                .split(BULK_LINKING_FILE_SEPARATOR)
            term, url = line_components
            terms_and_urls.append((term, url))
    return zip(*terms_and_urls)



def parse_arguments():
    argument_parser = ArgumentParser("Aeolus - directing you to your places - Bulk Linking", add_help=False)

    argument_parser.add_argument("-f", '--file', nargs=1, action="store", help="file path of csv containing terms + urls")

    args = argument_parser.parse_args()

    return args


def handle_bulk_linking(args):
    if len(args.file) < 1:
        print("You need to provide a file to read from")

    file_path = args.file[0]

    if not path.exists(file_path):
        print("The path you provided does not exist")

    if not path.isfile(file_path):
        print("The path you provided is not a file")

    if BULK_LINKING_FILE_EXTENSION not in file_path:
        print(f"The file must be a {BULK_LINKING_FILE_EXTENSION}")

    terms, urls = parse_file(file_path)

    handle_linking(terms, urls)

    

def main():
    args = parse_arguments()

    if args.file:
        handle_bulk_linking(args)


if __name__ == "__main__":
    main()