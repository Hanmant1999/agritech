from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3
import os 
import time
from datetime import datetime as dt
con=sqlite3.connect("pro.db")
cur=con.cursor()
ex="""CREATE TABLE IF NOT EXISTS Users(Name VARCHAR(4000),Email VARCHAR(4000),Password VARCHAR(4000),position VARCHAR(4000));"""
cur.execute(ex)
exa="""CREATE TABLE IF NOT EXISTS pri(crop_name VARCHAR(4000),region VARCHAR(4000),price VARCHAR(4000),updated_time VARCHAR(4000) );"""
cur.execute(exa)

K=Tk()
K.geometry("400x400")
K.title("Welcome to AgroTech")
frame=LabelFrame(K,text="AgroTech",bg="red",fg="black",padx="100",pady="100")
labt=Label(frame,text="Welcome To AgroTech")

def home():
 root=Toplevel()
 root.title("Welcome To Yogdhan Info")
 root.geometry("400x400")
 But=Button(root,text="Login",bg="blue",fg="black")
 mylabel=Label(root,text="Username")
 mylabel.grid(row=1,column=0)
 e6=Entry(root,width=20)
 global name
 name = e6.get()
 e6.grid(row=1,column=1)
 mylabel3=Label(root,text="     ")
 mylabel3.grid(row=2,column=0)
 mylabel2=Label(root,text="Password")
 mylabel2.grid(row=3,column=0)
 d=Entry(root,width=20,show='*')
 d.grid(row=3,column=1)
 mylabel4=Label(root,text="      ")
 mylabel4.grid(row=4,column=0)
 But=Button(root,text="Login",bg="blue",fg="black",command=lambda:check(e6.get(),d.get()))
 But1=Button(root,text="Register",bg="yellow",fg="black",command=reg) 
 But1.grid(row=0,column=0)
 But.grid(row=5,column=1)
def search(c,r):
 mb=(c,r)
 cur.execute("""SELECT price,updated_time  FROM pri WHERE crop_name = ? AND region= ? ORDER BY updated_time """,mb)
 l=cur.fetchall()
 g=list(l)[::-1]
 print(g)
 v=messagebox.showinfo("Details","Price is "+g[0][0]+"\n"+"Updated on "+g[0][1])

 
 
 
def add(name):
 g=name
 tab5=Toplevel()
 tab5.title("ADD Window")
 tab5.geometry("400x400")
 cur.execute("""SELECT position FROM Users   WHERE Name= ? """,(g,))
 n=cur.fetchone()
 print(n[0])

 if n[0] != "User":
  la=Label(tab5,text="Crop Name")
  la.grid(row=0,column=0)
  var=StringVar()
  var.set("Soyabean")
  k=OptionMenu(tab5,var,"Soyabean","Cotton","Moog","Tur")
  k.grid(row=0,column=1)
  la2=Label(tab5,text="Region")
  la2.grid(row=1,column=0)
  dar=StringVar()
  dar.set("NANDED")
  n=OptionMenu(tab5,dar,"NANDED","AURANGABAD","PARBHANI","PURNA")
  n.grid(row=1,column=1,padx=10,pady=10)
  lab3=Label(tab5,text="Price")
  lab3.grid(row=2,column=0)
  e3=Entry(tab5,width="24")
  e3.grid(row=3,column=1) 
  Buty=Button(tab5,text="Save",bg="blue",fg="black",command=lambda:Sam(var.get(),dar.get(),e3.get(),dt.now(),g))
  Buty.grid(row=5,column=1)
 else:
  l=messagebox.showerror("Sorry","You don't have right to update")
  pag(name)
 def Sam(m,n,o,w,g):
  a=g
  my=(m,n,o,w)
  ex1="""INSERT INTO pri VALUES(?,?,?,?);"""
  cur.execute(ex1,my)
  con.commit()
  pag(a)

  
 
def pag(a):
 fa=a
 pag1=Toplevel()
 pag1.title("Crop Values")
 pag1.geometry("400x400")
 lab13=Label(pag1,text="Crop Name")
 lab13.grid(row=0,column=0)
 mar=StringVar()
 mar.set("Soyabean")
 k=OptionMenu(pag1,mar,"Soyabean","Cotton","Moog","Tur")
 k.grid(row=0,column=1)
 lab14=Label(pag1,text="    ")
 tar=StringVar()
 tar.set("NANDED")
 lab14.grid(row=1,column=0)
 lab15=Label(pag1,text="region")
 lab15.grid(row=2,column=0)
 n=OptionMenu(pag1,tar,"NANDED","AURANGABAD","PARBHANI","PURNA")
 n.grid(row=2,column=1,padx=10,pady=10)
 
          
 But15=Button(pag1,text="search",bg="yellow",fg="black",command=lambda:search(mar.get(),tar.get())) 
 But15.grid(row=4,column=0)
 But16=Button(pag1,text="Add",bg="red",fg="black",command=lambda:add(fa)) 
 But16.grid(row=4,column=1)
 
 
def check(a,l):
 global name
 name=a
 cur.execute("""SELECT Password FROM Users WHERE Name = ?""",(a,))
 m=cur.fetchone()
 if m[0] == l:
  pag(name)
 else:
  j=messagebox.showerror("oops!!","please Enter a Valid Info or Please, Register")

 
 

def reg():
 tab2=Toplevel()
 tab2.title("Register Window")
 tab2.geometry("400x400")
 la=Label(tab2,text="UserName")
 la.grid(row=0,column=0)
 e=Entry(tab2,width="24")
 e.grid(row=0,column=1)
 la2=Label(tab2,text="Email Id")
 la2.grid(row=1,column=0)
 e1=Entry(tab2,width="24")
 e1.grid(row=1,column=1)
 lab3=Label(tab2,text="Password")
 lab3.grid(row=2,column=0)
 e2=Entry(tab2,width="24",show='*')
 e2.grid(row=2,column=1)
 lab4=Label(tab2,text="Confirm Password")
 lab4.grid(row=3,column=0)
 e3=Entry(tab2,width="24")
 e3.grid(row=3,column=1)
 But3=Button(tab2,text="Submit",bg="blue",fg="black",command=lambda:Submit(e.get(),e1.get(),e2.get(),"User"))
 But3.grid(row=4,column=1)
 def Submit(m,n,o,q):
  mk=(m,n,o,q)
  ex1="""INSERT INTO Users VALUES(?,?,?,?);"""
  cur.execute(ex1,mk)
  con.commit()
  home()

 

con.commit()

But5=Button(K,text="Next",bg="blue",fg="black",command=home)
But5.pack()
frame.pack()
labt.pack()
K.mainloop()
