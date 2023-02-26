import menu_print
import open_book
import save_phone
import change_phone_number
import search_phone_number
import delete_phone_number
import show_book
import add_contact

phone_book = []

while True:
    user_choise = menu_print.print_menu()
    match user_choise:
        case 1:
            open_book.open_phone_book()
        case 2:
            save_phone.save_phone_book()
        case 3:
            show_book.show_phone_book()
        case 4:
            add_contact.add_phone_book()
        case 5:
            change_phone_number.change_phone_book()
        case 6:
            search_phone_number.search_phone_book()
        case 7:
            delete_phone_number.delete_phone_book()
        case 8:
            print('Вы вышли из телефонного справочника')
            break


