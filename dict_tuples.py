"""
1. We have the following information on countries and their population (population is in crores),

    |Country|Population|
    |-------|----------|
    |China|143|
    |India|136|
    |USA|32|
    |Pakistan|21|
    1. Using above create a dictionary of countries and its population
    2. Write a program that asks user for three type of inputs,
        1. print: if user enter print then it should print all countries with their population in this format,
            ```
            china==>143
            india==>136
            usa==>32
            pakistan==>21
            ```
        1. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
        2. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
        3. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
"""


import math

d = {
    'China': 143,
    'India': 136,
    'USA': 32,
    'Pakistan': 21
}

inp = input()

if inp == 'print':
    print(d)
elif inp == 'add':
    country_name = input()
    if country_name in d:
        print('country name exist')
    else:
        population = input()
        d[country_name] = int(population)
        print(d)
elif inp == 'remove':
    country_name = input()
    if country_name in d:
        del d[country_name]
        print(d)
    else:
        print("country name doesn't exist")
else:
    country_name = input()
    print(d[country_name])

"""
2. You are given following list of stocks and their prices in last 3 days,

    |Stock|Prices|
    |-------|----------|
    |info|[600,630,620]|
    |ril|[1430,1490,1567]|
    |mtl|[234,180,160]|

    1. Write a program that asks user for operation. Value of operations could be,
        1. print: When user enters print it should print following,
            ```
            info ==> [600, 630, 620] ==> avg:  616.67
            ril ==> [1430, 1490, 1567] ==> avg:  1495.67
            mtl ==> [234, 180, 160] ==> avg:  191.33
            ```
        2. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks
"""

d = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

inp = input()

if inp == 'print':
    print(d)
elif inp == 'add':
    c_name = input()
    if c_name in d:
        prices = input()
        d[c_name].append(prices)
        print(d)
    else:
        l = []
        prices = int(input())
        l.append(prices)
        d[c_name] = l
        print(d)

"""
3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them
"""


def circle_calc(r):
    return math.pi * r * r, 2 * math.pi * r, 2 * r


a, b, c = circle_calc(2)
print(a, b, c)