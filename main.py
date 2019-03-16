## this is the main cli tool
## NLPK v 0.1
#display the main options
import bootstrap.py
import tokenizer.py

print("Welcome to NLPK")
while True:
    choice = input("choose one of the following options: ")
    bootstrap.displayMenu()
    if choice == "tokenizer":
        runTokenizer()