from tkinter import *
from datetime import datetime
from tkinter import messagebox
import os

logo = 'logotip.ico'
file_name_txt = 'contact.txt'
insert_line = 3*'-----------------------'

open_win_find_contact_flag = 0 # Если значение 0 окно закрыто, если значение 1 окно открыто.
open_win_add_contact_flag = 0 # Если значение 0 окно закрыто, если значение 1 окно открыто.
open_win_del_contact_flag = 0 # Если значение 0 окно закрыто, если значение 1 окно открыто.

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
    global win_find, entry_win_find, open_win_find_contact_flag
    if open_win_find_contact_flag == 0 and open_win_add_contact_flag == 0 and open_win_del_contact_flag == 0:    
        open_win_find_contact_flag = 1
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
    '''При нажатии кнопки "Добавить контакт"
       формируется окно win_add.'''
    global win_add, entry_last_name, entry_first_name, entry_address
    global entry_phone_number, entry_email, entry_add_inform, open_win_add_contact_flag
    if open_win_add_contact_flag == 0 and open_win_find_contact_flag == 0 and open_win_del_contact_flag == 0: 
        open_win_add_contact_flag = 1
        win_add = Tk()
        win_add.title('Добавить контакт')
        win_add.geometry('300x350+1000+150')
        win_add.resizable(0,0)
        win_add.iconbitmap(logo)

        label_last_name = Label(win_add, text='Введите фамилию:')
        label_last_name.pack()

        entry_last_name = Entry(win_add, font=('Courier New', 12), justify=CENTER)
        entry_last_name.pack(fill=X, padx=10)

        label_first_name = Label(win_add, text='Введите имя (отчество):')
        label_first_name.pack()

        entry_first_name = Entry(win_add, font=('Courier New', 12), justify=CENTER)
        entry_first_name.pack(fill=X, padx=10)

        label_address = Label(win_add, text='Введите адрес:')
        label_address.pack()

        entry_address = Entry(win_add, font=('Courier New', 12), justify=CENTER)
        entry_address.pack(fill=X, padx=10)

        label_phone_number = Label(win_add, text='Введите телефонный номер:')
        label_phone_number.pack()

        entry_phone_number = Entry(win_add, font=('Courier New', 12), justify=CENTER)
        entry_phone_number.pack(fill=X, padx=10)

        label_email = Label(win_add, text='Введите электронный адрес:')
        label_email.pack()

        entry_email = Entry(win_add, font=('Courier New', 12), justify=CENTER)
        entry_email.pack(fill=X, padx=10)

        label_add_inform = Label(win_add, text='Дополнительная информация:')
        label_add_inform.pack()

        entry_add_inform = Entry(win_add, font=('Courier New', 12), justify=CENTER)
        entry_add_inform.pack(fill=X, padx=10)
    
        # Событие нажатия кнопки "Добавить контакт" в окне "Добавить контакт"
        # обрабатывается функцией add_contact_gui().
        btn_add_inform = Button(win_add, text='Добавить контакт', command=add_contact_gui)
        btn_add_inform.pack(fill=X, padx=80, pady=10)
    
        # Событие нажатия кнопки "Закрыть" в окне "Добавить контакт"
        # обрабатывается функцией close_win_add()
        btn_close_add_cont = Button(win_add, text='Закрыть', command=close_win_add)
        btn_close_add_cont.pack(fill=X, padx=80, pady=5, side=BOTTOM)


# Функция-обработчик события нажатие кнопки "Удалить контакт".
def open_win_del():
    '''При нажатии кнопки "Удалить контакт"
       формируется окно win_del.'''
    global win_del, entry_win_del, open_win_del_contact_flag
    if open_win_del_contact_flag == 0 and open_win_find_contact_flag == 0 and open_win_add_contact_flag == 0: 
        open_win_del_contact_flag = 1
        win_del = Tk()
        win_del.title('Удалить контакт')
        win_del.geometry('300x130+1000+300')
        win_del.resizable(0,0)
        win_del.iconbitmap(logo)

        label_win_del = Label(win_del, text='Введите номер контакта для удаления:')
        label_win_del.pack()

        entry_win_del = Entry(win_del, font=('Courier New', 12), justify=CENTER)
        entry_win_del.pack(fill=X, padx=10)
    
        # Событие нажатия кнопки "Удалить контакт" в окне "Удалить контакт"
        # обрабатывается функцией start_del().
        btn_win_del = Button(win_del, text='Удалить контакт', command=start_del)
        btn_win_del.pack(fill=X, padx=80, pady=10)
    
        # Событие нажатия кнопки "Закрыть" в окне "Удалить контакт"
        # обрабатывается функцией close_win_del()
        btn_win_del_close = Button(win_del, text='Закрыть', command=close_win_del)
        btn_win_del_close.pack(fill=X, padx=80, pady=5, side=BOTTOM)

# Функция-обработчик события нажатие кнопки "Выход".
def close_win_root():
    '''Функция для обработки события нажатие
       кнопки "Выход" в окне win_root.'''
    if open_win_find_contact_flag: # Если окно "Поиск контакта" открыто.
        close_win_find() # Вызов функции для закрытия окна "Поиск контакта".
    elif open_win_add_contact_flag: # Иначе если окно "Добавить контакт" открыто.
        close_win_add() # Вызов функции для закрытия окна "Добавить контакт".
    elif open_win_del_contact_flag: # Иначе если окно "Удалить контакт" открыто.
        close_win_del() # Вызов функции для закрытия окна "Удалить контакт".
    win_root.destroy() # Закрытие корневого окна "Контакты".
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
    
    #----------------------Вывод на печать контакта абонента-------------------------------------------------------
    pr_line_1 = f'---------------   Контакт № {contact_number}'
    pr_line_2 = f'   ---   {contact_dt}   ---------------'
    #-------------------------------------В ЦВЕТЕ------------------------------------------------------------------
    text_win_root.insert(1.0, f' Дополнительная информация: {contact_add_inform}\n')
    text_win_root.tag_add('add_inform', '1.0', '1.27')
    text_win_root.tag_add('add_inform_text', '1.28', '1.100')
    text_win_root.tag_config('add_inform', font=('Courier New', 12), foreground='blue')
    text_win_root.tag_config('add_inform_text', font=('Courier New', 12, 'italic', 'bold'), foreground='green')
    
    text_win_root.insert(1.0, f' Электронный адрес: {contact_email}\n')
    text_win_root.tag_add('email', '1.0', '1.19')
    text_win_root.tag_add('email_text', '1.20', '1.60')
    text_win_root.tag_config('email', font=('Courier New', 12), foreground='blue')
    text_win_root.tag_config('email_text', font=('Courier New', 12, 'italic', 'bold'), foreground='green')
    
    text_win_root.insert(1.0, f' Номер телефона: {contact_phone_number}\n')
    text_win_root.tag_add('phone_number', '1.0', '1.16')
    text_win_root.tag_add('phone_number_text', '1.17', '1.60')
    text_win_root.tag_config('phone_number', font=('Courier New', 12), foreground='blue')
    text_win_root.tag_config('phone_number_text', font=('Courier New', 12, 'italic', 'bold'), foreground='green')
    
    text_win_root.insert(1.0, f' Адрес: {contact_address}\n')
    text_win_root.tag_add('address', '1.0', '1.7')
    text_win_root.tag_add('address_text', '1.8', '1.60')
    text_win_root.tag_config('address', font=('Courier New', 12), foreground='blue')
    text_win_root.tag_config('address_text', font=('Courier New', 12, 'italic', 'bold'), foreground='green')
    
    text_win_root.insert(1.0, f' Имя (Отчество): {contact_first_name}\n')
    text_win_root.tag_add('first_name', '1.0', '1.16')
    text_win_root.tag_add('first_name_text', '1.17', '1.60')
    text_win_root.tag_config('first_name', font=('Courier New', 12), foreground='blue')
    text_win_root.tag_config('first_name_text', font=('Courier New', 12, 'italic', 'bold'), foreground='green')
        
    text_win_root.insert(1.0, f' Фамилия: {contact_last_name}\n')
    text_win_root.tag_add('last_name', '1.0', '1.9')
    text_win_root.tag_add('last_name_text', '1.10', '1.50')
    text_win_root.tag_config('last_name', font=('Courier New', 12), foreground='blue')
    text_win_root.tag_config('last_name_text', font=('Courier New', 12, 'italic', 'bold'), foreground='green')
    
    text_win_root.insert(1.0, pr_line_1 + pr_line_2 + '\n')
    text_win_root.tag_add('line1', '1.0', '1.15')
    text_win_root.tag_add('Contact', '1.16', '1.31')
    text_win_root.tag_add('line2', '1.32', '1.36')
    text_win_root.tag_add('Datatime', '1.38', '1.58')
    text_win_root.tag_add('line3', '1.60', '1.83')
     
    text_win_root.tag_config('line1', font=('Courier New', 12, 'bold', 'italic'), foreground='black')
    text_win_root.tag_config('Contact', font=('Courier New', 13, 'bold'), foreground='red')
    text_win_root.tag_config('line2', font=('Courier New', 12, 'bold', 'italic'), foreground='black')
    text_win_root.tag_config('Datatime', font=('Courier New', 10, 'bold', 'italic'), foreground='#FB7200')
    text_win_root.tag_config('line3', font=('Courier New', 12, 'bold', 'italic'), foreground='black')
    #--------------------------------------------------------------------------------------------------------------
    
# Дополнительная функция для вызова из функции add_contact_gui().
def write_contact_txt_gui(file_name, contact):
    '''Для записи контакта в текстовый файл. 
       Отрытие файла. Запись. Закрытие файла'''
    file_txt = open(file_name, 'a')
    file_txt.write(contact)
    file_txt.close()  
    
# Функция-обработчик события нажатие кнопки "Начать поиск" в окне "Поиск".
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
        
# Дополнительная функция для вызова из функции start_find().
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

# Функция-обработчик события нажатие кнопки "Закрыть" в окне "Поиск".
def close_win_find():
    '''Функция для обработки события нажатие
       кнопки "Закрыть" в окне win_find.'''
    global open_win_find_contact_flag
    win_find.destroy() # Закрытие окна "Поиск контакта".
    text_win_root.delete(1.0, END) # Очистка поля.
    open_win_find_contact_flag = 0 # Окно закрыто.

# Функция-обработчик события нажатие кнопки "Добавить контакт".
def add_contact_gui():
    '''Для добавления контакта.
       Обработка данных. Формирование строки контакта.
       Запись контакта в текстовый файл.'''
    last_name = entry_last_name.get() # Получение "Фамилии" из окна ввода Entry.
    first_name = entry_first_name.get() # Получение "Имени" из окна ввода Entry.    
    address = entry_address.get() # Получение "Адреса" из окна ввода Entry.
    phone_number = entry_phone_number.get() # Получение "Тел. ном." из окна ввода Entry.
    email = entry_email.get() # Получение "Эл. адреса" из окна ввода Entry.
    add_inform = entry_add_inform.get() # Получение "Доп. инф." из окна ввода Entry.

    entry_last_name.delete(0, END) # Очистка поля ввода Entry.
    entry_first_name.delete(0, END) # Очистка поля ввода Entry. 
    entry_address.delete(0, END) # Очистка поля ввода Entry.
    entry_phone_number.delete(0, END) # Очистка поля ввода Entry.
    entry_email.delete(0, END) # Очистка поля ввода Entry.
    entry_add_inform.delete(0, END) # Очистка поля ввода Entry.

    # Получение даты и времени из ОС и присвоение
    # в виде строки переменной dt.
    dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    # Формирование строки с данными одного контакта. 
    contact = last_name + '&' + first_name + '&' + \
              address + '&' + phone_number + '&' + \
              email + '&' + add_inform + '&' + dt + '\n'
    text_win_root.delete(1.0, END)
    if last_name != '' and phone_number != '': # Если поля ввода "Введите фамилию:" и
                                               #"Введите телефонный номер не пустые. 
        write_contact_txt_gui(file_name_txt, contact) # Вызов функции для записи контакта в txt.
        read_contact_txt_gui(file_name_txt) # Вызов функции для отображения всех контактов.
    else: # Иначе если поля ввода пустые вывести информационное сообщение.
        text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
        text_win_root.insert(1.0, f' ЗАПОЛНИТЕ ПОЛЯ "Введите фамилию:" И "Введите телефонный номер:"\n')
        text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.

# Функция-обработчик события нажатие кнопки "Закрыть".
def close_win_add():
    '''Функция для обработки события нажатие
       кнопки "Закрыть" в окне win_add.'''
    global open_win_add_contact_flag
    win_add.destroy() # Закрытие окна "Добавить контакт".
    text_win_root.delete(1.0, END) # Очистка поля.
    open_win_add_contact_flag = 0 # Окно закрыто.

# Функция-обработчик события нажатие кнопки "Удалить контакт".
def start_del():
    '''Функция для обработки события нажатие
       кнопки "Удалить контакт" в окне win_del.'''
    contact_number_for_del = entry_win_del.get() # Получение номера контакта для удаления.
    text_win_root.delete(1.0, END) # Очистка текстового поля корневого окна.
    if contact_number_for_del != '': # Если полученный номер контакта для удаления не пустая строка.
        del_contact_gui(file_name_txt, contact_number_for_del) # Вызов функции для удаления контакта.
    else: # Иначе если строка пустая, не введён номер контакта для удаления.
        text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
        text_win_root.insert(1.0, f'    ВВЕДИТЕ НОМЕР КОНТАКТА ДЛЯ УДАЛЕНИЯ\n')
        text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
        
# Дополнительная функция для вызова из функции start_del().
def del_contact_gui(file_name, contact_number_for_del):
    '''Получает номер контакта. Удаляет контакт'''
    file_txt_r = open(file_name, 'r') # Открытие файла для чтения данных.
    contact_number = 0 # Начальное значение переменной для формирования номера контакта.
    list_for_new_txt = [] # Пустой список для формирования списка с контактами.
    while True: # Бесконечный цикл для обработки контактов построчно.
        data_str = file_txt_r.readline() # Получение строки контакта.
        if data_str == '': # Если строка пустая выход из цикла.
            file_txt_r.close() # Закрытие файла.
            # Если номер контакта больше чем всего число контактов
            # выводится информационное сообщение.
            if contact_number_for_del > str(contact_number): 
                text_win_root.delete(1.0, END) # Очистка текстового поля корневого окна.
                text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
                text_win_root.insert(1.0, f'    КОНТАКТ № {contact_number_for_del} НЕ СУЩЕСТВУЕТ\n')
                text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.
            break # Выход из цикла.
        contact_number += 1 # Присваевается номер контакта.
                            # С каждым проходом цикла увеличивается на единицу.                            
        # Если номер контакта совпадает с номером контакта для удаления
        # эта строка контакта не добавляется в список list_for_new_txt.
        # Из списка list_for_new_txt сформируется новый текстовый файл 
        # без удалённого контакта.                         
        if str(contact_number) == contact_number_for_del:
            contact_for_del = data_str # В переменной contact_for_del
                                       # сохраняется строка с данными 
                                       # контакта для удаления.
            continue # Если номер контакта совпадает с номером контакта для удаления
                     # эта строка контакта не добавляется в список list_for_new_txt.
                     # Следующий код этого цикла пропускается и переходит к
                     # следующей итерации цикла. 
        list_for_new_txt.append(data_str) # Добавляется в конец списка строка с контактом.   
    print_contact_gui(contact_for_del, contact_number_for_del) # Вызов функции для вывода контакта
                                                               # в текстовое поле корневого окна.
    choice_for_del =  messagebox.askokcancel(title='Удаление контакта',
                                             message=f'Удалить Контакт № {contact_number_for_del}?')
    if choice_for_del:
        os.remove(file_name) # Удаление текстового файла. Ниже будет создан новый текстовый файл.
                             # В этом файле будет отсутсвовать строка с удалённым контактом.

        while True: # Бесконечный цикл для выборки из списка list_for_new_txt строк с контактами
                    # и записи их в текстовый файл.
            contact_for_wr = list_for_new_txt.pop(0) # Получает из списка элемент с индексом 0,
                                                     # присваивает его значение переменной
                                                     # contact_for_wr, а в списке 
                                                     # list_for_new_txt удаляет его.
            write_contact_txt_gui(file_name, contact_for_wr) # Функция записи контакта в текстовый файл.
            if list_for_new_txt == []: # Если список пустой вывод на печать'Контакт №__ удалён' 
                                       # и выход из цикла.
                entry_win_del.delete(0, END) # Очистка поля для ввода.                      
                text_win_root.delete(1.0, END) # Очистка текстового поля корневого окна.
                text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления. 
                text_win_root.insert(1.0, f'    КОНТАКТ № {contact_number_for_del} УДАЛЁН\n')
                text_win_root.insert(1.0, f'{insert_line}\n') # Элемент оформления.                                       
                break # Выход из цикла.

# Функция-обработчик события нажатие кнопки "Закрыть".
def close_win_del():
    '''Функция для обработки события нажатие
       кнопки "Закрыть" в окне win_del.'''
    global open_win_del_contact_flag
    win_del.destroy() # Закрытие окна "Удалить контакт".
    text_win_root.delete(1.0, END) # Очистка поля.
    open_win_del_contact_flag = 0 # Окно закрыто.
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


