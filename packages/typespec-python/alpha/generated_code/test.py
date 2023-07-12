import json
from testunion.models import Animals, Cat, Dog
from testunion._model_base import AzureJSONEncoder, _deserialize

# Test serialize
model_cat = Animals(content=[Cat(eat_fish=True)])
model_dog = Animals(content=[Dog(eat_bone=True)])

print(json.dumps(model_cat, cls=AzureJSONEncoder)) # ok
print(json.dumps(model_dog, cls=AzureJSONEncoder)) # ok

# Test deserialize
response_cat = {"content": [{"eatFish": True}]}
response_dog = {"content": [{"eatBone": True}]}

deserialize_cat = _deserialize(Animals, response_cat)
deserialize_dog = _deserialize(Animals, response_dog)

print(deserialize_cat) # OK
print(deserialize_dog) # OK

print(deserialize_cat.content[0].eat_fish) # OK
print(deserialize_dog.content[0].eat_bone) # no
