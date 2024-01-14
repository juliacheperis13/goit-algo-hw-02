from palindrome_check import PalindromeCheck


def main():
    palindrome_check = PalindromeCheck()

    while True:
        user_input = input("Enter a string: ")
        palindrome_check.is_palindrome(user_input)


if __name__ == "__main__":
    main()
