#!/usr/bin/env python3

# pylint: disable=C0111  # docstrings are always outdated and wrong
# pylint: disable=W0511  # todo is encouraged
# pylint: disable=C0301  # line too long
# pylint: disable=R0902  # too many instance attributes
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0103  # single letter var names, func name too descriptive
# pylint: disable=R0911  # too many return statements
# pylint: disable=R0912  # too many branches
# pylint: disable=R0915  # too many statements
# pylint: disable=R0913  # too many arguments
# pylint: disable=R1702  # too many nested blocks
# pylint: disable=R0914  # too many local variables
# pylint: disable=R0903  # too few public methods
# pylint: disable=E1101  # no member for base
# pylint: disable=W0201  # attribute defined outside __init__
# pylint: disable=R0916  # Too many boolean expressions in if statement


import os
import sys
from pathlib import Path

import click


def eprint(*args, **kwargs):
    if 'file' in kwargs.keys():
        kwargs.pop('file')
    print(*args, file=sys.stderr, **kwargs)


try:
    from icecream import ic  # https://github.com/gruns/icecream
except ImportError:
    ic = eprint


from enumerate_input import enumerate_input
from getdents import paths
from getdents._getdents import (DT_BLK, DT_CHR, DT_DIR,  # noqa: ignore=F401
                                DT_FIFO, DT_LNK, DT_REG, DT_SOCK, DT_UNKNOWN)

# import pdb; pdb.set_trace()
# from pudb import set_trace; set_trace(paused=False)


@click.command()
@click.argument("path",
                type=click.Path(exists=False,
                                dir_okay=True,
                                file_okay=False,
                                path_type=str,
                                allow_dash=False),
                nargs=1,
                required=True)
@click.option('--verbose', is_flag=True)
@click.option('--debug', is_flag=True)
#@click.group()
def cli(path,
        verbose,
        debug,):

    path = Path(path)
    ic(path)
    for item in paths(path):
        ic(item)
