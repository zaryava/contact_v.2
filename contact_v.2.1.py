from tkinter import *

win_root = Tk()
win_root.title('Контакты')
win_root.iconbitmap('logotip.ico')
win_root.geometry('850x400+500+150')

text_win_root = Text(win_root)
text_win_root.pack()

btn_show_win_root = Button(win_root, text='Показать контакты')
btn_show_win_root.pack()

win_root.mainloop()










