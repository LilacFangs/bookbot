# function to find the number of words in a given book
def book_word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

# function to find the number of individual characters in a given book
def book_character_count(text):
    character_counts = {}
    character_dictionary_to_sort = {}
    for original_character in text:
        if original_character.isalpha() == True:
            character = original_character.lower()
            if character not in character_counts:
                character_counts[character] = 1
            else:
                character_counts[character] += 1
    return character_counts

# function to sort the dictionary of individual characters by most frequent to least frequent:
def book_character_sort(dictionary):
    character_dictionary_list = []
    #print(dictionary)
    for letter in dictionary:
        letter_count = dictionary[letter]
        character_dictionary_to_sort = {"char": letter, "num": letter_count}
        character_dictionary_list.append(character_dictionary_to_sort)
    character_dictionary_list.sort(reverse=True, key=sort_on)
    return character_dictionary_list

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]


    