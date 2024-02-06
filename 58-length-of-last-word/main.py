def length_of_last_word(s: str) -> int:
    i, length = len(s) - 1, 0
    while s[i] == " ":
        print(s[i])
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    print(length)
    return length


length_of_last_word("   fly me   to   the moon  ")
