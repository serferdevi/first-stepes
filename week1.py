name = input ("Как тебя зовут?")
print(name)

age = int(input("Сколько тебе лет?"))
print(type(name))
print(type(age))

height = 1.80
print(type(height))

next_year = age + 1
print(next_year)
if age >= 18:
    print("Ты совершеннолетний")
elif age == 18:
    print("Тебе ровно 18")
else:
    print("Ты несовершеннолетний")
