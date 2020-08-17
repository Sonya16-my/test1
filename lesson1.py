# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя человека, строка
# last_name - фамилия человека, строка
# patronymic - отчество человека, строка
# address - адрес человека, строка
# {tel:[last_name, first_name, patronymic, address]}

phone_book=dict()
value=list()

tel = input("Введите номер телефона: ")
first_name = input("Введите имя: ")
last_name = input("Введите фамилию : ")
patronymic = input("Введите отчество: ")
address = input("Введите адрес: ")

value.append(first_name)
value.append(last_name)
value.append(patronymic)
value.append(address)

phone_book[tel] = value
print(phone_book)










