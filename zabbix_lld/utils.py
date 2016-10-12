"""
Auxiliary functions
"""

import json


def format_lld(data_set):
    """Format JSON output for Zabbix LLD

    :param data_set: set or list of dictionaries
    :return: formatted Zabbix LLD data
    """

    return json.dumps({'data': data_set})


def table_to_dict(path, columns, sep=None, skip=None):
    """Convert tabled data to a dictionary

    :param path: path to the file to read
    :param columns: field names
    :param sep: fields separator
    :param skip: number of lines to skip on the source
    :return: dictionary
    """

    data_set = []

    with open(path) as source:
        if skip:
            source = list(source)[skip:]

        for line in source:
            values = line.split(sep, len(columns))
            data_set.append(dict(zip(columns, values)))

    return data_set
