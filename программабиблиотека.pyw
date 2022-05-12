from tkinter import *
import sys

def start():
    clean()
    label = Label(master, text='Добро пожаловать!\nВыберите действие:', font='Courier 30')
    label.pack()
    Button(text='Найти', command=found).pack()
    Button(text='Добавить', command=app).pack()
    Button(text='Показать все названия', command=look_names).pack()
    Button(text='Удалить всё', command=lock).pack()
    
def clean():
    global master
    master.destroy()
    master = Tk()

def lock():
    clean()
    Button(text='При нажатии на эту кнопку все данные будут стёрты', command=global_clean).pack() 
    end()

def global_clean():
    names = open('names.txt', 'w')
    print(' ', file=names)
    names.close()
    clean()
    end()

def end():
    Button(text='В главное меню', command=start).pack() 

def editfile():
    global entry, file_name
        
    txt_file = open(file_name + '.txt', 'w')
    text = entry.get()
    print(text, file=txt_file)
    txt_file.close()

    clean()
    label = Label(master, text='Файл создан', font='Courier 30')
    label.pack()
    end()

def makefile():
    global entry, file_name
        
    file_name = entry.get().replace(' ', '_')

    sys.stdin = open('names.txt')
    list_of_names = input().split() + [file_name]
    list_of_names.sort()
    sys.stdout = open('names.txt', 'w')
    for el in list_of_names:
        print(el, end=' ')

    clean()
    txt_file = open(file_name + '.txt', 'w')
    txt_file.close()
        
    clean()
    label = Label(master, text='Введите текст:', font='Courier 30')
    label.pack()
    entry = Entry()
    entry.pack(pady=10)
    Button(text='Создать', command=editfile).pack()    

def app():
    global entry
        
    clean()
        
    label = Label(master, text='Введите название:', font='Courier 30')
    label.pack()
        
    entry = Entry()
    entry.pack(pady=10)
    Button(text='Создать', command=makefile).pack()

def look():
    global entry
    file_name = entry.get()
    clean()
        
    sys.stdin = open('names.txt')
    names = input().split()

    flag = 0
    for i in range(len(names)):
        if names[i].lower().startswith(file_name.lower()):
            sys.stdin = open(names[i] + '.txt')
            label = Label(master, text='Успешно! Вот ваш файл:', font='Courier 40')
            label.pack()
            text = Text(wrap=WORD, font='Courier 20')
            text.insert(1.0, input())
            text.pack()
            flag = 1
            break
    if not flag:
        label = Label(master, text='Файл не найден', font='Courier 30')
        label.pack()
    end()

def found():
    global entry
    clean()

    label = Label(master, text='Введите название:', font='Courier 30')
    label.pack()

    entry = Entry()
    entry.pack(pady=10)
    Button(text='Поиск', command=look).pack()

def look_names():
    clean()
    
    sys.stdin = open('names.txt')
    t = ', '.join(input().split())
    print(t)
    label = Label(master, text=t, font='Courier 30')
    label.pack()
    end()


master = Tk()
master.attributes('-fullscreen', True)
entry = Entry()
start()
master.mainloop()
