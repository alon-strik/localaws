import requests
import json
# resp = requests.get("https://status.github.com/api/status.json")
# txt = resp.text
# obj = json.loads(txt)
#
# print(obj)
# print(type(obj))
# print(obj)
########################################################################

# class User(object):
#     def __init__(self, name, username, *args, **kwargs):
#         self.name = name
#         self.username = username
#
# import json
# j = json.loads('{"name": "John Smith", "username": "jsmith"}')
# u = User(**j)
# print (u.name)
########################################################################



#
# class AutoVar(object):
#   def __init__(self, data):
#       self.__dict__ = data
#
# json_data =  '{"a": "my data"}'
# data = json.loads(json_data)
#
# test = AutoVar(data)
# print (test.a)

class Something(object):
    @classmethod
    def _load_from_json(cls, blob):
        for k, v in blob.iteritems():
            setattr(cls, k, v)

