import json
import os
f = open("Hello.json", "w")
train_data = {}
key = input("Enter training data name = ")
lst = []
new_lst = []
while 1:
    more = input("type y if you want to enter data = ")
    if more == "y":
        lst.clear()
        q = input("enter your question = ")
        a = input("enter your answer = ")
        lst.append(q)
        lst.append(a)
    else:
        break

    new_lst.append(lst)
    print(new_lst)
train_data[key] = new_lst
print(train_data)
r = json.dumps(train_data, indent=4, sort_keys=True)
f.write(r)
f.close()
