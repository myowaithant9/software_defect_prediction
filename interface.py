import sys
from main import *

import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import *
import tkinter.ttk as ttk
import csv

import pandas as pd

from scipy.io import arff

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import interface_support
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix

from PIL import ImageTk,Image 

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


dataset = 0
dataset_path = ""
datactrl = 0

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    interface_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    interface_support.set_Tk_var()
    top = Toplevel1 (w)
    interface_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9' 
        _fgcolor = '#000000' 
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec'

        top.geometry("868x507+321+158")
        top.title("SDP System")
        top.configure(background="#a6ddf4")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        prj_info = prjInfo()  

class prjInfo:
    def __init__(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="green")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''*** Project Info ***''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.01, rely=0.214, height=31, width=161)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Project Description :''')
        
        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.8, rely=0.204, height=31, width=120)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Start''')
        self.Button1.configure(command=selectData)

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0.015, rely=0.31, relheight=0.105
                , relwidth=0.96)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''          Software Defect Prediction mechanisms are used to enhance the work of SQA process through the prediction of defect modules comprised with 5 stages :''')
        self.Message1.configure(width=623)

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.0138, rely=0.43, height=41, width=595)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#a6ddf4")
        self.Label4.configure(font="-family {Al Bayan} -size 16")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''1. Preprocessing       :   Remove null value, missing value and impossible instance''')

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.006, rely=0.525, height=31, width=586)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#a6ddf4")
        self.Label5.configure(font="-family {Al Bayan} -size 16")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(justify='left')
        self.Label5.configure(text='''2. Discretization        :   Convert continuous data values into finite set of values''')

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0.01, rely=0.74, relheight=0.099
                , relwidth=0.96)
        self.Message2.configure(background="#a6ddf4")
        self.Message2.configure(font="-family {Al Bayan} -size 16")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''4. Model Building      :   Adaptive Boosting based on Support Vector Machine-Radial \t\t Basis Function''')
        self.Message2.configure(width=625)

        self.Message3 = tk.Message(self.Frame2)
        self.Message3.place(relx=0.005, rely=0.615, relheight=0.085
                , relwidth=0.96)
        self.Message3.configure(background="#a6ddf4")
        self.Message3.configure(font="-family {Al Bayan} -size 16")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''3. Feature Selection :  Select features using Minimum Redundancy and Maximum \t\t Relevance (MRMR)''')
        self.Message3.configure(width=624)

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0.0045, rely=0.858, relheight=0.114
                , relwidth=0.96)
        self.Message4.configure(background="#a6ddf4")
        self.Message4.configure(font="-family {Al Bayan} -size 16")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text='''5. Comparison           :  Accuracy and performance measures used to compare with \t\t hybrid method against single classifier results''')
        self.Message4.configure(width=624)

class selectData:
    def viewData(self, top=None):
        global dataset_path
        global datactrl
        if self.TCombobox1.get() == "MW1":
            datactrl = 1
            dataset_path = 'MDP csv/MW1.csv'
            dataset = pd.read_csv(dataset_path)

        if self.TCombobox1.get() == "PC3":
            datactrl = 2
            dataset_path = 'MDP csv/PC3.csv'
            dataset = pd.read_csv(dataset_path)

        if self.TCombobox1.get() == "PC4":
            datactrl = 3
            dataset_path = 'MDP csv/PC4.csv'
            dataset = pd.read_csv(dataset_path)

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.0, rely=0.35, relheight=0.65, relwidth=1.0)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        TableMargin = Frame(self.Frame3, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=dataset.columns, height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
      
        for col in range(dataset.shape[1]):
            tree.heading(col, text=dataset.columns[col], anchor=W)
            tree.column('#'+str(col), stretch=NO, minwidth=0, width=100)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.pack()

        for i in range(dataset.shape[0]): 
            np.set_printoptions(formatter={'float_kind':'{:0f}'.format})
            tree.insert("", 0, values= dataset.values[i, :])

    def __init__(self, top=None):
        global dataset_path
        global datactrl
        datactrl = 0
        dataset_path = ''
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="green")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''*** Dataset Selection ***''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.0, rely=0.35, relheight=0.65, relwidth=1.0)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Label4 = tk.Label(self.Frame3)
        self.Label4.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(font="-family {Al Bayan} -size 16")
        self.Label4.configure(foreground="#171fff")
        self.Label4.configure(text='''Click "Import" button to view dataset''')


        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.031, rely=0.214, height=31, width=126)
        self.Label2.configure(background="#a6ddf4")
        self.Label2.configure(font="-family {Al Bayan} -size 16")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Choose Dataset''')

        self.TCombobox1 = ttk.Combobox(self.Frame2)
        self.TCombobox1.place(relx=0.264, rely=0.214, relheight=0.052
                , relwidth=0.319)
        self.TCombobox1['values']=("MW1", 'PC3', 'PC4')
        self.TCombobox1.configure(takefocus="")

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.62, rely=0.204, height=31, width=110)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Import''')
        self.Button1.configure(command=self.viewData)

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.822, rely=0.204, height=31, width=110)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocess''')
        self.Button2.configure(command=preprocess)

class preprocess:
    def ui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="green")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''*** Preprocessing ***''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.0, rely=0.35, relheight=0.65, relwidth=1.0)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0.031, rely=0.19, relheight=0.11, relwidth=0.8)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='nw')
        self.Message1.configure(text='''Preprocessing is done by removing item with impossible occurences and feature when all instances have same value''')
        self.Message1.configure(width=500)

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.8, rely=0.204, height=31, width=120)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Discretize''')
        self.Button1.configure(command=discretize)

        TableMargin = Frame(self.Frame3, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=pre_dataset.columns, height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
      
        for col in range(pre_dataset.shape[1]):
            tree.heading(col, text=pre_dataset.columns[col], anchor=W)
            tree.column('#'+str(col), stretch=NO, minwidth=0, width=100)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.pack()

        for i in range(pre_dataset.shape[0]):
            tree.insert("", 0, values= pre_dataset.values[i, :])

    def fun(self, top=None):
        global feature_data
        global target_data
        global pre_dataset

        pre_dataset, feature_data, target_data = main_preprocess(dataset_path, datactrl)

    def __init__(self, top=None):
        self.fun()
        self.ui()

class discretize:
    def ui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="green")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''*** Discretization ***''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.0, rely=0.35, relheight=0.65, relwidth=1.0)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0.031, rely=0.19, relheight=0.11, relwidth=0.8)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='nw')
        self.Message1.configure(text='''Discretization is done by transforming continuous data into discrete data ''')
        self.Message1.configure(width=500)

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.8, rely=0.204, height=31, width=120)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Build Model''')
        self.Button1.configure(command=selectModel)

        TableMargin = Frame(self.Frame3, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=pre_dataset.columns, height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
      
        for col in range(pre_dataset.shape[1]):
            tree.heading(col, text=pre_dataset.columns[col], anchor=W)
            tree.column('#'+str(col), stretch=NO, minwidth=0, width=100)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.pack()

        for i in range(discretize_data.shape[0]):
            tree.insert("", 0, values= discretize_data[i, :])

    def fun(self, top=None):
        global discretize_data
        discretize_data = main_discretize(feature_data)

    def __init__(self, top=None):
        self.fun()
        self.ui()

class selectModel:
    def ui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="green")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''*** Model Selection ***''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.0, rely=0.33, relheight=0.67, relwidth=1.0)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#a6ddf4")

        self.Message1 = tk.Message(self.Frame3)
        self.Message1.place(relx=0.031, rely=0.03, relheight=0.937
                , relwidth=0.936)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font='-family {Al Bayan} -size 16')
        self.Message1.configure(foreground="blue")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#a6ddf4")
        self.Message1.configure(text='''SVM Method
-   Predict data using Support Vector Machine with Radial Basis Function (RBF)

Hybrid Approach
-   Build model using Adaptive Boosting method based on RBF_SVM

MRMR
-   Select 10 features using Minimum-Redundancy-Maximum-Relevance (MRMR) method

Comparison Chart
-   Implement these methods and show comparison chart for Accuracy, Precision, Recall and F-score measures among them''')
        self.Message1.configure(width=604)

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.031, rely=0.214, height=31, width=126)
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 16")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Select Model''')

        self.TCombobox2 = ttk.Combobox(self.Frame2)
        self.TCombobox2.place(relx=0.224, rely=0.214, relheight=0.052
                , relwidth=0.319)
        self.TCombobox2["values"]=("SVM", "SVM + MRMR", "Hybrid Approach", "Hybrid Approach + MRMR", "Compare these methods")
        self.TCombobox2.configure(takefocus="")

        self.Button8 = tk.Button(self.Frame2)
        self.Button8.place(relx=0.58, rely=0.204, height=31, width=113)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(font="-family {Al Bayan} -size 16")
        self.Button8.configure(foreground="blue")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(relief="raised")
        self.Button8.configure(text='''Test Predict''')
        self.Button8.configure(command=self.testfun)

        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.78, rely=0.204, height=31, width=125)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Custom Predict''')
        self.Button9.configure(command=self.cusfun)

    def fun(self, top=None):
        global modelctrl
        if self.TCombobox2.get() == "SVM":
            modelctrl = 1
            if cusmodel == 0:
                outcome_ui = outcome()
            else:
                show_feature = showFeature()        
        elif self.TCombobox2.get() == "SVM + MRMR":
            modelctrl = 2
            show_feature = showFeature()        
        elif self.TCombobox2.get() == "Hybrid Approach":
            modelctrl = 3
            if cusmodel == 0:
                outcome_ui = outcome()
            else:
                show_feature = showFeature()     
        elif self.TCombobox2.get() == "Hybrid Approach + MRMR":
            modelctrl = 4
            show_feature = showFeature()     
        elif self.TCombobox2.get() == "Compare these methods":
            modelctrl = 5
            outcome_ui = outcome()
            
    def testfun(self, top=None):
        global cusmodel
        cusmodel = 0
        self.fun()

    def cusfun(self, top=None):
        global cusmodel
        cusmodel = 1
        self.fun()

    def __init__(self, top=None):
        self.ui()
      
class showFeature:
    def ui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="green")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''*** Feature Selection ***''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')
        
        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.031, rely=0.214, height=31, width=216)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Selected features list are :''')

        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.822, rely=0.214, height=31, width=87)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Next Step''')
        self.Button9.configure(command=outcome)

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0.005, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='sw')
        f1 = "1."+ pre_dataset.columns[feature_extraction[0][0]]
        self.Message1.configure(text=f1)
        self.Message1.configure(width=500)

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0.005, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message2.configure(background="#a6ddf4")
        self.Message2.configure(font="-family {Al Bayan} -size 16")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(anchor='sw')
        f2 = "2. "+ pre_dataset.columns[feature_extraction[0][1]]
        self.Message2.configure(text=f2)
        self.Message2.configure(width=500)

        self.Message3 = tk.Message(self.Frame2)
        self.Message3.place(relx=0.005, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message3.configure(background="#a6ddf4")
        self.Message3.configure(font="-family {Al Bayan} -size 16")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(anchor='sw')
        f3 = "3. "+ pre_dataset.columns[feature_extraction[0][2]]
        self.Message3.configure(text=f3)
        self.Message3.configure(width=500)

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0.005, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message4.configure(background="#a6ddf4")
        self.Message4.configure(font="-family {Al Bayan} -size 16")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(anchor='sw')
        f4 = "4. "+ pre_dataset.columns[feature_extraction[0][3]]
        self.Message4.configure(text=f4)
        self.Message4.configure(width=500)

        self.Message5 = tk.Message(self.Frame2)
        self.Message5.place(relx=0.005, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message5.configure(background="#a6ddf4")
        self.Message5.configure(font="-family {Al Bayan} -size 16")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(anchor='sw')
        f5 = "5. "+ pre_dataset.columns[feature_extraction[0][4]]
        self.Message5.configure(text=f5)
        self.Message5.configure(width=500)

        self.Message6 = tk.Message(self.Frame2)
        self.Message6.place(relx=0.5, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message6.configure(background="#a6ddf4")
        self.Message6.configure(font="-family {Al Bayan} -size 16")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(anchor='sw')
        f6 = "6. "+ pre_dataset.columns[feature_extraction[0][5]]
        self.Message6.configure(text=f6)
        self.Message6.configure(width=500)

        self.Message7 = tk.Message(self.Frame2)
        self.Message7.place(relx=0.5, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message7.configure(background="#a6ddf4")
        self.Message7.configure(font="-family {Al Bayan} -size 16")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(anchor='sw')
        f7 = "7. "+ pre_dataset.columns[feature_extraction[0][6]]
        self.Message7.configure(text=f7)
        self.Message7.configure(width=500)

        self.Message8 = tk.Message(self.Frame2)
        self.Message8.place(relx=0.5, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message8.configure(background="#a6ddf4")
        self.Message8.configure(font="-family {Al Bayan} -size 16")
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(anchor='sw')
        f8 = "8. "+ pre_dataset.columns[feature_extraction[0][7]]
        self.Message8.configure(text=f8)
        self.Message8.configure(width=500)

        self.Message9 = tk.Message(self.Frame2)
        self.Message9.place(relx=0.5, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message9.configure(background="#a6ddf4")
        self.Message9.configure(font="-family {Al Bayan} -size 16")
        self.Message9.configure(foreground="#000000")
        self.Message9.configure(highlightbackground="#d9d9d9")
        self.Message9.configure(highlightcolor="black")
        self.Message9.configure(anchor='sw')
        f9 = "9. "+ pre_dataset.columns[feature_extraction[0][8]]
        self.Message9.configure(text=f9)
        self.Message9.configure(width=500)

        self.Message10 = tk.Message(self.Frame2)
        self.Message10.place(relx=0.5, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message10.configure(background="#a6ddf4")
        self.Message10.configure(font="-family {Al Bayan} -size 16")
        self.Message10.configure(foreground="#000000")
        self.Message10.configure(highlightbackground="#d9d9d9")
        self.Message10.configure(highlightcolor="black")
        self.Message10.configure(anchor='sw')
        f10 = "10. "+ pre_dataset.columns[feature_extraction[0][9]]
        self.Message10.configure(text=f10)
        self.Message10.configure(width=500)

    def cusui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="green")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''*** Feature Selection ***''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')
        
        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.031, rely=0.214, height=31, width=386)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        if modelctrl == 1 or modelctrl == 3:
            self.Label3.configure(text='''Please add custom value for all features [1 ~ 10]:''')
        if modelctrl == 2 or modelctrl == 4:
            self.Label3.configure(text='''Please add custom value for selected features:''')
        
        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.66, rely=0.214, height=31, width=87)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Go Back''')
        self.Button9.configure(command=selectModel)

        self.Button10 = tk.Button(self.Frame2)
        self.Button10.place(relx=0.822, rely=0.214, height=31, width=87)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(font="-family {Al Bayan} -size 16")
        self.Button10.configure(foreground="blue")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(relief="raised")
        if modelctrl == 1 or modelctrl == 3:
            self.Button10.configure(text='''Next Page''')
            self.Button10.configure(command=self.page2)
        if modelctrl == 2 or modelctrl == 4:
            self.Button10.configure(text='''Predict''')
            self.Button10.configure(command=self.predict)

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f1 = "1."+ pre_dataset.columns[0]
        if modelctrl == 2 or modelctrl == 4:
            f1 = "1."+ pre_dataset.columns[feature_extraction[0][0]]
        self.Message1.configure(text=f1)
        self.Message1.configure(width=500)

        self.Entry1 = tk.Entry(self.Frame2)
        self.Entry1.place(relx=0.443, rely=0.35,height=27, relwidth=0.055)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message2.configure(background="#a6ddf4")
        self.Message2.configure(font="-family {Al Bayan} -size 16")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f2 = "2. "+ pre_dataset.columns[1]
        if modelctrl == 2 or modelctrl == 4:
            f2 = "2. "+ pre_dataset.columns[feature_extraction[0][1]]
        self.Message2.configure(text=f2)
        self.Message2.configure(width=500)

        self.Entry2 = tk.Entry(self.Frame2)
        self.Entry2.place(relx=0.443, rely=0.488,height=27, relwidth=0.055)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")        

        self.Message3 = tk.Message(self.Frame2)
        self.Message3.place(relx=0, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message3.configure(background="#a6ddf4")
        self.Message3.configure(font="-family {Al Bayan} -size 16")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f3 = "3. "+ pre_dataset.columns[2]
        if modelctrl == 2 or modelctrl == 4:        
            f3 = "3. "+ pre_dataset.columns[feature_extraction[0][2]]
        self.Message3.configure(text=f3)
        self.Message3.configure(width=500)

        self.Entry3 = tk.Entry(self.Frame2)
        self.Entry3.place(relx=0.443, rely=0.624,height=27, relwidth=0.055)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message4.configure(background="#a6ddf4")
        self.Message4.configure(font="-family {Al Bayan} -size 16")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f4 = "4. "+ pre_dataset.columns[3]
        if modelctrl == 2 or modelctrl == 4:
            f4 = "4. "+ pre_dataset.columns[feature_extraction[0][3]]
        self.Message4.configure(text=f4)
        self.Message4.configure(width=500)

        self.Entry4 = tk.Entry(self.Frame2)
        self.Entry4.place(relx=0.443, rely=0.759,height=27, relwidth=0.055)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Message5 = tk.Message(self.Frame2)
        self.Message5.place(relx=0, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message5.configure(background="#a6ddf4")
        self.Message5.configure(font="-family {Al Bayan} -size 16")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f5 = "5. "+ pre_dataset.columns[4]
        if modelctrl == 2 or modelctrl == 4:
            f5 = "5. "+ pre_dataset.columns[feature_extraction[0][4]]
        self.Message5.configure(text=f5)
        self.Message5.configure(width=500)

        self.Entry5 = tk.Entry(self.Frame2)
        self.Entry5.place(relx=0.443, rely=0.895,height=27, relwidth=0.055)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Message6 = tk.Message(self.Frame2)
        self.Message6.place(relx=0.5, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message6.configure(background="#a6ddf4")
        self.Message6.configure(font="-family {Al Bayan} -size 16")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f6 = "6. "+ pre_dataset.columns[5]
        if modelctrl == 2 or modelctrl == 4:
            f6 = "6. "+ pre_dataset.columns[feature_extraction[0][5]]
        self.Message6.configure(text=f6)
        self.Message6.configure(width=500)

        self.Entry6 = tk.Entry(self.Frame2)
        self.Entry6.place(relx=0.933, rely=0.35, height=27, relwidth=0.055)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Message7 = tk.Message(self.Frame2)
        self.Message7.place(relx=0.5, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message7.configure(background="#a6ddf4")
        self.Message7.configure(font="-family {Al Bayan} -size 16")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f7 = "7. "+ pre_dataset.columns[6]
        if modelctrl == 2 or modelctrl == 4:
            f7 = "7. "+ pre_dataset.columns[feature_extraction[0][6]]
        self.Message7.configure(text=f7)
        self.Message7.configure(width=500)

        self.Entry7 = tk.Entry(self.Frame2)
        self.Entry7.place(relx=0.933, rely=0.488, height=27, relwidth=0.055)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Message8 = tk.Message(self.Frame2)
        self.Message8.place(relx=0.5, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message8.configure(background="#a6ddf4")
        self.Message8.configure(font="-family {Al Bayan} -size 16")
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f8 = "8. "+ pre_dataset.columns[7]
        if modelctrl == 2 or modelctrl == 4:
            f8 = "8. "+ pre_dataset.columns[feature_extraction[0][7]]
        self.Message8.configure(text=f8)
        self.Message8.configure(width=500)

        self.Entry8 = tk.Entry(self.Frame2)
        self.Entry8.place(relx=0.933, rely=0.624, height=27, relwidth=0.055)
        self.Entry8.configure(background="white")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")

        self.Message9 = tk.Message(self.Frame2)
        self.Message9.place(relx=0.5, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message9.configure(background="#a6ddf4")
        self.Message9.configure(font="-family {Al Bayan} -size 16")
        self.Message9.configure(foreground="#000000")
        self.Message9.configure(highlightbackground="#d9d9d9")
        self.Message9.configure(highlightcolor="black")
        self.Message9.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f9 = "9. "+ pre_dataset.columns[8]
        if modelctrl == 2 or modelctrl == 4:
            f9 = "9. "+ pre_dataset.columns[feature_extraction[0][8]]
        self.Message9.configure(text=f9)
        self.Message9.configure(width=500)

        self.Entry9 = tk.Entry(self.Frame2)
        self.Entry9.place(relx=0.933, rely=0.759, height=27, relwidth=0.055)
        self.Entry9.configure(background="white")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")

        self.Message10 = tk.Message(self.Frame2)
        self.Message10.place(relx=0.5, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message10.configure(background="#a6ddf4")
        self.Message10.configure(font="-family {Al Bayan} -size 16")
        self.Message10.configure(foreground="#000000")
        self.Message10.configure(highlightbackground="#d9d9d9")
        self.Message10.configure(highlightcolor="black")
        self.Message10.configure(anchor='sw')
        if modelctrl == 1 or modelctrl == 3:
            f10 = "10. "+ pre_dataset.columns[9]
        if modelctrl == 2 or modelctrl == 4:
            f10 = "10. "+ pre_dataset.columns[feature_extraction[0][9]]
        self.Message10.configure(text=f10)
        self.Message10.configure(width=500)
        
        self.Entry10 = tk.Entry(self.Frame2)
        self.Entry10.place(relx=0.933, rely=0.895, height=27, relwidth=0.055)
        self.Entry10.configure(background="white")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(insertbackground="black")

    def page2(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="green")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''*** Feature Selection ***''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')
        
        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.031, rely=0.214, height=31, width=386)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Please add custom value for all features [11 ~ 20]:''')
        
        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.66, rely=0.214, height=31, width=87)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Go Back''')
        self.Button9.configure(command=self.cusui)

        self.Button10 = tk.Button(self.Frame2)
        self.Button10.place(relx=0.822, rely=0.214, height=31, width=87)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(font="-family {Al Bayan} -size 16")
        self.Button10.configure(foreground="blue")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(relief="raised")
        self.Button10.configure(text='''Next Page''')
        self.Button10.configure(command=self.page3)

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='sw')
        f1 = "11."+ pre_dataset.columns[10]
        self.Message1.configure(text=f1)
        self.Message1.configure(width=500)

        self.Entry11 = tk.Entry(self.Frame2)
        self.Entry11.place(relx=0.443, rely=0.35,height=27, relwidth=0.055)
        self.Entry11.configure(background="white")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message2.configure(background="#a6ddf4")
        self.Message2.configure(font="-family {Al Bayan} -size 16")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(anchor='sw')
        f2 = "12. "+ pre_dataset.columns[11]
        self.Message2.configure(text=f2)
        self.Message2.configure(width=500)

        self.Entry12 = tk.Entry(self.Frame2)
        self.Entry12.place(relx=0.443, rely=0.488,height=27, relwidth=0.055)
        self.Entry12.configure(background="white")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(insertbackground="black")        

        self.Message3 = tk.Message(self.Frame2)
        self.Message3.place(relx=0, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message3.configure(background="#a6ddf4")
        self.Message3.configure(font="-family {Al Bayan} -size 16")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(anchor='sw')
        f3 = "13. "+ pre_dataset.columns[12]
        self.Message3.configure(text=f3)
        self.Message3.configure(width=500)

        self.Entry13 = tk.Entry(self.Frame2)
        self.Entry13.place(relx=0.443, rely=0.624,height=27, relwidth=0.055)
        self.Entry13.configure(background="white")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(insertbackground="black")

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message4.configure(background="#a6ddf4")
        self.Message4.configure(font="-family {Al Bayan} -size 16")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(anchor='sw')
        f4 = "14. "+ pre_dataset.columns[13]
        self.Message4.configure(text=f4)
        self.Message4.configure(width=500)

        self.Entry14 = tk.Entry(self.Frame2)
        self.Entry14.place(relx=0.443, rely=0.759,height=27, relwidth=0.055)
        self.Entry14.configure(background="white")
        self.Entry14.configure(font="TkFixedFont")
        self.Entry14.configure(foreground="#000000")
        self.Entry14.configure(insertbackground="black")

        self.Message5 = tk.Message(self.Frame2)
        self.Message5.place(relx=0, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message5.configure(background="#a6ddf4")
        self.Message5.configure(font="-family {Al Bayan} -size 16")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(anchor='sw')
        f5 = "15. "+ pre_dataset.columns[14]
        self.Message5.configure(text=f5)
        self.Message5.configure(width=500)

        self.Entry15 = tk.Entry(self.Frame2)
        self.Entry15.place(relx=0.443, rely=0.895,height=27, relwidth=0.055)
        self.Entry15.configure(background="white")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(insertbackground="black")

        self.Message6 = tk.Message(self.Frame2)
        self.Message6.place(relx=0.5, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message6.configure(background="#a6ddf4")
        self.Message6.configure(font="-family {Al Bayan} -size 16")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(anchor='sw')
        f6 = "16. "+ pre_dataset.columns[15]
        self.Message6.configure(text=f6)
        self.Message6.configure(width=500)

        self.Entry16 = tk.Entry(self.Frame2)
        self.Entry16.place(relx=0.933, rely=0.35, height=27, relwidth=0.055)
        self.Entry16.configure(background="white")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(insertbackground="black")

        self.Message7 = tk.Message(self.Frame2)
        self.Message7.place(relx=0.5, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message7.configure(background="#a6ddf4")
        self.Message7.configure(font="-family {Al Bayan} -size 16")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(anchor='sw')
        f7 = "17. "+ pre_dataset.columns[16]
        self.Message7.configure(text=f7)
        self.Message7.configure(width=500)

        self.Entry17 = tk.Entry(self.Frame2)
        self.Entry17.place(relx=0.933, rely=0.488, height=27, relwidth=0.055)
        self.Entry17.configure(background="white")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(foreground="#000000")
        self.Entry17.configure(insertbackground="black")

        self.Message8 = tk.Message(self.Frame2)
        self.Message8.place(relx=0.5, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message8.configure(background="#a6ddf4")
        self.Message8.configure(font="-family {Al Bayan} -size 16")
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(anchor='sw')
        f8 = "18. "+ pre_dataset.columns[17]
        self.Message8.configure(text=f8)
        self.Message8.configure(width=500)

        self.Entry18 = tk.Entry(self.Frame2)
        self.Entry18.place(relx=0.933, rely=0.624, height=27, relwidth=0.055)
        self.Entry18.configure(background="white")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(foreground="#000000")
        self.Entry18.configure(insertbackground="black")

        self.Message9 = tk.Message(self.Frame2)
        self.Message9.place(relx=0.5, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message9.configure(background="#a6ddf4")
        self.Message9.configure(font="-family {Al Bayan} -size 16")
        self.Message9.configure(foreground="#000000")
        self.Message9.configure(highlightbackground="#d9d9d9")
        self.Message9.configure(highlightcolor="black")
        self.Message9.configure(anchor='sw')
        f9 = "19. "+ pre_dataset.columns[18]
        self.Message9.configure(text=f9)
        self.Message9.configure(width=500)

        self.Entry19 = tk.Entry(self.Frame2)
        self.Entry19.place(relx=0.933, rely=0.759, height=27, relwidth=0.055)
        self.Entry19.configure(background="white")
        self.Entry19.configure(font="TkFixedFont")
        self.Entry19.configure(foreground="#000000")
        self.Entry19.configure(insertbackground="black")

        self.Message10 = tk.Message(self.Frame2)
        self.Message10.place(relx=0.5, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message10.configure(background="#a6ddf4")
        self.Message10.configure(font="-family {Al Bayan} -size 16")
        self.Message10.configure(foreground="#000000")
        self.Message10.configure(highlightbackground="#d9d9d9")
        self.Message10.configure(highlightcolor="black")
        self.Message10.configure(anchor='sw')
        f10 = "20. "+ pre_dataset.columns[19]
        self.Message10.configure(text=f10)
        self.Message10.configure(width=500)
        
        self.Entry20 = tk.Entry(self.Frame2)
        self.Entry20.place(relx=0.933, rely=0.895, height=27, relwidth=0.055)
        self.Entry20.configure(background="white")
        self.Entry20.configure(font="TkFixedFont")
        self.Entry20.configure(foreground="#000000")
        self.Entry20.configure(insertbackground="black")
    
    def page3(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="green")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''*** Feature Selection ***''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')
        
        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.031, rely=0.214, height=31, width=386)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Please add custom value for all features [21 ~ 30]:''')
        
        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.66, rely=0.214, height=31, width=87)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Go Back''')
        self.Button9.configure(command=self.page2)

        self.Button10 = tk.Button(self.Frame2)
        self.Button10.place(relx=0.822, rely=0.214, height=31, width=87)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(font="-family {Al Bayan} -size 16")
        self.Button10.configure(foreground="blue")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(relief="raised")
        self.Button10.configure(text='''Next Page''')
        self.Button10.configure(command=self.page4)

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='sw')
        f1 = "21."+ pre_dataset.columns[20]
        self.Message1.configure(text=f1)
        self.Message1.configure(width=500)

        self.Entry21 = tk.Entry(self.Frame2)
        self.Entry21.place(relx=0.443, rely=0.35,height=27, relwidth=0.055)
        self.Entry21.configure(background="white")
        self.Entry21.configure(font="TkFixedFont")
        self.Entry21.configure(foreground="#000000")
        self.Entry21.configure(insertbackground="black")

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message2.configure(background="#a6ddf4")
        self.Message2.configure(font="-family {Al Bayan} -size 16")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(anchor='sw')
        f2 = "22. "+ pre_dataset.columns[21]
        self.Message2.configure(text=f2)
        self.Message2.configure(width=500)

        self.Entry22 = tk.Entry(self.Frame2)
        self.Entry22.place(relx=0.443, rely=0.488,height=27, relwidth=0.055)
        self.Entry22.configure(background="white")
        self.Entry22.configure(font="TkFixedFont")
        self.Entry22.configure(foreground="#000000")
        self.Entry22.configure(insertbackground="black")        

        self.Message3 = tk.Message(self.Frame2)
        self.Message3.place(relx=0, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message3.configure(background="#a6ddf4")
        self.Message3.configure(font="-family {Al Bayan} -size 16")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(anchor='sw')
        f3 = "23. "+ pre_dataset.columns[22]
        self.Message3.configure(text=f3)
        self.Message3.configure(width=500)

        self.Entry23 = tk.Entry(self.Frame2)
        self.Entry23.place(relx=0.443, rely=0.624,height=27, relwidth=0.055)
        self.Entry23.configure(background="white")
        self.Entry23.configure(font="TkFixedFont")
        self.Entry23.configure(foreground="#000000")
        self.Entry23.configure(insertbackground="black")

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message4.configure(background="#a6ddf4")
        self.Message4.configure(font="-family {Al Bayan} -size 16")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(anchor='sw')
        f4 = "24. "+ pre_dataset.columns[23]
        self.Message4.configure(text=f4)
        self.Message4.configure(width=500)

        self.Entry24 = tk.Entry(self.Frame2)
        self.Entry24.place(relx=0.443, rely=0.759,height=27, relwidth=0.055)
        self.Entry24.configure(background="white")
        self.Entry24.configure(font="TkFixedFont")
        self.Entry24.configure(foreground="#000000")
        self.Entry24.configure(insertbackground="black")

        self.Message5 = tk.Message(self.Frame2)
        self.Message5.place(relx=0, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message5.configure(background="#a6ddf4")
        self.Message5.configure(font="-family {Al Bayan} -size 16")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(anchor='sw')
        f5 = "25. "+ pre_dataset.columns[24]
        self.Message5.configure(text=f5)
        self.Message5.configure(width=500)

        self.Entry25 = tk.Entry(self.Frame2)
        self.Entry25.place(relx=0.443, rely=0.895,height=27, relwidth=0.055)
        self.Entry25.configure(background="white")
        self.Entry25.configure(font="TkFixedFont")
        self.Entry25.configure(foreground="#000000")
        self.Entry25.configure(insertbackground="black")

        self.Message6 = tk.Message(self.Frame2)
        self.Message6.place(relx=0.5, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message6.configure(background="#a6ddf4")
        self.Message6.configure(font="-family {Al Bayan} -size 16")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(anchor='sw')
        f6 = "26. "+ pre_dataset.columns[25]
        self.Message6.configure(text=f6)
        self.Message6.configure(width=500)

        self.Entry26 = tk.Entry(self.Frame2)
        self.Entry26.place(relx=0.933, rely=0.35, height=27, relwidth=0.055)
        self.Entry26.configure(background="white")
        self.Entry26.configure(font="TkFixedFont")
        self.Entry26.configure(foreground="#000000")
        self.Entry26.configure(insertbackground="black")

        self.Message7 = tk.Message(self.Frame2)
        self.Message7.place(relx=0.5, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message7.configure(background="#a6ddf4")
        self.Message7.configure(font="-family {Al Bayan} -size 16")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(anchor='sw')
        f7 = "27. "+ pre_dataset.columns[26]
        self.Message7.configure(text=f7)
        self.Message7.configure(width=500)

        self.Entry27 = tk.Entry(self.Frame2)
        self.Entry27.place(relx=0.933, rely=0.488, height=27, relwidth=0.055)
        self.Entry27.configure(background="white")
        self.Entry27.configure(font="TkFixedFont")
        self.Entry27.configure(foreground="#000000")
        self.Entry27.configure(insertbackground="black")

        self.Message8 = tk.Message(self.Frame2)
        self.Message8.place(relx=0.5, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message8.configure(background="#a6ddf4")
        self.Message8.configure(font="-family {Al Bayan} -size 16")
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(anchor='sw')
        f8 = "28. "+ pre_dataset.columns[27]
        self.Message8.configure(text=f8)
        self.Message8.configure(width=500)

        self.Entry28 = tk.Entry(self.Frame2)
        self.Entry28.place(relx=0.933, rely=0.624, height=27, relwidth=0.055)
        self.Entry28.configure(background="white")
        self.Entry28.configure(font="TkFixedFont")
        self.Entry28.configure(foreground="#000000")
        self.Entry28.configure(insertbackground="black")

        self.Message9 = tk.Message(self.Frame2)
        self.Message9.place(relx=0.5, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message9.configure(background="#a6ddf4")
        self.Message9.configure(font="-family {Al Bayan} -size 16")
        self.Message9.configure(foreground="#000000")
        self.Message9.configure(highlightbackground="#d9d9d9")
        self.Message9.configure(highlightcolor="black")
        self.Message9.configure(anchor='sw')
        f9 = "29. "+ pre_dataset.columns[28]
        self.Message9.configure(text=f9)
        self.Message9.configure(width=500)

        self.Entry29 = tk.Entry(self.Frame2)
        self.Entry29.place(relx=0.933, rely=0.759, height=27, relwidth=0.055)
        self.Entry29.configure(background="white")
        self.Entry29.configure(font="TkFixedFont")
        self.Entry29.configure(foreground="#000000")
        self.Entry29.configure(insertbackground="black")

        self.Message10 = tk.Message(self.Frame2)
        self.Message10.place(relx=0.5, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message10.configure(background="#a6ddf4")
        self.Message10.configure(font="-family {Al Bayan} -size 16")
        self.Message10.configure(foreground="#000000")
        self.Message10.configure(highlightbackground="#d9d9d9")
        self.Message10.configure(highlightcolor="black")
        self.Message10.configure(anchor='sw')
        f10 = "30. "+ pre_dataset.columns[29]
        self.Message10.configure(text=f10)
        self.Message10.configure(width=500)
        
        self.Entry30 = tk.Entry(self.Frame2)
        self.Entry30.place(relx=0.933, rely=0.895, height=27, relwidth=0.055)
        self.Entry30.configure(background="white")
        self.Entry30.configure(font="TkFixedFont")
        self.Entry30.configure(foreground="#000000")
        self.Entry30.configure(insertbackground="black")
    
    def page4(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="green")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''*** Feature Selection ***''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="blue")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''Outcome''')
        # -----------------------------siedebar end-----------------------------#
        
        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')
        
        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.031, rely=0.214, height=31, width=386)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Please add custom value for all features [31 ~ 37]:''')
        
        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.66, rely=0.214, height=31, width=87)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Go Back''')
        self.Button9.configure(command=self.page3)

        self.Button10 = tk.Button(self.Frame2)
        self.Button10.place(relx=0.822, rely=0.214, height=31, width=87)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(font="-family {Al Bayan} -size 16")
        self.Button10.configure(foreground="blue")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(relief="raised")
        self.Button10.configure(text='''Predict''')
        self.Button10.configure(command=self.predict)

        self.Message1 = tk.Message(self.Frame2)
        self.Message1.place(relx=0, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message1.configure(background="#a6ddf4")
        self.Message1.configure(font="-family {Al Bayan} -size 16")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(anchor='sw')
        f1 = "31."+ pre_dataset.columns[30]
        self.Message1.configure(text=f1)
        self.Message1.configure(width=500)

        self.Entry31 = tk.Entry(self.Frame2)
        self.Entry31.place(relx=0.443, rely=0.35,height=27, relwidth=0.055)
        self.Entry31.configure(background="white")
        self.Entry31.configure(font="TkFixedFont")
        self.Entry31.configure(foreground="#000000")
        self.Entry31.configure(insertbackground="black")

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message2.configure(background="#a6ddf4")
        self.Message2.configure(font="-family {Al Bayan} -size 16")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(anchor='sw')
        f2 = "32. "+ pre_dataset.columns[31]
        self.Message2.configure(text=f2)
        self.Message2.configure(width=500)

        self.Entry32 = tk.Entry(self.Frame2)
        self.Entry32.place(relx=0.443, rely=0.488,height=27, relwidth=0.055)
        self.Entry32.configure(background="white")
        self.Entry32.configure(font="TkFixedFont")
        self.Entry32.configure(foreground="#000000")
        self.Entry32.configure(insertbackground="black")        

        self.Message3 = tk.Message(self.Frame2)
        self.Message3.place(relx=0, rely=0.583, relheight=0.105, relwidth=0.5)
        self.Message3.configure(background="#a6ddf4")
        self.Message3.configure(font="-family {Al Bayan} -size 16")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(anchor='sw')
        f3 = "33. "+ pre_dataset.columns[32]
        self.Message3.configure(text=f3)
        self.Message3.configure(width=500)

        self.Entry33 = tk.Entry(self.Frame2)
        self.Entry33.place(relx=0.443, rely=0.624,height=27, relwidth=0.055)
        self.Entry33.configure(background="white")
        self.Entry33.configure(font="TkFixedFont")
        self.Entry33.configure(foreground="#000000")
        self.Entry33.configure(insertbackground="black")

        self.Message4 = tk.Message(self.Frame2)
        self.Message4.place(relx=0, rely=0.718, relheight=0.105, relwidth=0.5)
        self.Message4.configure(background="#a6ddf4")
        self.Message4.configure(font="-family {Al Bayan} -size 16")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(anchor='sw')
        f4 = "34. "+ pre_dataset.columns[33]
        self.Message4.configure(text=f4)
        self.Message4.configure(width=500)

        self.Entry34 = tk.Entry(self.Frame2)
        self.Entry34.place(relx=0.443, rely=0.759,height=27, relwidth=0.055)
        self.Entry34.configure(background="white")
        self.Entry34.configure(font="TkFixedFont")
        self.Entry34.configure(foreground="#000000")
        self.Entry34.configure(insertbackground="black")

        self.Message5 = tk.Message(self.Frame2)
        self.Message5.place(relx=0, rely=0.854, relheight=0.105, relwidth=0.5)
        self.Message5.configure(background="#a6ddf4")
        self.Message5.configure(font="-family {Al Bayan} -size 16")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(anchor='sw')
        f5 = "35. "+ pre_dataset.columns[34]
        self.Message5.configure(text=f5)
        self.Message5.configure(width=500)

        self.Entry35 = tk.Entry(self.Frame2)
        self.Entry35.place(relx=0.443, rely=0.895,height=27, relwidth=0.055)
        self.Entry35.configure(background="white")
        self.Entry35.configure(font="TkFixedFont")
        self.Entry35.configure(foreground="#000000")
        self.Entry35.configure(insertbackground="black")

        self.Message6 = tk.Message(self.Frame2)
        self.Message6.place(relx=0.5, rely=0.311, relheight=0.105, relwidth=0.5)
        self.Message6.configure(background="#a6ddf4")
        self.Message6.configure(font="-family {Al Bayan} -size 16")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(anchor='sw')
        f6 = "36. "+ pre_dataset.columns[35]
        self.Message6.configure(text=f6)
        self.Message6.configure(width=500)

        self.Entry36 = tk.Entry(self.Frame2)
        self.Entry36.place(relx=0.933, rely=0.35, height=27, relwidth=0.055)
        self.Entry36.configure(background="white")
        self.Entry36.configure(font="TkFixedFont")
        self.Entry36.configure(foreground="#000000")
        self.Entry36.configure(insertbackground="black")

        self.Message7 = tk.Message(self.Frame2)
        self.Message7.place(relx=0.5, rely=0.447, relheight=0.105, relwidth=0.5)
        self.Message7.configure(background="#a6ddf4")
        self.Message7.configure(font="-family {Al Bayan} -size 16")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(anchor='sw')
        f7 = "37. "+ pre_dataset.columns[36]
        self.Message7.configure(text=f7)
        self.Message7.configure(width=500)

        self.Entry37 = tk.Entry(self.Frame2)
        self.Entry37.place(relx=0.933, rely=0.488, height=27, relwidth=0.055)
        self.Entry37.configure(background="white")
        self.Entry37.configure(font="TkFixedFont")
        self.Entry37.configure(foreground="#000000")
        self.Entry37.configure(insertbackground="black")

    def predict(self, top=None):
        global cusdata 
        cusdata = np.zeros(len(pre_dataset.columns)-1).reshape(1,len(pre_dataset.columns)-1)

        if modelctrl ==  1 or modelctrl == 3:
            if self.Entry1.get() != "":
                cusdata[0][0] = self.Entry1.get()
            if self.Entry2.get() != "":            
                cusdata[0][1] = self.Entry2.get()
            if self.Entry3.get() != "":
                cusdata[0][2] = self.Entry3.get()
            if self.Entry4.get() != "":
                cusdata[0][3] = self.Entry4.get()
            if self.Entry5.get() != "":
                cusdata[0][4] = self.Entry5.get()
            if self.Entry6.get() != "":
                cusdata[0][5] = self.Entry6.get()
            if self.Entry7.get() != "":
                cusdata[0][6] = self.Entry7.get()
            if self.Entry8.get() != "":
                cusdata[0][7] = self.Entry8.get()
            if self.Entry9.get() != "":
                cusdata[0][8] = self.Entry9.get()
            if self.Entry10.get() != "":
                cusdata[0][9] = self.Entry10.get()
            if self.Entry11.get() != "":
                cusdata[0][10] = self.Entry11.get()
            if self.Entry12.get() != "":
                cusdata[0][11] = self.Entry12.get()
            if self.Entry13.get() != "":
                cusdata[0][12] = self.Entry13.get()
            if self.Entry14.get() != "":
                cusdata[0][13] = self.Entry14.get()
            if self.Entry15.get() != "":
                cusdata[0][14] = self.Entry15.get()
            if self.Entry16.get() != "":
                cusdata[0][15] = self.Entry16.get()
            if self.Entry17.get() != "":
                cusdata[0][16] = self.Entry17.get()
            if self.Entry18.get() != "":
                cusdata[0][17] = self.Entry18.get()
            if self.Entry19.get() != "":
                cusdata[0][18] = self.Entry19.get()
            if self.Entry20.get() != "":
                cusdata[0][19] = self.Entry20.get()
            if self.Entry21.get() != "":
                cusdata[0][20] = self.Entry21.get()
            if self.Entry22.get() != "":
                cusdata[0][21] = self.Entry22.get()
            if self.Entry23.get() != "":
                cusdata[0][22] = self.Entry23.get()
            if self.Entry24.get() != "":
                cusdata[0][23] = self.Entry24.get()
            if self.Entry25.get() != "":
                cusdata[0][24] = self.Entry25.get()
            if self.Entry26.get() != "":
                cusdata[0][25] = self.Entry26.get()
            if self.Entry27.get() != "":
                cusdata[0][26] = self.Entry27.get()
            if self.Entry28.get() != "":
                cusdata[0][27] = self.Entry28.get()
            if self.Entry29.get() != "":
                cusdata[0][28] = self.Entry29.get()
            if self.Entry30.get() != "":
                cusdata[0][29] = self.Entry30.get()
            if self.Entry31.get() != "":
                cusdata[0][30] = self.Entry31.get()
            if self.Entry32.get() != "":
                cusdata[0][31] = self.Entry32.get()
            if self.Entry33.get() != "":
                cusdata[0][32] = self.Entry33.get()
            if self.Entry34.get() != "":
                cusdata[0][33] = self.Entry34.get()
            if self.Entry35.get() != "":
                cusdata[0][34] = self.Entry35.get()
            if self.Entry36.get() != "":
                cusdata[0][35] = self.Entry36.get()
            if self.Entry37.get() != "":
                cusdata[0][36] = self.Entry37.get()
        if modelctrl ==  2 or modelctrl == 4:
            if self.Entry1.get() != "":
                cusdata[0][feature_extraction[0][0]] = self.Entry1.get()
            if self.Entry2.get() != "":            
                cusdata[0][feature_extraction[0][1]] = self.Entry2.get()
            if self.Entry3.get() != "":
                cusdata[0][feature_extraction[0][2]] = self.Entry3.get()
            if self.Entry4.get() != "":
                cusdata[0][feature_extraction[0][3]] = self.Entry4.get()
            if self.Entry5.get() != "":
                cusdata[0][feature_extraction[0][4]] = self.Entry5.get()
            if self.Entry6.get() != "":
                cusdata[0][feature_extraction[0][5]] = self.Entry6.get()
            if self.Entry7.get() != "":
                cusdata[0][feature_extraction[0][6]] = self.Entry7.get()
            if self.Entry8.get() != "":
                cusdata[0][feature_extraction[0][7]] = self.Entry8.get()
            if self.Entry9.get() != "":
                cusdata[0][feature_extraction[0][8]] = self.Entry9.get()
            if self.Entry10.get() != "":
                cusdata[0][feature_extraction[0][9]] = self.Entry10.get()
        outcome_ui = outcome()
        
    def fun(self, top=None):
        global selected_data
        global feature_extraction
        num_fea = 10
        feature_extraction = feature_extract(discretize_data, target_data, num_fea)

        selected_data = discretize_data[:, feature_extraction[0]]

    def __init__(self, top=None):
        self.fun()
        if cusmodel == 1:
            self.cusui()
        else:
            self.ui()

class outcome:
    def ui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="green")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''*** Outcome ***''')
        # -----------------------------siedebar end-----------------------------#

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        if datactrl == 1:
            tmp = "MW1 Dataset"
        if datactrl == 2:
            tmp = "PC3 Dataset"
        if datactrl == 3:
            tmp = "PC4 Dataset"

        if modelctrl == 1:
            modeltmp = tmp + " using SVM"
            self.Label3.place(relx=0.15, rely=0.214, height=31, width=416)
        elif modelctrl == 2:
            modeltmp = tmp + " using SVM with MRMR"
            self.Label3.place(relx=0.18, rely=0.214, height=31, width=416)
        elif modelctrl == 3:
            modeltmp = tmp + " using AdaBoost SVM-RBF"
            self.Label3.place(relx=0.18, rely=0.214, height=31, width=416)
        elif modelctrl == 4:
            modeltmp = tmp + " using AdaBoost SVM-RBF with MRMR"
            self.Label3.place(relx=0.18, rely=0.214, height=31, width=416)  
        self.Label3.configure(text=modeltmp)

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.023, rely=0.311, height=31, width=85)
        self.Label4.configure(background="#a6ddf4")
        self.Label4.configure(font="-family {Al Bayan} -size 16")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Accuracy :''')

        self.Label9 = tk.Label(self.Frame2)
        self.Label9.place(relx=0.215, rely=0.311, height=31, width=100)
        self.Label9.configure(background="#a6ddf4")
        self.Label9.configure(font="-family {Al Bayan} -size 16")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(justify='left')
        self.Label9.configure(text=float("{0:.3f}".format(accuracy)))

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.016, rely=0.408, height=31, width=96)
        self.Label5.configure(background="#a6ddf4")
        self.Label5.configure(font="-family {Al Bayan} -size 16")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(justify='left')
        self.Label5.configure(text='''Precision :''')

        self.Label10 = tk.Label(self.Frame2)
        self.Label10.place(relx=0.215, rely=0.408, height=31, width=100)
        self.Label10.configure(background="#a6ddf4")
        self.Label10.configure(font="-family {Al Bayan} -size 16")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(justify='left')
        self.Label10.configure(text=float("{0:.3f}".format(precision)))

        self.Label6 = tk.Label(self.Frame2)
        self.Label6.place(relx=0.026, rely=0.505, height=31, width=61)
        self.Label6.configure(background="#a6ddf4")
        self.Label6.configure(font="-family {Al Bayan} -size 16")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Recall :''')
        
        self.Label11 = tk.Label(self.Frame2)
        self.Label11.place(relx=0.215, rely=0.505, height=31, width=100)
        self.Label11.configure(background="#a6ddf4")
        self.Label11.configure(font="-family {Al Bayan} -size 16")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(justify='left')
        self.Label11.configure(text=float("{0:.3f}".format(recall)))

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.028, rely=0.602, height=31, width=73)
        self.Label7.configure(background="#a6ddf4")
        self.Label7.configure(font="-family {Al Bayan} -size 16")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''F-score :''')

        self.Label12 = tk.Label(self.Frame2)
        self.Label12.place(relx=0.215, rely=0.602, height=31, width=100)
        self.Label12.configure(background="#a6ddf4")
        self.Label12.configure(font="-family {Al Bayan} -size 16")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(justify='left')
        self.Label12.configure(text=float("{0:.3f}".format(fscore)))

        self.Label8 = tk.Label(self.Frame2)
        self.Label8.place(relx=0.028, rely=0.699, height=31, width=147)
        self.Label8.configure(background="#a6ddf4")
        self.Label8.configure(font="-family {Al Bayan} -size 16")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Confusion Matrix :''')

        self.Label13 = tk.Label(self.Frame2)
        self.Label13.place(relx=0.245, rely=0.699, height=62, width=100)
        self.Label13.configure(background="#a6ddf4")
        self.Label13.configure(font="-family {Al Bayan} -size 16")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(justify='left')
        self.Label13.configure(text=cm)

        self.Label14 = tk.Label(self.Frame2)
        self.Label14.place(relx=0.031, rely=0.835, height=31, width=239)
        self.Label14.configure(background="#a6ddf4")
        self.Label14.configure(font="-family {Al Bayan} -size 16")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(justify='left')
        self.Label14.configure(text='''Correctly Classified Instances :''')

        self.Label15 = tk.Label(self.Frame2)
        self.Label15.place(relx=0.4, rely=0.835, height=31, width=100)
        self.Label15.configure(background="#a6ddf4")
        self.Label15.configure(font="-family {Al Bayan} -size 16")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(justify='left')
        self.Label15.configure(text=correct)

        self.Label16 = tk.Label(self.Frame2)
        self.Label16.place(relx=0.016, rely=0.914, height=31, width=267)
        self.Label16.configure(background="#a6ddf4")
        self.Label16.configure(font="-family {Al Bayan} -size 16")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(justify='left')
        self.Label16.configure(text='''Incorrectly Classified Instances :''')

        self.Label17 = tk.Label(self.Frame2)
        self.Label17.place(relx=0.41, rely=0.913, height=31, width=100)
        self.Label17.configure(background="#a6ddf4")
        self.Label17.configure(font="-family {Al Bayan} -size 16")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(justify='left')
        self.Label17.configure(text=incorrect)

        self.Button8 = tk.Button(self.Frame2)
        self.Button8.place(relx=0.62, rely=0.9, height=31, width=130)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(font="-family {Al Bayan} -size 16")
        self.Button8.configure(foreground="blue")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(justify='left')
        self.Button8.configure(relief="raised")
        self.Button8.configure(text='''Rebuild Model''')
        self.Button8.configure(command=selectModel)

        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.835, rely=0.9, height=31, width=100)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(justify='left')
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Restart''')
        self.Button9.configure(command=prjInfo)

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.4, rely=0.311, relheight=0.5, relwidth=0.65)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        if modelctrl == 1:
            txt1 = "SVM"
        elif modelctrl == 2:
            txt1 = "SVM + MRMR"
        elif modelctrl == 3:
            txt1 = "Hybrid Approach"
        elif modelctrl == 4:
            txt1 = "Hybrid Approach + MRMR"
        
        if datactrl == 1:
            txt2 = "MW1"
        if datactrl == 2:
            txt2 = "PC3"
        if datactrl == 3:
            txt2 = "PC4"
        
        txt = txt1 +" for "+ txt2

        Data1 = {'Objects': ['Accuracy', 'Precision', 'Recall', 'F-score'],
        'Performance': [accuracy, precision, recall, fscore]
       }

        df1 = DataFrame(Data1, columns= ['Objects', 'Performance'])
        df1 = df1[['Objects', 'Performance']].groupby('Objects').sum()

        figure1 = plt.Figure(figsize=(6,1), dpi=70)
        ax1 = figure1.add_subplot(111)
        ax1.set_xlim([0.85, 1])
        bar1 = FigureCanvasTkAgg(figure1, self.Frame3)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1.plot(kind='barh', legend=True, ax=ax1)

        ax1.set_title(txt)
    
    def compare_ui(self, top=None):
        # -----------------------------siedebar start-----------------------------#
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.02, relheight=1.036, relwidth=0.259)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#21b5ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.057, height=52, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#21b5ff")
        self.Label2.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SDP System''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.0, rely=0.419, height=62, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(font="-family {Al Bayan} -size 16")
        self.Button2.configure(foreground="blue")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(justify='left')
        self.Button2.configure(relief="raised")
        self.Button2.configure(text='''Preprocessing''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.0, rely=0.305, height=62, width=227)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(font="-family {Al Bayan} -size 16")
        self.Button3.configure(foreground="blue")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(justify='left')
        self.Button3.configure(relief="raised")
        self.Button3.configure(text='''Dataset Selection''')

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.0, rely=0.533, height=62, width=227)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font="-family {Al Bayan} -size 16")
        self.Button4.configure(foreground="blue")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(justify='left')
        self.Button4.configure(relief="raised")
        self.Button4.configure(text='''Discretization''')

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.0, rely=0.648, height=62, width=227)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(font="-family {Al Bayan} -size 16")
        self.Button5.configure(foreground="blue")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(justify='left')
        self.Button5.configure(relief="raised")
        self.Button5.configure(text='''Model Selection''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.19, height=62, width=227)
        self.Button1.configure(activebackground="#ececec")#21b5ff
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")

        self.Button1.configure(font="-family {Al Bayan} -size 16")
        self.Button1.configure(foreground="blue")

        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(justify='left')
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Project Info''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.0, rely=0.762, height=62, width=227)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(font="-family {Al Bayan} -size 16")
        self.Button6.configure(foreground="blue")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(justify='left')
        self.Button6.configure(relief="raised")
        self.Button6.configure(text='''Feature Selection''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.0, rely=0.876, height=62, width=227)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(font="-family {Al Bayan} -size 16")
        self.Button7.configure(foreground="green")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(justify='left')
        self.Button7.configure(relief="raised")
        self.Button7.configure(text='''*** Outcome ***''')
        # -----------------------------siedebar end-----------------------------#

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.258, rely=-0.01, relheight=1.016
                , relwidth=0.743)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#a6ddf4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.07, height=46, width=475)
        self.Label1.configure(activebackground="#a6ddf4")
        self.Label1.configure(activeforeground="#1c38ed")
        self.Label1.configure(background="#a6ddf4")
        self.Label1.configure(font="-family {Al Bayan} -size 20 -weight bold")
        self.Label1.configure(foreground="#171fff")
        self.Label1.configure(highlightbackground="#ffffffffffff")
        self.Label1.configure(highlightcolor="#2b1582")
        self.Label1.configure(text='''Welcome to Software Defect Prediction System''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.2, rely=0.214, height=31, width=416)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#a6ddf4")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(font="-family {Al Bayan} -size 16")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        if datactrl == 1:
            tmp = "MW1"
        if datactrl == 2:
            tmp = "PC3"
        if datactrl == 3:
            tmp = "PC4"
        modeltmp = "Methods Comparison Chart for " + tmp + " Dataset"
        self.Label3.configure(text=modeltmp)
        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.202, rely=0.35, relheight=0.476, relwidth=0.628)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        txt = "For "+ tmp + " Dataset"

        Data1 = {'Objects': ['Accuracy', 'Precision', 'Recall', 'F-score'],
        'SVM': [accuracy_s, precision_s, recall_s, fscore_s],
        'SVM + MRMR': [accuracy_sf, precision_sf, recall_sf, fscore_sf],
        'Hybrid': [accuracy_a, precision_a, recall_a, fscore_a],
        'Hybrid + MRMR': [accuracy_af, precision_af, recall_af, fscore_af]
       }

        df1 = DataFrame(Data1, columns= ['Objects', 'SVM', 'Hybrid', 'SVM + MRMR', 'Hybrid + MRMR'])
        df1 = df1[['Objects', 'SVM', 'Hybrid', 'SVM + MRMR', 'Hybrid + MRMR']].groupby('Objects').sum()

        figure1 = plt.Figure(figsize=(6,1), dpi=70)
        ax1 = figure1.add_subplot(111)
        ax1.set_xlim([0.85, 1])
        bar1 = FigureCanvasTkAgg(figure1, self.Frame3)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1.plot(kind='barh', legend=True, ax=ax1)
        ax1.set_title(txt)
        
        self.Button8 = tk.Button(self.Frame2)
        self.Button8.place(relx=0.62, rely=0.9, height=31, width=130)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(font="-family {Al Bayan} -size 16")
        self.Button8.configure(foreground="blue")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(justify='left')
        self.Button8.configure(relief="raised")
        self.Button8.configure(text='''Rebuild Model''')
        self.Button8.configure(command=selectModel)

        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.835, rely=0.9, height=31, width=100)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(font="-family {Al Bayan} -size 16")
        self.Button9.configure(foreground="blue")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(justify='left')
        self.Button9.configure(relief="raised")
        self.Button9.configure(text='''Restart''')
        self.Button9.configure(command=prjInfo)

    def fun(self, top=None):
        global concat_data
        global accuracy
        global precision
        global recall
        global fscore
        global cm
        global correct
        global incorrect

        global accuracy_s
        global precision_s
        global recall_s
        global fscore_s

        global accuracy_sf
        global precision_sf
        global recall_sf
        global fscore_sf

        global accuracy_a
        global precision_a
        global recall_a
        global fscore_a

        global accuracy_af
        global precision_af
        global recall_af
        global fscore_af

        if modelctrl == 5:
            num_fea = 10
            feature_extraction_c = feature_extract(discretize_data, target_data, num_fea)
            selected_data_a = discretize_data[:, feature_extraction_c[0]]

            concat_data_s = concat(discretize_data, target_data)
            concat_data_a = concat(discretize_data, target_data)
            concat_data_sf = concat(selected_data_a, target_data)
            concat_data_af = concat(selected_data_a, target_data)

            train_data_s, test_data_s = train_test_split(concat_data_s, test_size=0.3, shuffle=False) # random_state=42 # shuffle true --> 0.8951612903225806 # shuffle false --> 0.9274193548387096
            train_data_sf, test_data_sf = train_test_split(concat_data_sf, test_size=0.3, shuffle=False) # random_state=42 # shuffle true --> 0.8951612903225806 # shuffle false --> 0.9274193548387096
            train_data_a, test_data_a = train_test_split(concat_data_a, test_size=0.3, shuffle=False) # random_state=42 # shuffle true --> 0.8951612903225806 # shuffle false --> 0.9274193548387096
            train_data_af, test_data_af = train_test_split(concat_data_af, test_size=0.3, shuffle=False) # random_state=42 # shuffle true --> 0.8951612903225806 # shuffle false --> 0.9274193548387096


            X_train_s = train_data_s[:,0:37]
            Y_train_s = train_data_s[:,37].astype('int')
            X_test_s = test_data_s[:,0:37]
            Y_test_s = test_data_s[:,37].astype('int')

            X_train_a = train_data_s[:,0:37]
            Y_train_a = train_data_s[:,37].astype('int')
            X_test_a = test_data_s[:,0:37]
            Y_test_a = test_data_s[:,37].astype('int')

            X_train_sf = train_data_af[:,0:10]
            Y_train_sf = train_data_af[:,10].astype('int')
            X_test_sf = test_data_af[:,0:10]
            Y_test_sf = test_data_af[:,10].astype('int')

            X_train_af = train_data_af[:,0:10]
            Y_train_af = train_data_af[:,10].astype('int')
            X_test_af = test_data_af[:,0:10]
            Y_test_af = test_data_af[:,10].astype('int')

           
            clf_tree_c = SVC(kernel='rbf', random_state=0, gamma=.01, C=10000)

            pred_train_s, pred_test_s = generic_clf(Y_train_s, X_train_s, Y_test_s, X_test_s, clf_tree_c)
            pred_train_sf, pred_test_sf = generic_clf(Y_train_sf, X_train_sf, Y_test_sf, X_test_sf, clf_tree_c)

            prf_s = precision_recall_fscore_support(Y_test_s, pred_test_s, average=None)
            prf_sf = precision_recall_fscore_support(Y_test_sf, pred_test_sf, average=None)

            precision_s = prf_s[0][0]
            recall_s = prf_s[1][0]
            fscore_s = prf_s[2][0]
            accuracy_s = accuracy_score(Y_test_s, pred_test_s)

            precision_sf = prf_sf[0][0]
            recall_sf = prf_sf[1][0]
            fscore_sf = prf_sf[2][0]
            accuracy_sf = accuracy_score(Y_test_sf, pred_test_sf)

            if (datactrl == 1):
                x_range_a = range(0, 2, 1)
                x_range_af = range(0, 13, 1)
            if (datactrl == 2):
                x_range_a = range(0, 13, 1)
                x_range_af = range(0, 2, 1)
            if (datactrl == 3):
                x_range_a = range(0, 2, 1)
                x_range_af = range(0, 6, 1)

            for M in x_range_a:  
                n_train_a, n_test_a = len(X_train_a), len(X_test_a)
                w = np.ones(n_train_a) / n_train_a
                pred_train_a, pred_test_a = [np.zeros(n_train_a), np.zeros(n_test_a)]

                for i in range(M):
                    clf_tree_c.fit(X_train_a, Y_train_a, sample_weight = w)
                    pred_train_a_i = clf_tree_c.predict(X_train_a)
                    pred_test_a_i = clf_tree_c.predict(X_test_a)

                    prf_a = precision_recall_fscore_support(Y_test_a, pred_test_a_i, average=None)

                    precision_a = prf_a[0][0]
                    recall_a = prf_a[1][0]
                    fscore_a = prf_a[2][0]
                    accuracy_a = accuracy_score(Y_test_a, pred_test_a_i)

                    miss_a = [int(x) for x in (pred_train_a_i != Y_train_a)]
                    miss2_a = [x if x==1 else -1 for x in miss_a]
                    err_m_a = np.dot(w,miss_a) / sum(w)

                    alpha_m_a = 0.5 * np.log( (1 - err_m_a) / float(err_m_a))
                    w = np.multiply(w, np.exp([float(x) * alpha_m_a for x in miss2_a]))

                    pred_train_a = [sum(x) for x in zip(pred_train_a, 
                                                    [x * alpha_m_a for x in pred_train_a_i])]
                    pred_test_a = [sum(x) for x in zip(pred_test_a, 
                                                    [x * alpha_m_a for x in pred_test_a_i])]
                pred_train_a, pred_test_a = np.sign(pred_train_a), np.sign(pred_test_a)
            
            for M_af in x_range_af:  
                n_train_af, n_test_af = len(X_train_af), len(X_test_af)
                w_af = np.ones(n_train_af) / n_train_af
                pred_train_af, pred_test_af = [np.zeros(n_train_af), np.zeros(n_test_af)]

                for i in range(M_af):
                    clf_tree_c.fit(X_train_af, Y_train_af, sample_weight = w_af)
                    pred_train_i_af = clf_tree_c.predict(X_train_af)
                    pred_test_i_af = clf_tree_c.predict(X_test_af)

                    prf_ada_af = precision_recall_fscore_support(Y_test_af, pred_test_i_af, average=None)

                    precision_af = prf_ada_af[0][0]
                    recall_af = prf_ada_af[1][0]
                    fscore_af = prf_ada_af[2][0]
                    accuracy_af = accuracy_score(Y_test_af, pred_test_i_af)
                    
                    miss_af = [int(x) for x in (pred_train_i_af != Y_train_af)]
                    miss2_af = [x if x==1 else -1 for x in miss_af]
                    err_m_af = np.dot(w_af,miss_af) / sum(w_af)

                    alpha_m_af = 0.5 * np.log( (1 - err_m_af) / float(err_m_af))
                    w_af = np.multiply(w_af, np.exp([float(x) * alpha_m_af for x in miss2_af]))

                    pred_train_af = [sum(x) for x in zip(pred_train_af, 
                                                    [x * alpha_m_af for x in pred_train_i_af])]
                    pred_test_af = [sum(x) for x in zip(pred_test_af, 
                                                    [x * alpha_m_af for x in pred_test_i_af])]
                pred_train_af, pred_test_af = np.sign(pred_train_af), np.sign(pred_test_af)
                        
        else:
            if modelctrl == 1 or modelctrl == 3:
                concat_data = concat(discretize_data, target_data)
            if modelctrl == 2 or modelctrl == 4:
                concat_data = concat(selected_data, target_data)
            train_data, test_data = train_test_split(concat_data, test_size=0.3, shuffle=False) # random_state=42 # shuffle true --> 0.8951612903225806 # shuffle false --> 0.9274193548387096
            
            if modelctrl == 1 or modelctrl == 3:
                X_train = train_data[:,0:37]
                Y_train = train_data[:,37].astype('int')
                X_test = test_data[:,0:37]
                Y_test = test_data[:,37].astype('int')

            if modelctrl == 2 or modelctrl == 4:
                X_train = train_data[:,0:10]
                Y_train = train_data[:,10].astype('int')

                X_test = test_data[:,0:10]
                Y_test = test_data[:,10].astype('int')

            clf_tree = SVC(kernel='rbf', random_state=0, gamma=.01, C=10000)

            if modelctrl == 1 or modelctrl == 2:
                pred_train, pred_test = generic_clf(Y_train, X_train, Y_test, X_test, clf_tree)
                prf = precision_recall_fscore_support(Y_test, pred_test, average=None)

                precision = prf[0][0]
                recall = prf[1][0]
                fscore = prf[2][0]

                accuracy = accuracy_score(Y_test, pred_test)
                
                cm = confusion_matrix(Y_test, pred_test)
                correct = cm[0][0] + cm[1][1]
                incorrect = cm[0][1] + cm[1][0]

            if modelctrl == 3 or modelctrl == 4:
                if modelctrl == 3:
                    if (datactrl == 1):
                        x_range = range(0, 2, 1)#0
                    if (datactrl == 2):
                        x_range = range(0, 13, 1)#11
                    if (datactrl == 3):
                        x_range = range(0, 2, 1)#0
                else:
                    if (datactrl == 1):
                        x_range = range(0, 13, 1)#11
                    if (datactrl == 2):
                        x_range = range(0, 2, 1)
                    if (datactrl == 3):
                        x_range = range(0, 6, 1)#4

                for M in x_range:  
                    n_train, n_test = len(X_train), len(X_test)
                    w = np.ones(n_train) / n_train
                    pred_train, pred_test = [np.zeros(n_train), np.zeros(n_test)]

                    for i in range(M):
                        clf_tree.fit(X_train, Y_train, sample_weight = w)
                        pred_train_i = clf_tree.predict(X_train)
                        pred_test_i = clf_tree.predict(X_test)

                        prf_ada = precision_recall_fscore_support(Y_test, pred_test_i, average=None)

                        precision = prf_ada[0][0]
                        recall = prf_ada[1][0]
                        fscore = prf_ada[2][0]
                        accuracy = accuracy_score(Y_test, pred_test_i)
                        
                        
                        cm = confusion_matrix(Y_test, pred_test_i)
                        if len(cm) == 1:
                            correct = cm[0][0]
                            incorrect = 0
                        else:
                            correct = cm[0][0] + cm[1][1]
                            incorrect = cm[0][1] + cm[1][0]
                       
                        miss = [int(x) for x in (pred_train_i != Y_train)]
                        miss2 = [x if x==1 else -1 for x in miss]
                        err_m = np.dot(w,miss) / sum(w)

                        alpha_m = 0.5 * np.log( (1 - err_m) / float(err_m))
                        w = np.multiply(w, np.exp([float(x) * alpha_m for x in miss2]))

                        pred_train = [sum(x) for x in zip(pred_train, 
                                                        [x * alpha_m for x in pred_train_i])]
                        pred_test = [sum(x) for x in zip(pred_test, 
                                                        [x * alpha_m for x in pred_test_i])]
                    pred_train, pred_test = np.sign(pred_train), np.sign(pred_test)
   
    def custestfun(self, top=None):
        global discretize_cusdata
        global discretize_cusmrmrdata

        discretize_cusdata = np.arange(len(pre_dataset.columns)-1).reshape(1,len(pre_dataset.columns)-1)
        discretize_cusmrmrdata = np.arange(10).reshape(1,10)
        feature_binddata = np.append(cusdata, feature_data, axis=0)
        discretize_binddata = main_discretize(feature_binddata)
        discretize_cusdata[0] = discretize_binddata[0,:]

        for i in range(10):
            discretize_cusmrmrdata[0][i] = discretize_cusdata[0][feature_extraction[0][i]]

        global concat_data
      
        if modelctrl == 1 or modelctrl == 3:
            concat_data = concat(discretize_data, target_data)
        if modelctrl == 2 or modelctrl == 4:
            concat_data = concat(selected_data, target_data)
        train_data, test_data = train_test_split(concat_data, test_size=0.3, shuffle=False) # random_state=42 # shuffle true --> 0.8951612903225806 # shuffle false --> 0.9274193548387096
        
        if modelctrl == 1 or modelctrl == 3:
            X_train = train_data[:,0:37]
            Y_train = train_data[:,37].astype('int')
            X_test = discretize_cusdata
            Y_test = 0

        if modelctrl == 2 or modelctrl == 4:
            X_train = train_data[:,0:10]
            Y_train = train_data[:,10].astype('int')

            X_test = discretize_cusmrmrdata
            Y_test = 0

        clf_tree = SVC(kernel='rbf', random_state=0, gamma=.01, C=10000)

        if modelctrl == 1 or modelctrl == 2:
            pred_train, pred_test = generic_clf(Y_train, X_train, Y_test, X_test, clf_tree)
            if pred_test[0] == 1 :
                tk.messagebox.showwarning('Outcome','Your module has classified as "Defective". Please check your code again to recover as much as possible.')
            else :
                tk.messagebox.showinfo('Outcome','Congratulations! Your module does not have defects.')

        if modelctrl == 3 or modelctrl == 4:
            if modelctrl == 3:
                if (datactrl == 1):
                    x_range = range(0, 2, 1)
                if (datactrl == 2):
                    x_range = range(0, 13, 1)
                if (datactrl == 3):
                    x_range = range(0, 2, 1)
            else:
                if (datactrl == 1):
                    x_range = range(0, 13, 1)
                if (datactrl == 2):
                    x_range = range(0, 2, 1)
                if (datactrl == 3):
                    x_range = range(0, 6, 1)

            for M in x_range:  
                n_train, n_test = len(X_train), len(X_test)
                w = np.ones(n_train) / n_train
                pred_train, pred_test = [np.zeros(n_train), np.zeros(n_test)]

                for i in range(M):
                    clf_tree.fit(X_train, Y_train, sample_weight = w)
                    pred_train_i = clf_tree.predict(X_train)
                    pred_test_i = clf_tree.predict(X_test)
                    global result
                    result = pred_test_i[0]

                    miss = [int(x) for x in (pred_train_i != Y_train)]
                    miss2 = [x if x==1 else -1 for x in miss]
                    err_m = np.dot(w,miss) / sum(w)

                    alpha_m = 0.5 * np.log( (1 - err_m) / float(err_m))
                    w = np.multiply(w, np.exp([float(x) * alpha_m for x in miss2]))

                    pred_train = [sum(x) for x in zip(pred_train, 
                                                    [x * alpha_m for x in pred_train_i])]
                    pred_test = [sum(x) for x in zip(pred_test, 
                                                    [x * alpha_m for x in pred_test_i])]
                pred_train, pred_test = np.sign(pred_train), np.sign(pred_test)
            if result == 1 :
                tk.messagebox.showwarning('Outcome','Your module has classified as "Defective". Please check your code again to recover as much as possible.')
            else :
                tk.messagebox.showinfo('Outcome','Congratulations! Your module does not have defects.')

    def __init__(self, top=None):
        if cusmodel == 0 :
            self.fun()
            if modelctrl == 5:
                self.compare_ui()
            else:
                self.ui()
        else:
            if modelctrl != 5:
                self.custestfun()

        
if __name__ == '__main__':
    vp_start_gui()
