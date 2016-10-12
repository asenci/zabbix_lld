"""
Disk related discovery functions
"""

from zabbix_lld.utils import table_to_dict


def get_file_systems():
    """Get a list of mounted file systems"""

    return table_to_dict(
        path='/etc/mtab',
        columns=('{#FSDEV}', '{#FSNAME}', '{#FSTYPE}', '{#FSOPTS}', '{#FSDUMP}', '{#FSCK}'))


def get_partitions():
    """Get a list of available partitions"""

    return table_to_dict(
        path='/proc/partitions',
        columns=('{#PTMAJOR}', '{#PTMINOR}', '{#PTBLOCKS}', '{#PTNAME}'),
        skip=2)


def get_swaps():
    """Get a list of active swap devices"""

    return table_to_dict(
        path='/proc/swaps',
        columns=('{#SWNAME}', '{#SWTYPE}', '{#SWSIZE}', '{#SWUSED}', '{#SWPRIO}'),
        skip=1)
