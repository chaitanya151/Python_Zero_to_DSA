"""
Longest Even Length Word: 
Write a function to return the longest even length word in a sentence.
"""


def longest_even_length(s: str):
    ch = s.split(" ")
    longest_word = ""
    for word in ch:
        if len(word) % 2 == 0:
            if len(word) > len(longest_word):
                longest_word = word

    # Return the longest even-length word, or indicate no such word exists
    if longest_word:
        return longest_word
    else:
        return "No even-length word found"


s = " Be not afraid of greatness, some are born great,\
    some achieve greatness, and some\
    have greatness thrust upon them."

print(longest_even_length(s))
