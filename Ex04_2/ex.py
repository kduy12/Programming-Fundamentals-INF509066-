# 1.Write python program:
# a)Convert two lists into a dictionary
def convert_2_list_to_dict(a, b):
    res = {}
    for i in range(len(a)):
        res[a[i]]=b[i]
    return res

# b)Merge two Python dictionaries into one
def merge_dict(a, b):
    return a.update(b)

# c)Print the value of key ‘history’ from the below dict
#    {‘id’:4, ’history’:’sample’, ’price’:73}
def print_history():
    a = {'id':4, 'history':'sample', 'price':73}
    print(a['history'])

# a)Initialize dictionary with default values
def initialize_dict(keys, default_value):
    res = {}
    for key in keys:
        res[key] = default_value
    return res

# b)Create a dictionary by extracting the keys from a given dictionary
def copy_keys(my_dict, keys):
    res = {}
    for k in keys:
        if k in my_dict:
            res[k] = my_dict[k]
    return res

# c)Delete a list of keys from a dictionary
def delete_keys(my_dict, keys):
    for k in keys:
        if k in my_dict:
            del my_dict[k]
    return my_dict

# d)Check if a value exists in a dictionary
def is_in(my_dict, value):
    return value in my_dict.values()
# e)Rename key of a dictionary
def rename_keys(my_dict, old_key, new_key):
    tmp = my_dict[old_key]
    my_dict[new_key] = tmp
    del my_dict[old_key]
    return my_dict

# f)Get the key of a minimum value from the following dictionary
def dict_min(my_dict = {'a':4, 'b':18, 'c':73}):
    min = list(my_dict.values())[0]
    for k in my_dict.keys():
        if my_dict[k] < min:
            min = my_dict[k]
    return min

# a)Change value of a key in a nested dictionary
def change_value(my_dict, target_key, new_value):
    for k, v in my_dict.items():
        if k == target_key:
            my_dict[k] = new_value
        elif type(v) == dict:
            change_value(v, target_key, new_value)
    return my_dict

#2.Write a Python program that counts the number of times characters
# appear in a text paragraph and its appearing positions.
def chars_count(my_dict):
 #tao mot dict co key la char va value la mot dict gom so lan xuat hien va list vi tri
    res = {}
    cnt = 1
    for char in my_dict:
        if char not in res:
            tmp = {'freq':1, 'pos':[cnt]}
            res[char] = tmp
        else:
            res[char]['freq'] += 1
            res[char]['pos'].append(cnt)
        cnt += 1

    return res







# 3.Write a program using a dictionary containing keys starting from 1
# and values​​containing prime numbers less than a value N.
def prime_dict(n):
    res = {}
    def is_prime(num):
        from math import isqrt
        if num < 2:
            return False
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    i = 1
    num = 1
    while (n):
        if is_prime(num):
            res[i] = num
            i += 1
        n -= 1
        num += 1

    return res

if __name__ == '__main__':
    print(chars_count('hello'))









