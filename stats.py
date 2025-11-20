def get_word_count(file_contents):
    word_count = 0
    words = file_contents.split()
    for word in words:
        word_count += 1

    return word_count

def get_char_count(file_contents):
    chars = {}
    for ch in file_contents:
        ch = ch.lower()
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1
    return chars