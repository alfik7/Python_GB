# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных
# о пользователе одной строкой.

name2 = str(input("Имя: "))
surname2 = str(input("Фамилия: "))
year2 = str(input("Возраст: "))
city2 = str(input("Город: "))
email2 = str(input("email: "))
phone2 = str(input("Телефон: "))


def p_info(name, surname, year, city, email, phone):
    return ' '.join([
        "Имя: ", name,
        ". Фамилия: ", surname,
        ". Возраст: ", year,
        ". Город: ", city,
        ". emaiL: ", email,
        ". Телефон: ", phone, "."
    ])


print(p_info(name=name2, surname=surname2, year=year2, city=city2, email=email2, phone=phone2))
