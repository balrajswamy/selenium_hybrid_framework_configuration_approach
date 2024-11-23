import configparser


def reading_config(section,key):
    # Create a ConfigParser instance
    config = configparser.ConfigParser()

    # Read the config.ini file
    config.read('confingurations/config.ini')
    return config.get(section,key)
