#!/bin/env python3
"""
Author: Marloe Uy
Purpose: Just learning shit
"""
import argparse


# ---------------------------- #
def get_args():
    """Get command-line arguments and offer usage instruction"""

    parser = argparse.ArgumentParser(description="Say HELLO")
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")
    return parser.parse_args()


# ---------------------------- #
def main():
    """standard main function"""
    args = get_args()
    print("Hello, " + args.name + "!")


# ---------------------------- #
if __name__ == "__main__":

    main()
