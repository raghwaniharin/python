import random
from colorama import init, Fore
init()
GREEN = Fore.GREEN
RESET = Fore.RESET


def random_char():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    spec = "!@#$%&?~"  # you can add more
    chars = [upper, lower, nums, spec]
    n = random.randrange(0, 4)
    return random.choice(chars[n])


def main(length, number):
    for n in range(0, number):
        passwd = ""
        for l in range(0, length):
            passwd += random_char()
        print(f"[*] Your Password : {GREEN}{passwd}{RESET}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", dest="length", default=8)
    parser.add_argument("-n", "--number", dest="number", default=1)
    args = parser.parse_args()
    leng = int(args.length)
    num = int(args.number)
    length = 8
    number = 1
    if leng > 0:
        length = leng
    if num > 1:
        number = num
    main(length, number)

