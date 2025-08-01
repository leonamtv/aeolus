import socket
import json
import webbrowser

from config.config import MAPPING_KEY, MATCHER_KEY, PROTOCOL_PREFIX, get_mapper_filepath
from argparser import parse_arguments

args = parse_arguments()

if args.matcher:
    matchers = args.matcher

    mapper = json.loads(open(get_mapper_filepath(), 'r').read())

    strings_to_match_hash = [ mapper[MAPPING_KEY][matcher] \
                            for matcher in matchers \
                            if matcher in mapper[MAPPING_KEY]]

    matched_objects = [ mapper[MATCHER_KEY][string_to_match_hash] \
                    for string_to_match_hash in strings_to_match_hash]

    if len(matched_objects) == 0 :
        raise Exception(f"Term '{matchers[0]}' didn't match with any links")

    for matched_object in matched_objects:
        if args.print_details:
            print(matched_object)

        if args.go_to:
            try:
                webbrowser.open_new_tab(PROTOCOL_PREFIX + matched_object['url'])
            except socket.error as e:
                pass

if args.add_url:
    with open(get_mapper_filepath(), 'r+') as mapper_file:
        mapper = json.loads(mapper_file.read())
        
        urls_to_add = args.add_url
        terms_to_add = args.add_term
        
        if len(urls_to_add) != len(terms_to_add) \
            or len(urls_to_add) == 0 \
            or len(urls_to_add) == 0:
            raise Exception("You need to provide one link and one term to match")
        
        url_to_add = urls_to_add[0]
        term_to_add = terms_to_add[0]

        existing_matching_matchers = [url_id for url_id in mapper[MATCHER_KEY] \
                                      if mapper[MATCHER_KEY][url_id]['url'] == url_to_add ]
        
        if len(existing_matching_matchers) > 0 :
            corresponding_id = existing_matching_matchers[0]
            mapper[MAPPING_KEY][term_to_add] = str(corresponding_id)

            print(f"Adding link between term: {term_to_add} and existing url: {url_to_add}")
        else :
            last_id = max(int(item) for item in mapper[MATCHER_KEY].keys()) 
            next_id = last_id + 1 if last_id is not None else 1

            mapper[MATCHER_KEY][str(next_id)] = { "url" : url_to_add }
            mapper[MAPPING_KEY][term_to_add] = str(next_id)

            print(f"Adding link between term: {term_to_add} and url: {url_to_add}")
        

        mapper_file.seek(0)
        mapper_file.write(json.dumps(mapper, indent=4))
