import random
import string
import sys

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return f"Random string of length {length} is: {result_str}"

def main():
    pass_length = int(sys.argv[1]) if len(sys.argv) >=2 else 8
    print(get_random_string(pass_length))

if __name__ == "__main__":
    main()
