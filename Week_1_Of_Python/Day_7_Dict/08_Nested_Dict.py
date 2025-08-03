# Nested Dictionaries

# means dictionaries inside Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# To Access Items in Nested Dictionaries
print(myfamily["child1"]["name"])#Emil


# looping the nested Dicts
# Using items() methods

for i, y in myfamily.items():
    print(i)
    for x in y:
        print(x , ":",y[x])