from word_list import *

class spellcast:
    
    def __init__(self,chars: str, gems: str, letter_bonus: tuple,letter_multiplier: int, word_bonus: tuple = None,round: int = 1)-> None:
        assert len(chars) == 25, "length of chars string must be 25"
        assert len(gems) == 25, "length of gems string must be 25"
        self.SCORE = [1,4,5,3,1,5,3,4,1,7,6,3,4,2,1,4,8,2,2,2,4,5,5,7,4,8]
        self.chars = chars
        self.grid_chars = [[chars[5 * y + x] for x in range(5)] for y in range(5)]
        self.grid_gems = [[gems[5 * y + x] for x in range(5)] for y in range(5)]
        self.letter_bonus = letter_bonus
        self.letter_multiplier = letter_multiplier
        self.word_bonus = word_bonus

    def neighbours(self,coord_a,coord_b):
        return abs(coord_a[0]-coord_b[0]) <= 1 and abs(coord_a[1]-coord_b[1]) <= 1

    def is_viable_word(self, wordx: str) -> list:
        """
        Input: a pruned word that can be spelt with available characters
        Output 1: A list representing the coordinate of each letter that forms the word on the grid 
        (given word can be spelt with conventions)
        Output 2: None, representing that word cannot be spelt using conventions
        """
        word = wordx[:]
        all_viable_words = []
        #for every instance of the starting word
        start_coords = self.get_coord(word[0])
        for coords in start_coords:
            all_viable_words += [self.is_viable_word_aux(word[1:],[coords],len(word))]

        if len(all_viable_words) == 0:
            return None
        return all_viable_words

    def is_viable_word_aux(self, word: str, coords,length: int):
        
        #if word length is 0, reached end of word
        if len(word) == 0:
            return coords
        #get every occurence of first letter in word
        all_coords = self.get_coord(word[0])
        #for every coordinate
        for new_coord in all_coords:
            #if both word coords are neighbours and coordinate isn't already in list
            # if new_coord == (3,2):
            #     print("hello")
            #if both word positions are viable, and letter hasn't already been used
            if self.neighbours(new_coord,coords[-1]) and new_coord not in coords:
                #create new recursive
                x = self.is_viable_word_aux(word[1:],coords + [new_coord],length)
                if x is not None and len(x) == length:
                    return x
        return None


    def get_coord(self, char: str) -> list:
        """
        Input: a character that is contained on the grid
        Output: a list of tuples that represent coordinates where that character is on the grid
        """
        all_coords = []
        #for y coordinates
        for y in range(5):
            #for x coordinates
            for x in range(5):
                #if coordinates contains character
                if self.grid_chars[y][x] == char:
                    all_coords += [(y,x)]
        return all_coords

    def get_word_score(self,word: list):
        """
        Input: a list of tuples representing the position of every character of the word on the board
        Output: a integer value representing the score that that word would give you
        """
        score = 0
        #for every character coord in list
        # if word == [(0, 1), (0, 0), (1, 1), (2, 0), (2, 1), (3, 2), (2, 3)]:
        #     print('hello')
        for coord in word:
            score += self.SCORE[ord(self.grid_chars[coord[0]][coord[1]])-97] * (self.letter_multiplier if coord == self.letter_bonus else 1)
        if self.word_bonus is not None and self.word_bonus in word:
            score *= 2
        if len(word) >= 7:
            score += 20
        return score
    
    def get_best_words(self):
        all_words = []
        all_word_coords = []
        all_scores = []
        for i in range(25,0,-1):
            #get all pruned words of one length list
            words = prune_words(self.chars,f"processed_word_lists\english_words25x\{i}-len.txt")
            #for every resulting word
            for word in words:
                word_coords = self.is_viable_word(word)
                #for every possible word coordinate, calculate highest scoring version
                max_score = None
                max_index = None
                
                for i in range(len(word_coords)):
                    #if valid word
                    if word_coords[i] is not None and len(word_coords[i]) == len(word) and None not in word_coords[i]:
                        score = self.get_word_score(word_coords[i])
                        if max_score == None or score > max_score:
                            max_score, max_index = score, i
                if max_score is not None:
                    all_words += [word]
                    all_word_coords += [word_coords[max_index]]
                    all_scores += [max_score]
        all_scores, all_words, all_word_coords = zip(*sorted(zip(all_scores,all_words,all_word_coords),reverse=True))
        for i in range(min(len(all_scores),20)):
            print(f"#{i+1}: {all_words[i]}, {all_scores[i]}, {all_word_coords[i]}")
                        
if __name__ == "__main__":
    #s = spellcast("ogaotbyolttrsekiatwefmoeg","0110000110111001100001000",(4,0),2,(3,4))
    #s.get_best_words()

    #words = prune_words("iljsmibthaexwiuigearaquyo","processed_word_lists\english_words25x.txt")
    s = spellcast("ogaotbyolttrsekiatwefmoeg","0110000110111001100001000",(4,0),2,None)
    #s.get_best_words()
    x = s.is_viable_word("gyrates")
    print(x)
    #print(words)
    # word = "cat"
    # print(s.is_viable_word(word))
    # print(word)
    # for i in range(25,0,-1):
    #     words = prune_words(s.chars,f"processed_word_lists\english_words25x\{i}-len.txt")
    #     for word in words:
    #         word_coords = s.is_viable_word(word)
    #         #for every possible word_coordinate
    #         for i in range(len(word_coords)):
    #             if None not in word_coords:
    #                 print(word, word_coords[i], s.get_word_score(word_coords[0]))
                

        #print(words)
    #print(s.get_word_score([(3, 2), (3, 3), (2, 2)]))