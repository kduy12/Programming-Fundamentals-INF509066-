# Set
# 1.Write a Python program to find the maximum and minimum values in a set.
def max_min(my_set):
    return max(my_set), min(my_set)


# 2.Write a Python program to check if a given value is present in a set or not.
def is_in(value, my_set):
    return value in my_set


# 3.Write a Python program to check if two given sets have no elements in common.
def are_mutually_exclusive(set_a, set_b):
    return set_a & set_b == set()


# 4.Write a Python program to find all the unique words and count the frequency of occurrence from
# a given list of strings. Use Python set data type.
def count_unique_words(s):
    words = s.split()
    unique = set(words)
    freq = {}
    for w in unique:
        freq[w] = words.count(w)
    return freq


# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set
# as compared to the first and vice versa. Use the Python set.
def missing_number(set_a, set_b):
    return set_a - set_b, set_b - set_a


# Dictionary
# Restructuring the company data: Suppose you have a dictionary that contains information about employees at a company.
# Each employee is identified by an ID number, and their information includes their name, department, and salary.

# You want to create a nested dictionary that groups employees by department so that you can easily see the names and
# salaries of all employees in each department.

# Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees,
# which groups employees by department.
def regroup_dict():
    employees = {
        1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
        1002: {"name": "Bob", "department": "Sales", "salary": 50000},
        1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
        1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
        1005: {"name": "Eve", "department": "Sales", "salary": 55000}
    }

    def depts(employees):
        res = set()
        for employee in employees.values():
            res.add(employee['department'])
        return res

    def create_dict(employees):
        my_depts = depts(employees)
        new_dict = {}
        for dept in my_depts:
            new_dict[dept] = {}
            for emp_id, info in employees.items():
                if info['department'] == dept:
                    # chỉ giữ lại name và salary
                    new_dict[dept][emp_id] = {
                        "name": info["name"],
                        "salary": info["salary"]
                    }
        return new_dict

    return create_dict(employees)

if __name__ == '__main__':
    print(regroup_dict())
