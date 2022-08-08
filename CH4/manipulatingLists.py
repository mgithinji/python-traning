# list
profile = ["Morgan", "Githinji", 26, 180.5, True]
lastname = profile[1]
print(lastname)

# dict
profile_dict = {"first name": "Morgan", "last name": "Githinji", "age": 26, "weight": 180.5, "male": True}
lastname = profile_dict['last name']
print(lastname)

# updating
profile[0] = "Gordon" # updating the list
profile_dict['first name'] = "Gordon" # updating the dict

print(profile)
print(profile_dict)

# list search
idx = profile.index("Githinji")
print(idx)

# list concatenate
school = ["Univ. of Maryland", "Electrical Engineering", 3.6]

full_profile = profile + school
print(full_profile)

# list slicing
small_profile = full_profile[4:6]
print(small_profile)

# list indexing in reverse
gpa = full_profile[-1]
print(gpa)

