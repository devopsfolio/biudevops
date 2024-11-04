def main_count_Alice():
    alice_text = read_Alice_text('/home/sergeyk/biu/biudevops/python/Alice.txt')
    Alice_words = clean_Alice(alice_text)
    (words_dict, max_word_count) = count_words_in_Alice(Alice_words)
    print( f"Total words: {len(words_dict)}" )
    print( f"Top word: {max_word_count}" )


def read_Alice_text(file_name):
    alice_file = open(file_name)
    alice_text = alice_file.read()
    alice_file.close()
    return alice_text

def clean_Alice(draft_text):
    
    clean_text = ''
    
    for letter in draft_text:
        if letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            clean_text += letter
        else:
            clean_text += " "
    
    clean_text = clean_text.lower()
    
    clean_words_list = clean_text.split()
    
    return clean_words_list

def count_words_in_Alice(words_list):
    words_dict = {}
    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    
    key_max = max(words_dict, key = words_dict.get)
    val_max = words_dict[key_max]

    top_word = { key_max: val_max}
    result = (words_dict, top_word)
    return result

main_count_Alice()
