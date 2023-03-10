import logger as log
import menu as menu
import note as note
import csv

def notes():
    while True:
        menu.main_menu()
        c = input("Enter choice: ")
        if c == '0':
            break
        if c == '1':
            log.logger("Добавлена новая заметка")
            note.add_note()
            print('\nЗаметка успешно сохранена!')
            # menu.main_menu()
            # c = input("Enter choice: ")
            continue
            

        elif c == '2':
            log.logger("Открыт список заметок")
            note.show_notes_list()
            continue

        elif c == '3':
            log.logger('Редактирование заметки')
            note.show_notes_list()
            note.edit_note()
            continue

        elif c == '4':
            log.logger('Удаление заметки')
            note.show_notes_list()
            note.remove_note()
            continue
        
        else:
                log.logger("Invalid value entered")
                print ("Invalid value")
                continue
    return
