dict={
    'name':"USman",
    'neigh':"Ali",
    'friend':"Ahmed"
}
print(dict)
print(dict['name'])
print(dict['neigh'])
print(dict['friend'])
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get(1))    #none throwing automa error
print(dict.get(4, "Not Found"))  # Default value if key not found
print(type(dict))
for i in dict.keys():
    print(dict[i])