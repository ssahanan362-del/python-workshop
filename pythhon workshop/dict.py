data = {"name": "tomy", "Age": 23, "gender": "female", "country": "india"}
print(data)
print(type(data))

data["Age"] = 25
print(data)

print(data.values())
print(data.keys())


data.update({"Name": "tomy", "name": "jerry"})
print(data)
