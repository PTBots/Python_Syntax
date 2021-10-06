def print_upper_words(words):
    for word in words:
        print(word.upper())

print(print_upper_words(["hello", "Hey", "hOwDy"]))

def print_e_words_upper_case(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print(print_e_words_upper_case(["eugene", "harry", "earth"]))

def print_select_words_upper_case(words, starts_with):
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
            
print(print_select_words_upper_case(["young", "old", "origin", "moon"], "o"))