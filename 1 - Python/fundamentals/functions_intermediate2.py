#1 Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
# Change the value 20 in z to 30
z[0]['y'] = 30


#2 Iterate Through a List of Dictionaries
students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iteratedictionary(some_list):
    for k in some_list:
        print(k)

print(iteratedictionary(students))


#3 Get Values From a List of Dictionaries
def iteratedictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        for key, val in some_list[i].items():
            if key == key_name:
                print(val)

print(iteratedictionary2('first_name', students))


#4 Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val), key)
        for i in range(len(val)):
            print(val[i])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)