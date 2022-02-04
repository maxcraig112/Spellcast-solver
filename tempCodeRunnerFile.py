for i in range(25,0,-1):
        words = prune_words(s.chars,f"processed_word_lists\english_words25x\{i}-len.txt")
        for word in words:
            x = s.is_viable_word(word)
            if None not in x:
                print(word, x)