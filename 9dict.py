# your_dict={'key':'value',....}
# dict not use index 

# user1={'name':"Chirag",'age':52}
# print(user1)

# which type of data dict can store 
# list tuple int char string set dict

# user_info={
#     'name':"Chirag",
#     'age':85,
#     'Fav_movie':['DDLJ','COCO'],
#     'Hobbies':['game','movie'],
# }
# print(user_info)

# print(type(user_info))

# Add the data in dict 

# user_info={}
# user_info['Name']="Chirag"
# user_info['age']=90

# print(user_info)


user_info={
    'name':"Chirag",
    'age':85,
    'Fav_movie':['DDLJ','COCO'],
    'Hobbies':['game','movie'],
}

# {'name': 'Chirag', 'age': 85, 'Fav_movie': ['DDLJ', 'COCO'], 'Hobbies': ['game', 'movie']}
# user_info['name']="DDD"
# print(user_info)#{'name': 'DDD', 'age': 85, 'Fav_movie': ['DDLJ', 'COCO'], 'Hobbies': ['game', 'movie']}

# in keyword dict 

# for key 
# if 'name' in user_info:
#     print("Yes")
# else:
#     print("No")

# for value 

# if 'Chirag' in user_info.values():
#     print("Yes")
# else:
#     print("No")

# loop in dict 

# for key 

# for i in user_info:
#     print(i)

# for value 
# print(user_info['name'])

# 1st to get value 
# for i in user_info:
#      print(user_info[i])

# for i in user_info.values():
#     print(i)



# values() method  

# user_info_values=user_info.values()
# print(user_info_values)


# keys() method 
 
# user_info_keys=user_info.keys()
# print(user_info_keys)


# item() method

# user_info_items=user_info.items()
# print(user_info_items)

# item method using loop 
# for key,value in user_info.items():
#     print(f"this is key {key} and value is {value}")

# for i in user_info.items():
#     print(type(i))

# for i in user_info.items():
#     for j in i:
#         print(j)
    

# dict in len 
# print(len(user_info))

# remove method in dict 
# pop method 
# user_info.pop('name')
# print(user_info)

# popitem 
# user_info.popitem()

# del method
# print(user_info)
 
# del user_info['name']
# print(user_info)

# copy()  method 
# user_info_copy=user_info.copy()
# print(user_info_copy)


# user_info.clear()
# print(user_info)







