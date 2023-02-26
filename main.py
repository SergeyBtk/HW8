# phone_book = []
#
# def open_phone_book():
#     with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
#         phone_book = data.readlines()
#         print('! телефонный справочник открыт ! \n')
#         return phone_book
#
# def save_phone_book():
#     with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
#         for i in phone_book:
#             data.write(i)
#
# def show_phone_book():
#     print(phone_book)
#     if len(phone_book) == 0:
#         print('вы не открыли телефонный справочник, либо он пуст')
#     else:
#         for i in phone_book:
#             print(' __'.join(i.split(';')))
#
# def add_phone_book():
#     if len(phone_book) == 0:
#         print('вы не открыли телефонный справочник, либо он пуст')
#     else:
#         user_info = input('Введите данные нового контакта: ')
#         user_info = ' __'.join(user_info.split())
#         phone_book.append('\n' + user_info)
#         print(user_info)
#         # save_phone_book()
#
# def change_phone_book():
#     user_info = input('Введите номер телефона контакта, который хотите изменить: ')
#     for i in range(len(phone_book)):
#         if user_info in phone_book[i]:
#             print(phone_book[i])
#             new_user = input('введите новый номер телефона')
#             phone_book[i] = phone_book[i].replace(user_info, new_user)
#             save_phone_book()
#
# def search_phone_book():
#     user_info = input('Введите номер телефона контакта для поиска в телефонном справочнике: ')
#     for i in range(len(phone_book)):
#         if user_info in phone_book[i]:
#             print(phone_book[i])
#
# def delete_phone_book():
#     user_info = input('Введите номер телефона контакта, который хотите удалить: ')
#     for i in range(len(phone_book)):
#         if user_info in phone_book[i]:
#             print(phone_book[i])
#             phone_book.pop(i)
#             save_phone_book()
#             break
#
# phone_book = open_phone_book()
# show_phone_book()
# add_phone_book()
# change_phone_book()
# save_phone_book()
# show_phone_book()
# search_phone_book()
# delete_phone_book()
# show_phone_book()
# print(phone_book)