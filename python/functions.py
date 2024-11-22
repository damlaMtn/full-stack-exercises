def div(a, b):
    return a / b

div(10,2)

#--------------------

def con(a, b):
    return(a + b)

con("2", "2")
con((1,2,3,4),(5,6,7))
con(['a', 1], ['b', 1])


def findKey(string, passedKey):
    words = []
    words = string.split()
    Dict = {}
    for key in words:
        if(key == passedKey):
            Dict[key] = words.count(key)
    print("Total Count:",Dict)

findKey("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go", "little")