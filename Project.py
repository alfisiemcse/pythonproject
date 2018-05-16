
from tkinter import *
from tkinter import *
import calendar
import datetime
import sys


def submit1():
    name = entry1.get()
    password= entry2.get()
    if name == "md555191":
        if password == "Cisco123##":


            screen = Tk()
            screen.title("Flight Reservation System")
            screen.geometry("430x400+450+100")
            label1 = Label(screen, text="Book Domestic & International Flight", font='Helvetica 18 bold')
            label1.grid(row=0, columnspan=3)
            """"------------------------------------------------Radio button of the trip--------------------------------------------------------------------"""

            def sel():
                selection = "You selected the option " + str(var.get())
                print(selection)

            var = IntVar()
            R1 = Radiobutton(screen, text="Round Trip", variable=var, command=sel, value=1)
            R1.grid(row=1, column=0,sticky=W)
            R2 = Radiobutton(screen, text="One way", variable=var, value=2, command=sel)
            R2.grid(row=1, column=1, sticky=W)


            """----------------------------------------From Label with combo box-----------------------------------------------------------------------------"""

            def change_dropdown(*args):
                print(tkvar.get())

            label = Label(screen, text="From", font='Helvetica 10 bold')
            tkvar = StringVar(screen)
            # Dictionary with options
            choices = {'Halifax                 ', 'Ontario                ', 'Toronto                ',
                       'Manitoba                  ', 'Ottawa                 '}
            tkvar.set('                                 ')  # set the default option
            popupMenu = OptionMenu(screen, tkvar, *choices).grid(row=3, columnspan=3, sticky=W)
            label.grid(row=2, sticky=W)
            # link function to change dropdown
            tkvar.trace('w', change_dropdown)
            """"-----------------------------------------------------------------------------------------------------------------------------------------"""

            """----------------------------------------To Label with combo box-----------------------------------------------------------------------------"""

            def change_dropdown1(*args):
                print(tkvar1.get())

            label2 = Label(screen, text="To", font='Helvetica 10 bold')
            tkvar1 = StringVar(screen)
            # Dictionary with options
            choices = {'Halifax                       ', 'Ontario                      ',
                       'Toronto                      ', 'Manitoba                     ', 'Ottawa                      '}
            tkvar1.set('                                   ')  # set the default option
            popupMenu1 = OptionMenu(screen, tkvar1, *choices).grid(row=3, columnspan=3, sticky=E)
            label2.grid(row=2, column=2, sticky=E)
            # link function to change dropdown
            tkvar1.trace('w', change_dropdown1)
            """"---------------------------------------------------------------------------------------------------------------------------------------------"""

            """----------------------------------------------------------------calendar widget-----------------------------------------------------------------"""

            class Calendar:
                def __init__(self, parent, values):
                    self.values = values
                    self.parent = parent
                    self.parent.geometry("180x290+575+280")
                    self.cal = calendar.TextCalendar(calendar.SUNDAY)
                    self.year = datetime.date.today().year
                    self.month = datetime.date.today().month
                    self.wid = []
                    self.day_selected = 1
                    self.month_selected = self.month
                    self.year_selected = self.year
                    self.day_name = ''

                    self.setup(self.year, self.month)

                def clear(self):
                    for w in self.wid[:]:
                        w.grid_forget()
                        # w.destroy()
                        self.wid.remove(w)

                def go_prev(self):
                    if self.month > 1:
                        self.month -= 1
                    else:
                        self.month = 12
                        self.year -= 1
                    # self.selected = (self.month, self.year)
                    self.clear()
                    self.setup(self.year, self.month)

                def go_next(self):
                    if self.month < 12:
                        self.month += 1
                    else:
                        self.month = 1
                        self.year += 1

                    # self.selected = (self.month, self.year)
                    self.clear()
                    self.setup(self.year, self.month)

                def selection(self, day, name):
                    self.day_selected = day
                    self.month_selected = self.month
                    self.year_selected = self.year
                    self.day_name = name

                    # data
                    self.values['day_selected'] = day
                    self.values['month_selected'] = self.month
                    self.values['year_selected'] = self.year
                    self.values['day_name'] = name
                    self.values['month_name'] = calendar.month_name[self.month_selected]

                    self.clear()
                    self.setup(self.year, self.month)

                def setup(self, y, m):
                    left = Button(self.parent, text='<', command=self.go_prev)
                    self.wid.append(left)
                    left.grid(row=10, column=1)

                    header = Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
                    self.wid.append(header)
                    header.grid(row=10, column=2, columnspan=3)

                    right = Button(self.parent, text='>', command=self.go_next)
                    self.wid.append(right)
                    right.grid(row=10, column=5)

                    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                    for num, name in enumerate(days):
                        t = Label(self.parent, text=name[:3])
                        self.wid.append(t)
                        t.grid(row=0, column=num)

                    for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
                        for d, day in enumerate(week):
                            if day:
                                # print(calendar.day_name[day])
                                b = Button(self.parent, width=1, text=day,
                                           command=lambda day=day: self.selection(day,
                                                                                  calendar.day_name[(day - 1) % 7]))
                                self.wid.append(b)
                                b.grid(row=w, column=d)

                    sel = Label(self.parent, height=2, text='{} {} {} {}'.format(
                        self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
                    self.wid.append(sel)
                    sel.grid(row=20, column=0, columnspan=7)

                    ok = Button(self.parent, width=5, text='OK', command=self.kill_and_save)
                    self.wid.append(ok)
                    ok.grid(row=21, column=2, columnspan=3, pady=10)

                def kill_and_save(self):
                    self.parent.destroy()

            if __name__ == '__main__':
                class Control:
                    def __init__(self, parent):
                        self.parent = parent
                        self.choose_btn = Button(self.parent, text='Date', command=self.popup)
                        # self.show_btn = Button(self.parent, text='Show Selected', command=self.print_selected_date)
                        self.choose_btn.grid(row=4, column=0, columnspan=3)
                        # self.show_btn.grid()
                        self.data = {}

                    def popup(self):
                        child = Toplevel()
                        cal = Calendar(child, self.data)

                    def print_selected_date(self):
                        print(self.data)

                app = Control(screen)

            """------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

            screen.mainloop()











        else:
            root.quit()







#This is the code for the first window


root = Tk()
root.title("Flight Reservation System")
root.geometry("400x120+450+250")
label1 = Label(root,text= "LOGIN PAGE",font='Helvetica 18 bold')
label1.grid(row =0, sticky = W)
button1 = Button(root,text= "Submit",command = submit1,fg = "black" )
entry1 = Entry(root)
entry2 = Entry(root,show = "*")
namelabel = Label(root, text = "LOGIN ID")
passwordlabel = Label(root, text = "PASSWORD")
namelabel.grid(row =1,sticky = W)
passwordlabel.grid(row =2,sticky = W)
button1.grid(row =3,column = 2,columnspan = 2,sticky = W)
entry1.grid(row = 1,column = 3,sticky = W )
entry2.grid(row = 2, column = 3,sticky = W)
x = entry1.get()
print(x)
root.mainloop()


# The code for the first window ends here