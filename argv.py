#!/usr/bin/python -B

"""
A collection of simple command-line parsing functions.
"""

from __future__ import print_function as __print  # hide from help(argv)

import sys, os, glob

def filenames(patterns, extensions=None, sort=False):
    """
    Examples:
      filenames, basenames = argv.filenames(sys.argv[1:])
      filenames, basenames = argv.filenames(sys.argv[1:], [".ppm", ".png"], sort=True)
    """
    filenames = [glob.glob(filepattern) for filepattern in patterns]                # expand wildcards
    filenames = [item for sublist in filenames for item in sublist]                 # flatten nested lists
    filenames = [f for f in set(filenames) if os.path.exists(f)]                    # check file existence
    if extensions is not None:
        filenames = [f for f in filenames if os.path.splitext(f)[1] in extensions]  # filter by extension
    filenames = sorted(filenames) if sort else filenames                            # sort if requested
    basenames = [os.path.splitext(f)[0] for f in filenames]                         # strip extensions
    return filenames, basenames

def exists(argname):
    """
    Example:
      showHelp = argv.exists("--help")
    """
    if argname in sys.argv:
        argidx = sys.argv.index(argname)
        del sys.argv[argidx]
        return True
    else:
        return False

def exitIfAnyUnparsedOptions():
    isOptionArg = ["--" in arg for arg in sys.argv]
    if any(isOptionArg):
        argname = sys.argv[isOptionArg.index(True)]
        print("Unrecognized command-line option: %s"%(argname))
        sys.exit(-1)
