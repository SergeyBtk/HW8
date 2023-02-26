import open_book
phone_book = []
def delete_phone_book():
    phone_book = open_book.open_phone_book()
    user_info = input('Введите номер телефона контакта, который хотите удалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            search_user = int(input(f'Вы дейтсвительно хотите удалить контакт: {phone_book[i]} \n'
                  f'Если да нажмите: 1 \n'
                  f'Если нет нажмите: 2 \n'))
            if search_user == 2:
                print(f'контакт: {phone_book[i]}  не удален из словаря')
                break
            else:
                phone_book.pop(i)
                print(f'контакт: {phone_book[i]} удален из словаря')
                with open('phone_book.txt', 'w', encoding='utf-8') as data:
                    for i in phone_book:
                        data.write(i)
                break

