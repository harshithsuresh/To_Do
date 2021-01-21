from configparser import ConfigParser
from os.path import isfile

def read_config(file_path):
    """
    Read the configuration from the file path passed.

    Args:
        file_path : A string representing the configuration file path.

    Returns:
        Configuration in the form of a dict where the keys are the section in the file
        while values are another dict containing the keys and values under that section.

    Raises:
        ValueError : When no, empty or invalid file_path is passed.
        TypeError : When non string file_path is passed.
    """
    if not file_path:
        raise ValueError('No file_path is passed.')
    if not isinstance(file_path, str):
        raise TypeError('file_path should be str.')
    if not isfile(file_path):
        raise ValueError('file_path is invalid.')

    config = ConfigParser(allow_no_value=True)
    config.read(file_path)

    return config