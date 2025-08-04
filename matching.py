import socket
import json
import webbrowser

from config.config import MAPPING_KEY, MATCHER_KEY, PROTOCOL_PREFIX, get_mapper_filepath


def handle_matching(matchers, print_url: False, goto_url: False):
    """
    This method handles matching between a term (i.e. matcher) and an url, both being
    provided as command line arguments.
    """

    with open(get_mapper_filepath(), 'r') as mapper_file:
        mapper = json.loads(mapper_file.read())

        strings_to_match_hash = [ mapper[MAPPING_KEY][matcher] \
                                    for matcher in matchers \
                                    if matcher in mapper[MAPPING_KEY]]

        matched_objects = [ mapper[MATCHER_KEY][string_to_match_hash] \
                            for string_to_match_hash in strings_to_match_hash]

        if len(matched_objects) == 0 :
            raise Exception(f"Term '{matchers[0]}' didn't match with any links")

        for matched_object in matched_objects:
            if print_url:
                print(matched_object)

            if goto_url:
                try:
                    webbrowser.open_new_tab(PROTOCOL_PREFIX + matched_object['url'])
                except socket.error as e:
                    pass