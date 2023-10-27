def count_occurrences(phrase: str, letter: str) -> int:
    #gfhjkgbnl

    return len([char for char in phrase if char.lower() == letter.lower()])