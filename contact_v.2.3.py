from tkinter import *

logo = 'logotip.ico'
file_name_txt = 'contact.txt'
#--------------------------Функции-обработчики событий------------------------------

# Функция-обработчик события нажатие кнопки "Показать контакты"
def show_contact():
    read_contact_txt_gui(file_name_txt)

# Функция-обработчик события нажатие кнопки "Поиск"
def open_win_find(): 
    pass

# Функция-обработчик события нажатие кнопки "Добавить контакт"
def open_win_add(): 
    pass

# Функция-обработчик события нажатие кнопки "Удалить контакт"
def open_win_del(): 
    pass

# Функция-обработчик события нажатие кнопки "Выход"
def close_win_root():
    pass

#-----------------------------------------------------------------------------------

#--------------------Дополнительные функции для обработки событий-------------------

def read_contact_txt_gui(file_name):
    '''Для получения данных из текстового файла.
       Обработка данных. Вызов функции для
       вывода на печать всех контактов'''
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
       Обработка данных. Вывод на печать контакта'''
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
#-----------------------------------------------------------------------------------

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




