from word_list import *

class spellcast:
    
    def __init__(self,chars: str, gems: str, letter_bonus: tuple, word_bonus: tuple,round: int = 1) -> None:
        self.SCORE = [1,4,5,3,1,5,3,4,1,7,6,3,4,2,1,4,8,2,2,2,4,5,5,7,4,8]
        self.chars = chars
        self.grid_chars = [[chars[5 * y + x] for x in range(5)] for y in range(5)]
        self.grid_gems = [[gems[5 * y + x] for x in range(5)] for y in range(5)]
        self.letter_multiplier = 2 if round == 1 else 3

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
            all_viable_words += [self.is_viable_word_aux(word[1:],[coords])]

        if len(all_viable_words) == 0:
            return None
        return all_viable_words

    def is_viable_word_aux(self, word: str, coords):
        
        #if word length is 0, reached end of word
        if len(word) == 0:
            return coords
        #get every occurence of first letter in word
        all_coords = self.get_coord(word[0])
        #for every coordinate
        for new_coord in all_coords:
            #if both word coords are neighbours and coordinate isn't already in list
            if self.neighbours(new_coord,coords[-1]) and new_coord not in coords:
                #create new recursive
                return self.is_viable_word_aux(word[1:],coords + [new_coord])


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

if __name__ == "__main__":
    s = spellcast("qiuyinfgaikeaaaboeimsdiva","1000010010001101010101100",(3,3),(3,1))
    # word = "cat"
    # print(s.is_viable_word(word))
    # print(word)
    for i in range(25,0,-1):
        words = prune_words(s.chars,f"processed_word_lists\english_words25x\{i}-len.txt")
        for word in words:
            x = s.is_viable_word(word)
            if None not in x:
                print(word, x)
        #print(words)