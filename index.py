import random
import json
shares = []
def risk():
    scores = []
    for x in range(10):
        risky = random.uniform(0.1, 0.9) #calculates the risk involed just random
        scores.append(risky)
    myList = []
    for x in range(len(shares[0])): 
        num1 = shares[0][x] * scores[x] #risk * price = value
        myList.append(int(num1))
    shares.insert(1, myList)
def price(): 
    priceStocks = []
    for x in range(10): 
        num1 = random.randrange(1, 100) #price of the stock
        priceStocks.append(num1)
    shares.insert(0, priceStocks)
    risk()
price()
def tag(): 
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "x", "z"]
    stocks = []
    for x in range(10):
        myList = []
        for x in range(3): 
            num1 = random.randrange(0, len(letters)-1) #stock tag
            myList.append(letters[num1])
        newWord = "".join(myList)
        stocks.append(newWord) 
    shares.insert(2, stocks)
tag()
value = []
for x in range(len(shares[0])): 
    value.append(shares[0][x] - shares[1][x]) #value of the stock price - risk
tags = []
for x in range(len(shares[len(shares)-1])): 
    tags.append(shares[len(shares)-1][x])
f = open("index.txt", "w")
for x in range(len(value)): 
    f.write("stock tag " + str(tags[x]) + " at $" + str(value[x]))
    f.write("\n")
f.close()
