#add groceries 
groceries = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# the value is 0 in the beginning so u gotta add the values
def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
        return total
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(food):
    total = 0 
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -=1
            return total 

    
