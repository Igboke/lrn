import random
from string import ascii_letters, digits, printable, punctuation

class Passwordgenerator:
    def __init__(self,length:int,special_characters=False):
        self.length = length
        self.add_char = special_characters
    
    def generatepass(self):
        if not self.add_char:
            mid_split = self.length//2
            letters_ = random.sample(ascii_letters,mid_split+1) 
            numbers_ = random.sample(digits,mid_split+1)
            word = letters_ + numbers_
            return ''.join(random.sample(word,self.length))
        else:
            mid_split = self.length//3
            letters_ = random.sample(ascii_letters,mid_split+1)  
            numbers_ = random.sample(digits,mid_split+1)
            punc_ = random.sample(punctuation,mid_split+1)
            word = letters_ + numbers_ + punc_
            return ''.join(random.sample(word,self.length)) 
            
if __name__ == '__main__':
    danny = Passwordgenerator(8,)
    print(danny.generatepass())                                                    