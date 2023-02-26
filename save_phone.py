import open_book
phone_book = []
def save_phone_book():
    phone_book = open_book.open_phone_book()
    with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
        for i in phone_book:
            data.write(i)

