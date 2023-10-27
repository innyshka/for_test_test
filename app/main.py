def count_occurrences(phrase: str, letter: str) -> int:
    #commentsdfghjhlguyuyvjhbjhbjbjbbhjfdtstchgvhmbkn,ljhkjgvfdsdfffffffffffffffffffffffffffffffffffffffffff
    return len([char for char in phrase if char.lower() == letter.lower()])