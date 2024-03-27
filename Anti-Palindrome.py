"https://open.kattis.com/problems/antipalindrome"
def preprocess(text):
    # Remove non-alphabetic characters and convert to lowercase
    processed_text = ''.join(char.lower() for char in text if char.isalpha())
    return processed_text

def is_palindrome(processed_text):
    # Check if the text is a palindrome
    for i in range(len(processed_text)-1):
        if processed_text[i] == processed_text[i + 1]:
            return True
    for i in range(len(processed_text)-2):
        if processed_text[i] == processed_text[i + 2]:
            return True
    return False

def check_palindrome(text):
    processed_text = preprocess(text)
    if is_palindrome(processed_text):
        print("Palindrome")
    else:
        print("Anti-palindrome")

# Read input
text = input()

# Check for palindrome
check_palindrome(text)