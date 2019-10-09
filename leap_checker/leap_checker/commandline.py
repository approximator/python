"""
Command line application for checking if specified year is leap
"""

import sys
import logging
import argparse

from .is_leap import is_leap


def main() -> int:
    """
    This function is meant to be used by CLI (command line interface)
    :return: 0 if the year is leap, 1 otherwise. This value can be used in shell commands.
    """
    parser = argparse.ArgumentParser(description='Leap Year Checker')
    parser.add_argument('--log', required=False, default='INFO', help='Log level')
    parser.add_argument('year', type=int, help='Year to check')
    args = parser.parse_args()

    logging.basicConfig(level=args.log)
    logger = logging.getLogger('leap')

    leap = is_leap(args.year)
    logger.debug(f'The year {args.year} is {"not" if not leap else ""} leap')
    return 0 if leap else 1


if __name__ == '__main__':
    sys.exit(main())
