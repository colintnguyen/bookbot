def main():
    filepath = 'books/frankenstein.txt'
    with open(filepath, 'r') as file:
        content = file.read()
        count_words(content, filepath)

def count_words(text, filepath):
    words = text.split()
    print(f"--- Begin report of {filepath} ---")
    print(f"{len(words)} words found in the document\n")
    lowered_text_dict = {}
    lowered_text = text.lower()
    for lower in lowered_text:
        if lower in lowered_text_dict:
            lowered_text_dict[lower] += 1
        else:
            lowered_text_dict[lower] = 1
    char_list = [{'char': lower, 'count': count} for lower, count in lowered_text_dict.items()]
    sorted_list = sorted(char_list, key=sort_on, reverse=True)
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

def sort_on(item):
    return item['count']



if __name__ == '__main__':
    main()
