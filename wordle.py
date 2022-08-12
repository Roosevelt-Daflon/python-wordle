import random

class wordle:
    
    def __init__(self, num_attempts):
        self.num_attempts = num_attempts
        
    def start(self):
        lines = open("words.txt").read().splitlines()
        self.word = random.choice(lines)
        print(self.word)
        
    def check_word(self, word_attempt):
        temp_word = []
        
        for i in range(len(self.word)):
            if self.word[i] == word_attempt[i]:
                temp_word.append(self.word[i])
            else:
                temp_word.append(" ")
        
        if ''.join(temp_word) == self.word:
            return (True, temp_word)
        else:
            self.num_attempts -= 1
            return (False, temp_word)
