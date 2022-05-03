first_name = "Morgan" #string
last_name = "Githinji" #string

age = 26 #integer
weight = 180.5 #float

employed = True
student = False

gender = "Male"

# full_name = first_name + last_name
# print(full_name)

# name_and_age = full_name + age
# print(name_and_age)

# age_plus_weight = age + weight
# print(age_plus_weight)

# employed_and_student = employed or student
# print(employed_and_student)

profile_list = ["Morgan", "Male", "Githinji", 26, 180.5, True, False]
profile_dict = {'first name': "Morgan", 'gender': "Male", 'last name': "Githinji", 'age': 26, 'employed': True, 'student': False}

user_last_name = profile_list[2]
print(user_last_name)

user_last_name = profile_dict['last name']
print(user_last_name)

reviews_list = [2.4, 3.3, 4.0, 1.2, 5, 3.7]
reviews_dict = {'a': 2.4, 'b': 3.3, 'c': 4.0, 'd': 1.2, 'e':5, 'f': 3.7}

import numpy as np 

average = np.mean(reviews_list)
print(average)

sum = np.sum(reviews_list)
print(sum)

min_rating = np.min(reviews_list)
print(min_rating)

max_rating = np.max(reviews_list)
print(max_rating)