# Count Letters

# Program Description:
# This program asks the user to enter a sentence.
# It counts how many times each letter appears in the sentence and displays the results in alphabetical order.
# Uppercase and lowercase letters are treated as the same letter.

# Ask the user to enter a sentence
# Convert the sentence to lowercase so that
# 'A' and 'a' are counted as the same letter
sentence = input("Enter a sentence: ").lower()

# Create an empty dictionary to store the results
# The key is the letter and the value is the number of times it appears
letters = {}

# Go through each character in the sentence
for letter in sentence:

    # Only count alphabet letters
    # Ignore spaces, numbers and symbols
    if letter.isalpha():

        # If the letter is not in the dictionary,
        # add it with a starting count of 1
        if letter not in letters:
            letters[letter] = 1

        # Otherwise, increase its count by 1
        else:
            letters[letter] += 1

'''
Example:

Input:
apple

letters = {
    'a': 1,
    'p': 2,
    'l': 1,
    'e': 1
}
'''

# Display the letters in alphabetical order
for letter, count in sorted(letters.items()):
    print(letter, ":", count)

'''
Example Output

Enter a sentence: Apple

a : 1
e : 1
l : 1
p : 2

The program counts how many times each letter appears
and prints the results in alphabetical order.
'''
