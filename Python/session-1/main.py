# Line comment

'''
multiline comment
'''

# Variable type and declaration
user_name = 'Samuel'
age = 18
is_active = True
gender = 'm'
pets = ['dog', 'cat', 'bird']

# Print values
# No recommended
print(user_name, age, is_active, gender, pets)
print(user_name, " tiene ", age, " años ", is_active, " es de género ", gender, " y sus mascotas son: ", pets)

# This form is recommended
print(f"{user_name} tiene, {age} años, {is_active} es de género, {gender} y sus mascotas son: {pets}")

# Conditional scope
# First example
if is_active:
    print("Usuario activo")
else:
    print("usuario no activo")

# Second example
if gender == "f":
    print("Es femenino")
else:
    print("Es masculino")

# Third example
is_active_value = ''

if is_active:
    is_active_value = 'Usuario activo'
else:
    is_active_value = 'usuario no activo'

# Fourth example
gender_value = ''
if gender == "f":
    gender_value = 'Es femenino'
else:
    gender_value = 'Es masculino'

print(f'{is_active_value} de género {gender_value}')

# Fifth example
def mayor_de_edad(age):
    if age >= 18:
        print('Es mayor de edad')
    else:
        print('Es menor de edad')

mayor_de_edad(19)

'''
Clasify per age groups:
0 - 7 -> Infante
8 - 12 -> Niño
13 - 17 -> Adolescente
>= 18 -> Mayor de edad
'''
age_value_classification = ''

if age >= 0 and age <= 7:
    age_value_classification ='Es infante'
elif age >= 8 and age <= 12:
    age_value_classification ='Es niño'
elif age >= 13 and age <= 17:
    age_value_classification ='Es adolescente'
elif age >= 18:
    age_value_classification ='Es mayor de edad'
else:
    age_value_classification ='Edad inválida'

print(age_value_classification)

# Last exercise
if age < 18:
    is_active = False
elif age >= 18 and (gender == 'f' or gender == 'F'):
    is_active = False
elif age >= 18 and (gender == 'm' or  gender == 'M'):
    is_active = True

