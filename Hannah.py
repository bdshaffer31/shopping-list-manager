good_words = ['happy','better']

introduction = input('hello\n')
if introduction == "hi": 
    response = input('How are you\n')
    if response == "bad" or response== "sad" or response == "bored":
        response = input('why\n')
    elif response == "good" or response =="happy" or response == "great":
        response = input('yay!\n')
    else: 
        response = input('I do not understand. Are you happy or sad?')
        if response == "happy":
            response = input('yay!\n')
            if response == "how are you" or response== "thanks for asking" or response == "yay!":
                response = input('have a nice day!\n')
        elif response == "sad":
            response = input('oh noooooo\n')
            if response == "you are just a robot why do you care":
                response = input('I love you\n')
            else:
                response = input('I hope you feel better\n')
            
            