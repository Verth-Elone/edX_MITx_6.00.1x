def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    word = word.lower()
    letter_list = list(word)
    if word in wordList:
        for key, value in hand.items():
            for i in range(0, value):
                try:
                    letter_list.remove(key)
                except ValueError:
                    pass

    if len(letter_list) == 0:
        return True
    else:
        return False


with open('words.txt') as f:
    word_list = [x.lower() for x in f.read().split('\n')]

x = isValidWord('hammer', {'m': 2, 'a': 1, 'e': 1, 'r': 1, 'h': 1}, word_list)
print(x)
