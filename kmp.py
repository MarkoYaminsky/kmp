def build_pattern(string: str) -> list[int]:
    pattern = [0 for _ in string]
    longest_prefix = 0
    index = 1
    while index < len(string):
        if string[index] == string[longest_prefix]:
            longest_prefix += 1
            pattern[index] = longest_prefix
            index += 1
        elif longest_prefix > 0:
            longest_prefix = pattern[longest_prefix - 1]
        else:
            index += 1
    return pattern


def does_match(string: str, substring: str, pattern: list[int]) -> bool:
    match_beginning = 0
    position_in_substring = 0
    string_length = len(string)
    while match_beginning < string_length:
        if string[match_beginning] == substring[position_in_substring]:
            match_beginning += 1
            position_in_substring += 1
        if position_in_substring == len(substring):
            return True
        elif match_beginning < string_length and substring[position_in_substring] != string[match_beginning]:
            if position_in_substring > 0:
                position_in_substring = pattern[position_in_substring - 1]
            else:
                match_beginning += 1
    return False


def knuth_morris_pratt(string: str, substring: str) -> bool:
    pattern = build_pattern(substring)
    return does_match(string, substring, pattern)
