import json

from config.config import MAPPING_KEY, MATCHER_KEY, get_mapper_filepath


def handle_linking(terms_to_add, urls_to_add):
    """
    This method handles linking between a term and an url, both being
    provided as command line arguments
    """
    with open(get_mapper_filepath(), 'r+') as mapper_file:
        mapper = json.loads(mapper_file.read())
            
        if len(urls_to_add) != len(terms_to_add) \
                or len(urls_to_add) == 0 \
                or len(terms_to_add) == 0:
            raise Exception("You need to provide one link and one term to match")

        for term_to_add, url_to_add in zip(terms_to_add, urls_to_add):

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