import open_book
phone_book = []
def change_phone_book():
    phone_book = open_book.open_phone_book()
    user_info = input('Введите номер телефона контакта, который хотите изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            new_user = input('введите новый номер телефона: ')
            phone_book[i] = phone_book[i].replace(user_info, new_user)
            with open('phone_book.txt', 'w', encoding='utf-8') as data:
                for i in phone_book:
                    data.write(i)

