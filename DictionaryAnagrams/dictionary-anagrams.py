def read_words(file_name="words.txt"):
    with open(file_name,"r") as f:
        return [line.strip() for line in f]

def get_word_map(words):
    return [("".join(sorted(word)), word) for word in words]

def sort_word_map(words_map):
    return sorted(words_map, key=lambda entry : entry[0])

def main():
    words     = read_words()
    words_map = get_word_map(words)
    words_map = sort_word_map(words_map)
    
    for i, (word_sign, word) in enumerate(words_map):
        print(word)  
        if i + 1 < len(words_map) and word_sign != words_map[i+1][0]:
            print()

if __name__ == "__main__": main()