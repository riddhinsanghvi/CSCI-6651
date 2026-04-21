"""
Algorithm:
1. Start program.
2. Enter infinite loop to continually accept user input.
3. Prompt user: "Enter Chars (Non Alpha Quits) > ".
4. Read user input, make lower case, and trim.
5. Validate user input:
If user input contains any character that is not an alphabetic character (a-z A-Z)
→ print "Good Bye!" and exit loop (it's the end of the program).
Otherwise continue.
6. Create all unique permutations (combinations) of user input characters through a
recursive routine.
7. Sort the list of permutations and print it as a comma delimited list.
8. For each permutation, apply “possible word” heuristic:
Does the permutation contain a vowel, with consonants on both sides (CVC pattern)?
9. Store permutations that meet the heuristic and print them as "Possible Words:"
(or "None" if none).
10. Go to step 3.
"""
def is_valid_string(s: str) -> bool:
    """Check if string contains only alphabetic characters."""
    return s.isalpha()
def generate_permutations(s: str) -> list:
    """
    Recursively generate all permutations of the input string.
    """
    if len(s) == 0:
        return ['']
    permutations = []
    for i in range(len(s)):
    # Choose the character at index i
        char = s[i]
        # Generate permutations for the remaining characters
        remaining = s[:i] + s[i+1:]
        for p in generate_permutations(remaining):
            permutations.append(char + p)
    # Remove duplicates if input has repeated letters
    return sorted(list(set(permutations)))
def is_possible_word(word: str) -> bool:
    """
    Simple heuristic:
    Consider a word 'possible' if it contains a vowel surrounded by consonants.
    """
    vowels = "aeiou"
    for i in range(1, len(word) - 1):
        if word[i-1] not in vowels and word[i] in vowels and word[i+1] not in vowels:
            return True
    return False
def main():
    while True:
        user_input = input("Enter Chars (Non Alpha Quits) > ").lower().strip()
        if not is_valid_string(user_input):
            print("Good Bye!")
            break
        combinations = generate_permutations(user_input)
        print("Combinations:", ",".join(combinations))
        possible_words = [w for w in combinations if is_possible_word(w)]
        print("Possible Words:", ",".join(possible_words) if possible_words else "None")

if __name__ == "__main__":
    main()
