def main():
    book_path = "books/frankenstein.txt"
    book_content = read_book(book_path)
    num_of_words = count_word(book_content)
    
    num_of_each_latter = count_letters(book_content)

    formatted_dict = format_dict(num_of_each_latter)

    generate_report(num_of_words,formatted_dict)

def generate_report(num_of_words,formatted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")
    print("")
    for i in formatted_list:
        print(i)
    print("--- End report ---")

def format_dict(latter_dict):
    temp_list = []
    for k , v in latter_dict.items():
        temp_dict = {
            "latter" : k,
            "num" :v
        }
        temp_list.append(temp_dict)
    temp_list.sort(reverse=True,key=sort_on)


    lines = []
    for i in temp_list:
        if i["latter"].isalpha():
            lines.append(f"The '{i["latter"]}' character was found {i["num"]} times")
    
    return lines
    
def read_book(path_of_book):
    with open(path_of_book) as f:
        file_content = f.read()
        return file_content
    
def count_word(content):
    words = content.split()
    return len(words)
    
def count_letters(content):
    content_lower = content.lower()
    num_of_each_latter = {}
    for i in content_lower:
        if i in num_of_each_latter:
            num_of_each_latter[i]+=1
        else:
            num_of_each_latter[i] = 1
    return num_of_each_latter

def sort_on(dict):
    return dict["num"]

main()