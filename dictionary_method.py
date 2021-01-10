myDict = {

    "fast"            : "very fast",
    "slow"            : "very slow",
    "shubham vishnoi" : "tushar vishnoi",
    "golu"            : "pashu vishnoi",
}

# dictionary method ...
#print(myDict.keys())   # prints the keys of the dictionary...

               #print(list(myDict.keys()))
               #print(type(myDict.keys()))
#print(myDict.values())    # print the value of the dictionary...

#print(myDict.items())    # prints the (key, value)  for all items of the dictionary...

#updateDict = {
#      "lovish"   : "friends",
#      "sangeeta" : "girlfriend",
#      "golu"     : "rajan vishnoi",   # purane wale ko bhi ye change kar dega yaha par according to the users choices...
#  }
# myDict.update(updateDict)    # update the dictionary by adding key-value pairs from updateDict
# print(myDict)



print(myDict.get("slow"))       # print value associated with key value
print(myDict["slow"])           # print value associated with key value
#   the difference between .get and [] syntax in dictionaries..
print(myDict.get("slow1"))       # return none   as slow is not present in the dictionary(interview question )
print(myDict["slow1"])           # through error  as slow is not present in the dictionary(interview question)
 