MAPPING_KEY = 'mapping'
MATCHER_KEY = 'matchers'

PROTOCOL_PREFIX = 'https://'

DEFAULT_MAPPER_FILEPATH = 'resources/default_mapper.json'
MAPPER_FILEPATH = ''

def get_mapper_filepath():
    return DEFAULT_MAPPER_FILEPATH \
        if MAPPER_FILEPATH == '' or MAPPER_FILEPATH is None \
        else MAPPER_FILEPATH