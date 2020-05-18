# word counter

def word_counter(s):
    word ={}
    for char in s:
        word[char]=s.count(char)
    return word

user_inp = input("Enter a string:- ").strip()
print(word_counter(user_inp))
# {'N': 1, 'i': 2, 't': 1, 'n': 1}