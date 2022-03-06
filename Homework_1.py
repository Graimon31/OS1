import os
import json
import xml.etree.ElementTree as ET
import zipfile as zf
import shutil

total, used, free = shutil.disk_usage('/')
total = total / 1024 / 1024 / 1024
used = used / 1024 / 1024 / 1024
free = free / 1024 / 1024 / 1024
print(f'Место\nВсего: {total:.2f}Gb\nИспользовано: {used:.2f}Gb\nСвободно: {free:.2f}Gb')

print("Здраствуйте, я ваш помощник Султан. Вы хотите работать или взаимодействовать с файлом?")
otvet = input().lower()
if otvet == "yes" or otvet == "да":
    rabota_file = input(
        'Что хотите сделать?\n0 - Просто работа с файлом \n1 - Работа с json\n2 - Работа с XML\n3 - Работа с ZIP\n')
    if rabota_file == '0':
        function = input('Напишите функцию, которую хотите выполнить||')
        file_format = input('Напишите имя и формат файла||')
        if function == "Создать файл" or function == "Создай файл" or function == "Создай файл, Султан":
            if os.path.isfile(file_format):
                print("Простите, но я не могу создать файл, так как файл с таким именем уже существует")
            else:
                file = open(file_format, 'w')
                print('Выполнено')
                file.close()
        elif function == "Записать в файл" or function == "Запиши в файл" or function == "Запиши в файл, Султан":
            if not os.path.isfile(file_format):
                print("Файл автоматически создан")
            else:
                file = open(file_format, 'r')
                file.write(input('Напишите, что вы хотите ввести в файл? ||'))
                file.close()
        elif function == "Прочитать файл" or function == "Прочитай файл" or function == "Прочитай файл, Султан":
            if os.path.isfile(file_format):
                file = open(file_format, 'r')
                print(file.read())
                file.close()
            else:
                print('Ошибка: файла нет')
        elif function == "Удалить файл" or function == "Удали файл" or function == "Удали файл, Султан":
            if os.path.isfile(file_format):
                os.remove(file_format)
                print("Выполнено")
            else:
                print("Не выполнено, так как файла не существует")
        else:
            print('Не выполнена, инструкции нет')
    elif rabota_file == '1':
        function = input('Напишите функцию, которую хотите выполнить||')
        file_format = input('Напишите имя и формат файла||')
        if function == "Создать файл" or function == "Создай файл" or function == "Создай файл, Султан":
            if os.path.isfile(file_format):
                print("Простите, но я не могу создать файл, так как файл с таким именем уже существует")
            else:
                file = open(file_format, 'w')
                print('Выполнено')
                file.close()
        elif function == "Записать в файл" or function == "Запиши в файл" or function == "Запиши в файл, Султан":
            if not os.path.isfile(file_format):
                print("Файл автоматически создан")
            else:
                file = open(file_format, 'w')
                string = input('Напишите, что вы хотите ввести в файл? ||')
                file.read(json.dumps(file_format))
                file.close()
        elif function == "Прочитать файл" or function == "Прочитай файл" or function == "Прочитай файл, Султан":
            if os.path.isfile(file_format):
                file = open(file_format, 'r')
                print(json.loads(file.read()))
                file.close()
            else:
                print("Ошибочка вышла, файла нет, создайте его")
        elif function == "Удалить файл" or function == "Удали файл" or function == "Удали файл, Султан":
            if os.path.isfile(file_format):
                os.remove(file_format)
                print("Выполнено")
            else:
                print("Не выполнено, так как файла не существует")
        else:
            print('Не выполнена, инструкции нет')
    elif rabota_file == '2':
        function = input('Напишите функцию, которую хотите выполнить||')
        file_format = input('Напишите имя и формат файла||')
        if function == "Создать файл" or function == "Создай файл" or function == "Создай файл, Султан":
            if os.path.isfile(file_format):
                print("Простите, но я не могу создать файл, так как файл с таким именем уже существует")
            else:
                root = ET.Element(file_format)
                doc = ET.SubElement(root, 'doc')
                tree = ET.ElementTree(root)
                tree.write(file_format)
        elif function == "Записать в файл" or function == "Запиши в файл" or function == "Запиши в файл, Султан":
            if os.path.isfile(file_format):
                tree = ET.parse(file_format)
                root = tree.getroot()
                root[0].text = input('To: ')
                root[1].text = input('From: ')
                root[2].text = input('Heading: ')
                root[3].text = input('Body: ')
                tree.write(file_format)
            else:
                print('Error: такого файла нет')
        elif function == "Прочитать файл" or function == "Прочитай файл" or function == "Прочитай файл, Султан":
            if os.path.isfile(file_format):
                tree = ET.parse(file_format)
                root = tree.getroot()
                print(f'To: {root[0].text}\nFrom: {root[1].text}\nHeading: {root[2].text}\nBody: {root[3].text}')
            else:
                print("Ошибочка вышла, файла нет, создайте его")
        elif function == "Удалить файл" or function == "Удали файл" or function == "Удали файл, Султан":
            if os.path.isfile(file_format):
                os.remove(file_format)
                print("Выполнено")
            else:
                print("Не выполнено, так как файла не существует")
        else:
            print('Не выполнена, инструкции нет')
    elif rabota_file == '3':
        function = input('Напишите функцию, которую хотите выполнить||')
        file_format_zip = input('Напишите имя архива||')
        file_format = input('Напишите имя и формат файла||')
        if function == "Создать файл" or function == "Создай файл" or function == "Создай файл, Султан":
            if os.path.isfile(file_format_zip):
                print("Простите, но я не могу создать файл, так как файл с таким именем уже существует")
            else:
                file = open(file_format_zip, 'w')
                print('Выполнено')
                file.close()
        elif function == "Записать в файл" or function == "Запиши в файл" or function == "Запиши в файл, Султан":
            if not os.path.isfile(file_format):
                file = open(file_format_zip, 'w')
                print('Файл автоматически создан')
                file.close()
            if not os.path.isfile(file_format_zip):
                zfile = zf.Zipfile(file_format_zip)
                print('Архив создан')
                zfile.close()
            if zf.is_zipfile(file_format_zip):
                print('Архив не является zip файлом')
                zfile = zf.Zipfile(file_format_zip, 'w')
                zfile.write(file_format)
                print('Выполнено')
            else:
                print('Error: такого файла нет')
        elif function == "Прочитать файл" or function == "Прочитай файл" or function == "Прочитай файл, Султан":
            if os.path.isfile(file_format_zip) and zf.is_zipfile(file_format_zip):
                zfile = zf.ZipFile(file_format_zip)
                print('Файлы в архиве:')
                zfile.printdir()
                path = input('Введите файл который надо разархивировать > ')
                try:
                    zfile.extract(file_format)
                except KeyError:
                    print('Такого файла в архиве нет')
                else:
                    file = open(file_format, 'r')
                    print(file.read())
                    file.close()
            else:
                print("Ошибочка вышла, файла нет, создайте его")
        elif function == "Удалить файл" or function == "Удали файл" or function == "Удали файл, Султан":
            if os.path.isfile(file_format):
                os.remove(file_format)
                print("Выполнено")
            else:
                print("Не выполнено, так как файла не существует")
        else:
            print('Не выполнена, инструкции нет')
