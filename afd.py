from classes.AFDProcessor import AFD
import argparse
import os

def main():
    
    # Set inputs in CLI
    parser = argparse.ArgumentParser(description="The AFD processor")
    parser.add_argument('-ft',help='Path of the transition functions with .txt format file')
    parser.add_argument('-q0',help='Initial state')
    parser.add_argument('-qfs',help='Final state(s)')
    parser.add_argument('-w',help='Test words')

    # Recive inputs and store variable
    args = parser.parse_args()

    # Trate exeption if not pass inputs in CLI
    try:
        for word in str(args.w).split(','):
            AFD(args.ft, args.q0, args.qfs, word)

    except TypeError:
        print("\nPlease, read the help descriptions below>>")
        os.system('python afd.py -h')


if __name__ == "__main__":
    main()