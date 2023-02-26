def open_phone_book():
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        phone_book = data.readlines()
        print('! телефонный справочник открыт ! \n')
        return phone_book