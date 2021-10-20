dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

dict2= {
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": True,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": None
}

print(dict2["address"]["state"])

print(dict2["phoneNumbers"][1]["number"])

dict2["phoneNumbers"].append({
  "type": "private",
  "number" : "696 420-6969"
})

for e in dict2["phoneNumbers"]:
  print(e)
  
"""
dictionary["bird"] = "canary"
# del dictionary["cat"]

for k,v in dictionary.items():
    print(k,v)
    

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
"""