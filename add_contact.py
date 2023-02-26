import open_book
phone_book = []
def add_phone_book():
    phone_book = open_book.open_phone_book()
    if len(phone_book) == 0:
        print('вы не открыли телефонный справочник, либо он пуст')
    else:
        user_info = input('Введите данные нового контакта: ')
        user_info = ' __'.join(user_info.split())
        phone_book.append('\n' + user_info)
        print(user_info)
        with open('phone_book.txt', 'w', encoding='utf-8') as data:
            for i in phone_book:
                data.write(i)
# phone_book = open_book.open_phone_book()
