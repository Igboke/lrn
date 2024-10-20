from random import sample
from string import ascii_letters, digits, punctuation
def password_generator(pass_length:int,special_char:bool=False):
    '''improved password generator, now can return a longer length of password and explicit addition of all elements'''
    word_pool = ascii_letters + digits
    if pass_length < 8:
            return 'Minimum Length must be greater than 8'
    if special_char:
        word_pool += punctuation
        password = sample(ascii_letters,1) + sample(digits,1) + sample(punctuation,1)
        while len(password) < pass_length:
            password += sample(word_pool,1)
        return ''.join(password)
    else:
        password = sample(ascii_letters,1) + sample(digits,1)
        while len(password) < pass_length:
            password += sample(word_pool,1)
        return ''.join(password)

if __name__ == '__main__':
    print(password_generator(9,True))

            
        
