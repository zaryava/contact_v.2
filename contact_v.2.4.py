from tkinter import *

logo = 'logotip.ico'
file_name_txt = 'contact.txt'
insert_line = 3*'-----------------------'

#----------------------Функции-обработчики событий корневого окна------------------------

# Функция-обработчик события нажатие кнопки "Показать контакты".
def show_contact():
    '''При нажатии кнопки "Показать контакты"
       Вывод контактов в текстовое поле виджета text_win_root.'''
    read_contact_txt_gui(file_name_txt)

# Функция-обработчик события нажатие кнопки "Поиск".
def open_win_find():
    '''При нажатии кнопки "Поиск"
       формируется окно win_find.'''
    global win_find, entry_win_find
    win_find = Tk()
    win_find.title('Поиск контакта')
    win_find.geometry('300x130+1000+300')
    win_find.resizable(0,0)
    win_find.iconbitmap(logo)

    label_win_find = Label(win_find, text='Введите информацию для поиска контакта')
    label_win_find.pack()

    entry_win_find = Entry(win_find, font=('Courier New', 12), justify=CENTER)
    entry_win_find.pack(fill=X, padx=10)
    
    # Событие нажатия кнопки "Начать поиск" в окне "Поиск"
    # обрабатывается функцией start_find().
    btn_win_find = Button(win_find, text='Начать поиск', command=start_find)
    btn_win_find.pack(fill=X, padx=80, pady=10)

    # Событие нажатия кнопки "Закрыть" в окне "Поиск"
    # обрабатывается функцией close_win_find().
    btn_win_find_close = Button(win_find, text='Закрыть', command=close_win_find)
    btn_win_find_close.pack(fill=X, padx=80, pady=5, side=BOTTOM)    

# Функция-обработчик события нажатие кнопки "Добавить контакт".
def open_win_add(): 
    pass

# Функция-обработчик события нажатие кнопки "Удалить контакт".
def open_win_del(): 
    pass

# Функция-обработчик события нажатие кнопки "Выход".
def close_win_root():
    '''Функция для обработки события нажатие
       кнопки "Выход" в окне win_root.'''
    win_root.destroy()

#----------------------------------------------------------------------------------------

#----------------------Дополнительные функции для обработки событий----------------------

def read_contact_txt_gui(file_name):
    '''Для получения данных из текстового файла.
       Обработка данных. Вызов функции для
       вывода на печать всех контактов.'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.        
    contact_number = 0 # Начальное значение переменной для формирования номера контакта.
    text_win_root.delete(1.0, END) # После каждого нажатия кнопки "Показать контакты"
                                   # осуществляется очистка текстового поля.                                 
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str_n = file_txt_r.readline() # Получение строки. 
        if data_str_n == '': # Если строка пустая то выход из цикла.
            file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.                                   
        # Функция print_contact_gui() принимает два аргумента.                                 
        print_contact_gui(data_str_n, contact_number) # Функция вывода на печать.

def print_contact_gui(data_str_n, contact_number):
    '''Получает строку контакта и его номер.
       Обработка данных. Вывод на печать контакта.'''
    data_str = data_str_n.rstrip('\n') # Удаляет '\n' в конце строки.
    data_list = data_str.split('&')    # Полученная строка разделяется по символу &.
                                       # Формируется список data_list.
    contact_last_name = data_list[0]       # Получение фамилии.
    contact_first_name = data_list[1]      # Получение имени.
    contact_address = data_list[2]         # Получение адреса.   
    contact_phone_number = data_list[3]    # Получение номера телефона.
    contact_date_time_write = data_list[4] # Получение даты и времени записи контакта.
    contact_email = data_list[4]           # Получение электронного адреса.
    contact_add_inform = data_list[5]      # Получение дополнительной информации.
    contact_dt = data_list[6]              # Получение даты и времени записи контакта.
    
    #----------------------Вывод на печать контакта абонента---------------------------
    pr_line_1 = f'---------------   Контакт № {contact_number}'
    pr_line_2 = f'   ---   {contact_dt}   ---------------'
    text_win_root.insert(1.0, f' Дополнительная информация: {contact_add_inform}\n')
    text_win_root.insert(1.0, f' Электронный адрес: {contact_email}\n')
    text_win_root.insert(1.0, f' Номер телефона: {contact_phone_number}\n')
    text_win_root.insert(1.0, f' Адрес: {contact_address}\n')
    text_win_root.insert(1.0, f' Имя (Отчество): {contact_first_name}\n')
    text_win_root.insert(1.0, f' Фамилия: {contact_last_name}\n')
    text_win_root.insert(1.0, pr_line_1 + pr_line_2 + '\n')
    #----------------------------------------------------------------------------------
    
def start_find():
    '''Функция для обработки события нажатие
       кнопки "Начать поиск" в окне win_find.'''
    find_str = entry_win_find.get() # Переменной find_str присваивается строка
                                    # (Элемент поиска) введённая в виджет Entry.
    text_win_root.delete(1.0, END) # Очистка текстового поля корневого окна.
    if find_str != '': # Если полученная из виджета Entry строка не пустая.
        find_contact_gui(file_name_txt, find_str) # Вызов функции find_contact_gui
    else: # Иначе если строка пустая вывести в тестовое поле корневого окна.
        text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления. 
        text_win_root.insert(1.0, f'    ВВЕДИТЕ ИНФОРМАЦИЮ ДЛЯ ПОИСКА КОНТАКТА\n')
        text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.

def find_contact_gui(file_name, find_str):
    '''Для поиска контакта по элементу данных переданных в виде строки.
       Обработка данных. Вызов функции для
       вывода на печать найденного контакта(ов).'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.
    contact_number = 0 # Начальное значение переменной для формирования номера контакта.
    id_str = '' # Создаётся пустая строка.
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str_n = file_txt_r.readline() # Получение строки. 
        if data_str_n == '': # Если строка пустая то выход из цикла.
            if id_str.find('1') == -1: # Перед выходом из цикла проверяем строку 
                                       # id_str на наличие идентификатора(ов) совпадений.
                                       # Если условие верно значит совпадений нет.
                text_win_root.delete(1.0, END) # Очистка поля.
                text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
                text_win_root.insert(1.0, f'    ДЛЯ ЭЛЕМЕНТА ПОИСКА < {find_str} > - СОВПАДЕНИЙ НЕТ\n')
                text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
                entry_win_find.delete(0, END) # Очистка поля для ввода информации для поиска.
                file_txt_r.close() # Закрытие текстового файла.
            break # Выход из цикла
        data_str = data_str_n.rstrip('\n') # Удаляет '\n' в конце строки.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.
        find_str_lower = find_str.lower() # Переменной find_str_lower присваивается
                                          # строка элемента для поиска преобразованная
                                          # к нижнему регистру.
        data_str_lower = data_str.lower() # Переменной data_str_lower присваивается
                                          # строка контакта, полученная их текстового файла,
                                          # преобразованная к нижнему регистру.
        if data_str_lower.find(find_str_lower) != -1: # Если совпадения есть, к строке
                                                      # id_str прибавляется '1'.
            id_str = id_str + '1'
            entry_win_find.delete(0, END) # Очистка поля для ввода информации для поиска.
            print_contact_gui(data_str, contact_number) # Функция вывода на печать.                 
        else:                             # Иначе к строке id_str прибавляется '0'.
            id_str = id_str + '0'

# Функция-обработчик события нажатие кнопки "Закрыть".
def close_win_find():
    '''Функция для обработки события нажатие
       кнопки "Закрыть" в окне win_find.'''
    text_win_root.delete(1.0, END) # Очистка поля.
    win_find.destroy()    
#----------------------------------------------------------------------------------------
    
#--------------------------Формирование корневого окна программы-------------------------
win_root = Tk()
win_root.title('Контакты')
win_root.iconbitmap(logo)
win_root.geometry('940x405+50+150')
win_root.resizable(0,0)

text_win_root = Text(win_root, font=('Courier New', 12), wrap=WORD)
text_win_root.pack(padx=2, pady=2, side=LEFT)

btn_show_win_root = Button(win_root, text='Показать контакты', command=show_contact)
btn_show_win_root.pack(fill=X, padx=5, pady=2)

btn_find_win_root = Button(win_root, text='Поиск', command=open_win_find)
btn_find_win_root.pack(fill=X, padx=5, pady=2)

btn_add_win_root = Button(win_root, text='Добавить контакт', command=open_win_add)
btn_add_win_root.pack(fill=X, padx=5, pady=2)

btn_del_win_root = Button(win_root, text='Удалить контакт', command=open_win_del)
btn_del_win_root.pack(fill=X, padx=5, pady=2)

btn_exit_win_root = Button(win_root, text='Выход', command=close_win_root)
btn_exit_win_root.pack(fill=X, padx=5, pady=2, side=BOTTOM)

win_root.mainloop()
#----------------------------------------------------------------------------------------


