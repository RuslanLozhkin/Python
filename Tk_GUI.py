# -*- coding: utf-8 -*-
'''
Ruslan Lozhkin 
ruslanlozhkin@yahoo.com
26.09.2017
Coding practic
'''
from tkinter import *

age = 45
name = 'Sedric'

root = Tk()
root.title(':)GUI Windos')
tx = Text(font = ('times', 12), width = 50, height = 15, wrap = WORD)
tx.pack(expand = NO, fill = BOTH)
tx.insert(100.100, 'Возраст {0} -- {1} лет.\n' \
'Почему {0} забавляется с этим языком программирования.' .format(name, age))
root.mainloop()