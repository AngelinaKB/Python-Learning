import random 

low = 1
high = 100

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(low, high) # random number between given range 
print(number)

num = random.random() # random floating point number 
print(num)

options = random.choice(options) # random choice 
print(options)

shuffle =  random.shuffle(cards) # shuffle deck randomly 
print(cards)
