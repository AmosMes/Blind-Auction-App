from art import logo
import os
print(logo)
biddings = {}
finished_bidding = False

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while not finished_bidding:
    
    name = input("What is you\'re name? ").lower()
    bid = int(input("What is you\'re biding price? $"))
    biddings[name] = bid
    answer = input('Is there anyone else who would like to bid? type "yes" or "no". ')   

    if answer == "no":
        finished_bidding = True
        find_max = max(biddings, key=biddings.get)
        #print(find_max, biddings[find_max])
        print(f"Bidding is finised, the winner is {find_max} for ${biddings[find_max]}.")
    elif answer == "yes":
        clearConsole()
        print(logo)
