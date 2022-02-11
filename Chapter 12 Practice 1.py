# syntax for creating a dictionary

# dictionary_name = {key1:value1, key2:value2....}

# a dictionary using strings

countries = {"CA": "Canada",
             "US": "United States",
             "MX": "Mexico",
             "GB": "Great Britain"}

# numbers as keys and strings as values

numbers = {1: "One", 2: "Two", 3: "Three"}

# strings as key, values of mixed types

movie = {"name": "The Holy Grail",
         "year": 1975,
         "price": 9.99}


# An empty dictionary

book_catalog = {}

# Code that prints dictionary to the console

print(movie)


# syntax for accessing a value

# dictionary_name[key]

# Code that gets a value from a dictionary

country = countries["MX"]
print(country)

# Code that sets a value if the key is in the dictionary

countries["GB"] = "United Kingdom"

# Code the adds a key/value pair if the key isn't in the dictionary

countries["FR"] = "France"

# Syntax for checking whether a key is in a dictionary

# key in dictionary

code = "IE"
if code in countries:
    country = countries[code]
    print(country)
else:
    print("There is no country for this code: " + code)

# get() method of a dictionary object

# get(key[, default value])

# Code the uses the get() method

#country = countries.get("MX")
#country = countries.get("IE")
country = countries.get("IE", "Unknown")

print(country)

# Syntax for Deleting an item in dictionary

# del dictionary_name[key]

# Code that uses the del keyword to delete an item

# del countries["FR"]
# del countries["IE"]

# Code that checks if a key is in a dictionary before deleting the item

code = "IE"
if code in countries:
    country = countries[code]
    del countries[code]
    print(country + " was deleted.")
else:
    print("There is no country for this code: " + code)

# Two dictionary methods for deleting items

# pop(key[, default_value]) = returns the value of specified key & deletes the key/value pair
# clear() = Deletes all items

# Code that uses the pop() method to delete an item

#country = countries.pop("FR")
#country = countries.pop("IE")
#country = countries.pop("IE", "Unknown")

# print(country)
# print(countries)

# Code that uses the pop() method to prevent a KeyError from occuring
code = "IE"
country = countries.pop(code, "Unknown country")
print(country + " was deleted.")


# Code that uses the clear() method to delete all items

# countries.clear()

# print(countries)

# Three dictionary methods for getting all keys and values

# 1. Keys() = returns a view object that contains all the keys in the dictionary
# 2. items() = returns a view object that contains a tuple for each key/value pair in the dictionary
# 3. values() = returns a view object that contains all the values in the dictionary

# Code that loops through all keys and values

# for code in countries.keys():
#   print(code + "    " + countries[code])

# Another way to get the same results cos the default iterator contains keys

for code in countries:
    print(code + "    " + countries[code])
    

# Code that unpacks a tuple as it loops through all keys and values

for code, name in countries.items():
    print(code + "    " + name)

# Code that loops through all values

for name in countries.values():
    print(name)

# Built-in constructors for creating dictionaries and lists

# list(view) = Converts the specified view object to a list
# dict(list) = Converts the specified 2 Dimensional list or tuple to a dictionary.

# Code that converts the keys of a dictionary to a list and sorts them

countries = {"CA": "Canada",
             "US": "United States",
             "MX": "Mexico",
             "GB": "Great Britain"}
codes = list(countries.keys())
codes.sort()
for code in codes:
    print(code + "    " + countries[code])

# Code that converts a 2 Dimensional list to a dictionary

countries = [["GB", "United Kingdom"], ["NL", "Netherlands"], ["DE", "Germany"]]
countries = dict(countries)
print(countries)