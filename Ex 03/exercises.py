# 1. Write a Python program to sum all the items in a list.
def sum_list(lst):
    res = 0.0
    for i in lst:
        res += i
    return res


# 2. Write a Python program to multiply all the items in a list.
def multiply_lst(lst):
    res = 1.0
    for i in lst:
        res *= i
    return res


# 3. Write a Python program to get the largest number from a list
def largest_number(lst):
    res = lst[0]
    for i in lst:
        res = i if i > res else res
    return res


# 4. Write a Python program to get the smallest number from a list
def smallest_number(lst):
    res = lst[0]
    for i in lst:
        res = i if i < res else res
    return res


# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def string_count(lst):
    res = 0

    def is_string(s):
        if len(s) >= 2 and (s[0] == s[-1]):
            return True
        return False

    for i in lst:
        if is_string(i):
            res += 1

    return res


# 6. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def sort_by_last_element(lst):
    return sorted(lst, key=lambda x: x[-1])


# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))


# 8. Write a Python program to check if a list is empty or not
def is_empty(lst):
    return len(lst) == 0


# 9. Write a Python program to clone or copy a list.
def copy_list(lst):
    return lst.copy()


# 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.
def words_longer_than_n(lst, n):
    res = []
    for word in lst:
        if len(word) > n:
            res.append(word)
    return res


# 11. Write a Python function that takes two lists and returns True if they have at
# least one common member.
def is_common(lstA, lstB):
    return len(set(lstA) & set(lstB)) > 0


# 12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def remove_0_4_5(lst):
    new_lst = lst[1:4] + lst[6:]
    print(new_lst)
    return new_lst


# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
def generate_star_3Darray():
    k = []
    for _ in range(6):
        k.append('*')
    j = []
    for _ in range(4):
        j.append(copy_list(k))
    i = []
    for _ in range(3):
        i.append(copy_list(j))
    return i


# 14. Write a Python program to print the numbers of a specified list after removing
# even numbers from it.
def remove_even(lst):
    new_lst = []
    for i in lst:
        if type(i) is not int:
            new_lst.append(i)
        else:
            if (i % 2 != 0):
                new_lst.append(i)
    print(new_lst)
    return new_lst


# 15. Write a Python program to shuffle and print a specified list.
def shuffle_list(lst):
    import random
    shuffled = copy_list(lst)
    random.shuffle(shuffled)
    print(shuffled)
    return shuffled


# 16. Write a Python program to generate and print a list of the first and last 5
# elements where the values are square numbers between 1 and 30 (both
# included).
def square_list():
    import math
    def is_square(n):
        root = int(math.sqrt(n))
        return root ** 2 == n

    lst = []
    for i in range(1, 31):
        if (is_square(i)):
            lst.append(i)
    res = lst[:5] + lst[-5:]
    print(res)
    return res


# 17. Write a Python program to check if each number is prime in a given list of
# numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> Fals

def is_prime_list(lst):
    import math
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    for i in lst:
        if not is_prime(i):
            return False
    return True


# 18. Write a Python program to generate all permutations of a list in Python.
def permutation(lst):
    permu, res = [], []

    def search(n):
        if (n == len(lst)):
            res.append(copy_list(permu))
            return
        for i in lst:
            if i not in permu:
                permu.append(i)
                search(n + 1)
                permu.pop()

    search(0)
    return res


# 19. Write a Python program to calculate the difference between the two lists.
def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))


# 20. Write a Python program to access the index of a list
def index_access(lst):
    for i in range(len(lst)):
        print(f"Index:{i}, value:{lst[i]}")


# 21. Write a Python program to convert a list of characters into a string.
def list_to_string(lst):
    return ''.join(str(x) for x in lst)


# 22. Write a Python program to find the index of an item in a specified list.
def find_index(lst, value):
    return lst.index(value) if value in lst else -1


# 23. Write a Python program to flatten a shallow list.
def flatten_list(lst):
    res = []
    for sublist in lst:
        for i in sublist:
            res.append(i)
    return res


# 24. Write a Python program to append a list to the second list.
def append_list_to_list(lst1, lst2):
    lst2 = lst2.extend(lst1)
    return lst2


# 25. Write a Python program to select an item randomly from a list
def random_item(lst):
    import random
    random_index = random.randint(0, len(lst) - 1)
    return lst[random_index]


# 26. Write a Python program to check whether two lists are circularly identical.
def is_circular_identical(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    doubled = lst1 + lst1
    for i in range(len(lst1)):
        if (doubled[i:i + len(lst1)] == lst2):
            return True
    return False


# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]

    first = second = float('inf')
    for i in lst:
        if i < first:
            second = first
            first = i
        elif first < i < second:
            second = i
    return second


# 28. Write a Python program to find the second largest number in a list.
def second_largest(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] < lst[1] else lst[1]

    first = second = -float('inf')
    for i in lst:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i
    return second


# 29. Write a Python program to get unique values from a list.
def unique_values(lst):
    return list(set(lst))


# 30. Write a Python program to get the frequency of elements in a list.
def frequency_count(lst):
    freq = {}
    for i in lst:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


# 31. Write a Python program to count the number of elements in a list within a
# specified range
def count_in_range(lst, start, end):
    count = 0
    for i in lst:
        if start <= i <= end:
            count += 1
    return count


# 32. Write a Python program to check whether a list contains a sublist.
def is_nested_list(lst):
    for i in lst:
        if type(i) is list:
            return True
    return False


# 33. Write a Python program to generate all sublists of a list.

def generate_sublists(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            res.append(lst[i:j + 1])
    return res


# 34. Write a Python program that uses the Sieve of Eratosthenes method to
# compute prime numbers up to a specified number.

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    prime = []
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p] is True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    for i in range(n + 1):
        if is_prime[i] is True:
            prime.append(i)

    return prime


# 35. Write a Python program to create a list by concatenating a given list with a
# range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def concat_with_range(lst, n):
    concatenated_list = []
    for i in range(1, n + 1):
        for j in range(len(lst)):
            concatenated_list.append(str(lst[j] + str(i)))

    return concatenated_list


# 36. Write a Python program to get a variable with an identification number or
# string.
def identification(x):
    return id(x)

# 37. Write a Python program to find common items in two lists.
def common_items(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 38. Write a Python program to change the position of every n-th value to the
# (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def swap_adjacent(lst):
    for i in range(0, len(lst), 2):
        tmp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = tmp
    return lst


# 39. Write a Python program to convert a list of multiple integers into a single
# integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

def list_to_int(lst):
    def count_digits(n):
        count = 0
        while n > 0:
            n //= 10
            count += 1
        return count
    res = 0
    for i in lst:
        res = res * (10 ** count_digits(i)) + i
    return res

# 40. Write a Python program to split a list based on the first character of a word.
def list_split(lst):
    res = {}
    for word in lst:
        if word[0] not in res:
            res[word[0]] = []
        res[word[0]].append(word)
    return res

#41. Write a Python program to create multiple lists.
def create_multi_lists(n):
    return [[] for _ in range(n)]

# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second lis
def missing_additional(lst1, lst2):
    missing = set(lst1) - set(lst2)
    additional = set(lst2) - set(lst1)
    return list(missing), list(additional)

# 43. Write a Python program to split a list into different variables.
def split_into_variables(lst):
    x, y, z, *res = lst
    return x, y, z, res

# 44. Write a Python program to generate groups of five consecutive numbers in a
# list.
def group_of_5(n):
    res = []
    for i in range(n):
        tmp = []
        for j in range(1, 6):
            tmp.append(5 * i + j)
        res.append(tmp)
    return res

# 45. Write a Python program to convert a pair of values into a sorted unique array.
def pairs_to_sorted_unique_array(lst):
    st = set()
    for i in lst:
        for j in i:
            st.add(j)
    return sorted(list(st))

# 46. Write a Python program to select the odd items from a list.
def odd_items(lst):
    res = []
    for i in lst:
        if i % 2 == 1:
            res.append(i)
    return res

# 47. Write a Python program to insert an element before each element of a list.
def insert_before_all(lst, value):
    res = []
    for i in lst:
        res.append(value)
        res.append(i)
    return res

# 48. Write a Python program to print nested lists (each list on a new line) using
# the print() function.
def print_nested_list(lst):
    for i in lst:
        print(i)

# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
# "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name':
# 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def list_to_list_of_dict(lst):
    res = {}
    for i in range(len(lst[0])):
        res[lst[0][i]] = lst[1][i]
    return res

# 50. Write a Python program to sort a list of nested dictionaries.
def sort_nested_dict(dct):
    return sorted(dct)



