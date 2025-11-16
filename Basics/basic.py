import sys
from decimal import Decimal as dec #designed for huge number of fraction values
from fractions import Fraction as frac
globalVar = 45
class Person:
    def __init__(self, firstName,lastName):
        self.fName = firstName
        self.lName = lastName
        print('constructor called and details setup as ',self.fName + ' ' +self.lName)

    def setAddress(self, address):
        self.Address = address
        print('address setup successfully as - ',self.Address)

    '''
    Everything in Python is an object.
    The id() function returns a unique id for the specified object. 
    All objects in Python has its own unique id. The id is assigned to the object when it is created. 
    The id is the object's memory address, and will be different for each time you run the program.
    value types are immutable. complex types are mutable.
    If something is immutable eg: when x holds value 20 then its id will change if value changes
    since original value was immutable and hence on change of x python created a new memory location to hold new value.
    Original value never changes.
    If something is mutable, then even if value is changed in a variable, its id doesnt change ie 
    variable memory location still stay the same and underlying value changes
    '''

    def checkMutabilityAndImmutability(self):
        x = 10
        print(f" variable x has id of {id(x)} and it holds value {x} and id of its value itself is {id(10)}")
        x = 20
        print(f" variable x has id of {id(x)} and it holds value {x} and id of its value itself is {id(20)}")
        print(f"just checking what is id of x variable again {id(x)} and type of x is {type(x)}")
        # checking address or id of something that doesnt exists in program. But as soon as we write it is exists in 
        # program as well. 
        print(f"id of 30 is {id(30)}")
        # Mutable types
        s = set()
        print(f" set is {s} id of set type is {id(s)}")
        s.add('kunal') # we make change to the value of the type
        print(f" set is {s} id of set type is {id(s)}") #stay the same after change too
        # checking for strings
        print(f"id of kunal is {id('kunal')}")
        print(f"id of bharat is {id('bharat')}")
        print(f"id of kunal is {id('kunal')}")
        #special case of upcasting between bollean and integer
        x = 10
        y = True # will be treated as 1
        print(f"after upcasting of boolean value sum is {x+y}")
        #similarly we can do something like this too
        isBoiling = 10 #  any positive or negative number except 0 ie treated as value exists.
        print(f"boiling state was {bool(isBoiling)}")
        isBoiling = 0 #  0 is treated as False
        print(f"boiling state was {bool(isBoiling)}")
        isBoiling = '' #  no value is also treated as False
        print(f"boiling state was {bool(isBoiling)}")       
        isBoiling = None #  None is also false
        print(f"boiling state as None was {bool(isBoiling)}") 
        isBoiling = 'kunal' #  any value presence is treated as True
        print(f"boiling state was {bool(isBoiling)}")   
        isBoiling = set() #  any complex type without value is treated as False
        print(f"boiling state when set as complex type was {bool(isBoiling)}") 
        isBoiling = set('kunal') #  any complex type with value is treated as True
        print(f"boiling state when set as complex type was {bool(isBoiling)}") 
        #and , or , not usual stuff

    def someExamples(self):
        print(sys.float_info)
        print()
    
    def handleStringType(self):
        #strings are immutable as other value types
        x = "coffee and chocola"
        print(x[0:6]) #on every 1 character
        print(x[0:len(x):2])#on every 2nd elements
        print(x[::-1])#reverse, -1 is ending index
        #encoding and decoding used for special characters and multilingual systems
        someText = "Hi this is kunäl"
        print(someText.encode("utf-8")) #this will ensure that data is handled in system correctly
        #b'Hi this is kun\xc3\xa4l'
        #to print we have to decode
        print(someText.encode("utf-8").decode("utf-8"))

    def handleTuples(self): # (..) - immutable so cant be changed
        spices = ('ginger','garlic','cardamum')
        (spice1,spice2,spice3) = spices
        print(f"spices are {spice1}, {spice2}, {spice3}")
        #example of value swap
        x,y = 10,20  #under the hood this looks like tuple destructing
        print(f"x is {x} and y is {y}")
        x,y = y,x
        print(f"x is {x} and y is {y}")
        #membership testing
        print(f"Is ginger in spices? {'ginger' in spices}") #exact match and membership check

    def handleLists(self): #[..], mutable type
        spices = ["ginger",'garlic','cloves']
        spices.append("cardamum")
        spices.insert(1,"fennel seeds")
        sweets = ['sugar','shakkar','jaggery']
        spices.extend(sweets)
        print("spices are ",spices)
        spices.sort()
        spices.reverse()
        print("spices are ",spices)
        # + also work to concat lists. this is kind of  operator overloading built in for this type
        listconcat = spices + sweets
        print("spices are ",listconcat)
        #  * usage
        print(f"spices are {spices * 3}")
        #min max etc
        x = [1,2,3,4,5]
        print(f"min is {min(x)} and max is {max(x)}")
        x.pop()
        print("list after pop is ", x)

    def handleSets(self): #{..}- mutable
        set1 = {1,2,3,4,5}
        set2 = {1,4,7,8,9}
        print(set1.union(set2))
        print(set1 | set2) #also for union
        print(set1.intersection(set2))
        print(set1 & set2) #also intersect or common part
        print(set1.difference(set2))
        print(set1 - set2) #also diff
        #membership test
        print("if exists in set", 11 in set1)
        #to make immutable unordered set
        set3 = frozenset({1,2,3,4,5}) #no add, update methods here
        print("frozen set is", set3)

    def handleDictionary(self): #key-value pairs,mutable, named based indexing system
        print("type of {} is ",type({}))
        print("type of {1,2,3} is ",type({1,2,3}))
        print("type of dict(a=1,b=2,c=3) is ",type(dict(a=1,b=2,c=3)))
        x = {"a":1,"b":2,"c":3}
        print("type of {'a':1,'b':2,'c':3} is ",type({"a":1,"b":2,"c":3}))
        #x = {a:1,b:2,c:3} - this is incorrect since keys are acting as variables like this and will throw error
        print("type of {a=1,b=2,c=3} is ",type({"a":1,"b":2,"c":3}))
        print("type of [] is ",type([]))
        print("type of () is ",type(()))
        #general dictionary usage
        teaProcess = {}
        teaProcess["hasMilk"]=True
        teaProcess["WaterQuan"]=1
        teaProcess["SugarInGrams"]=20
        teaProcess["name"]="Masala Chai"
        print("tea making process has ", teaProcess)
        del teaProcess["hasMilk"]
        print("tea making process without milk has ", teaProcess)
        #another special case where we check can a complex thing be dict key. although doesnt make sense
        x = (1,2,3,4)
        y = {x:"kunal"}
        print(dict[x])
        #membership test is same
        print("tea has sugar ", 'SugarInGrams' in teaProcess)
        print(teaProcess.keys())
        print(teaProcess.values())
        print(f"tea process is {teaProcess.items()} each item has type as { type(teaProcess.items()) }")
        lastItem = teaProcess.popitem() #last item removed from original dictionary
        print(lastItem)
        print(teaProcess)
        teaProcess["name"]="masala chai"
        newDic = dict(name="just chai", newKey = 999)
        teaProcess.update(newDic) #original dict got updated where keys matched AND any new key-value got added
        print(teaProcess)

    def EnumerateExample(self):  # has yield return approach
        lst = ["kunal","bharat","anshum","kaayna","jenissa","all"]
        print(list(enumerate(lst,start=2))) #we can use list, tuple to cast it
        for index,name in enumerate(lst,start=1):
            print(f"for order {index} and for customer {name} food is ready")
    
    def usingZipToCombineInformation(self): #generate tuples by combining all passed items. Extra items are not considered.
        names = ["kunal","anshum","kanu","jenni"]
        ids = [1,2,3,4]
        for item in zip(ids,names):
            print(f"individual person information as tuple is {item}")
            if 5 in item:
                break
        else:
            print("this is loop fallback and will only be executed if loop never got broken by break statement")


    def usingWalrusOperator(self): 
        # := where we define variable directly inline and assign value to it as well and using it in an expression directly
        selectedCandidates = ["kunal","anshum","kanu","jenni"]
        if newGuy := input("enter candidate name") in selectedCandidates:
            print(f"candidate {newGuy} is part of selected candidates")
        else:
            print("not selected")

    globalVar = 10 #global scope
    def checkScopes(self):
        globalVar = 20 #local scope or can be enclosing scope
        print("global var value under enclosing scope is ", globalVar)
        def innerFunc():  #function inside a function 
            nonlocal globalVar  #referring to enclosed scope variable just above current scope. If not there then error.
            # the nonlocal keyword lets you declare a variable in a nested function as not local to that function. 
            # It allows you to modify variables defined in the enclosing scope from within an inner function.
            globalVar = 30
            print("global var value under local scope is ", globalVar)
            def innerMostFunc():
                global globalVar  #impure function since it access global variables
                globalVar = 15  #setting global scope variable 
            innerMostFunc()
        innerFunc()
        print("global var value after it was updated under child function is ", globalVar)

    #*args is used for passing positional arguments, **kwargs is used for passing keyword arguments
    def TestingPositionalANDKeywordArgumentsInAFunction(self, *positionalArgs, **keywordArgs): # *args and **kwargs
        print(f"positionalArgs are regular positional arguments and type of standard args is {type(positionalArgs)}")
        print(positionalArgs)
        print(f"keywordArgs are keyword arguments and type of them is  {type(keywordArgs)}")
        print(keywordArgs)
        # we can set default value for method params too in general or set it to None as well if we know state may change
        # we can check if param is None:  etc
    
    def TestMultiReturns(self):
        x,y = 10,20 #we can initialize multiple variables in same line in an order.
        print(f"x is {x} and y is {y}")
        return 10, 20 #method return multiple values at same time possible

    def TestLambdaFunction(self):
        names = ["kunal","anshum","kanu","jeenu","kunal","kanu"]
        namesWithKunal = filter(lambda name: name=="kunal",names) #yield return an iterator for which passed function(item) or lambda is true ie predicate return true
        print("type of filter is ",type(namesWithKunal))
        print(list(namesWithKunal))
        namesWithNoKunu = filter(lambda name: name!="kanu",names)
        print(list(namesWithNoKunu))
        print("type of filter is ",type(namesWithNoKunu))

    def UseDocStringsInFunctions(self, param1):
        """
        Method shows ample of doc strings that should be very first statement
        :param1: first parameter passed
        :return: (a small message)

        """
        print(param1)


man = Person('kunal','sehgal')
man.setAddress("utrecht address")
man.checkMutabilityAndImmutability()
man.handleStringType()
man.handleTuples()
man.handleLists()
man.handleSets()
man.handleDictionary()
man.EnumerateExample()
man.usingZipToCombineInformation()
man.usingWalrusOperator()
man.checkScopes()
print("global var value global scope level is now ", globalVar)
man.TestingPositionalANDKeywordArgumentsInAFunction("water","milk","sugar","tea", foam=True, ExtraSugar=True, GlassCup="Required")
x,y = man.TestMultiReturns()
print(f"reading multiple return values in one line with x is {x} and y is {y}")
#pure functions - that do not manipulate or access global scope variables
man.TestLambdaFunction()
'''
Functions that don't modify their arguments or produce any other side-effects are called pure. 
Functions that modify their arguments or cause other actions to occur are called impure
'''
man.UseDocStringsInFunctions(param1=10)
print(Person.UseDocStringsInFunctions.__doc__) #dunder doc function called .__xxx__ are called dunder functions

#import approaches
import Parent1.Functionality1.utilities as utils #import whole module
print('sum result is ',utils.sum(10,20))

from Parent1.Functionality2 import utilities2 as u
print('div result is ' , u.divide(100,10))

from Parent2.Functionality1.utilities import minus as m #specific imports
print('minus result is ', m(30,10))



