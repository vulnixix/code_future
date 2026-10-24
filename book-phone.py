book_phone = {
    'Саша' : '88800332323',
    "Петя" : "89323232323"
}


def add_contact():
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    #проверить что первые буквы phone +7 или 8
    if phone[0:2] != "+7" or phone[0] != "8" and len(phone) > 12:
         print("Номер некорректный")
         return
        
    if name in book_phone:
        print("Такой контакт уже существует!")
    else:
        book_phone[name] = phone
        print(f"Контакт {name} успешно добавлен!")


def find_contact():
    name = input("Введите имя: ")
    if not isinstance(name,str):
        print("Ошибка введите строку")
        return
    
    #return book_phone.get(name, "Контакт не найден")
    print("Результат поиска: ", book_phone.get(name, "Контакт не найден"))


def remove_contact():
    name = input("Введите имя: ")
    if not isinstance(name,str):
        print("Ошибка введите строку")
        return

    if name in book_phone:
        del book_phone[name]
        print("Данный контакт удален из книги")
    else:
        print("Такого контакта нет")


def show_contacts():
    for name, phone in book_phone.items():
        print(f"Имя: {name} -> Номер: {phone}")


def menu():
    print("1.Добавить контант")
    print("2.Удалить контакт")
    print("3.Найти контакт")
    print("4.Показать все контакты")
    print("5.Выход")


while True:
    menu()
    choice = input("Введите действие: ")
    if choice == "1":
        add_contact()
    
    #если выбрали 2 то вызываем функцию remove_contact
    elif choice == "2":
        remove_contact()

    elif choice == "3":
        find_contact()

    elif choice == "4":
        show_contacts()
    
    elif choice == "5":
        print('Программа завершена')
        break
