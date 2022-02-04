import os

def openf(file_name):
    """
    Reads a .txt file as to copy words into a list
    """
    with open(file_name) as f:
        words = f.readlines()
        for i in range(len(words)):
            words[i] = words[i][:-1]
    return words

def collate_lists(suffix: list, file_name: str):
    """
    Input a list which represents all englishw-word files that want to collated together, and a resulting file_name
    """
    #collate all word lists into 1 main file
    with open(file_name,"w") as f:
        #for every file that is going to be read
        for i in range(len(suffix)):
            #read all lines
            lst_words = openf(f"raw_word_lists/english-words.{suffix[i]}")
            #for every word in list
            for word in lst_words:
                #write word to main file
                f.write(word + "\n")

def filter_list(file_name):
    """
    Input a file and return that file with
    - all 's words removed
    - no accented words
    - all words that are > 25 in length
    """
    lst_words = openf(file_name)
    with open(f"{file_name[:-4]}x.txt","w") as f:
        for word in lst_words:
            if '\'' not in word and all(ord(char) < 128 for char in word) and len(word) <= 25:
                f.write(word + "\n")

def split_file(file_name):
    """
    from a given txt file with a list of words
    - create a directory with that txt files name
    - create corresponding txt files in that directory that contact all different length words in the original txt
    """
    if not os.path.isdir(file_name[:-4]):
        os.mkdir(file_name[:-4])
    lst_words = openf(file_name)
    #get min and max len of words in lst
    min_len, max_len = len(min(lst_words, key=len)), len(max(lst_words, key=len))
    files = [open(f'{file_name[:-4]}\{min_len + i}-len.txt',"w") for i in range(max_len - min_len + 1)]
    for word in lst_words:
        files[len(word) - 1].write(word + "\n")

def prune_words(chars:str, lst_words:list or str) -> list:
    """
    given a string meant to represent a list of characters, take an inputted list of words (or file directory to be converted),
    and return a list representing all words that can be formed formed from those given characters
    """
    #convert file directory to word list
    if type(lst_words) == str:
        lst_words = openf(lst_words)

    final_lst_words = []
    #for every word in list
    for i in range(len(lst_words)):
        #create duplicate of chars
        temp_chars = [c for c in chars]
        word_char = [c for c in lst_words[i]]
        #while length of word != 0 and 
        while len(word_char) != 0 and word_char[-1] in temp_chars:
            #if condition met, pop last element off list, remove from temp_chars
            temp_chars.remove(word_char.pop())
        if len(word_char) == 0:
            final_lst_words += [lst_words[i]]
    return final_lst_words
            
    



if __name__ == "__main__":
    pass
    #collate_lists([10,20,35,40,50,55,60,70,80,95],"processed_word_lists\english_words100.txt")
    #collate_lists([10,20,35,40,50,55,60,70,80],"processed_word_lists\english_words52.txt")
    #collate_lists([10,20,35,40,50,55,60,70],"processed_word_lists\english_words25.txt")
    #filter_list("processed_word_lists\english_words52.txt")
    #split_file("processed_word_lists\english_words52x.txt")
    words = prune_words("doomer",["doomer","domer","d","ddoomer","merdoo"])
    print(words)
    # for i in range(25,0,-1):
    #     words = prune_words("kunjdvisriiopfeabadewowti",f"processed_word_lists\english_words25x\{i}-len.txt")
    #     print(words)
    
