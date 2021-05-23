import argparse

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected in showvectors')


def stringdetector(s):
    if not isinstance(s, str):
        raise argparse.ArgumentTypeError('An input was expected to be a string')


def intdetector(i):
    if not isinstance(i, int):
        raise argparse.ArgumentTypeError('An input was expected to be an integer')


def floatdetector(f):
    if not isinstance(f, float):
        raise argparse.ArgumentTypeError('An input was expected to be a float')