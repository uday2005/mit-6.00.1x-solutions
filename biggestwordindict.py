
def largest_so_far(aDict):
    biggest = ""
    for k in  aDict: # iterate over the dict key
        for words in aDict[k]: # iterat eover string of key of loops
            if len(words) > len(biggest):
                biggest = words

    return biggest

animals = { 'a': ['aarlkbifvfsgursi'], 'b': ['baboonjgh'], 'c': ['coati'],'d':['donkey'] }
why = largest_so_far(animals)

print(why)

