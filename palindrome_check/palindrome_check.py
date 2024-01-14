from collections import deque


class PalindromeCheck:
    d = deque()

    def is_palindrome(self, string):
        formatted_string = self.format_string(string)
        self.fill(formatted_string)

        while len(self.d) > 1:
            right_letter = self.d.pop()
            left_letter = self.d.popleft()

            if right_letter != left_letter:
                self.clear()
                print(f'{string} is not a palindrome.')
                return False

        self.clear()
        print(f'{string} is a palindrome.')
        return True

    def format_string(self, string):
        return string.replace(" ", "").lower()

    def fill(self, string):
        for letter in string:
            self.d.append(letter)

    def clear(self):
        self.d.clear()
