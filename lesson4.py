# ЦИКЛЫ

# for / while

# some_list = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 34]    # [index start 0]

# for i in some_list:
#     print(f'element {i}')

some_str = '1,-,2,-,3,-,4,-,5,-,6,-,7,-,8,-,9,-,10'

# for i in some_str[0:48:4]:
#     if i == '1' and some_str.index(i) != 0:
#         print(10)
#     else:
#         print(f'element {i} index is {some_str.index(i)}')

some_list = some_str.split(',-,')

# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# for i in some_list:
#     # index = some_list.index(i)
#     # i = int(i)*2
#     # some_list[index] = i
#     some_list[some_list.index(i)] = int(i)*2


# for i in range(0, len(some_list)):
#     some_list[i] = int(some_list[i]) + 5

new_str = '; '.join(some_list)

print(new_str)