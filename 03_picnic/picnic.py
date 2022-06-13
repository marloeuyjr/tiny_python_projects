#!/usr/bin/env python3
"""
Author : marloe.uy <marloe.uy@localhost>
Date   : 2022-06-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Going on a picnic. List the food to bring.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items', metavar='str', nargs='+', help='Items to bring.')
    
    parser.add_argument('--sorted', '-s',
                        help='Sort the items',
                        action='store_true',
                        )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.sorted is True: args.items.sort()
    if len(args.items) > 2:
       last_item = args.items.pop()
       print(f'You are bringing {", ".join(args.items)}, and {last_item}.')
    else:
       print(f'You are bringing {" and ".join(args.items)}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
