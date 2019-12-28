try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import sqlite3
from tkcalendar import Calendar
from datetime import datetime
from tkinter import messagebox
db=sqlite3.connect("farmers.sqlite")
db.execute("Create table if not exists workrecord (Date date,name text,hour varchar(10),work varchar(20),total bigfloat,given bigfloat)")
db.execute("Create table if not exists givenrecord (workdate date,Date date,name text,given bigfloat)")
class Window:
    def __init__(self,window):
        self.window=window


    def delete(self):
        def delete():
            try:
                sqlquery2="SELECT name FROM WORKRECORD WHERE name='{0}' AND DATE='{1}'".format(self.name.get(),self.date.get())
                cursor=db.cursor()
                row=cursor.execute(sqlquery2)
                record=row.fetchall()
                if len(record)==0:
                    raise IOError
                sqlquery="DELETE FROM WORKRECORD WHERE NAME='{0}' AND DATE='{1}'".format(self.name.get(),self.date.get())
                sqlquery1="DELETE FROM GIVENRECORD WHERE NAME='{0}' AND WORKDATE='{1}'".format(self.name.get(),self.date.get())
                db.execute(sqlquery)
                db.execute(sqlquery1)
                db.commit()
                messagebox.showinfo("success","Delete succesfuly")
                top.destroy()

            except IOError:
                messagebox.showinfo("Unsuccess","Delete Unsuccesfuly\n Name of Farmer Not Found or Invalid Date of Work")
                top.destroy()



        top=tk.Toplevel(self.window)
        top.geometry("1280x768")
        self.name=tk.StringVar(top)
        tk.Label(top,text="").grid(row=0)
        tk.Label(top,text="Name",font=("Aerial 14")).grid(row=1,column=0)
        tk.Entry(top,textvariable=self.name,font=("Aerial 14")).grid(row=1,column=1)
        tk.Label(top,text="").grid(row=2)
        tk.Label(top,text="   Date",font=("Aerial 14")).grid(row=3,column=0,padx=15)
        self.date=tk.StringVar(top)
        tk.Label(top,text="Enter Date").grid(row=3,column=0)
        tk.Entry(top,textvariable=self.date).grid(row=3,column=1,pady=15)
        tk.Button(top,text="Delete",command=delete).grid(row=4,column=2,pady=15)

    def view(self):

        def viewdata():

            name1=list.get(tk.ACTIVE)
            try:
                sqlquery="SELECT Date,hour,work,total,given from workrecord WHERE name='{0}'".format(name1[0])
                row=cursor.execute(sqlquery)
            finally:
                tk.Label(top,text='Date').grid(row=1,column=2)
                list1=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                scr3=tk.Scrollbar(top,command=list1.yview,orient=tk.VERTICAL)
                scr4=tk.Scrollbar(top,command=list1.xview,orient=tk.HORIZONTAL)
                list1.config(yscrollcommand=scr3.set,xscrollcommand=scr4.set)
                list1.grid(row=2,column=2,padx=5,sticky='ns')
                scr3.grid(row=2,column=3,sticky='ns')
                scr4.grid(row=3,column=2,sticky='we')
                # worktype
                tk.Label(top,text='WorkType').grid(row=1,column=4,padx=10)
                list2=tk.Listbox(top,font=("Aerial 12"),width=10,height=25)
                scr5=tk.Scrollbar(top,command=list2.yview,orient=tk.VERTICAL)
                scr6=tk.Scrollbar(top,command=list2.xview,orient=tk.HORIZONTAL)
                list2.config(yscrollcommand=scr5.set,xscrollcommand=scr6.set)
                list2.grid(row=2,column=4,padx=5,sticky='ns')
                scr5.grid(row=2,column=5,sticky='ns')
                scr6.grid(row=3,column=4,sticky='we')
                # hours
                tk.Label(top,text='Hour').grid(row=1,column=6,padx=10)
                list3=tk.Listbox(top,font=("Aerial 12"),width=10,height=25)
                scr7=tk.Scrollbar(top,command=list3.yview,orient=tk.VERTICAL)
                scr8=tk.Scrollbar(top,command=list3.xview,orient=tk.HORIZONTAL)
                list3.config(yscrollcommand=scr7.set,xscrollcommand=scr8.set)
                list3.grid(row=2,column=6,padx=5,sticky='ns')
                scr8.grid(row=3,column=6,sticky='we')
                # Transaction
                tk.Label(top,text='Total amount to paid').grid(row=1,column=8,padx=10)
                list4=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                scr9=tk.Scrollbar(top,command=list4.yview,orient=tk.VERTICAL)
                scr10=tk.Scrollbar(top,command=list4.xview,orient=tk.HORIZONTAL)
                list4.config(yscrollcommand=scr9.set,xscrollcommand=scr10.set)
                list4.grid(row=2,column=8,padx=5,sticky='ns')
                scr9.grid(row=2,column=9,sticky='ns')
                scr10.grid(row=3,column=8,sticky='we')
                total=tk.IntVar(top,value=0)
                sqlquery1="SELECT total from WORKRECORD WHERE name='{0}'".format(name1[0])
                cursor1=db.cursor()
                row1=cursor1.execute(sqlquery1)
                sum=0
                for tot, in row1:
                    sum=sum+tot
                total.set(sum)
                tk.Entry(top,textvariable=total,font=("Aerial 11"),width=15).grid(row=4,column=8,padx=5)
                # Given
                tk.Label(top,text='Given amount').grid(row=1,column=10,padx=10)
                list5=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                scr11=tk.Scrollbar(top,command=list5.yview,orient=tk.VERTICAL)
                scr12=tk.Scrollbar(top,command=list5.xview,orient=tk.HORIZONTAL)
                list5.config(yscrollcommand=scr11.set,xscrollcommand=scr12.set)
                list5.grid(row=2,column=10,padx=5,sticky='ns')
                scr11.grid(row=2,column=11,sticky='ns')
                scr12.grid(row=3,column=10,sticky='we')
                given=tk.IntVar(top,value=0)
                sqlquery1="SELECT given from WORKRECORD WHERE name='{0}'".format(name1[0])
                cursor1=db.cursor()
                row1=cursor1.execute(sqlquery1)
                sum=0
                for giv, in row1:
                    sum=sum+giv
                given.set(sum)
                tk.Entry(top,textvariable=given,font=("Aerial 11"),width=15).grid(row=4,column=10,padx=5)
                remaining=tk.IntVar(top)
                remaining.set(total.get()-given.get())
                tk.Entry(top,textvariable=remaining,font=("Aerial 11"),width=15).grid(row=4,column=11,padx=5)
                ID=1
                try:
                    for date,hour,work,total,given in row:
                        list1.insert(ID,date)
                        list2.insert(ID,work)
                        list3.insert(ID,hour)
                        list4.insert(ID,total)
                        list5.insert(ID,given)
                        ID=ID+1
                except:
                        list1.insert(0,"no record")
                        list2.insert(0,"no record")
                        list3.insert(0,"no record")
                        list4.insert(0,"no record")
                        list5.insert(0,"no record")

        top=tk.Toplevel(self.window)
        top.geometry("1280x768")
        tk.Label(top,text="").grid(row=0,column=0)
        tk.Label(top,text="Name of farmer").grid(row=1,column=0)
        list=tk.Listbox(top,font=("Aerial 14"),width=40,height=25)
        scr1=tk.Scrollbar(top,command=list.yview ,orient=tk.VERTICAL)
        scr2=tk.Scrollbar(top,command=list.xview,orient=tk.HORIZONTAL)
        list.config(yscrollcommand=scr1.set,xscrollcommand=scr2.set)
        cursor=db.cursor()
        db.commit()
        row=cursor.execute("SELECT distinct name FROM WORKRECORD")
        ID=1
        for name in row:
            list.insert(ID,name)
            ID=ID+1
        scr1.grid(row=2,column=1,sticky='ns')
        scr2.grid(row=3,column=0,sticky='we')
        list.grid(row=2,column=0,padx=5)
        tk.Button(top,text="view",command=viewdata).grid(row=4,column=0)

    def search(self):
            def Datasearch():
                try:
                    sqlquery="SELECT Date,hour,work,total from workrecord WHERE name='{0}'".format(self.name.get())

                    cursor=db.cursor()
                    row=cursor.execute(sqlquery)

                finally:
                    tk.Label(top,text='Date',font=("Aerial 14")).grid(row=1,column=0)
                    list1=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                    scr1=tk.Scrollbar(top,command=list1.yview,orient=tk.VERTICAL)
                    list1.config(yscrollcommand=scr1.set)
                    list1.grid(row=2,column=0,padx=5,sticky='ns')
                    scr1.grid(row=2,column=1,sticky='ns')

                    # worktype
                    tk.Label(top,text='Worktype').grid(row=1,column=2)
                    list2=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                    scr2=tk.Scrollbar(top,command=list2.yview,orient=tk.VERTICAL)
                    list2.config(yscrollcommand=scr2.set)
                    list2.grid(row=2,column=2,sticky='ns')
                    scr2.grid(row=2,column=3,sticky='ns')
                    # Hour
                    tk.Label(top,text='Hour').grid(row=1,column=4)
                    list3=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                    scr3=tk.Scrollbar(top,command=list3.yview,orient=tk.VERTICAL)
                    list3.config(yscrollcommand=scr3.set)
                    list3.grid(row=2,column=4,sticky='ns')
                    scr3.grid(row=2,column=5,sticky='ns')
                    # Total amount
                    tk.Label(top,text='Total amount to paid').grid(row=1,column=6)
                    list4=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                    scr4=tk.Scrollbar(top,command=list4.yview,orient=tk.VERTICAL)
                    list4.config(yscrollcommand=scr4.set)
                    list4.grid(row=2,column=6,sticky='ns')
                    scr4.grid(row=2,column=7,sticky='ns')
                    total=tk.IntVar(top,value=0)
                    sqlquery1="SELECT total from WORKRECORD WHERE name='{0}'".format(self.name.get())
                    cursor1=db.cursor()
                    row2=cursor1.execute(sqlquery1)
                    sum=0
                    for giv, in row2:
                        sum=sum+giv
                    total.set(sum)
                    tk.Entry(top,textvariable=total,font=("Aerial 12"),width=10).grid(row=3,column=6,sticky='we',pady=10)
                    # Given amount
                try:
                        sqlquery="SELECT Date,given from givenrecord WHERE name='{0}'".format(self.name.get())
                        cursor1=db.cursor()
                        row1=cursor1.execute(sqlquery)

                finally:

                        tk.Label(top,text='amount given').grid(row=1,column=8)
                        list5=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                        scr5=tk.Scrollbar(top,command=list5.yview,orient=tk.VERTICAL)
                        list5.config(yscrollcommand=scr5.set)
                        list5.grid(row=2,column=8,sticky='ns')
                        scr5.grid(row=2,column=9,sticky='ns')
                        given=tk.IntVar(top,value=0)
                        sqlquery1="SELECT given from GIVENRECORD WHERE name='{0}'".format(self.name.get())
                        cursor1=db.cursor()
                        row2=cursor1.execute(sqlquery1)
                        sum=0
                        for giv, in row2:
                           sum=sum+giv
                        given.set(sum)
                        tk.Entry(top,textvariable=given,font=("Aerial 12"),width=10).grid(row=3,column=8,sticky='we',pady=10)
                        # Given amount date

                        tk.Label(top,text='date of amount given').grid(row=1,column=10)
                        list6=tk.Listbox(top,font=("Aerial 12"),width=15,height=25)
                        scr6=tk.Scrollbar(top,command=list6.yview,orient=tk.VERTICAL)
                        list6.config(yscrollcommand=scr6.set)
                        list6.grid(row=2,column=10,sticky='ns')
                        scr6.grid(row=2,column=11,sticky='ns')
                        remaining=tk.IntVar(top)
                        remaining.set(total.get()-given.get())
                        tk.Entry(top,textvariable=remaining,font=("Aerial 11"),width=15).grid(row=3,column=10,padx=5)

                        ID=1
                        try:
                            for date,hour,work,total in row:
                                list1.insert(ID,date)
                                list2.insert(ID,work)
                                list3.insert(ID,hour)
                                list4.insert(ID,total)
                                ID=ID+1
                        except:
                            list1.insert(0,"no record")
                            list2.insert(0,"no record")
                            list3.insert(0,"no record")
                            list4.insert(0,"no record")
                        ID=1
                        try:
                            for date,given in row1:
                                list5.insert(ID,given)
                                list6.insert(ID,date)
                                ID+=1
                        except:
                           list5.insert(0,"No Record")
                           list6.insert(0,"No Record")

            top=tk.Toplevel(self.window)
            top.geometry("1280x768")
            frame=tk.Frame(top)
            frame.grid(row=0,column=0,sticky='nsew')
            self.name=tk.StringVar(top)
            tk.Label(frame,text='').grid(row=0)
            tk.Label(frame,text='Name',font=("Aerial 14")).grid(row=1,column=0)
            tk.Label(frame,text='').grid(row=1,column=1)
            tk.Entry(frame,textvariable=self.name,width=30,font=("Aerial 14")).grid(row=1,column=2)
            tk.Button(frame,text="Search",command=Datasearch,font=("Aerial 14")).grid(row=1,column=3,padx=5)


    def update(self) :
        def updatename():
            def updatevalue1():
                try:
                    sqlquery2="SELECT name FROM WORKRECORD WHERE name='{0}'".format(self.oldname.get())
                    cursor=db.cursor()
                    row=cursor.execute(sqlquery2)
                    record=row.fetchall()
                    if len(record)==0:
                        raise IOError

                    sqlquery="UPDATE WORKRECORD SET name='{0}' WHERE name='{1}'".format(self.name.get(),self.oldname.get())
                    db.execute(sqlquery)
                    sqlquery1="UPDATE GIVENRECORD SET name='{0}' WHERE name='{1}'".format(self.name.get(),self.oldname.get())
                    db.execute(sqlquery1)
                    db.commit()
                    messagebox.showinfo("Success","Update Succesfuly")
                    top.destroy()
                except IOError:
                    messagebox.showinfo("Unsuccess","Update Unsuccesfuly\n Name of Farmer Not Found")
                    top.destroy()
            tk.Label(top,text="").grid(row=5,column=0,pady=10)
            tk.Label(top,text="Name",font=("Aerial 14")).grid(row=6,column=0,sticky='we')
            self.name=tk.StringVar(top)
            tk.Entry(top,font=("Aerial 14"),width=30,textvariable=self.name).grid(row=6,column=1)
            self.top=top
            tk.Button(top,text="Update",font=("Aerial 14"),command=updatevalue1).grid(row=6,column=2)


        def updatehour():
            def updatevalue2():
                try:
                    sqlquery2="SELECT hour FROM WORKRECORD WHERE name='{0}'".format(self.oldname.get())
                    cursor=db.cursor()
                    row=cursor.execute(sqlquery2)
                    record=row.fetchall()
                    if len(record)==0:
                        raise IOError

                    sqlquery="UPDATE WORKRECORD SET hour='{0}' WHERE name='{1}' AND Date='{2}'".format(self.hour.get(),self.oldname.get(),self.date.get())
                    db.execute(sqlquery)
                    db.commit()
                    messagebox.showinfo("Success","Update Succesfuly")
                    top.destroy()
                except IOError:

                    messagebox.showinfo("Unsuccess","Update Unsuccesfuly\n Name of Farmer Not Found")
                    top.destroy()
            tk.Label(top,text="").grid(row=5,column=0,pady=10)
            tk.Label(top,text="Hour",font=("Aerial 14")).grid(row=6,column=0,sticky='we')
            self.hour=tk.StringVar(top)
            tk.Entry(top,font=("Aerial 14"),width=30,textvariable=self.hour).grid(row=6,column=1)
            self.top=top
            tk.Button(top,text="Update",font=("Aerial 14"),command=updatevalue2).grid(row=6,column=2)

        def updatetotal():
            def updatevalue3():
                try:
                    sqlquery2="SELECT total FROM WORKRECORD WHERE name='{0}'".format(self.oldname.get())
                    cursor=db.cursor()
                    row=cursor.execute(sqlquery2)
                    record=row.fetchall()
                    if len(record)==0:
                        raise IOError
                    sqlquery="UPDATE WORKRECORD SET total='{0}' WHERE name='{1}' AND Date='{2}'".format(self.total.get(),self.oldname.get(),self.date.get())
                    db.execute(sqlquery)
                    db.commit()
                    messagebox.showinfo("Success","Update Succesfuly")
                    top.destroy()
                except IOError:
                    messagebox.showinfo("Unsuccess","Update Unsuccesfuly\n Name of Farmer Not Found")
                    top.destroy()
            tk.Label(top,text="").grid(row=5,column=0,pady=10)
            tk.Label(top,text="Total amount",font=("Aerial 14")).grid(row=6,column=0,sticky='we')
            self.total=tk.IntVar(top)
            tk.Entry(top,font=("Aerial 14"),width=30,textvariable=self.total).grid(row=6,column=1)
            tk.Button(top,text="Update",font=("Aerial 14"),command=updatevalue3).grid(row=6,column=2)


        def updategiven():
            def updatevalue4():
                try:
                    sqlquery="SELECT given FROM WORKRECORD WHERE name='{0}' AND Date='{1}'".format(self.oldname.get(),self.date.get())
                    cursor=db.cursor()
                    row=cursor.execute(sqlquery)
                    sqlquery1="UPDATE WORKRECORD SET given={0} WHERE name='{1}' AND Date='{2}'".format(row.fetchone()[0]+self.given.get(),self.oldname.get(),self.date.get())
                    sqlquery2="INSERT INTO GIVENRECORD VALUES('{0}','{1}','{2}',{3})".format(self.date.get(),datetime.now().strftime("%Y-%m-%d"),self.oldname.get(),self.given.get())
                    db.execute(sqlquery1)
                    db.execute(sqlquery2)
                    db.commit()
                    messagebox.showinfo("Success","Update Succesfuly")
                    top.destroy()
                except:
                    messagebox.showinfo("Unsuccess","Update Unsuccesfuly\n Name of Farmer Not Found")
                    top.destroy()
            tk.Label(top,text="").grid(row=5,column=0,pady=10)
            tk.Label(top,text="Given amount",font=("Aerial 14")).grid(row=6,column=0,sticky='we')
            self.given=tk.IntVar(top,value=0)
            tk.Entry(top,font=("Aerial 14"),width=30,textvariable=self.given).grid(row=6,column=1)
            tk.Button(top,text="Update",font=("Aerial 14"),command=updatevalue4).grid(row=6,column=2)



        top=tk.Toplevel(self.window)
        top.geometry("1280x768")
        tk.Label(top,text="").grid(row=0,column=0)
        tk.Label(top,text="Enter Date Of Work").grid(row=1,column=0)
        tk.Label(top,text="Format:YYYY-MM-DD",font=("Aerial 14")).grid(row=1,column=2,sticky='NW',padx=10)
        self.date=tk.StringVar(top)
        tk.Entry(top,width=30,textvariable=self.date,font=("Aerial 14")).grid(row=1,column=1,sticky="NW")
        tk.Label(top,text='').grid(row=2,column=0)
        tk.Label(top,text='Name For Update').grid(row=2,column=0,pady=10)
        self.oldname=tk.StringVar(top,value="")
        tk.Entry(top,textvariable=self.oldname,width=30,font=("Aerial 14")).grid(row=2,column=1)

        tk.Label(top,text="Update:").grid(row=3,column=0,pady=10)
        tk.Radiobutton(top,text='Name',value=1,command=updatename).grid(row=4,column=0)
        tk.Radiobutton(top,text='Hour',value=2,command=updatehour).grid(row=4,column=1)
        tk.Radiobutton(top,text='Total amount',value=3,command=updatetotal).grid(row=4,column=2)
        tk.Radiobutton(top,text='Given amount',value=4,command=updategiven).grid(row=4,column=3)
        tk.Label(top,text="").grid(row=5,column=0)

    def submitrecord(self):
            sqlquery="INSERT INTO WORKRECORD (Date,name,hour,work,total,given) VALUES('{0}','{1}','{2}','{3}',{4},{5})".format(self.date.get(),self.name.get(),self.hour.get(),self.worktype.get(),self.total.get(),self.given.get())
            db.execute(sqlquery)
            sqlquery1="INSERT INTO GIVENRECORD (workdate,Date,name,given) VALUES('{0}','{1}','{2}',{3})".format(self.date.get(),self.date.get(),self.name.get(),self.given.get())
            db.execute(sqlquery1)
            db.commit()
            messagebox.showinfo("Success","Record inserted")
            self.Register()
    def Register(self):
        tk.Label(self.window,text="").grid(row=0,column=0,sticky="NW")
        tk.Label(self.window,text="Select Date: ",font=("Aerial 14")).grid(row=1,column=0,sticky="NW")
        tk.Label(self.window,text="Format:YYYY-MM-DD",font=("Aerial 14")).grid(row=1,column=2,sticky='NW')
        self.date=tk.StringVar(self.window)
        tk.Entry(self.window,width=30,textvariable=self.date,font=("Aerial 14")).grid(row=1,column=1,sticky="NW")
        tk.Label(self.window,text="").grid(row=16,column=0)
        self.hour()
        self.name_farmer()
        self.worktype()
        self.transaction()
        tk.Button(self.window,text="Submit",command=self.submitrecord,font=("Aerial 14")).grid(row=17,column=1,padx=15)


    def name_farmer(self):
            tk.Label(self.window,text="").grid(row=2,column=0)
            tk.Label(self.window,text="Name Of Farmer:",font=("Aerial 14")).grid(row=3,column=0)
            self.name=tk.StringVar(self.window)
            name_of_farmer=tk.Entry(self.window,width=40,font=("Aerial 14"),textvariable=self.name)
            scr=tk.Scrollbar(self.window,orient=tk.HORIZONTAL,command=name_of_farmer.xview)
            name_of_farmer.config(xscrollcommand=scr.set)
            scr.grid(row=4,column=1,sticky='ew')
            name_of_farmer.grid(row=3,column=1)
    def worktype(self):
            tk.Label(self.window,text="Work Type:",font=("Aerial 14")).grid(row=5,column=0)
            self.worktype=tk.StringVar(self.window)
            tk.Entry(self.window,textvariable=self.worktype,font=("Aerial 14")).grid(row=5,column=1,sticky='we')

    def hour(self):
                self.hour=tk.IntVar(self.window)
                tk.Label(self.window,text="").grid(row=6,column=0)
                tk.Label(self.window,text="Hour",font=("Aerial 14")).grid(row=7,column=0)
                tk.Entry(self.window,textvariable=self.hour,width=5,font=("Aerial 14")).grid(row=7,column=1)

    def transaction(self):
                self.total=tk.IntVar(self.window,value=0)
                tk.Label(self.window,text="").grid(row=8,column=0)
                tk.Label(self.window,text="Total amount to Paid",font=("Aerial 14")).grid(row=9,column=0)
                tk.Entry(self.window,textvariable=self.total,width=10,font=("Aerial 14")).grid(row=9,column=1)
                self.given=tk.IntVar(self.window,value=0)
                tk.Label(self.window,text="").grid(row=10,column=0)
                tk.Label(self.window,text="amount given to farmer",font=("Aerial 14")).grid(row=11,column=0)
                tk.Entry(self.window,textvariable=self.given,width=10,font=("Aerial 14")).grid(row=11,column=1)
                def Calculate():
                    self.Remaining.set(self.total.get()-self.given.get())
                self.Remaining=tk.IntVar(self.window)
                tk.Label(self.window,text="").grid(row=12,column=0)
                tk.Label(self.window,text="Calculate remaining amount",font=("Aerial 14")).grid(row=13,column=0)
                tk.Button(self.window,text="Calculate",command=Calculate,font=("Aerial 14")).grid(row=13,column=1)
                tk.Label(self.window,text="").grid(row=14,column=0)
                tk.Label(self.window,text="remaining amount",font=("Aerial 14")).grid(row=15,column=0)
                tk.Entry(self.window,textvariable=self.Remaining,width=10,font=("Aerial 14")).grid(row=15,column=1)


    def monthwise(self):
        def allrecord():
            cursor=db.cursor()
            row=cursor.execute("select * from workrecord  where date like '{0}-{1}%'".format(year.get(),month.get()))
            tk.Label(top,text="").grid(row=5,column=0)
            tk.Label(top,text="Name of farmer").grid(row=6,column=0)
            list=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
            scr=tk.Scrollbar(top,command=list.yview,orient=tk.VERTICAL)
            scr0=tk.Scrollbar(top,command=list.xview,orient=tk.HORIZONTAL)
            list.config(yscrollcommand=scr.set,xscrollcommand=scr0.set)
            scr.grid(row=7,column=1,sticky='ns')
            scr0.grid(row=8,column=0,sticky='we')
            list.grid(row=7,column=0,padx=5)

            tk.Label(top,text='Date',font=("Aerial 14")).grid(row=6,column=2)
            list1=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
            scr1=tk.Scrollbar(top,command=list1.yview,orient=tk.VERTICAL,width=10)
            list1.config(yscrollcommand=scr1.set)
            list1.grid(row=7,column=2,padx=5,sticky='ns')
            scr1.grid(row=7,column=3,sticky='ns',)

            # worktype
            tk.Label(top,text='Worktype').grid(row=6,column=4)
            list2=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
            scr2=tk.Scrollbar(top,command=list2.yview,orient=tk.VERTICAL)
            list2.config(yscrollcommand=scr2.set)
            list2.grid(row=7,column=4,sticky='ns')
            scr2.grid(row=7,column=5,sticky='ns')
            # Hour
            tk.Label(top,text='Hour').grid(row=6,column=6)
            list3=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
            scr3=tk.Scrollbar(top,command=list3.yview,orient=tk.VERTICAL)
            list3.config(yscrollcommand=scr3.set)
            list3.grid(row=7,column=6,sticky='ns')
            scr3.grid(row=7,column=7,sticky='ns')
            # Total amount
            tk.Label(top,text='Total amount to paid').grid(row=6,column=8)
            list4=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
            scr4=tk.Scrollbar(top,command=list4.yview,orient=tk.VERTICAL)
            list4.config(yscrollcommand=scr4.set)
            list4.grid(row=7,column=8,sticky='ns')
            scr4.grid(row=7,column=9,sticky='ns')

            tk.Label(top,text='Given Amount').grid(row=6,column=10)
            list6=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
            scr6=tk.Scrollbar(top,command=list6.yview,orient=tk.VERTICAL)
            list6.config(yscrollcommand=scr6.set)
            list6.grid(row=7,column=10,sticky='ns')
            scr6.grid(row=7,column=11,sticky='ns')
            ID=1
            sum=0
            sum1=0
            try:
                for date,name,hour,work,total,given in row:
                    list.insert(ID,name)
                    list1.insert(ID,date)
                    list2.insert(ID,work)
                    list3.insert(ID,hour)
                    sum=sum+total
                    sum1=sum1+given
                    list4.insert(ID,total)
                    list6.insert(ID,given)
                    ID=ID+1
            except:
                list.insert(0,"no record")
                list1.insert(0,"no record")
                list2.insert(0,"no record")
                list3.insert(0,"no record")
                list4.insert(0,"no record")
                list6.insert(0,"no record")
            total=tk.IntVar(top)
            given=tk.IntVar(top)
            total.set(sum)
            given.set(sum1)
            tk.Entry(top,font="Aerial 12",textvariable=total).grid(row=8,column=8,pady=5)
            tk.Entry(top,font="Aerial 12",textvariable=given).grid(row=8,column=10,pady=5)
            tk.Label(top,text="Remaining").grid(row=9,column=8)
            remain=tk.IntVar(top)
            remain.set(total.get()-given.get())
            tk.Entry(top,font="Aerial 12",textvariable=remain).grid(row=9,column=10,pady=5)
        def particular():
            def selectedrecord():
                tk.Label(top,text="").grid(row=5,column=0)
                tk.Label(top,text="Name of farmer").grid(row=6,column=0)
                list=tk.Listbox(top, font=("Aerial 14"),width=15,height=20)
                scr=tk.Scrollbar(top,command=list.yview,orient=tk.VERTICAL)
                scr0=tk.Scrollbar(top,command=list.xview,orient=tk.HORIZONTAL)
                list.config(yscrollcommand=scr.set,xscrollcommand=scr0.set)
                scr.grid(row=7,column=1,sticky='ns')
                scr0.grid(row=8,column=0,sticky='we')
                list.grid(row=7,column=0,padx=5)

                tk.Label(top,text='Date',font=("Aerial 14")).grid(row=6,column=2)
                list1=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
                scr1=tk.Scrollbar(top,command=list1.yview,orient=tk.VERTICAL,width=10)
                list1.config(yscrollcommand=scr1.set)
                list1.grid(row=7,column=2,padx=5,sticky='ns')
                scr1.grid(row=7,column=3,sticky='ns',)

                # worktype
                tk.Label(top,text='Worktype').grid(row=6,column=4)
                list2=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
                scr2=tk.Scrollbar(top,command=list2.yview,orient=tk.VERTICAL)
                list2.config(yscrollcommand=scr2.set)
                list2.grid(row=7,column=4,sticky='ns')
                scr2.grid(row=7,column=5,sticky='ns')
                # Hour
                tk.Label(top,text='Hour').grid(row=6,column=6)
                list3=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
                scr3=tk.Scrollbar(top,command=list3.yview,orient=tk.VERTICAL)
                list3.config(yscrollcommand=scr3.set)
                list3.grid(row=7,column=6,sticky='ns')
                scr3.grid(row=7,column=7,sticky='ns')
                # Total amount
                tk.Label(top,text='Total amount to paid').grid(row=6,column=8)
                list4=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
                scr4=tk.Scrollbar(top,command=list4.yview,orient=tk.VERTICAL)
                list4.config(yscrollcommand=scr4.set)
                list4.grid(row=7,column=8,sticky='ns')
                scr4.grid(row=7,column=9,sticky='ns')

                tk.Label(top,text='Given Amount').grid(row=6,column=10)
                list6=tk.Listbox(top,font=("Aerial 14"),width=15,height=20)
                scr6=tk.Scrollbar(top,command=list6.yview,orient=tk.VERTICAL)
                list6.config(yscrollcommand=scr6.set)
                list6.grid(row=7,column=10,sticky='ns')
                scr6.grid(row=7,column=11,sticky='ns')
                cursor=db.cursor()
                row=cursor.execute("select * from workrecord where name='{0}' AND date like '{1}-{2}%'".format(self.name.get(),year.get(),month.get()))
                sum=0
                sum1=0
                ID=1
                try:
                    for date,name,hour,work,total,given in row:
                        list.insert(ID,name)
                        list1.insert(ID,date)
                        list2.insert(ID,work)
                        list3.insert(ID,hour)
                        sum=sum+total
                        sum1=sum1+given
                        list4.insert(ID,total)
                        list6.insert(ID,given)
                        ID=ID+1
                except:
                    list.insert(0,"no record")
                    list1.insert(0,"no record")
                    list2.insert(0,"no record")
                    list3.insert(0,"no record")
                    list4.insert(0,"no record")
                    list6.insert(0,"no record")
                total=tk.IntVar(top)
                given=tk.IntVar(top)
                total.set(sum)
                given.set(sum1)
                tk.Entry(top,font="Aerial 12",textvariable=total).grid(row=8,column=8,pady=5)
                tk.Entry(top,font="Aerial 12",textvariable=given).grid(row=8,column=10,pady=5)
                tk.Label(top,text="Remaining").grid(row=9,column=8)
                remain=tk.IntVar(top)
                remain.set(total.get()-given.get())
                tk.Entry(top,font="Aerial 12",textvariable=remain).grid(row=9,column=10,pady=5)



            # print(row.fetchall())
            self.name=tk.StringVar(top)
            tk.Label(top,text="Name").grid(row=5,column=0)
            tk.Entry(top,textvariable=self.name,font=("Aerial 14"),width=10).grid(row=5,column=2)
            tk.Button(top,text="show",font=("Aerial 14"),command=selectedrecord,width=10).grid(row=5,column=4)



        top=tk.Toplevel(self.window)
        top.geometry("1280x768")
        tk.Label(top,text="").grid(row=0,column=0)
        tk.Label(top,text="Enter year").grid(row=1,column=0)
        year=tk.StringVar(top)
        tk.Entry(top,textvariable=year,font=("Aerial 14"),width=10).grid(row=1,column=2,padx=15)
        tk.Label(top,text="").grid(row=2,column=0)
        tk.Label(top,text="Enter month").grid(row=3,column=0)
        month=tk.StringVar(top)
        tk.Entry(top,textvariable=month,font=("Aerial 14"),width=10).grid(row=3,column=2,padx=15)
        tk.Radiobutton(top,text="View all Record",command=allrecord,value=1).grid(row=4,column=0,padx=10,pady=10)
        tk.Radiobutton(top,text="View particular Record ",command=particular,value=2).grid(row=4,column=2,padx=10,pady=10)


if __name__=="__main__":
    window=tk.Tk()
    window.geometry("1280x768")
    window.title("Farmer's Work Record",)
    menubar=tk.Menu(window)
    box=Window(window)
    menubar.add_cascade(label='View Record',command=box.view)
    menubar.add_cascade(label='Search Record',command=box.search)
    menubar.add_cascade(label='Update Record',command=box.update)
    menubar.add_cascade(label="Delete Record",command=box.delete)
    menubar.add_cascade(label="View Monthwise",command=box.monthwise)
    window.config(menu=menubar)
    box.Register()
    window.mainloop()
