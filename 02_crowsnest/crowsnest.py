#!/usr/bin/env python3
"""
Author : marloe.uy <marloe.uy@localhost>
Date   : 2022-05-28
Purpose: Chapter 2 Exercise
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Chapter 2 Exercise",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("object", metavar="str", help="Object appearing.")

    return parser.parse_args()


# --------------------------------------------------


def prep_message():
    """Prep the message to output"""
    article = ''
    args = get_args()
    pos_arg = args.object
    vowel = 'aeiou'
    article = "an" if pos_arg[0].lower() in vowel else "a"
    message = ["Ahoy, Captain,", article, pos_arg, "off the larboard bow!"]
    return " ".join(message)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    print(prep_message())


# --------------------------------------------------
if __name__ == "__main__":
    main()
