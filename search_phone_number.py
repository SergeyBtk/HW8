import open_book
def search_phone_book():
    phone_book = open_book.open_phone_book()
    user_info = input('Введите номер телефона контакта для поиска в телефонном справочнике: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])