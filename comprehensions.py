'''
for filtering - transforming items/objects - flatten nested items - create new collections
used with lists - sets - dictionaries
. Better than loops by reducing code and make it more cleaner and understanble.
Sometimes faster as well.
Also it is more functional style of coding.
IMP - there are Generator comprehensionas as well for memory optimisation.

'''
#list based 
teamTypes = ["ice tea","ice tea with choco","hot tea","lipton ice team macha","choco tea"]
iceOnly = [tea for tea in teamTypes if "ice" in tea]
print(iceOnly)

iceOnly = [tea.upper() for tea in teamTypes if "ice" in tea]
print(iceOnly)

#set based
objects = {"tea","milk","sugar","pan","cardamam","tea","cloves","cinnaman"}
objs = {item for item in objects} #works ??can we loop over sets too?
print(objs)

#making set out of disctionary
teamtypes = {
    "masala tea": ["cloves","tea","milk","sugar","extraSpices"],
    "ice tea": ["icecubes","tea","sugar"],
    "black tea":["tea","water"]
}

uniqueIngredients = {item for ingredient in teamtypes.values() for item in ingredient}
print("unique ingredients are ", uniqueIngredients)

#dictionary based
teaPricesInINR = {
    "masala tea": 100,
    "ice tea": 250,
    "black tea": 80,
     "Hard black tea": 800,
      "Macha tea": 1000
}

teaPricesInUSD = {teaType:inrPrice/80 for teaType,inrPrice in teaPricesInINR.items() if inrPrice < 1000}
print(teaPricesInUSD)


#generator based comprehensions - (..) best for high memory requirements where we dont want
# to calculate and load everything into buffer to do something. example in stream based operations
# where system read values as they arrive and then perform operations.

teaPricesInINR = {
    "masala tea": 100,
    "ice tea": 250,
    "black tea": 80,
     "Hard black tea": 800,
      "Macha tea": 1000
}

teaPricesInUSD = (inrPrice/80 for teaType,inrPrice in teaPricesInINR.items() if inrPrice < 1000)
print(teaPricesInUSD)  #this will not run but print generator type
print(next(teaPricesInUSD))
print(next(teaPricesInUSD))
print(next(teaPricesInUSD))
print(next(teaPricesInUSD))
try:
    print(next(teaPricesInUSD)) #finally throw error
except:
    print("finally error caught")

#IMP - if we call aggregate method or something on generator directly then it will execute
teaPricesInUSD = sum(inrPrice/80 for teaType,inrPrice in teaPricesInINR.items() if inrPrice < 1000)
print(teaPricesInUSD)  #now this will give us value but under the hood it kept summing as values came in

