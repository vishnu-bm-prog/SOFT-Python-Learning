# variables in python

first_name = "Vishnu"
last_name = "BM"
country = "India"
city = "Karunagappally"
age = 19
is_married = False
skills =["HTML", "CSS", "JS", "C", "C++"]

person_info = {
    "firstname": "Vishnu",
    "Lastname": "BM",
    "country": "India",
    "city:": "Karunagappally"
}

# Printing the values stored in the variable

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variable in one line

first_name, last_name, country, age, is_married = "Vishnu", "BM", "India", 19, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)