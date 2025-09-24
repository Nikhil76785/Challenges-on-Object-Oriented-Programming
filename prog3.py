import random

class FruitQuiz:

    def __init__(self):
        self.fruits = {
            'Apple': 'red',
            'Orange': 'orange',
            'Watermelon': 'green',
            'Banana': 'yellow'
        }

    def quiz(self):
        while(True):
            fruit, colour = random.choice(list(self.fruits.items()))
            print(f"What is the colour of {fruit}")
            user_ans = input()
            
            if(user_ans.lower() == colour):
                print("Correct Answer")
            else:
                print("Wrong Answer")
            
            opt = int(input("Enter 0 if you want to play again otherwise enter 1: "))
            if(opt):
                break

print("Welcome to fruit quiz.")
obj = FruitQuiz()
obj.quiz()