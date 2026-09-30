def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Requirement 1: Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Requirement 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Requirement 3 & 4: Punctuation check and Number rules
    # Track if we have encountered a number yet
    has_started_number = False

    for char in s:
        # Check for periods, spaces, or punctuation
        if not char.isalnum():
            return False

        # If it's a number
        if char.isdigit():
            # The first number used cannot be a '0'
            if not has_started_number and char == '0':
                return False
            has_started_number = True

        # Numbers cannot be in the middle (a letter cannot follow a number)
        elif char.isalpha():
            if has_started_number:
                return False

    return True


if __name__ == "__main__":
    main()
