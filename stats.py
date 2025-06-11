def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count
def char_count(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict            
def sort_char_count(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list


