def count_occurrences(phrase: str, letter: str) -> int:
    low_letter = letter.lower()    
    low_phrase = phrase.lower()
    count = 0
    for ch in low_phrase:
        if ch == low_letter:
            count += 1
    return count
