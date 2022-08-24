import os
import yaml


def load_settings(config_name: str):
    # Load the config.yaml file
    stream = open(config_name, 'r')
    settings = yaml.load(stream, yaml.SafeLoader)
    print(settings)

    return settings
    # authorize_url = '{0}{1}'.format(
    #     settings['authority'], settings['authorize_endpoint'])
    # token_url = '{0}{1}'.format(
    #     settings['authority'], settings['token_endpoint'])
