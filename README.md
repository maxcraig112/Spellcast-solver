# Spellcast-solver
A bot designed to prune and determine the highest scoring words in a game of discord spellcast

- Kevin Atkinsons wordlist is used
- http://wordlist.aspell.net/scowl-readme/

NOTES
- in the processed_word_lists folder, the number on the end represents the % of all english words that are contained in that file
- as well, here are the word lists that constitute each percentage
    100 - [10,95]
    52 -  [10,80]
    25 -  [10,70]

- x at the end represents lists which have been pruned such that accented words, and 's have been removed, and words with length greater than 25, as they are not possible in spellcast