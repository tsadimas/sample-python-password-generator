import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return f"Random string of length {length} is: {result_str}"

def main():
    print(get_random_string(8))

if __name__ == "__main__":
    main()
