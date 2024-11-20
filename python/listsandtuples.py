a_list = [1, "hello", [1, 2, 3], True]
a_list[1]
a_list[1:4]
A = [1, "a"]
B = [2, 1, "d"]
A + B

##

shopping_list = ["watch", "laptop", "shoes", "pen", "clothes"]
shopping_list.append("Football")
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list)
print(shopping_list[1:3])
shopping_list[3] = "notebook"
print(shopping_list)
del(shopping_list[4])
print(shopping_list)

#######################################################

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple
len(genres_tuple)
genres_tuple[3]
genres_tuple[3:6]
genres_tuple[0:2]
"disco".find('s')

C_tuple=(-5, 1, -3)
sorted(C_tuple)