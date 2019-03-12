def count_upper_case(message):
    if isinstance(message, str):
        return sum([1 for c in message if c.isupper()])
    else:
        return 0

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("ABC") == 3, "Three upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case(0) == 0, "Number Zero"
assert count_upper_case("A123Babc") == 2, "Mixed characters"

print("All the tests passed")