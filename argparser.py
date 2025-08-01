from argparse import ArgumentParser


def parse_arguments():
    argument_parser = ArgumentParser("Aeolus - directing you to your places", add_help=False)

    argument_parser.add_argument('-m', '--matcher', nargs=1, action='store', help='string to match with link')
    argument_parser.add_argument('-u', '--add-url', nargs=1, action='store', help='url to add to mapping')
    argument_parser.add_argument('-t', '--add-term', nargs=1, action='store', help='term to add to mapping')
    argument_parser.add_argument("-p", '--print-details', action="store_true", help="prints details of matched link")
    argument_parser.add_argument("-g", '--go-to', action="store_true", help="go to matched link")

    args = argument_parser.parse_args()

    validate_arguments(args)

    return args


def validate_arguments(args):
    if args.matcher or args.print_details or args.go_to:
        if args.matcher and ( not args.print_details and not args.go_to ):
            raise Exception("You need to provide at least -p or -g along -m")
        if not args.matcher and ( args.print_details or args.go_to ):
            raise Exception("You need to provide -m if you want to either print or go to url")
    if args.add_url or args.add_term:
        if args.add_url and not args.add_term:
            raise Exception("You need to provide the term you want to match with the url")
        if not args.add_url and args.add_term:
            raise Exception("You need to provide the url you want to match with the term")
