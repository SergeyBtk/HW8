import open_book
def show_phone_book():
    phone_book = open_book.open_phone_book()
    # print(phone_book)
    if len(phone_book) == 0:
        print('вы не открыли телефонный справочник, либо он пуст')
    else:
        for i in phone_book:
            print(' __'.join(i.split(';')))


