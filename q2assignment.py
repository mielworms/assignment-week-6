#loop each key in prices. each key, print the key along with the price stock numbers. 
price = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
# add stock 
stock = {
"banana":8,
"apple":0,
"orange":9,
"pear":2
}
#for loop now!!
for key in price:
    print(key)
    print(" price: %s " % price[key])
    print(" stock: %s " % stock[key])
    
   