import random
word_list=("apple","banana","mango")
word=random.choice(word_list)
def scramble(word):
    str_list=list(word)
    random.shuffle(str_list)
    newWord=''.join(str_list)
    return newWord
print("welcome to the word scramble game ")
print("try to guess the original word")
print(scramble(word))
print("you have 5 attempts")
x=5
while x:
    print("enter your guess")
    myGuess=input()
    if(myGuess==word):
        print("congratulation ,you have guessed the word")
        break
    else:
        x-=1
        print("incorrect guess")
    