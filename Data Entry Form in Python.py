from tkinter import *
from tkinter import ttk
from pyexcel_ods import get_data
from pyexcel_ods import save_data
import datetime
from tkcalendar import Calendar
import json

#file spec
file_path = r"C:\bhavesh traders\New Trad Book copy1.ods"
data_sheet = (get_data(file_path))


# Create a root window
root = Tk()
root.title("BT Trade Book")
root.state('zoomed')
root.configure(bg = '#FFFFFF')
root.columnconfigure(0,weight = 1)
root.rowconfigure(0,weight = 1)

# cretae a frame
frame_a = Frame(root,highlightbackground = '#000000',highlightthickness = 2,bg = "beige")
frame_a.grid(row = 0,column = 0,sticky = 'nsew')

#creates header bhavesh traders
label_bt = Label(root,text= "Bhavesh Traders",bg="beige",fg='blue')
label_bt.config(font=('Thaoma',25))
label_bt.place(x=501,y=13)

#creates a label displayinf Financial year
label_FY = Label(frame_a,bg="beige",text = "Financial Year 2022/2023")
label_FY.config(font=('Thaoma',15))
label_FY.place(x=1075,y = 13)
#creates a horizontal line
horizontal_line = Frame(root,bg='blue',height = 1,width = root.winfo_screenwidth())
horizontal_line.place(x=0,y=50)

#create labels
labels = [["Date",'1','0'],["Vch No.",'1','2'],["Site",'1','4'],["Item",'1','7']]
label_d = {}
for i in labels:
    label_d[i[0]]=Label(frame_a,text = i[0],bg = "beige")
    label_d[i[0]].config(font=('Thaoma',12))

label_d["Date"].place(x=14,y=82)
label_d["Vch No."].place(x=14,y=160)
label_d["Site"].place(x=14,y=238)
label_d["Item"].place(x=14,y=316)


#create variables to set and get values
date_val = StringVar()
challan_val  = IntVar()
site_val = StringVar()
item_val = StringVar()
unit_val = StringVar()
pp_val = StringVar()
sp_val = StringVar()
truck_val = StringVar()
measure_var = DoubleVar() # a variable to store and retrive measurement
pr_val = DoubleVar()
sr_val = DoubleVar()
pa_val = DoubleVar()
sa_val = DoubleVar()
profit_val = DoubleVar()
margin_val = DoubleVar()
percent_val = DoubleVar()
for i in[challan_val,pr_val,sr_val,pa_val,sa_val,measure_var]:
    i.set(' ')

#Set date and time
current_time = datetime.datetime.now()
def ShowDate(x=Event):
    cal_frame = Frame(root,bg = 'beige',highlightbackground = "black",highlightthickness=2)
    cal_frame.place(x=205,y=82)
    Cal = Calendar(cal_frame,selectmode = 'day',year=current_time.year,month=current_time.month,day=current_time.day,date_pattern='DD/MM/YYYY')
    Cal.grid(row=0,column=0,padx=2,pady=2)
    def fetch_n_forget(event):
        date_val.set(Cal.get_date())
        Date.config(textvariable=date_val)        
        cal_frame.place_forget()
        Date.focus()

    cal_select_b = Button(cal_frame,command=lambda :fetch_n_forget(event),text="Select Date",width = 17)
    cal_select_b.grid(row=1,column=0,padx=1,pady=1)
    cal_select_b.focus()
    cal_select_b.bind('<Return>',fetch_n_forget)

#create a button for date picker
dt_bu =ttk. Button(frame_a,text='∷',command=ShowDate)
dt_bu.place(x=215,y=81,width = 20)
#Create entries
Date = ttk.Entry(frame_a,width = 14,font=('Thaoma',15),textvariable = date_val)
Date.place(x = 75,y = 80)
Challan = ttk.Entry(frame_a,width=14,font=('Thaoma',15),textvariable = challan_val)
Challan.place(x=80,y=160)

site_set =[]
item_set =[]
pp_set = []
sp_set = []
truck_set = []
unit_set =[]
def getset(s = site_set,p = item_set,q = pp_set,c = sp_set,t = truck_set,u = unit_set):
    for i in data_sheet["2022-2023"][7:]:
       if len(i) > 0:
           s.append(i[7])
           p.append(i[4])
           q.append(i[3])
           c.append(i[10])
           t.append(i[1])
           u.append(i[6])
getset()
#creating combo boxes for predifined entries
Site =ttk.Combobox(frame_a, width = 25, textvariable = site_val)
Site['values']=list([*set(site_set)])
Site.place(x=65,y=238,height = 25)
Item =ttk.Combobox(frame_a, width = 25, textvariable = item_val)
Item['values']=list([*set(item_set)])
Item.place(x=65,y=316,height = 25)

def Show(event,i):
    i.focus()
    
#Create function for measurement
    
#create quantity label
me_label = Label(frame_a,text = "Quantity",bg = 'beige',font=('Thaoma',12))
me_label.place(x =250,y =316 )
me_entry = ttk.Entry(frame_a,textvariable = measure_var ,width = 18,font=('Thaoma,15'))
me_entry.place(x =375,y =316 ,height = 25)
def callback(event):
    #This is the Window
    top = Toplevel(frame_a,bg='beige')
    top.geometry("450x375")
    top.title("Measurement")
    #creates label and entry for truck number
    label_truck = Label(top,text = "Truck No.",bg = 'beige',font=('Thaoma',12),width = 15).grid(row = 0,column = 0,padx = 1,pady = 1,sticky = 'e')
    entry_truck=ttk.Combobox(top, width = 15, textvariable = truck_val)
    entry_truck['values']=list([*set(truck_set)])
    entry_truck.grid(row = 0,column = 1,padx = 1,pady = 1,sticky='w')
    entry_truck.focus()
    #creates label and entry for Unit
    label_unit = Label(top,text = "Unit",bg = 'beige',font=('Thaoma',12),width = 15)
    label_unit.grid(row = 1,column = 0,padx = 1,pady = 1,sticky = 'ne')
    entry_unit= ttk.Combobox(top, width = 15, textvariable = unit_val)
    entry_unit['values']= list([*set(unit_set)])
    entry_unit.grid(row = 1,column = 1,padx = 1,pady = 1,sticky='nw')
    top.rowconfigure((0,1,2,3),weight = 1)
    top.columnconfigure((0,1),weight = 1)
    #Creates a frame for measurement
    measure_frame = LabelFrame(top,bg="beige",text='Measurement')
    measure_frame.grid(row=2,column=0,columnspan =2,sticky='nsew',padx=2,pady=2)
    #creates labels for measurement
    label_m = [["Length",'0','0'],["Length(inch)",'0','2'],["Width",'1','0'],["Width(inch)",'1','2'],["Height",'2','0'],["Height(inch)",'2','2']]
    label_m_d = {}
    for i in label_m:
            label_m_d[i[0]]=Label(measure_frame,text = i[0],bg = "beige")
            label_m_d[i[0]].config(font=('Thaoma',12))
            label_m_d[i[0]].grid(row = int(i[1]),column = int(i[2]),padx=1,pady = 1)
    #creates entry fields for measurement
    entry_mea_list = [["Length",'0','1'],["Length(inch)",'0','3'],["Width",'1','1'],["Width(inch)",'1','3'],["Height",'2','1'],["Height(inch)",'2','3']]
    entry_m_d = {}
    measurement_dict = {}
    for i in entry_mea_list :
        measurement_dict[i[0]] = DoubleVar()
        measurement_dict[i[0]].set('')
        entry_m_d[i[0]] = ttk.Entry(measure_frame,width=3,textvariable = measurement_dict[i[0]],font=('Thaoma',12))
        entry_m_d[i[0]].grid(row = int(i[1]),column = int(i[2]),padx=1,pady = 1,sticky='nsew')
    #configure row and column for measure_frame
    for i in range(3):
        measure_frame.rowconfigure(i,weight=1)
    for i in range(4):
        measure_frame.columnconfigure(i,weight=1)
    #this part will perform calculation of measurement
    measurement_l = []    
    def cal_m(a = measurement_l,b = measure_var):
        for i in measurement_dict :
            measurement_l.append(measurement_dict[i].get())
        b.set(((measurement_l[0]+measurement_l[1]/12)*(measurement_l[2]+measurement_l[3]/12)*(measurement_l[4]+measurement_l[5]/12))/100)
        label_display_m = Label(top,text = "The measurement is " + str(round(b.get(),2)),bg='beige',width =100)
        label_display_m.configure(font=('Thaoma',13))
        label_display_m.grid(row =3 ,column = 0,columnspan = 2,sticky="nsew")
    entry_m_d["Height(inch)"].bind('<Return>',cal_m)
    me_entry.focus()

    entry_truck.bind('<Return>',lambda p:Show(p,entry_unit))
    entry_unit.bind('<Return>',lambda p:Show(p,entry_m_d['Length']))
    for e in range(len(entry_mea_list)-1):
        def binding(event,x = entry_m_d[entry_mea_list[int(e+1)][0]]):
            Show(event,x)

        entry_m_d[entry_mea_list[e][0]].bind('<Return>',binding)
            

Item.bind('<Return>', callback)


#now i will create purchase entries

#create entry for purchase party
pp_label = Label(frame_a,text = "Purchase Party",bg = 'beige',font=('Thaoma',12))
pp_label.place(x =250,y = 80)
pp_entry=ttk.Combobox(frame_a, width = 25, textvariable = pp_val)
pp_entry['values']=list([*set(pp_set)])
pp_entry.place(x = 375,y = 80,height=25)
pp_entry.config(textvariable = pp_val)

#create entry for purchase rate
pr_label = Label(frame_a,text = "Purchase Rate",bg = 'beige',font=('Thaoma',12))
pr_label.place(x=250,y=160)
pr_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 18)
pr_entry.place(x =375,y = 160,height=25)
pr_entry.config(textvariable = pr_val )

#create entry for purchase Amount
pa_label = Label(frame_a,text = "Purchase Rs",bg = 'beige',font=('Thaoma',12))
pa_label.place(x=250,y=238)
pa_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 18,textvariable = pa_val)
pa_entry.place(x = 375,y =238,height=25 )
def puramount(event,l=pr_val,d=measure_var,r=pa_val):
    pa_entry.focus()
    r.set(l.get()*d.get())
pr_entry.bind('<Return>',lambda a: puramount(a))


#create entry for Sale party
sp_label = Label(frame_a,text = "Sale Party",bg = 'beige',font=('Thaoma',12))
sp_label.place(x=570,y=80)
sp_entry=ttk.Combobox(frame_a, width = 25, textvariable = sp_val)
sp_entry['values']=list([*set(sp_set)])
sp_entry.place(x=650,y=80,height = 25)
sp_entry.config(textvariable = sp_val)

#create entry for Sale rate
sr_label = Label(frame_a,text = "Sale Rate",bg = 'beige',font=('Thaoma',12)).place(x=570,y=160)
sr_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 18,textvariable = sr_val)
sr_entry.place(x=655,y=160,height = 25)

#create entry for Sale Amount
sa_label = Label(frame_a,text = "Sale Rs",bg = 'beige',font=('Thaoma',12)).place(x=570,y=238)
sa_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 20,textvariable = sa_val )
sa_entry.place(x=640,y=238,height =25)
def salamount(event,l=sr_val,d=measure_var,r=sa_val):
    sa_entry.focus()
    r.set(l.get()*d.get())
    #get profit,percent,margin
    profit_val.set(sa_val.get()-pa_val.get())
    percent_val.set((profit_val.get()/pa_val.get())*100)
    margin_val.set(sr_val.get()-pr_val.get())
sr_entry.bind('<Return>',lambda a: salamount(a))


#Profit calc
profit_label = Label(frame_a,text = "Profit" + str(' '),bg = 'beige',font=('Thaoma',15)).place(x=850,y=80)
profit_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 18,textvariable = profit_val)
profit_entry.place(x=920,y=80,height=25)
margin_label = Label(frame_a,text = "Margin" + str(' '),bg = 'beige',font=('Thaoma',15)).place(x=850,y=160)
margin_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 18,textvariable = margin_val)
margin_entry.place(x=920,y=160,height=25)
percent_label = Label(frame_a,text = "%" + str(' '),bg = 'beige',font=('Thaoma',15)).place(x=850,y=238)
percent_entry = ttk.Entry(frame_a,font=('Thaoma,15'),width = 18,textvariable = percent_val)
percent_entry.place(x=920,y=238,height=25)


#create separator
sep_frame = Frame(root,bg='black',width = root.winfo_screenwidth(),height = 1)
sep_frame.place(x = 0,y = 355)
def change_tab_order():
    dt_bu.focus()
    wgs = [dt_bu,Challan,Site,Item,me_entry,pp_entry,pr_entry,pa_entry,sp_entry,sr_entry,sa_entry,profit_entry,margin_entry,percent_entry]
    for i in wgs:
        i.lift()
def focusing():
    dt_bu.bind('<Return>',ShowDate)  
    Date.bind('<Return>',lambda p:Show(p,Challan))
    Challan.bind('<Return>',lambda p:Show(p,Site))
    Site.bind('<Return>',lambda p:Show(p,Item))
    me_entry.bind('<Return>',lambda p:Show(p,pp_entry))
    pp_entry.bind('<Return>',lambda p:Show(p,pr_entry))
    pa_entry.bind('<Return>',lambda p:Show(p,sp_entry))
    sp_entry.bind('<Return>',lambda p:Show(p,sr_entry))
    
focusing()
change_tab_order()



    
#this part will deal with sheet review
style=ttk.Style()
style.configure("mysheet.Treeview",font=('Tahoma',10))
S_Sheet = ttk.Treeview(frame_a,style="mysheet.Treeview")
#columns in tree
S_Sheet['columns'] = ('Date','Truck NO','Challan NO','Purchase ','Item','Quantity','Unit','Site','Rate','Purchase Amount','Sale party','Sale Rate','Sale Amount','Net Profit')
for i in S_Sheet['columns']:
    S_Sheet.column(i,anchor =CENTER,width =30)
    S_Sheet.heading(i,text = i,anchor = CENTER )
S_Sheet.column("#0",stretch =NO,width=0)
S_Sheet.heading("#0", text ="")
def get_values_r():
    count = 0
    for rec in reversed(data_sheet['2022-2023'][7:]):
        if len(rec) > 0 :
            S_Sheet.insert(parent = '',index = 'end', iid = count,text="",values=(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8],rec[9],rec[10],rec[11],rec[12],rec[13]))
            count += 1
    S_Sheet.place(x = 9, y = 375,width=(root.winfo_screenwidth()-20),height=300)
    S_Sheet.selection_set(0)
get_values_r()



    
def save_D(event):
    date_val.set(datetime.datetime.strptime(date_val.get() + 'T00:00:00','%d/%m/%YT%H:%M:%S').date())
    Entry_data_list =[date_val.get()] 
    for i in [truck_val,challan_val,pp_val,item_val,measure_var,unit_val,site_val,pr_val,pa_val,sp_val,sr_val,sa_val,profit_val,percent_val,margin_val]:
        Entry_data_list.append(i.get())
    data_sheet['2022-2023'].insert(-3,Entry_data_list)
    save_data(file_path,data_sheet)
    #CreateSheet()
    get_values_r()
save_style =ttk.Style()
save_style.configure("save.TButton",font=('Thaoma,20'))
save_button = ttk.Button(frame_a,text="Save Entry",command = lambda p :save_D(p),style="save.TButton")
save_button.place(x=1100,y=80,width=240,height=150)
sa_entry.bind('<Return>',lambda p:Show(p,save_button))
save_button.bind('<Return>',lambda p:save_D(p))

#finding an entry based on challan number
def ShowSearchEntry() :
    SearchEntry = IntVar()
    SearchEntry.set('')
    Search_Entry = ttk.Entry(frame_a,width=18,textvariable=SearchEntry)
    Search_Entry.place(x = 1230, y=240,height=45)
    border = LabelFrame(frame_a, bd = 1, bg = "blue")
    border.place(x = 1230,y =240,height =45)
    def highlightVch(event,q=data_sheet['2022-2023']) :
        count = 0
        for i in reversed(q[7:]): 
            if len(i) > 0 :
                if SearchEntry.get() == i[2]  :
                    count = count  + 1
                    S_Sheet.focus(int(count-1))
                    S_Sheet.selection_set(count-1)
                else :
                    count = count + 1
    Search_Entry.bind('<Return>',lambda p:highlightVch(p))
find_b = ttk.Button(frame_a, text ='⌕ Find Entry',command=ShowSearchEntry)
find_b.place(x =1100 ,y= 240,height=45,width=120)

#label for net profit
profitNet = IntVar()
for i in data_sheet['2022-2023'][7:]:
    if len(i) > 0:
        profitNet.set(profitNet.get()+ float(i[13])) 
Profit_net = Label(frame_a,textvariable = profitNet,font=('Thaoma',20),fg ='green',width=14,bg="beige",highlightthickness=1,highlightbackground="green")
Profit_net.place(x=1101,y=300,height=40)
CreateSheet()    
root.mainloop()
