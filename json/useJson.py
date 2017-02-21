import json

## JSON to PYTHON
print "JSON to PYTHON\n---------------"
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)
print jsonToPython
print jsonToPython['name'],
print jsonToPython['age']

## PYTHON to JSON
print "\nPYTHON to JSON\n---------------"
pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)
print dictionaryToJson

##################################################################

class Employee(object):
    def __init__(self, name):
        self.name = name

def jsonDefault(object):
    return object.__dict__

abder = Employee('Abder')
jsonAbder = json.dumps(abder, default=jsonDefault)
print jsonAbder