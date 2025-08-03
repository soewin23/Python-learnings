        # Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

Dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "active": True
}

x = Dict["model"]
print(x)#Mustang
"""Or"""
# also have the method get()
y = Dict.get("model")
print(y)#Mustang


"""to add new items in Dict"""
Dict = {"brand": "Ford","model": "Mustang","year": 1964,"active": True}

Dict["color"]  = "White"

print(Dict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'active': True, 'color': 'White'}

# to get the key of a dict Using 
""""       keys()"""
b = Dict.keys()
print(b)#dict_keys(['brand', 'model', 'year', 'active'])

# to get the value of Dict 
c =Dict.values()
print(c)#dict_values(['Ford', 'Mustang', 1964, True])


#       Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

dict = {"name":"Soe Win", "Age":18,"year": 2007, "Male":True}
c = dict.items()
print(c)#dict_items([('name', 'Soe Win'), ('Age', 18), ('year', 2007), ('Male', True)])
print(c)
dict["abc"]= "red"
print(dict)

# to check if the keys is in the dict

if "name"in dict:
    print("Yes, it has")


