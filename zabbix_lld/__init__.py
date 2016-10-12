"""
Low level discovery functions for Zabbix
"""

import argparse
import sys

import zabbix_lld.disk
import zabbix_lld.utils


def main(args=None):
    functions = {
        'fs': zabbix_lld.disk.get_file_systems,
        'part': zabbix_lld.disk.get_partitions,
        'swap': zabbix_lld.disk.get_swaps,
    }

    parser = argparse.ArgumentParser(
        description='Low level discovery functions for Zabbix')
    parser.add_argument('function', choices=sorted(functions.keys()))

    try:
        parsed_args = parser.parse_args(args)
    except:
        print('ZBX_NOTSUPPORTED')
        sys.exit(1)

    function = functions.get(parsed_args.function)
    data_set = function()
    formatted_data_set = zabbix_lld.utils.format_lld(data_set)

    print(formatted_data_set)


if __name__ == '__main__':
    main()
