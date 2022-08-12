import wordle

wordle = wordle.wordle(5)

wordle.start()

while True:
    if wordle.num_attempts == 0:
        print(f"A palavra é {wordle.word}")
        break
    
    word = input("Digite sua palavra: ")
    response = wordle.check_word(word)
    if(response[0] == True):
        print(response[1])
        break
    else:
        print(f"{response[1]} : {wordle.num_attempts}")