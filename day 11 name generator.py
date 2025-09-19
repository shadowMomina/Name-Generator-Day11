"""
Day 11 of 90-Day Coding Series
Beginner-Friendly Name Generator

This program lets you generate random names in 3 ways:

1) Names starting with specific letters.
2) Names made ONLY from letters you choose.
3) “Pronounceable” names (consonant + vowel pattern).

After each generated name, you choose:
    1 = Quit the program
    2 = Generate another name

This is free to use (no warranty).
"""

import random
import string

# ---------------------------
# Some helpful letter groups
# ---------------------------

# Vowels in English
VOWELS = "aeiou"

# Consonants (all letters except vowels)
CONSONANTS = "".join([c for c in string.ascii_lowercase if c not in VOWELS])


# ---------------------------
# Functions to make names
# ---------------------------

def generate_start_with(prefix, length):
    """
    Make a name that starts with 'prefix'
    and is 'length' characters long.

    Example:
      prefix = 'Al', length = 6  → 'Alxyza'
    """
    prefix = prefix.lower()

    # If prefix is already longer than length, cut it down
    if len(prefix) >= length:
        name = prefix[:length]
    else:
        # Add random letters after prefix until we reach the required length
        remaining = length - len(prefix)
        random_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(remaining))
        name = prefix + random_letters

    # Capitalize first letter for nicer display
    return name.capitalize()


def generate_from_alphabet(allowed_letters, length):
    """
    Make a name using ONLY the letters you provide.

    Example:
      allowed_letters = 'abc', length = 5 → 'Cbbac'
    """
    allowed = [c.lower() for c in allowed_letters if c.isalpha()]

    if not allowed:
        raise ValueError("You didn’t provide any valid letters!")

    name = ''.join(random.choice(allowed) for _ in range(length))
    return name.capitalize()


def generate_pronounceable(length):
    """
    Make a name that *looks* pronounceable
    by alternating consonant and vowel.

    Example:
      length = 6 → 'Lomaru'
    """
    name_chars = []

    # Randomly decide whether to start with a consonant or vowel
    start_with_consonant = random.choice([True, False])

    for i in range(length):
        # Decide if this position should be consonant or vowel
        use_consonant = (i % 2 == 0 and start_with_consonant) or \
                        (i % 2 == 1 and not start_with_consonant)

        if use_consonant:
            name_chars.append(random.choice(CONSONANTS))
        else:
            name_chars.append(random.choice(VOWELS))

    return ''.join(name_chars).capitalize()


# ---------------------------
# Small helper to get a number safely
# ---------------------------

def get_int(prompt, min_value=1, max_value=50):
    """Ask user for a number until they give a valid one."""
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            n = int(s)
            if n < min_value:
                print(f"Please enter a number ≥ {min_value}.")
            elif n > max_value:
                print(f"Please enter a number ≤ {max_value}.")
            else:
                return n
        else:
            print("Please enter a valid number.")


# ---------------------------
# Main program starts here
# ---------------------------

def main():
    print("=== Day 11: Name Generator ===")
    print("Choose how you want to generate names:")
    print("A) Start with given letters")
    print("B) Use only chosen letters")
    print("C) Pronounceable (consonant-vowel pattern)")

    mode = input("Enter A, B or C: ").strip().upper()

    # --- Ask mode-specific questions ---
    if mode == "A":
        prefix = input("Enter starting letters (prefix): ").strip()
        if prefix == "":
            print("Empty prefix — I’ll pick a random letter.")
            prefix = random.choice(string.ascii_lowercase)
        length = get_int("Enter total name length (e.g. 4-12): ", 1, 30)
        generator = lambda: generate_start_with(prefix, length)

    elif mode == "B":
        allowed = input("Enter allowed letters (e.g. abcxyz): ").strip()
        cleaned = ''.join([c for c in allowed if c.isalpha()])
        if cleaned == "":
            print("No valid letters — defaulting to 'abcde'.")
            cleaned = "abcde"
        length = get_int("Enter name length (e.g. 3-12): ", 1, 30)
        generator = lambda: generate_from_alphabet(cleaned, length)

    elif mode == "C":
        length = get_int("Enter name length (e.g. 3-10): ", 2, 12)
        generator = lambda: generate_pronounceable(length)

    else:
        print("Invalid choice. Exiting.")
        return

    # --- Loop to generate names until user quits ---
    while True:
        try:
            name = generator()
        except Exception as e:
            print("Error generating name:", e)
            break

        print("\nGenerated name:", name)
        print("\nWhat would you like to do next?")
        print("1. Quit")
        print("2. Generate another name")

        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            print("Goodbye! Thanks for using the Name Generator.")
            break
        elif choice == "2":
            continue
        else:
            print("Invalid choice, exiting.")
            break


# This runs only if you run this file directly (not if you import it elsewhere)
if __name__ == "__main__":
    main()
