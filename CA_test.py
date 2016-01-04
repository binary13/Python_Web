prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0
for key in prices:
    num = prices[key] * stock[key]
    print('You have {} {}s worth a total of ${:4.2f}'.format(stock[key], key, num))
    total += num

print('The total worth of your inventory is ${:5.2f}.'.format(total))
