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

# helper function for sorting
def sort_on(items):
    return items["num"]

def sort_char_count(char_dict):
    char_counts = []
    for ch in char_dict:
        new_dict = {}
        new_dict["char"] = ch # first key:value pair: "char: a" for example
        
        value = char_dict[ch]
        new_dict["num"] = value # second key:value pair: "num: 1000" for example
        
        char_counts.append(new_dict)
    
    char_counts.sort(reverse=True, key=sort_on)

    return char_counts