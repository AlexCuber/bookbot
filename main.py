
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        #return file_contents
    
    counted_words = count_words(file_contents)
    counted_characters = count_characters(file_contents)
    sorted_characters = character_list_sorted(counted_characters)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{counted_words} words found in the document")
    print()
    
    for sort_c in sorted_characters:
        if not sort_c['name'].isalpha():
            continue
        print(f"The '{sort_c['name']}' character was found {sort_c['num']} times")
        

def count_words(file):
    n_words = len(file.split())
    print(n_words)
    
    
def count_characters(file):
    string_lower = file.lower()
    char_count = {}
    for char in string_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_on(dict):
    return dict["num"]
    
def character_list_sorted(dict_characters):
    character_list = []
    for chr in dict_characters:
        character_list.append({"name": chr, "num": dict_characters[chr]})
    
    character_list.sort(reverse=True, key=sort_on)
    
    return character_list
    
main("books/frankenstein.txt")

