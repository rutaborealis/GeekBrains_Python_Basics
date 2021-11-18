# Lesson 3
# Task 2
def user_data(name, surname, birth_year, city, email, phone):
    return f'User:\nname: {name}; surname: {surname}; birth year: {birth_year}; city: {city}; e-mail: {email}; phone number: {phone}'


print(user_data(surname=input('Enter your surname: '), name=input('Enter your name: '),
                city=input('Enter your city: '), birth_year=input('Enter year of birth: '),
                phone=input('Enter your phone number: '), email=input('Enter your e-mail: ')))
