from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import pandas as pd
leca3={"AM3":0,"DLDA":0,"DS":0,"DM":0,"ECCF":0,"OOPM":0}
lecb3={"AM3":0,"DLDA":0,"DS":0,"DM":0,"ECCF":0,"OOPM":0}
leca4={"AM4":0,"CG":0,"OS":0,"COA":0,"AOA":0,"OSTL":0}
lecb4={"AM4":0,"CG":0,"OS":0,"COA":0,"AOA":0,"OSTL":0}
leca5={"MIC":0,"TCS":0,"CN":0,"DBMS":0,"OPT1":0}
lecb5={"MIC":0,"TCS":0,"CN":0,"DBMS":0,"OPT1":0}
leca6={"SE":0,"SPCC":0,"DWM":0,"CSS":0,"DLO":0}
lecb6={"SE":0,"SPCC":0,"DWM":0,"CSS":0,"DLO":0}
leca7={"DSIP":0,"ILO1":0,"AISC":0,"MCC":0,"OPT3":0}
lecb7={"DSIP":0,"ILO1":0,"AISC":0,"MCC":0,"OPT3":0}
leca8={"HMI":0,"ILO2":0,"OPT4":0,"DC":0}
lecb8={"HMI":0,"ILO2":0,"OPT4":0,"DC":0}
#INITIALISING LISTS TO USE FURTHER IN THE CODE
#3
studin3Aa=[]
studin3Ab=[]
studin3Ac=[]
studin3Ad=[]
studin3Ba=[]
studin3Bb=[]
studin3Bc=[]
studin3Bd=[]
am3b=[]
dldab=[]
dmb=[]
dsb=[]
eccfb=[]
oopmb=[]
am3a=[]
dldaa=[]
dma=[]
dsa=[]
eccfa=[]
oopma=[]
rnoa3=[]
rnob3=[]
totpera3=[]
totperb3=[]
totleca3=[]
totlecb3=[]
studa3=0
studb3=0
#4
studin4Aa=[]
studin4Ab=[]
studin4Ac=[]
studin4Ad=[]
studin4Ba=[]
studin4Bb=[]
studin4Bc=[]
studin4Bd=[]
am4b=[]
cgb=[]
coab=[]
osb=[]
aoab=[]
ostlb=[]
am4a=[]
cga=[]
coaa=[]
osa=[]
aoaa=[]
ostla=[]
rnoa4=[]
rnob4=[]
totpera4=[]
totperb4=[]
totleca4=[]
totlecb4=[]
studa4=0
studb4=0
#5
studin5Aa=[]
studin5Ab=[]
studin5Ac=[]
studin5Ad=[]
studin5Ba=[]
studin5Bb=[]
studin5Bc=[]
studin5Bd=[]
micb=[]
tcsb=[]
dbmsb=[]
cnb=[]
opt1b=[]
mica=[]
tcsa=[]
dbmsa=[]
cna=[]
opt1a=[]
rnoa5=[]
rnob5=[]
totpera5=[]
totperb5=[]
totleca5=[]
totlecb5=[]
studa5=0
studb5=0
#6
studin6Aa=[]
studin6Ab=[]
studin6Ac=[]
studin6Ad=[]
studin6Ba=[]
studin6Bb=[]
studin6Bc=[]
studin6Bd=[]
seb=[]
spccb=[]
cssb=[]
dwmb=[]
dlob=[]
sea=[]
spcca=[]
cssa=[]
dwma=[]
dloa=[]
rnoa6=[]
rnob6=[]
totpera6=[]
totperb6=[]
totleca6=[]
totlecb6=[]
studa6=0
studb6=0
#7
studin7Aa=[]
studin7Ab=[]
studin7Ac=[]
studin7Ad=[]
studin7Ba=[]
studin7Bb=[]
studin7Bc=[]
studin7Bd=[]
dsipb=[]
opt3b=[]
mccb=[]
aiscb=[]
ilo1b=[]
dsipa=[]
opt3a=[]
mcca=[]
aisca=[]
ilo1a=[]
rnoa7=[]
rnob7=[]
totpera7=[]
totperb7=[]
totleca7=[]
totlecb7=[]
studa7=0
studb7=0
#8
studin8Aa=[]
studin8Ab=[]
studin8Ac=[]
studin8Ad=[]
studin8Ba=[]
studin8Bb=[]
studin8Bc=[]
studin8Bd=[]
hmib=[]
ilo2b=[]
dcb=[]
opt4b=[]
opt1b=[]
hmia=[]
ilo2a=[]
dca=[]
opt4a=[]
opt1a=[]
rnoa8=[]
rnob8=[]
totleca8=[]
totlecb8=[]
totpera8=[]
totperb8=[]
studa8=0
studb8=0
#dataframes for div A and B
dfa3={"Roll.No":rnoa3,"AM3":am3a,"DLDA":dldaa,"DS":dsa,"DM":dma,"ECCF":eccfa,"OOPM":oopma,"Lectures Attended":totleca3,"Total Percentage":totpera3}
dfb3={"Roll.No":rnob3,"AM3":am3b,"DLDA":dldab,"DS":dsb,"DM":dmb,"ECCF":eccfb,"OOPM":oopmb,"Lectures Attended":totlecb3,"Total Percentage":totperb3}
dfa4={"Roll.No":rnoa4,"AM4":am4a,"CG":cga,"OS":osa,"COA":coaa,"AOA":aoaa,"OSTL":ostla,"Lectures Attended":totleca4,"Total Percentage":totpera4}
dfb4={"Roll.No":rnob4,"AM4":am4b,"CG":cgb,"OS":osb,"COA":coab,"AOA":aoab,"OSTL":ostlb,"Lectures Attended":totlecb4,"Total Percentage":totperb4}
dfa5={"Roll.No":rnoa5,"MIC":mica,"TCS":tcsa,"CN":cna,"DBMS":dbmsa,"OPT1":opt1a,"Lectures Attended":totleca5,"Total Percentage":totpera5}
dfb5={"Roll.No":rnob5,"MIC":micb,"TCS":tcsb,"CN":cnb,"DBMS":dbmsb,"OPT1":opt1b,"Lectures Attended":totlecb5,"Total Percentage":totperb5}
dfa6={"Roll.No":rnoa6,"SE":sea,"SPCC":spcca,"DWM":dwma,"CSS":cssa,"DLO":dloa,"Lectures Attended":totleca6,"Total percentage6":totpera6}
dfb6={"Roll.No":rnob6,"SE":seb,"SPCC":spccb,"DWM":dwmb,"CSS":cssb,"DLO":dlob,"Lectures Attended":totlecb6,"Total percentage6":totperb6}
dfa7={"Roll.No":rnoa7,"DSIP":dsipa,"ILO1":opt3a,"AISC":aisca,"MCC":mcca,"OPT3":ilo1a,"Lectures Attended":totleca7,"Total Percentage":totpera7}
dfb7={"Roll.No":rnob7,"DSIP":dsipb,"ILO1":opt3b,"AISC":aiscb,"MCC":mccb,"OPT3":ilo1b,"Lectures Attended":totlecb7,"Total Percentage":totperb7}
dfa8={"Roll.No":rnoa8,"HMI":hmia,"ILO2":ilo2a,"OPT4":opt4a,"DC":dca,"Lectures Attended":totleca8,"Total Percentage":totpera8}
dfb8={"Roll.No":rnob8,"HMI":hmib,"ILO2":ilo2b,"OPT4":opt4b,"DC":dcb,"Lectures Attended":totlecb8,"Total Percentage":totperb8}
#Tkinter root
root=Tk()
root.geometry('500x600')
w=Label(root,text="Attendance Management System").grid(row=1,column=1)
rad_val=IntVar()
rad_val1=IntVar()
rad_val2=IntVar()
rad_val3=IntVar()
rad_val4=IntVar()
rad_val5=IntVar()
rad_val6=IntVar()
rad_val7=IntVar()
def init3(studa3,studb3):
    for j in range (0,studa3+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        ot="A"+"%d"%(300+j)
        rnoa3.append(ot)
        am3a.append(0)
        dldaa.append(0)
        dma.append(0)
        dsa.append(0)
        eccfa.append(0)
        oopma.append(0)
        totpera3.append(0)
        totleca3.append(0)
    for j in range (0,studb3+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        ot="B"+"%d"%(300+j)
        rnob3.append(ot)
        am3b.append(0)
        dldab.append(0)
        dmb.append(0)
        dsb.append(0)
        eccfb.append(0)
        oopmb.append(0)
        totperb3.append(0)
        totlecb3.append(0)
    rnoa3[0]='TOTAL'
    rnob3[0]='TOTAL'
    totpera3[0]=100
    totperb3[0]=100
dfs3=pd.read_excel("SEM3.xlsx",sheet_name=None)
name=[]
l=[]
if not (dfs3['A-Sem3'].shape[0]==0 and dfs3['B-Sem3'].shape[0]==0):
    for sheetname in dfs3.keys():
        name.append(sheetname)
        l.append(dfs3[sheetname].shape[0]-1)
    studa3=l[0]
    studb3=l[1]
    s_name1=name[0]
    s_name2=name[1]
    init3(studa3,studb3)
    for i in range (0,studa3+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        rnoa3[i]=dfs3[s_name1].iloc[i,0]
        am3a[i]=dfs3[s_name1].iloc[i,1]
        dldaa[i]=dfs3[s_name1].iloc[i,2]
        dsa[i]=dfs3[s_name1].iloc[i,3]
        dma[i]=dfs3[s_name1].iloc[i,4]
        eccfa[i]=dfs3[s_name1].iloc[i,5]
        oopma[i]=dfs3[s_name1].iloc[i,6]
        totleca3[i]=dfs3[s_name1].iloc[i,7]
        totpera3[i]=dfs3[s_name1].iloc[i,8]
    for i in range (0,studb3+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        rnob3[i]=dfs3[s_name2].iloc[i,0]
        am3b[i]=dfs3[s_name2].iloc[i,1]
        dldab[i]=dfs3[s_name2].iloc[i,2]
        dsb[i]=dfs3[s_name2].iloc[i,3]
        dmb[i]=dfs3[s_name2].iloc[i,4]
        eccfb[i]=dfs3[s_name2].iloc[i,5]
        oopmb[i]=dfs3[s_name2].iloc[i,6]
        totlecb3[i]=dfs3[s_name2].iloc[i,7]
        totperb3[i]=dfs3[s_name2].iloc[i,8]
def clear3():
    rnoa3.clear()
    am3a.clear()
    dldaa.clear()
    dma.clear()
    dsa.clear()
    eccfa.clear()
    oopma.clear()
    totpera3.clear()
    totleca3.clear()
    rnob3.clear()
    am3b.clear()
    dldab.clear()
    dmb.clear()
    dsb.clear()
    eccfb.clear()
    oopmb.clear()
    totperb3.clear()
    totlecb3.clear()
    init3(studa3,studb3)
def Search3():
    r=""
    dfs3=pd.read_excel("SEM3.xlsx",sheet_name=None)
    if not (dfs3['A-Sem3'].shape[0]==0 and dfs3['B-Sem3'].shape[0]==0):
        div=simpledialog.askstring("Division","DIV?\nA or B?")
        if div=='A'or div=='a':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=300-rno
            if studa3>=rno:
                r='A'+'%d'%(300+rno)
                ot=[]
                ot=dfs3['A-Sem3'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        if div=='B'or div=='b':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=300-rno
            if studb3>=rno:
                r='B'+'%d'%(300+rno)
                ot=""
                ot=dfs3['A-Sem3'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def AM3():#FOR AM3
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    messagebox.showinfo("Welcome","This is AM3")
    sub="AM3"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca3[sub],div)
        ot+=" And total students in the class are %d"%studa3 
        messagebox.showinfo("GOTCHA",ot)
        am3a[0]=leca3[sub]
        for i in range(0,lec):
            for j in range (1,studa3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa3[j]))
                if(s=='P'or s=='p'):
                    am3a[j]+=1
        dfa3[sub]=am3a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb3[sub],div)
        ot+=" And total students in the class are %d"%studb3 
        messagebox.showinfo("GOTCHA",ot)
        am3b[0]=lecb3[sub]
        for i in range(0,lec):
            for j in range (1,studb3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob3[j]))
                if(s=='P'or s=='p'):
                    am3b[j]+=1               
        dfb3[sub]=am3b
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DM():#FOR DM
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    messagebox.showinfo("Welcome","This is DM")
    sub="DM"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca3[sub],div)
        ot+=" And total students in the class are %d"%studa3 
        messagebox.showinfo("GOTCHA",ot)
        dma[0]=leca3[sub]
        for i in range(0,lec):
            for j in range (1,studa3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa3[j]))
                if(s=='P'or s=='p'):
                    dma[j]+=1               
        dfa3[sub]=dma
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb3[sub],div)
        ot+=" And total students in the class are %d"%studb3 
        messagebox.showinfo("GOTCHA",ot)
        dmb[0]=lecb3[sub]
        for i in range(0,lec):
            for j in range (1,studb3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob3[j]))
                if(s=='P'or s=='p'):
                    dmb[j]+=1               
        dfb3[sub]=dmb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DS(): #FOR DS
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    messagebox.showinfo("Welcome","This is DS")
    sub="DS"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca3[sub],div)
        ot+=" And total students in the class are %d"%studa3 
        messagebox.showinfo("GOTCHA",ot)
        dsa[0]=leca3[sub]
        for i in range(0,lec):
            for j in range (1,studa3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa3[j]))
                if(s=='P'or s=='p'):
                    dsa[j]+=1               
        dfa3[sub]=dsa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb3[sub],div)
        ot+=" And total students in the class are %d"%studb3 
        messagebox.showinfo("GOTCHA",ot)
        dsb[0]=lecb3[sub]
        for i in range(0,lec):
            for j in range (1,studb3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob3[j]))
                if(s=='P'or s=='p'):
                    dsb[j]+=1               
        dfb3[sub]=dsb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DLDA(): #FOR DLDA
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    messagebox.showinfo("Welcome","This is DLDA")
    sub="DLDA"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca3[sub],div)
        ot+=" And total students in the class are %d"%studa3 
        messagebox.showinfo("GOTCHA",ot)
        dldaa[0]=leca3[sub]
        for i in range(0,lec):
            for j in range (1,studa3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa3[j]))
                if(s=='P'or s=='p'):
                    dldaa[j]+=1               
        dfa3[sub]=dldaa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb3[sub],div)
        ot+=" And total students in the class are %d"%studb3 
        messagebox.showinfo("GOTCHA",ot)
        dldab[0]=lecb3[sub]
        for i in range(0,lec):
            for j in range (1,studb3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob3[j]))
                if(s=='P'or s=='p'):
                    dldab[j]+=1               
        dfb3[sub]=dldab
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def ECCF():#FOR ECCF
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    messagebox.showinfo("Welcome","This is ECCF")
    sub="ECCF"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca3[sub],div)
        ot+=" And total students in the class are %d"%studa3 
        messagebox.showinfo("GOTCHA",ot)
        eccfa[0]=leca3[sub]
        for i in range(0,lec):
            for j in range (1,studa3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa3[j]))
                if(s=='P'or s=='p'):
                    eccfa[j]+=1               
        dfa3[sub]=eccfa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb3[sub],div)
        ot+=" And total students in the class are %d"%studb3 
        eccfb[0]=lecb3[sub]
        messagebox.showinfo("GOTCHA",ot)
        for i in range(0,lec):
            for j in range (1,studb3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob3[j]))
                if(s=='P'or s=='p'):
                    eccfb[j]+=1               
        dfb3[sub]=eccfb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def OOPM(): #FOR OOPM
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    messagebox.showinfo("Welcome","This is OOPM")
    sub="OOPM"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca3[sub],div)
        ot+=" And total students in the class are %d"%studa3 
        messagebox.showinfo("GOTCHA",ot)
        oopma[0]=leca3[sub]
        for i in range(0,lec):
            for j in range (1,studa3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa3[j]))
                if(s=='P'or s=='p'):
                    oopma[j]+=1               
        dfa3[sub]=oopma
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb3[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb3[sub],div)
        ot+=" And total students in the class are %d"%studb3 
        messagebox.showinfo("GOTCHA",ot)
        oopmb[0]=lecb3[sub]
        for i in range(0,lec):
            for j in range (1,studb3+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob3[j]))
                if(s=='P'or s=='p'):
                    oopmb[j]+=1               
        dfb3[sub]=oopmb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def Bifercate3():#FOR BIFERCATION BASED ON FINAL PERCENTAGE
    for i in range (1,studa3+1):
        if totpera3[i]>=75:
            studin3Aa.append(rnoa3[i])
        elif totpera3[i]>=60:
            studin3Ab.append(rnoa3[i])
        elif totpera3[i]>=50:
            studin3Ac.append(rnoa3[i])
        else:
            studin3Ad.append(rnoa3[i])
    for i in range (1,studb3+1):
        if totperb3[i]>=75:
            studin3Ba.append(rnob3[i])
        elif totperb3[i]>=60:
            studin3Bb.append(rnob3[i])
        elif totperb3[i]>=50:
            studin3Bc.append(rnob3[i])
        else:
            studin3Bd.append(rnob3[i])
    if rad_val.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin3Aa:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in A-Sem3",ot)
    if rad_val1.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin3Ab:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in A-Sem3",ot)
    if rad_val2.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin3Ac:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=50 & <60 in A-Sem3",ot)
    if rad_val3.get()==1:
        ot=()
        ot="List of the students having attendance <50\n" 
        for i in studin3Ad:
            ot+="%s\n"%(i) 
        messagebox.showinfo("<50 in A-Sem3",ot)
    if rad_val4.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin3Ba:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in B-Sem3",ot)
    if rad_val5.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin3Bb:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in B-Sem3",ot)
    if rad_val6.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin3Bc:
            ot+="%s\n"%(i)
        messagebox.showinfo(">=50 & <60 in B-Sem3",ot)
    if rad_val7.get()==1:
        ot="List of the students having attendance <50\n" 
        for i in studin3Bd:
            ot+="%s\n"%(i)
        messagebox.showinfo("<50 in B-Sem3",ot)
    studin3Aa.clear()
    studin3Ab.clear()
    studin3Ac.clear()
    studin3Ad.clear()
    studin3Ba.clear()
    studin3Bb.clear()
    studin3Bc.clear()
    studin3Bd.clear()
def Sem3GUI():
    w1=Label(root,text="SEM3").grid(row=3,column=2)
    w1=Label(root,text="BIFERCATE DIV A").grid(row=3,column=1)  
    radio1=Checkbutton(root,text=">=75",variable=rad_val).grid(row=4,column=1)
    radio2=Checkbutton(root,text=">=60&<75",variable=rad_val1).grid(row=5,column=1)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val2).grid(row=6,column=1)
    radio4=Checkbutton(root,text="<50",variable=rad_val3).grid(row=7,column=1)
    w2=Label(root,text="BIFERCATE DIV B").grid(row=3,column=5)
    radio5=Checkbutton(root,text=">=75",variable=rad_val4).grid(row=4,column=5)
    radio6=Checkbutton(root,text=">=60&<75",variable=rad_val5).grid(row=5,column=5)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val6).grid(row=6,column=5)
    radio3=Checkbutton(root,text="<50",variable=rad_val7).grid(row=7,column=5)
    but=Button(root,text="BIFERCATE",command=Bifercate3).grid(row=8,column=2)
def percentage3(): #FOr FINDING FINAL TOTAL PERCENTAGE
    global studa3
    global studb3
    if studa3 == 0 and studb3==0:  #CONTINUE
        studa3=simpledialog.askinteger("SEM3","Enter no. of students in DIV A")
        studb3=simpledialog.askinteger("SEM3","Enter no. of students in DIV B")
        init3(studa3,studb3)
    totleca3[0]=am3a[0]+dsa[0]+dldaa[0]+dma[0]+eccfa[0]+oopma[0]
    totlecb3[0]=am3b[0]+dsb[0]+dldab[0]+dmb[0]+eccfb[0]+oopmb[0]
    if not(totlecb3[0]==0 and totleca3[0]==0):
        for i in range (1,studa3+1):
            totleca3[i]=am3a[i]+dsa[i]+dldaa[i]+dma[i]+eccfa[i]+oopma[i]
            if(totleca3[0]>0):
                totpera3[i]=100*(totleca3[i]/totleca3[0])
        for i in range (1,studb3+1):
            totlecb3[i]=am3b[i]+dsb[i]+dldab[i]+dmb[i]+eccfb[i]+oopmb[i]
            if(totlecb3[0]>0):
                totperb3[i]=100*(totlecb3[i]/totlecb3[0])
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def display3(): #FOR SAVING AND WRITING IN THE EXCEL SHEET
    percentage3()
    df=pd.DataFrame(dfa3)
    df1=pd.DataFrame(dfb3)
    writer=pd.ExcelWriter("SEM3.xlsx",engine="xlsxwriter")
    dfs={'A-Sem3':df,'B-Sem3':df1}
    for sheetname in dfs.keys():
        dfs[sheetname].to_excel(writer,sheet_name=sheetname,index=False)
        print("WRITTEN in "+sheetname)
    writer.save()
    for sheetname in dfs.keys():
        w=pd.read_excel("SEM3.xlsx",sheet_name=sheetname)
        print(w)
#SEM4 starts
def init4(studa4,studb4):
    for j in range (0,studa4+1):#init3IALISING EVERYTHING TO ZERO fOR DIV a
        ot="A"+"%d"%(400+j)
        rnoa4.append(ot)
        am4a.append(0)
        cga.append(0)
        coaa.append(0)
        osa.append(0)
        aoaa.append(0)
        ostla.append(0)
        totpera4.append(0) 
        totleca4.append(0)
    for j in range (0,studb4+1):#init3IALISING EVERYTHING TO ZERO FOR dIV b
        ot="B"+"%d"%(400+j)
        rnob4.append(ot)
        am4b.append(0)
        cgb.append(0)
        coab.append(0)
        osb.append(0)
        aoab.append(0)
        ostlb.append(0)
        totperb4.append(0)        
        totlecb4.append(0)
    rnoa4[0]='TOTAL'
    rnob4[0]='TOTAL'
    totpera4[0]=100
    totperb4[0]=100
dfs4=pd.read_excel("SEM4.xlsx",sheet_name=None)
name=[]
l=[]
if not (dfs4['A-Sem4'].shape[0]==0 and dfs4['B-Sem4'].shape[0]==0):
    for sheetname in dfs4.keys():
        name.append(sheetname)
        l.append(dfs4[sheetname].shape[0]-1)
    studa4=l[0]
    studb4=l[1]
    s_name1=name[0]
    s_name2=name[1]
    init4(studa4,studb4)
    for i in range (0,studa4+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        rnoa4[i]=dfs4[s_name1].iloc[i,0]
        am4a[i]=dfs4[s_name1].iloc[i,1]
        cga[i]=dfs4[s_name1].iloc[i,2]
        osa[i]=dfs4[s_name1].iloc[i,3]
        coaa[i]=dfs4[s_name1].iloc[i,4]
        aoab[i]=dfs4[s_name1].iloc[i,5]
        ostlb[i]=dfs4[s_name1].iloc[i,6]
        totleca4[i]=dfs4[s_name1].iloc[i,7]
        totpera4[i]=dfs4[s_name1].iloc[i,8]
    for i in range (0,studb4+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        rnob4[i]=dfs4[s_name2].iloc[i,0]
        am4b[i]=dfs4[s_name2].iloc[i,1]
        cgb[i]=dfs4[s_name2].iloc[i,2]
        osb[i]=dfs4[s_name2].iloc[i,3]
        coab[i]=dfs4[s_name2].iloc[i,4]
        aoab[i]=dfs4[s_name2].iloc[i,5]
        ostlb[i]=dfs4[s_name2].iloc[i,6]
        totlecb4[i]=dfs4[s_name2].iloc[i,7]
        totperb4[i]=dfs4[s_name2].iloc[i,8]
def clear4():
    rnoa4.clear()
    am4a.clear()
    cga.clear()
    osa.clear()
    coaa.clear()
    aoaa.clear()
    ostla.clear()
    totpera4.clear()
    totleca4.clear()
    rnob4.clear()
    am4b.clear()
    cgb.clear()
    osb.clear()
    coa.clear()
    aoab.clear()
    ostlb.clear()
    totperb4.clear()
    totlecb4.clear()
    init4(studa4,studb4)
def Search4():
    r=""
    dfs4=pd.read_excel("SEM4.xlsx",sheet_name=None)
    if not (dfs4['A-Sem4'].shape[0]==0 and dfs4['B-Sem4'].shape[0]==0):
        div=simpledialog.askstring("Division","DIV?\nA or B?")
        if div=='A'or div=='a':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=400-rno
            if studa4>=rno:
                r='A'+'%d'%(400+rno)
                ot=[]
                ot=dfs4['A-Sem4'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        if div=='B'or div=='b':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=400-rno
            if studb4>=rno:
                r='B'+'%d'%(400+rno)
                ot=""
                ot=dfs4['A-Sem4'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def AM4():#FOR AM4
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    messagebox.showinfo("Welcome","This is AM4")
    sub="AM4"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca4[sub],div)
        ot+=" And total students in the class are %d"%studa4 
        messagebox.showinfo("GOTCHA",ot)
        am4a[0]=leca4[sub]
        for i in range(0,lec):
            for j in range (1,studa4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa4[j]))
                if(s=='P'or s=='p'):
                    am4a[j]+=1
        dfa4[sub]=am4a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb4[sub],div)
        ot+=" And total students in the class are %d"%studb4 
        messagebox.showinfo("GOTCHA",ot)
        am4b[0]=lecb4[sub]
        for i in range(0,lec):
            for j in range (1,studb4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob4[j]))
                if(s=='P'or s=='p'):
                    am4b[j]+=1               
        dfb4[sub]=am4b
    
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def COA():#FOR COA
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    messagebox.showinfo("Welcome","This is COA")
    sub="COA"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca4[sub],div)
        ot+=" And total students in the class are %d"%studa4 
        messagebox.showinfo("GOTCHA",ot)
        coaa[0]=leca4[sub]
        for i in range(0,lec):
            for j in range (1,studa4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa4[j]))
                if(s=='P'or s=='p'):
                    coaa[j]+=1               
        dfa4[sub]=coaa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb4[sub],div)
        ot+=" And total students in the class are %d"%studb4 
        messagebox.showinfo("GOTCHA",ot)
        coab[0]=lecb4[sub]
        for i in range(0,lec):
            for j in range (1,studb4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob4[j]))
                if(s=='P'or s=='p'):
                    coab[j]+=1               
        dfb4[sub]=coab
    
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def OS(): #FOR OS
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    messagebox.showinfo("Welcome","This is OS")
    sub="OS"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca4[sub],div)
        ot+=" And total students in the class are %d"%studa4 
        messagebox.showinfo("GOTCHA",ot)
        osa[0]=leca4[sub]
        for i in range(0,lec):
            for j in range (1,studa4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa4[j]))
                if(s=='P'or s=='p'):
                    osa[j]+=1               
        dfa4[sub]=osa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb4[sub],div)
        ot+=" And total students in the class are %d"%studb4 
        messagebox.showinfo("GOTCHA",ot)
        osb[0]=lecb4[sub]
        for i in range(0,lec):
            for j in range (1,studb4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob4[j]))
                if(s=='P'or s=='p'):
                    osb[j]+=1               
        dfb4[sub]=osb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def CG(): #FOR CG
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    messagebox.showinfo("Welcome","This is CG")
    sub="CG"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca4[sub],div)
        ot+=" And total students in the class are %d"%studa4 
        messagebox.showinfo("GOTCHA",ot)
        cga[0]=leca4[sub]
        for i in range(0,lec):
            for j in range (1,studa4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa4[j]))
                if(s=='P'or s=='p'):
                    cga[j]+=1               
        dfa4[sub]=cga
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb4[sub],div)
        ot+=" And total students in the class are %d"%studb4 
        messagebox.showinfo("GOTCHA",ot)
        cgb[0]=lecb4[sub]
        for i in range(0,lec):
            for j in range (1,studb4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob4[j]))
                if(s=='P'or s=='p'):
                    cgb[j]+=1               
        dfb4[sub]=cgb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def AOA():#FOR AOA
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    messagebox.showinfo("Welcome","This is AOA")
    sub="AOA"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca4[sub],div)
        ot+=" And total students in the class are %d"%studa4 
        messagebox.showinfo("GOTCHA",ot)
        aoaa[0]=leca4[sub]
        for i in range(0,lec):
            for j in range (1,studa4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa4[j]))
                if(s=='P'or s=='p'):
                    aoaa[j]+=1               
        dfa4[sub]=aoaa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb4[sub],div)
        ot+=" And total students in the class are %d"%studb4 
        aoab[0]=lecb4[sub]
        messagebox.showinfo("GOTCHA",ot)
        for i in range(0,lec):
            for j in range (1,studb4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob4[j]))
                if(s=='P'or s=='p'):
                    aoab[j]+=1               
        dfb4[sub]=aoab
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def OSTL(): #FOR OSTL
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    messagebox.showinfo("Welcome","This is OSTL")
    sub="OSTL"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca4[sub],div)
        ot+=" And total students in the class are %d"%studa4 
        messagebox.showinfo("GOTCHA",ot)
        ostla[0]=leca4[sub]
        for i in range(0,lec):
            for j in range (1,studa4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa4[j]))
                if(s=='P'or s=='p'):
                    ostla[j]+=1               
        dfa4[sub]=ostla
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb4[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb4[sub],div)
        ot+=" And total students in the class are %d"%studb4 
        messagebox.showinfo("GOTCHA",ot)
        ostlb[0]=lecb4[sub]
        for i in range(0,lec):
            for j in range (1,studb4+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob4[j]))
                if(s=='P'or s=='p'):
                    ostlb[j]+=1               
        dfb4[sub]=ostlb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def Bifercate4():#FOR BIFERCATION BASED ON FINAL PERCENTAGE
    for i in range (1,studa4+1):
        if totpera4[i]>=75:
            studin4Aa.append(rnoa4[i])
        elif totpera4[i]>=60:
            studin4Ab.append(rnoa4[i])
        elif totpera4[i]>=50:
            studin4Ac.append(rnoa4[i])
        else:
            studin4Ad.append(rnoa4[i])
    for i in range (1,studb4+1):
        if totperb4[i]>=75:
            studin4Ba.append(rnob4[i])
        elif totperb4[i]>=60:
            studin4Bb.append(rnob4[i])
        elif totperb4[i]>=50:
            studin4Bc.append(rnob4[i])
        else:
            studin4Bd.append(rnob4[i])
    if rad_val.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin4Aa:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in A-Sem4",ot)
    if rad_val1.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin4Ab:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in A-Sem4",ot)
    if rad_val2.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin4Ac:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=50 & <60 in A-Sem4",ot)
    if rad_val3.get()==1:
        ot=()
        ot="List of the students having attendance <50\n" 
        for i in studin4Ad:
            ot+="%s\n"%(i) 
        messagebox.showinfo("<50 in A-Sem4",ot)
    if rad_val4.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin4Ba:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in B-Sem4",ot)
    if rad_val5.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin4Bb:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in B-Sem4",ot)
    if rad_val6.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin4Bc:
            ot+="%s\n"%(i)
        messagebox.showinfo(">=50 & <60 in B-Sem4",ot)
    if rad_val7.get()==1:
        ot="List of the students having attendance <50\n" 
        for i in studin4Bd:
            ot+="%s\n"%(i)
        messagebox.showinfo("<50 in B-Sem4",ot)
    studin4Aa.clear()
    studin4Ab.clear()
    studin4Ac.clear()
    studin4Ad.clear()
    studin4Ba.clear()
    studin4Bb.clear()
    studin4Bc.clear()
    studin4Bd.clear()
def Sem4GUI():
    w1=Label(root,text="SEM4").grid(row=3,column=2)   
    w1=Label(root,text="BIFERCATE DIV A").grid(row=3,column=1)  
    radio1=Checkbutton(root,text=">=75",variable=rad_val).grid(row=4,column=1)
    radio2=Checkbutton(root,text=">=60&<75",variable=rad_val1).grid(row=5,column=1)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val2).grid(row=6,column=1)
    radio4=Checkbutton(root,text="<50",variable=rad_val3).grid(row=7,column=1)
    w2=Label(root,text="BIFERCATE DIV B").grid(row=3,column=5)
    radio5=Checkbutton(root,text=">=75",variable=rad_val4).grid(row=4,column=5)
    radio6=Checkbutton(root,text=">=60&<75",variable=rad_val5).grid(row=5,column=5)
    radio4=Checkbutton(root,text=">=50&<60",variable=rad_val6).grid(row=6,column=5)
    radio4=Checkbutton(root,text="<50",variable=rad_val7).grid(row=7,column=5)
    but=Button(root,text="BIFERCATE",command=Bifercate4).grid(row=8,column=2)
def percentage4(): #FOr FINDING FINAL TOTAL PERCENTAGE
    global studa4
    global studb4
    if studa4 == 0 and studb4==0:
        studa4=simpledialog.askinteger("SEM4","Enter no. of students in DIV A")
        studb4=simpledialog.askinteger("SEM4","Enter no. of students in DIV B")
        init4(studa4,studb4)
    totleca4[0]=am4a[0]+coaa[0]+osa[0]+cga[0]+aoaa[0]+ostla[0]
    totlecb4[0]=am4b[0]+coab[0]+osb[0]+cgb[0]+aoab[0]+ostlb[0]
    if not(totlecb4[0]==0 and totleca4[0]==0):
        for i in range (1,studa4+1):
            totleca4[i]=am4a[i]+coaa[i]+osa[i]+cga[i]+aoaa[i]+ostla[i]
            if(totleca4[0]>0):
                totpera4[i]=100*(totleca4[i]/totleca4[0])
        for i in range (1,studb4+1):
            totlecb4[i]=am4b[i]+coab[i]+osb[i]+cgb[i]+aoab[i]+ostlb[i]
            if(totlecb4[0]>0):
                totperb4[i]=100*(totlecb4[i]/totlecb4[0])
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def display4(): #FOR SAVING AND WRITING IN THE EXCEL SHEET
    percentage4()
    df=pd.DataFrame(dfa4)
    df1=pd.DataFrame(dfb4)
    writer=pd.ExcelWriter("SEM4.xlsx",engine="xlsxwriter")
    dfs={'A-Sem4':df,'B-Sem4':df1}
    for sheetname in dfs.keys():
        dfs[sheetname].to_excel(writer,sheet_name=sheetname,index=False)
        print("WRITTEN in "+sheetname)
    writer.save()
    for sheetname in dfs.keys():
        w=pd.read_excel("SEM4.xlsx",sheet_name=sheetname)
        print(w)
#SEM5 starts
def init5(studa5,studb5):
    for j in range (0,studa5+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        ot="A"+"%d"%(500+j)
        rnoa5.append(ot)
        mica.append(0)
        tcsa.append(0)
        dbmsa.append(0)
        cna.append(0)
        opt1a.append(0)
        totpera5.append(0)
        totleca5.append(0)
    for j in range (0,studb5+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        ot="B"+"%d"%(500+j)
        rnob5.append(ot)
        micb.append(0)
        tcsb.append(0)
        dbmsb.append(0)
        cnb.append(0)
        opt1b.append(0)
        totperb5.append(0)
        totlecb5.append(0)
    rnoa5[0]='TOTAL'
    rnob5[0]='TOTAL'
    totpera5[0]=100
    totperb5[0]=100
dfs5=pd.read_excel("SEM5.xlsx",sheet_name=None)
name=[]
l=[]
if not (dfs5['A-Sem5'].shape[0]==0 and dfs5['B-Sem5'].shape[0]==0):
    for sheetname in dfs5.keys():
        name.append(sheetname)
        l.append(dfs5[sheetname].shape[0]-1)
    studa5=l[0]
    studb5=l[1]
    s_name1=name[0]
    s_name2=name[1]
    init5(studa5,studb5)
    for i in range (0,studa5+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        rnoa5[i]=dfs5[s_name1].iloc[i,0]
        mica[i]=dfs5[s_name1].iloc[i,1]
        tcsa[i]=dfs5[s_name1].iloc[i,2]
        cna[i]=dfs5[s_name1].iloc[i,3]
        dbmsa[i]=dfs5[s_name1].iloc[i,4]
        opt1a[i]=dfs5[s_name1].iloc[i,5]
        totleca5[i]=dfs5[s_name1].iloc[i,6]
        totpera5[i]=dfs5[s_name1].iloc[i,7]
    for i in range (0,studb5+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        rnob7[i]=dfs5[s_name2].iloc[i,0]
        micb[i]=dfs5[s_name2].iloc[i,1]
        tcsb[i]=dfs5[s_name2].iloc[i,2]
        cnb[i]=dfs5[s_name2].iloc[i,3]
        dbmsb[i]=dfs5[s_name2].iloc[i,4]
        opt1b[i]=dfs5[s_name2].iloc[i,5]
        totlecb5[i]=dfs5[s_name1].iloc[i,6]
        totperb5[i]=dfs5[s_name2].iloc[i,7]
def clear5():
    rnoa5.clear()
    mica.clear()
    tcsa.clear()
    dbmsa.clear()
    cna.clear()
    opt1a.clear()
    totpera5.clear()
    totleca5.clear()
    rnob5.clear()
    micb.clear()
    tcsb.clear()
    dbmsb.clear()
    cnb.clear()
    opt1b.clear()
    totperb5.clear()
    totlecb5.clear()
    init5(studa5,studb5)
def Search5():
    r=""
    dfs5=pd.read_excel("SEM5.xlsx",sheet_name=None)
    if not (dfs5['A-Sem5'].shape[0]==0 and dfs5['B-Sem5'].shape[0]==0):
        div=simpledialog.askstring("Division","DIV?\nA or B?")
        if div=='A'or div=='a':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=500-rno
            if studa5>=rno:
                r='A'+'%d'%(500+rno)
                ot=""
                ot=dfs5['A-Sem5'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        if div=='B'or div=='b':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=500-rno
            if studb5>=rno:
                r='B'+'%d'%(500+rno)
                ot=""
                ot=dfs5['A-Sem5'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def MIC():#FOR MIC
    global studa5
    global studb5
    if studa5 == 0 and studb5==0:
        studa5=simpledialog.askinteger("SEM5","Enter no. of students in DIV A")
        studb5=simpledialog.askinteger("SEM5","Enter no. of students in DIV B")
        init5(studa5,studb5)
    messagebox.showinfo("Welcome","This is MIC")
    sub="MIC"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca5[sub],div)
        ot+=" And total students in the class are %d"%studa5 
        messagebox.showinfo("GOTCHA",ot)
        mica[0]=leca5[sub]
        for i in range(0,lec):
            for j in range (1,studa5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa5[j]))
                if(s=='P'or s=='p'):
                    mica[j]+=1
        dfa5[sub]=mica
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb5[sub],div)
        ot+=" And total students in the class are %d"%studb5 
        messagebox.showinfo("GOTCHA",ot)
        micb[0]=lecb5[sub]
        for i in range(0,lec):
            for j in range (1,studb5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob5[j]))
                if(s=='P'or s=='p'):
                    micb[j]+=1
        dfb5[sub]=micb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DBMS():#FOR DBMS
    global studa5
    global studb5
    if studa5 == 0 and studb5==0:
        studa5=simpledialog.askinteger("SEM5","Enter no. of students in DIV A")
        studb5=simpledialog.askinteger("SEM5","Enter no. of students in DIV B")
        init5(studa5,studb5)
    messagebox.showinfo("Welcome","This is DBMS")
    sub="DBMS"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca5[sub],div)
        ot+=" And total students in the class are %d"%studa5 
        messagebox.showinfo("GOTCHA",ot)
        dbmsa[0]=leca5[sub]
        for i in range(0,lec):
            for j in range (1,studa5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa5[j]))
                if(s=='P'or s=='p'):
                    dbmsa[j]+=1               
        dfa5[sub]=dbmsa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb5[sub],div)
        ot+=" And total students in the class are %d"%studb5 
        messagebox.showinfo("GOTCHA",ot)
        dbmsb[0]=lecb5[sub]
        for i in range(0,lec):
            for j in range (1,studb5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob5[j]))
                if(s=='P'or s=='p'):
                    dbmsb[j]+=1               
        dfb5[sub]=dbmsb
    
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def CN(): #FOR CN
    global studa5
    global studb5
    if studa5 == 0 and studb5==0:
        studa5=simpledialog.askinteger("SEM5","Enter no. of students in DIV A")
        studb5=simpledialog.askinteger("SEM5","Enter no. of students in DIV B")
        init5(studa5,studb5)
    messagebox.showinfo("Welcome","This is CN")
    sub="CN"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca5[sub],div)
        ot+=" And total students in the class are %d"%studa5 
        messagebox.showinfo("GOTCHA",ot)
        cna[0]=leca5[sub]
        for i in range(0,lec):
            for j in range (1,studa5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa5[j]))
                if(s=='P'or s=='p'):
                    cna[j]+=1               
        dfa5[sub]=cna
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb5[sub],div)
        ot+=" And total students in the class are %d"%studb5 
        messagebox.showinfo("GOTCHA",ot)
        cnb[0]=lecb5[sub]
        for i in range(0,lec):
            for j in range (1,studb5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob5[j]))
                if(s=='P'or s=='p'):
                    cnb[j]+=1               
        dfb5[sub]=cnb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def TCS(): #FOR TCS
    global studa5
    global studb5
    if studa5 == 0 and studb5==0:
        studa5=simpledialog.askinteger("SEM5","Enter no. of students in DIV A")
        studb5=simpledialog.askinteger("SEM5","Enter no. of students in DIV B")
        init5(studa5,studb5)
    messagebox.showinfo("Welcome","This is TCS")
    sub="TCS"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca5[sub],div)
        ot+=" And total students in the class are %d"%studa5 
        messagebox.showinfo("GOTCHA",ot)
        tcsa[0]=leca5[sub]
        for i in range(0,lec):
            for j in range (1,studa5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa5[j]))
                if(s=='P'or s=='p'):
                    tcsa[j]+=1               
        dfa5[sub]=tcsa
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb5[sub],div)
        ot+=" And total students in the class are %d"%studb5 
        messagebox.showinfo("GOTCHA",ot)
        tcsb[0]=lecb5[sub]
        for i in range(0,lec):
            for j in range (1,studb5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob5[j]))
                if(s=='P'or s=='p'):
                    tcsb[j]+=1               
        dfb5[sub]=tcsb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def OPT1():#FOR OPT1
    global studa5
    global studb5
    if studa5 == 0 and studb5==0:
        studa5=simpledialog.askinteger("SEM5","Enter no. of students in DIV A")
        studb5=simpledialog.askinteger("SEM5","Enter no. of students in DIV B")
        init5(studa5,studb5)
    messagebox.showinfo("Welcome","This is OPT1")
    sub="OPT1"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca5[sub],div)
        ot+=" And total students in the class are %d"%studa5 
        messagebox.showinfo("GOTCHA",ot)
        opt1a[0]=leca5[sub]
        for i in range(0,lec):
            for j in range (1,studa5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa5[j]))
                if(s=='P'or s=='p'):
                    opt1a[j]+=1               
        dfa5[sub]=opt1a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb5[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb5[sub],div)
        ot+=" And total students in the class are %d"%studb5 
        opt1b[0]=lecb5[sub]
        messagebox.showinfo("GOTCHA",ot)
        for i in range(0,lec):
            for j in range (1,studb5+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob5[j]))
                if(s=='P'or s=='p'):
                    opt1b[j]+=1               
        dfb5[sub]=opt1b
    else:
         messagebox.showinfo("ERROR","Invalid Division")  
def Bifercate5():#FOR BIFERCATION BASED ON FINAL PERCENTAGE
    for i in range (1,studa5+1):
        if totpera5[i]>=75:
            studin5Aa.append(rnoa5[i])
        elif totpera5[i]>=60:
            studin5Ab.append(rnoa5[i])
        elif totpera5[i]>=50:
            studin5Ac.append(rnoa5[i])
        else:
            studin5Ad.append(rnoa5[i])
    for i in range (1,studb5+1):
        if totperb5[i]>=75:
            studin5Ba.append(rnob5[i])
        elif totperb5[i]>=60:
            studin5Bb.append(rnob5[i])
        elif totperb5[i]>=50:
            studin5Bc.append(rnob5[i])
        else:
            studin5Bd.append(rnob5[i])
    if rad_val.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin5Aa:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in A-Sem5",ot)
    if rad_val1.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin5Ab:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in A-Sem5",ot)
    if rad_val2.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin5Ac:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=50 & <60 in A-Sem5",ot)
    if rad_val3.get()==1:
        ot=()
        ot="List of the students having attendance <50\n" 
        for i in studin5Ad:
            ot+="%s\n"%(i) 
        messagebox.showinfo("<50 in A-Sem5",ot)
    if rad_val4.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin5Ba:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in B-Sem5",ot)
    if rad_val5.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin5Bb:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in B-Sem5",ot)
    if rad_val6.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin5Bc:
            ot+="%s\n"%(i)
        messagebox.showinfo(">=50 & <60 in B-Sem5",ot)
    if rad_val7.get()==1:
        ot="List of the students having attendance <50\n" 
        for i in studin5Bd:
            ot+="%s\n"%(i)
        messagebox.showinfo("<50 in B-Sem5",ot)
    studin5Aa.clear()
    studin5Ab.clear()
    studin5Ac.clear()
    studin5Ad.clear()
    studin5Ba.clear()
    studin5Bb.clear()
    studin5Bc.clear()
    studin5Bd.clear()
def Sem5GUI():
    w1=Label(root,text="SEM5").grid(row=3,column=2)  
    w1=Label(root,text="BIFERCATE DIV A").grid(row=3,column=1)  
    radio1=Checkbutton(root,text=">=75",variable=rad_val).grid(row=4,column=1)
    radio2=Checkbutton(root,text=">=60&<75",variable=rad_val1).grid(row=5,column=1)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val2).grid(row=6,column=1)
    radio4=Checkbutton(root,text="<50",variable=rad_val3).grid(row=7,column=1)
    w2=Label(root,text="BIFERCATE DIV B").grid(row=3,column=5)
    radio5=Checkbutton(root,text=">=75",variable=rad_val4).grid(row=4,column=5)
    radio6=Checkbutton(root,text=">=60&<75",variable=rad_val5).grid(row=5,column=5)
    radio5=Checkbutton(root,text=">=50&<60",variable=rad_val6).grid(row=6,column=5)
    radio5=Checkbutton(root,text="<50",variable=rad_val7).grid(row=7,column=5)
    but=Button(root,text="BIFERCATE",command=Bifercate5).grid(row=8,column=2)
def percentage5(): #FOr FINDING FINAL TOTAL PERCENTAGE
    global studa5
    global studb5
    if studa5 == 0 and studb5==0:
        studa5=simpledialog.askinteger("SEM5","Enter no. of students in DIV A")
        studb5=simpledialog.askinteger("SEM5","Enter no. of students in DIV B")
        init5(studa5,studb5)
    totleca5[0]=mica[0]+dbmsa[0]+cna[0]+tcsa[0]+opt1a[0]
    totlecb5[0]=micb[0]+dbmsb[0]+cnb[0]+tcsb[0]+opt1b[0]
    if not(totlecb5[0]==0 and totleca5[0]==0):
        for i in range (1,studa5+1):
            totleca5[i]=mica[i]+dbmsa[i]+cna[i]+tcsa[i]+opt1a[i]
            if(totleca5[0]>0):
                totpera5[i]=100*(totleca5[i]/totleca5[0])
        for i in range (1,studb5+1):
            totlecb5[i]=micb[i]+dbmsb[i]+cnb[i]+tcsb[i]+opt1b[i]
            if(totlecb5[0]>0):
                totperb5[i]=100*(totlecb5[i]/totlecb5[0])
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def display5(): #FOR SAVING AND WRITING IN THE EXCEL SHEET
    percentage5()
    df=pd.DataFrame(dfa5)
    df1=pd.DataFrame(dfb5)
    writer=pd.ExcelWriter("SEM5.xlsx",engine="xlsxwriter")
    dfs={'A-Sem5':df,'B-Sem5':df1}
    for sheetname in dfs.keys():
        dfs[sheetname].to_excel(writer,sheet_name=sheetname,index=False)
        print("WRITTEN in "+sheetname)
    writer.save()
    for sheetname in dfs.keys():
        w=pd.read_excel("SEM5.xlsx",sheet_name=sheetname)
        print(w)
#SEM6 starts
def init6(studa6,studb6):
    for j in range (0,studa6+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        ot="A"+"%d"%(600+j)
        rnoa6.append(ot)
        sea.append(0)
        spcca.append(0)
        cssa.append(0)
        dwma.append(0)
        dloa.append(0)
        totpera6.append(0)
        totleca6.append(0)
    for j in range (0,studb6+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        ot="B"+"%d"%(600+j)
        rnob6.append(ot)
        seb.append(0)
        spccb.append(0)
        cssb.append(0)
        dwmb.append(0)
        dlob.append(0)
        totperb6.append(0)
        totlecb6.append(0)
    rnoa6[0]='TOTAL'
    rnob6[0]='TOTAL'
    totpera6[0]=100
    totperb6[0]=100
dfs6=pd.read_excel("SEM6.xlsx",sheet_name=None)
name=[]
l=[]
if not (dfs6['A-Sem6'].shape[0]==0 and dfs6['B-Sem6'].shape[0]==0):
    for sheetname in dfs6.keys():
        name.append(sheetname)
        l.append(dfs6[sheetname].shape[0]-1)
    studa6=l[0]
    studb6=l[1]
    s_name1=name[0]
    s_name2=name[1]
    init6(studa6,studb6)
    for i in range (0,studa6+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        rnoa6[i]=dfs6[s_name1].iloc[i,0]
        sea[i]=dfs6[s_name1].iloc[i,1]
        spcca[i]=dfs6[s_name1].iloc[i,2]
        dwma[i]=dfs6[s_name1].iloc[i,3]
        cssa[i]=dfs6[s_name1].iloc[i,4]
        dloa[i]=dfs6[s_name1].iloc[i,6]
        totleca6[i]=dfs6[s_name1].iloc[i,6]
        totpera6[i]=dfs6[s_name1].iloc[i,7]
    for i in range (0,studb6+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        rnob7[i]=dfs6[s_name2].iloc[i,0]
        seb[i]=dfs6[s_name2].iloc[i,1]
        spccb[i]=dfs6[s_name2].iloc[i,2]
        dwmb[i]=dfs6[s_name2].iloc[i,3]
        cssb[i]=dfs6[s_name2].iloc[i,4]
        dlob[i]=dfs6[s_name2].iloc[i,6]
        totlecb6[i]=dfs6[s_name1].iloc[i,6]
        totperb6[i]=dfs6[s_name2].iloc[i,7]
def clear6():
    rnoa6.clear()
    sea.clear()
    spcca.clear()
    cssa.clear()
    dwma.clear()
    dloa.clear()
    totpera6.clear()
    totleca6.clear()
    rnob6.clear()
    seb.clear()
    spccb.clear()
    cssb.clear()
    dwmb.clear()
    dlob.clear()
    totperb6.clear()
    totlecb6.clear()
    init6(studa6,studb6)
def Search6():
    r=""
    dfs6=pd.read_excel("SEM6.xlsx",sheet_name=None)
    if not (dfs6['A-Sem6'].shape[0]==0 and dfs6['B-Sem6'].shape[0]==0):
        div=simpledialog.askstring("Division","DIV?\nA or B?")
        if div=='A'or div=='a':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=600-rno
            if studa6>=rno:
                r='A'+'%d'%(600+rno)
                ot=""
                ot=dfs6['A-Sem6'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        if div=='B'or div=='b':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=600-rno
            if studb6>=rno:
                r='B'+'%d'%(600+rno)
                ot=""
                ot=dfs6['A-Sem6'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def SE():#FOR SE
    global studa6
    global studb6
    if studa6 == 0 and studb6==0:
        studa6=simpledialog.askinteger("SEM6","Enter no. of students in DIV A")
        studb6=simpledialog.askinteger("SEM6","Enter no. of students in DIV B")
        init6(studa6,studb6)
    messagebox.showinfo("Welcome","This is SE")
    sub="SE"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca6[sub],div)
        ot+=" And total students in the class are %d"%studa6
        messagebox.showinfo("GOTCHA",ot)
        sea[0]=leca6[sub]
        for i in range(0,lec):
            for j in range (1,studa6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa6[j]))
                if(s=='P'or s=='p'):
                    sea[j]+=1
        dfa6[sub]=sea
    #FOR div b
    elif div=='b' or div=='B':
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb6[sub],div)
        ot+=" And total students in the class are %d"%studb6
        messagebox.showinfo("GOTCHA",ot)
        seb[0]=lecb6[sub]
        for i in range(0,lec):
            for j in range (1,studb6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob6[j]))
                if(s=='P'or s=='p'):
                    seb[j]+=1
        dfb6[sub]=seb

    else:
         messagebox.showinfo("ERROR","Invalid Division")
def CSS():#FOR CSS
    global studa6
    global studb6
    if studa6 == 0 and studb6==0:
        studa6=simpledialog.askinteger("SEM6","Enter no. of students in DIV A")
        studb6=simpledialog.askinteger("SEM6","Enter no. of students in DIV B")
        init6(studa6,studb6)
    messagebox.showinfo("Welcome","This is CSS")
    sub="CSS"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca6[sub],div)
        ot+=" And total students in the class are %d"%studa6
        messagebox.showinfo("GOTCHA",ot)
        cssa[0]=leca6[sub]
        for i in range(0,lec):
            for j in range (1,studa6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa6[j]))
                if(s=='P'or s=='p'):
                    cssa[j]+=1
        dfa6[sub]=cssa
    #FOR div b
    elif div=='b' or div=='B':
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb6[sub],div)
        ot+=" And total students in the class are %d"%studb6
        messagebox.showinfo("GOTCHA",ot)
        cssb[0]=lecb6[sub]
        for i in range(0,lec):
            for j in range (1,studb6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob6[j]))
                if(s=='P'or s=='p'):
                    cssb[j]+=1
        dfb6[sub]=cssb

    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DWM(): #FOR DWM
    global studa6
    global studb6
    if studa6 == 0 and studb6==0:
        studa6=simpledialog.askinteger("SEM6","Enter no. of students in DIV A")
        studb6=simpledialog.askinteger("SEM6","Enter no. of students in DIV B")
        init6(studa6,studb6)
    messagebox.showinfo("Welcome","This is DWM")
    sub="DWM"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca6[sub],div)
        ot+=" And total students in the class are %d"%studa6
        messagebox.showinfo("GOTCHA",ot)
        dwma[0]=leca6[sub]
        for i in range(0,lec):
            for j in range (1,studa6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa6[j]))
                if(s=='P'or s=='p'):
                    dwma[j]+=1
        dfa6[sub]=dwma
    #FOR div b
    elif div=='b' or div=='B':
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb6[sub],div)
        ot+=" And total students in the class are %d"%studb6
        messagebox.showinfo("GOTCHA",ot)
        dwmb[0]=lecb6[sub]
        for i in range(0,lec):
            for j in range (1,studb6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob6[j]))
                if(s=='P'or s=='p'):
                    dwmb[j]+=1
        dfb6[sub]=dwmb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def SPCC(): #FOR SPCC
    global studa6
    global studb6
    if studa6 == 0 and studb6==0:
        studa6=simpledialog.askinteger("SEM6","Enter no. of students in DIV A")
        studb6=simpledialog.askinteger("SEM6","Enter no. of students in DIV B")
        init6(studa6,studb6)
    messagebox.showinfo("Welcome","This is SPCC")
    sub="SPCC"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca6[sub],div)
        ot+=" And total students in the class are %d"%studa6
        messagebox.showinfo("GOTCHA",ot)
        spcca[0]=leca6[sub]
        for i in range(0,lec):
            for j in range (1,studa6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa6[j]))
                if(s=='P'or s=='p'):
                    spcca[j]+=1
        dfa6[sub]=spcca
    #FOR div b
    elif div=='b' or div=='B':
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb6[sub],div)
        ot+=" And total students in the class are %d"%studb6
        messagebox.showinfo("GOTCHA",ot)
        spccb[0]=lecb6[sub]
        for i in range(0,lec):
            for j in range (1,studb6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob6[j]))
                if(s=='P'or s=='p'):
                    spccb[j]+=1
        dfb6[sub]=spccb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DLO():#FOR DLO
    global studa6
    global studb6
    if studa6 == 0 and studb6==0:
        studa6=simpledialog.askinteger("SEM6","Enter no. of students in DIV A")
        studb6=simpledialog.askinteger("SEM6","Enter no. of students in DIV B")
        init6(studa6,studb6)
    messagebox.showinfo("Welcome","This is DLO")
    sub="DLO"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca6[sub],div)
        ot+=" And total students in the class are %d"%studa6
        messagebox.showinfo("GOTCHA",ot)
        dloa[0]=leca6[sub]
        for i in range(0,lec):
            for j in range (1,studa6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa6[j]))
                if(s=='P'or s=='p'):
                    dloa[j]+=1
        dfa6[sub]=dloa
    #FOR div b
    elif div=='b' or div=='B':
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb6[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb6[sub],div)
        ot+=" And total students in the class are %d"%studb6
        dlob[0]=lecb6[sub]
        messagebox.showinfo("GOTCHA",ot)
        for i in range(0,lec):
            for j in range (1,studb6+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob6[j]))
                if(s=='P'or s=='p'):
                    dlob[j]+=1
        dfb6[sub]=dlob
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def Bifercate6():#FOR BIFERCATION BASED ON FINAL PERCENTAGE
    for i in range (1,studa6+1):
        if totpera6[i]>=75:
            studin6Aa.append(rnoa6[i])
        elif totpera6[i]>=60:
            studin6Ab.append(rnoa6[i])
        elif totpera6[i]>=50:
            studin6Ac.append(rnoa6[i])
        else:
            studin6Ad.append(rnoa6[i])
    for i in range (1,studb6+1):
        if totperb6[i]>=75:
            studin6Ba.append(rnob6[i])
        elif totperb6[i]>=60:
            studin6Bb.append(rnob6[i])
        elif totperb6[i]>=50:
            studin6Bc.append(rnob6[i])
        else:
            studin6Bd.append(rnob6[i])
    if rad_val.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin6Aa:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in A-Sem6",ot)
    if rad_val1.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin6Ab:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in A-Sem6",ot)
    if rad_val2.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin6Ac:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=50 & <60 in A-Sem6",ot)
    if rad_val3.get()==1:
        ot=()
        ot="List of the students having attendance <50\n" 
        for i in studin6Ad:
            ot+="%s\n"%(i) 
        messagebox.showinfo("<50 in A-Sem6",ot)
    if rad_val4.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin6Ba:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in B-Sem6",ot)
    if rad_val5.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin6Bb:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in B-Sem6",ot)
    if rad_val6.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin6Bc:
            ot+="%s\n"%(i)
        messagebox.showinfo(">=50 & <60 in B-Sem6",ot)
    if rad_val7.get()==1:
        ot="List of the students having attendance <50\n" 
        for i in studin6Bd:
            ot+="%s\n"%(i)
        messagebox.showinfo("<50 in B-Sem6",ot)
    studin6Aa.clear()
    studin6Ab.clear()
    studin6Ac.clear()
    studin6Ad.clear()
    studin6Ba.clear()
    studin6Bb.clear()
    studin6Bc.clear()
    studin6Bd.clear()
def Sem6GUI():
    w1=Label(root,text="SEM6").grid(row=3,column=2)  
    w1=Label(root,text="BIFERCATE DIV A").grid(row=3,column=1)  
    radio1=Checkbutton(root,text=">=75",variable=rad_val).grid(row=4,column=1)
    radio2=Checkbutton(root,text=">=60&<75",variable=rad_val1).grid(row=5,column=1)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val2).grid(row=6,column=1)
    radio4=Checkbutton(root,text="<50",variable=rad_val3).grid(row=7,column=1)
    w2=Label(root,text="BIFERCATE DIV B").grid(row=3,column=5)
    radio5=Checkbutton(root,text=">=75",variable=rad_val4).grid(row=4,column=5)
    radio6=Checkbutton(root,text=">=60&<75",variable=rad_val5).grid(row=5,column=5)
    radio5=Checkbutton(root,text=">=50&<60",variable=rad_val6).grid(row=6,column=5)
    radio5=Checkbutton(root,text="<50",variable=rad_val7).grid(row=7,column=5)
    but=Button(root,text="BIFERCATE",command=Bifercate6).grid(row=8,column=2)
def percentage6(): #FOr FINDING FINAL TOTAL PERCENTAGE
    global studa6
    global studb6
    if studa6 == 0 and studb6==0:
        studa6=simpledialog.askinteger("SEM6","Enter no. of students in DIV A")
        studb6=simpledialog.askinteger("SEM6","Enter no. of students in DIV B")
        init6(studa6,studb6)
    totleca6[0]=sea[0]+cssa[0]+dwma[0]+spcca[0]+dloa[0]
    totlecb6[0]=seb[0]+cssb[0]+dwmb[0]+spccb[0]+dlob[0]
    if not(totlecb6[0]==0 and totleca6[0]==0):
        for i in range (1,studa6+1):
            totleca6[i]=sea[i]+cssa[i]+dwma[i]+spcca[i]+dloa[i]
            if(totleca6[0]>0):
                totpera6[i]=100*(totleca6[i]/totleca6[0])
        for i in range (1,studb6+1):
            totlecb6[i]=seb[i]+cssb[i]+dwmb[i]+spccb[i]+dlob[i]
            if(totlecb6[0]>0):
                totperb6[i]=100*(totlecb6[i]/totlecb6[0])
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def display6(): #FOR SAVING AND WRITING IN THE EXCEL SHEET
    percentage6()
    df=pd.DataFrame(dfa6)
    df1=pd.DataFrame(dfb6)
    writer=pd.ExcelWriter("SEM6.xlsx",engine="xlsxwriter")
    dfs={'A-Sem6':df,'B-Sem6':df1}
    for sheetname in dfs.keys():
        dfs[sheetname].to_excel(writer,sheet_name=sheetname,index=False)
        print("WRITTEN in "+sheetname)
    writer.save()
    for sheetname in dfs.keys():
        w=pd.read_excel("SEM6.xlsx",sheet_name=sheetname)
        print(w)
#SEM7 starts
def init7(studa7,studb7):
    for j in range (0,studa7+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        ot="A"+"%d"%(700+j)
        rnoa7.append(ot)
        dsipa.append(0)
        opt3a.append(0)
        mcca.append(0)
        aisca.append(0)
        ilo1a.append(0)
        totpera7.append(0)
        totleca7.append(0)
    for j in range (0,studb7+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        ot="B"+"%d"%(700+j)
        rnob7.append(ot)
        dsipb.append(0)
        opt3b.append(0)
        mccb.append(0)
        aiscb.append(0)
        ilo1b.append(0)
        totperb7.append(0)
        totlecb7.append(0)
    rnoa7[0]='TOTAL'
    rnob7[0]='TOTAL'
    totpera7[0]=100
    totperb7[0]=100
dfs7=pd.read_excel("SEM7.xlsx",sheet_name=None)
name=[]
l=[]
if not (dfs7['A-Sem7'].shape[0]==0 and dfs7['B-Sem7'].shape[0]==0):
    for sheetname in dfs7.keys():
        name.append(sheetname)
        l.append(dfs7[sheetname].shape[0]-1)
    studa7=l[0]
    studb7=l[1]
    s_name1=name[0]
    s_name2=name[1]
    init7(studa7,studb7)
    for i in range (0,studa7+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        rnoa7[i]=dfs7[s_name1].iloc[i,0]
        dsipa[i]=dfs7[s_name1].iloc[i,1]
        opt3a[i]=dfs7[s_name1].iloc[i,2]
        mcca[i]=dfs7[s_name1].iloc[i,3]
        aisca[i]=dfs7[s_name1].iloc[i,4]
        ilo1a[i]=dfs7[s_name1].iloc[i,5]
        totleca7[i]=dfs7[s_name1].iloc[i,6]
        totpera7[i]=dfs7[s_name1].iloc[i,7]
    for i in range (0,studb7+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        rnob7[i]=dfs7[s_name2].iloc[i,0]
        dsipb[i]=dfs7[s_name2].iloc[i,1]
        opt3b[i]=dfs7[s_name2].iloc[i,2]
        mccb[i]=dfs7[s_name2].iloc[i,3]
        aiscb[i]=dfs7[s_name2].iloc[i,4]
        ilo1b[i]=dfs7[s_name2].iloc[i,5]
        totlecb7[i]=dfs7[s_name1].iloc[i,6]
        totperb7[i]=dfs7[s_name2].iloc[i,7]
def clear7():
    rnoa7.clear()
    dsipa.clear()
    opt3a.clear()
    mcca.clear()
    aisca.clear()
    ilo1a.clear()
    totpera7.clear()
    totleca7.clear()
    rnob7.clear()
    dsipb.clear()
    opt3b.clear()
    mccb.clear()
    aiscb.clear()
    ilo1b.clear()
    totperb7.clear()
    totlecb7.clear()
    init7(studa7,studb7)
def Search7():
    r=""
    dfs7=pd.read_excel("SEM7.xlsx",sheet_name=None)
    if not (dfs7['A-Sem7'].shape[0]==0 and dfs7['B-Sem7'].shape[0]==0):
        div=simpledialog.askstring("Division","DIV?\nA or B?")
        if div=='A'or div=='a':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=700-rno
            if studa7>=rno:
                r='A'+'%d'%(700+rno)
                ot=""
                ot=dfs7['A-Sem7'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        if div=='B'or div=='b':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=700-rno
            if studb7>=rno:
                r='B'+'%d'%(700+rno)
                ot=""
                ot=dfs7['A-Sem7'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def DSIP():#FOR DSIP
    global studa7
    global studb7
    if studa7 == 0 and studb7==0:
        studa7=simpledialog.askinteger("SEM7","Enter no. of students in DIV A")
        studb7=simpledialog.askinteger("SEM7","Enter no. of students in DIV B")
        init7(studa7,studb7)
    messagebox.showinfo("Welcome","This is DSIP")
    sub="DSIP"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca7[sub],div)
        ot+=" And total students in the class are %d"%studa7
        messagebox.showinfo("GOTCHA",ot)
        dsipa[0]=leca7[sub]
        for i in range(0,lec):
            for j in range (1,studa7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa7[j]))
                if(s=='P'or s=='p'):
                    dsipa[j]+=1
        dfa7[sub]=dsipa
        #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb7[sub],div)
        ot+=" And total students in the class are %d"%studb7 
        messagebox.showinfo("GOTCHA",ot)
        dsipb[0]=lecb7[sub]
        for i in range(0,lec):
            for j in range (1,studb7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob7[j]))
                if(s=='P'or s=='p'):
                    dsipb[j]+=1               
        dfb7[sub]=dsipb 
    else:
        messagebox.showinfo("ERROR","Invalid Division")
def MCC():#FOR MCC
    global studa7
    global studb7
    if studa7 == 0 and studb7==0:  #CONTINUE
        studa7=simpledialog.askinteger("SEM7","Enter no. of students in DIV A")
        studb7=simpledialog.askinteger("SEM7","Enter no. of students in DIV B")
        init7(studa7,studb7)
    messagebox.showinfo("Welcome","This is MCC")
    sub="MCC"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca7[sub],div)
        ot+=" And total students in the class are %d"%studa7 
        messagebox.showinfo("GOTCHA",ot)
        mcca[0]=leca7[sub]
        for i in range(0,lec):
            for j in range (1,studa7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa7[j]))
                if(s=='P'or s=='p'):
                    mcca[j]+=1
        dfa7[sub]=mcca
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb7[sub],div)
        ot+=" And total students in the class are %d"%studb7 
        messagebox.showinfo("GOTCHA",ot)
        mccb[0]=lecb7[sub]
        for i in range(0,lec):
            for j in range (1,studb7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob7[j]))
                if(s=='P'or s=='p'):
                    mccb[j]+=1               
        dfb7[sub]=mccb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def AISC(): #FOR AISC
    global studa7
    global studb7
    if studa7 == 0 and studb7==0:  #CONTINUE
        studa7=simpledialog.askinteger("SEM7","Enter no. of students in DIV A")
        studb7=simpledialog.askinteger("SEM7","Enter no. of students in DIV B")
        init7(studa7,studb7)
    messagebox.showinfo("Welcome","This is AISC")
    sub="AISC"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca7[sub],div)
        ot+=" And total students in the class are %d"%studa7 
        messagebox.showinfo("GOTCHA",ot)
        aisca[0]=leca7[sub]
        for i in range(0,lec):
            for j in range (1,studa7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa7[j]))
                if(s=='P'or s=='p'):
                    aisca[j]+=1               
        dfa7[sub]=aisca
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb7[sub],div)
        ot+=" And total students in the class are %d"%studb7 
        messagebox.showinfo("GOTCHA",ot)
        aiscb[0]=lecb7[sub]
        for i in range(0,lec):
            for j in range (1,studb7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob7[j]))
                if(s=='P'or s=='p'):
                    aiscb[j]+=1               
        dfb7[sub]=aiscb
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def ILO1(): #FOR ILO1
    global studa7
    global studb7
    if studa7 == 0 and studb7==0:  #CONTINUE
        studa7=simpledialog.askinteger("SEM7","Enter no. of students in DIV A")
        studb7=simpledialog.askinteger("SEM7","Enter no. of students in DIV B")
        init7(studa7,studb7)
    messagebox.showinfo("Welcome","This is ILO1")
    sub="ILO1"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca7[sub],div)
        ot+=" And total students in the class are %d"%studa7 
        messagebox.showinfo("GOTCHA",ot)
        opt3a[0]=leca7[sub]
        for i in range(0,lec):
            for j in range (1,studa7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa7[j]))
                if(s=='P'or s=='p'):
                    opt3a[j]+=1               
        dfa7[sub]=opt3a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb7[sub],div)
        ot+=" And total students in the class are %d"%studb7 
        messagebox.showinfo("GOTCHA",ot)
        opt3b[0]=lecb7[sub]
        for i in range(0,lec):
            for j in range (1,studb7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob7[j]))
                if(s=='P'or s=='p'):
                    opt3b[j]+=1               
        dfb7[sub]=opt3b
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def OPT3():#FOR OPT3
    global studa7
    global studb7
    if studa7 == 0 and studb7==0:  #CONTINUE
        studa7=simpledialog.askinteger("SEM7","Enter no. of students in DIV A")
        studb7=simpledialog.askinteger("SEM7","Enter no. of students in DIV B")
        init7(studa7,studb7)
    messagebox.showinfo("Welcome","This is OPT3")
    sub="OPT3"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca7[sub],div)
        ot+=" And total students in the class are %d"%studa7 
        messagebox.showinfo("GOTCHA",ot)
        ilo1a[0]=leca7[sub]
        for i in range(0,lec):
            for j in range (1,studa7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa7[j]))
                if(s=='P'or s=='p'):
                    ilo1a[j]+=1               
        dfa7[sub]=ilo1a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb7[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb7[sub],div)
        ot+=" And total students in the class are %d"%studb7 
        ilo1b[0]=lecb7[sub]
        messagebox.showinfo("GOTCHA",ot)
        for i in range(0,lec):
            for j in range (1,studb7+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob7[j]))
                if(s=='P'or s=='p'):
                    ilo1b[j]+=1               
        dfb7[sub]=ilo1b
    else:
         messagebox.showinfo("ERROR","Invalid Division")   
def Bifercate7():#FOR BIFERCATION BASED ON FINAL PERCENTAGE
    for i in range (1,studa7+1):
        if totpera7[i]>=75:
            studin7Aa.append(rnoa7[i])
        elif totpera7[i]>=60:
            studin7Ab.append(rnoa7[i])
        elif totpera7[i]>=50:
            studin7Ac.append(rnoa7[i])
        else:
            studin7Ad.append(rnoa7[i])
    for i in range (1,studb7+1):
        if totperb7[i]>=75:
            studin7Ba.append(rnob7[i])
        elif totperb7[i]>=60:
            studin7Bb.append(rnob7[i])
        elif totperb7[i]>=50:
            studin7Bc.append(rnob7[i])
        else:
            studin7Bd.append(rnob7[i])
    if rad_val.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin7Aa:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in A-Sem7",ot)
    if rad_val1.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin7Ab:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in A-Sem7",ot)
    if rad_val2.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin7Ac:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=50 & <60 in A-Sem7",ot)
    if rad_val3.get()==1:
        ot=()
        ot="List of the students having attendance <50\n" 
        for i in studin7Ad:
            ot+="%s\n"%(i) 
        messagebox.showinfo("<50 in A-Sem7",ot)
    if rad_val4.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin7Ba:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in B-Sem7",ot)
    if rad_val5.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin7Bb:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in B-Sem7",ot)
    if rad_val6.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin7Bc:
            ot+="%s\n"%(i)
        messagebox.showinfo(">=50 & <60 in B-Sem7",ot)
    if rad_val7.get()==1:
        ot="List of the students having attendance <50\n" 
        for i in studin7Bd:
            ot+="%s\n"%(i)
        messagebox.showinfo("<50 in B-Sem7",ot)
    studin7Aa.clear()
    studin7Ab.clear()
    studin7Ac.clear()
    studin7Ad.clear()
    studin7Ba.clear()
    studin7Bb.clear()
    studin7Bc.clear()
    studin7Bd.clear()
def Sem7GUI():
    w1=Label(root,text="SEM7").grid(row=3,column=2)  
    w1=Label(root,text="BIFERCATE DIV A").grid(row=3,column=1)  
    radio1=Checkbutton(root,text=">=75",variable=rad_val).grid(row=4,column=1)
    radio2=Checkbutton(root,text=">=60&<75",variable=rad_val1).grid(row=5,column=1)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val2).grid(row=6,column=1)
    radio4=Checkbutton(root,text="<50",variable=rad_val3).grid(row=7,column=1)
    w2=Label(root,text="BIFERCATE DIV B").grid(row=3,column=5)
    radio5=Checkbutton(root,text=">=75",variable=rad_val4).grid(row=4,column=5)
    radio6=Checkbutton(root,text=">=60&<75",variable=rad_val5).grid(row=5,column=5)
    radio7=Checkbutton(root,text=">=50&<60",variable=rad_val6).grid(row=6,column=5)
    radio8=Checkbutton(root,text="<50",variable=rad_val7).grid(row=7,column=5)
    but=Button(root,text="BIFERCATE",command=Bifercate7).grid(row=8,column=2)
def percentage7():#FOr FINDING FINAL TOTAL PERCENTAGE
    global studa7
    global studb7
    if studa7 == 0 and studb7==0:  #CONTINUE
        studa7=simpledialog.askinteger("SEM7","Enter no. of students in DIV A")
        studb7=simpledialog.askinteger("SEM7","Enter no. of students in DIV B")
        init7(studa7,studb7)
    totleca7[0]=dsipa[0]+mcca[0]+aisca[0]+opt3a[0]+ilo1a[0]
    totlecb7[0]=dsipb[0]+mccb[0]+aiscb[0]+opt3b[0]+ilo1b[0]
    if not(totlecb7[0]==0 and totleca7[0]==0):
        for i in range (1,studa7+1):
            totleca7[i]=dsipa[i]+mcca[i]+aisca[i]+opt3a[i]+ilo1a[i]
            if(totleca7[0]>0):
                totpera7[i]=100*(totleca7[i]/totleca7[0])
        for i in range (1,studb7+1):
            totlecb7[i]=dsipb[i]+mccb[i]+aiscb[i]+opt3b[i]+ilo1b[i]
            if(totlecb7[0]>0):
                totperb7[i]=100*(totlecb7[i]/totlecb7[0])
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def display7(): #FOR SAVING AND WRITING IN THE EXCEL SHEET
    percentage7()
    df=pd.DataFrame(dfa7)
    df1=pd.DataFrame(dfb7)
    writer=pd.ExcelWriter("SEM7.xlsx",engine="xlsxwriter")
    dfs7={'A-Sem7':df,'B-Sem7':df1}
    for sheetname in dfs7.keys():
        dfs7[sheetname].to_excel(writer,sheet_name=sheetname,index=False)
        print("WRITTEN in "+sheetname)
    writer.save()
    for sheetname in dfs7.keys():
        w=pd.read_excel("SEM7.xlsx",sheet_name=sheetname)
        print(w)


#SEM8 starts
def init8(studa8,studb8):
    for j in range (0,studa8+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        ot="A"+"%d"%(800+j)
        rnoa8.append(ot)
        hmia.append(0)
        ilo2a.append(0)
        dca.append(0)
        opt4a.append(0)
        totpera8.append(0)
        totleca8.append(0)
    for j in range (0,studb8+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        ot="B"+"%d"%(800+j)
        rnob8.append(ot)
        hmib.append(0)
        ilo2b.append(0)
        dcb.append(0)
        opt4b.append(0)
        totperb8.append(0)
        totlecb8.append(0)
    rnoa8[0]='TOTAL'
    rnob8[0]='TOTAL'
    totpera8[0]=100
    totperb8[0]=100
dfs8=pd.read_excel("SEM8.xlsx",sheet_name=None)
name=[]
l=[]
if not (dfs8['A-Sem8'].shape[0]==0 and dfs8['B-Sem8'].shape[0]==0):
    for sheetname in dfs8.keys():
        name.append(sheetname)
        l.append(dfs8[sheetname].shape[0]-1)
    studa8=l[0]
    studb8=l[1]
    s_name1=name[0]
    s_name2=name[1]
    init8(studa8,studb8)
    for i in range (0,studa8+1):#INITIALISING EVERYTHING TO ZERO fOR DIV a
        rnoa8[i]=dfs8[s_name1].iloc[i,0]
        hmia[i]=dfs8[s_name1].iloc[i,1]
        ilo2a[i]=dfs8[s_name1].iloc[i,2]
        opt4a[i]=dfs8[s_name1].iloc[i,3]
        dca[i]=dfs8[s_name1].iloc[i,4]
        totleca8[i]=dfs8[s_name1].iloc[i,5]
        totpera8[i]=dfs8[s_name1].iloc[i,6]
    for i in range (0,studb8+1):#INITIALISING EVERYTHING TO ZERO FOR dIV b
        rnob8[i]=dfs8[s_name2].iloc[i,0]
        hmib[i]=dfs8[s_name2].iloc[i,1]
        ilo2b[i]=dfs8[s_name2].iloc[i,2]
        opt4b[i]=dfs8[s_name2].iloc[i,3]
        dcb[i]=dfs8[s_name2].iloc[i,4]
        totlecb8[i]=dfs8[s_name1].iloc[i,5]
        totperb8[i]=dfs8[s_name2].iloc[i,6]
def clear8():
    rnoa8.clear()
    hmia.clear()
    opt4a.clear()
    dca.clear()
    ilo2a.clear()
    totpera8.clear()
    totleca8.clear()
    rnob8.clear()
    hmib.clear()
    opt4b.clear()
    dcb.clear()
    ilo2b.clear()
    totperb8.clear()
    totlecb8.clear()
    init8(studa8,studb8)
def Search8():
    r=""
    dfs8=pd.read_excel("SEM8.xlsx",sheet_name=None)
    if not (dfs8['A-Sem8'].shape[0]==0 and dfs8['B-Sem8'].shape[0]==0):
        div=simpledialog.askstring("Division","DIV?\nA or B?")
        if div=='A'or div=='a':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=800-rno
            if studa8>=rno:
                r='A'+'%d'%(800+rno)
                ot=[]
                ot=dfs8['A-Sem8'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        if div=='B'or div=='b':
            rno=simpledialog.askinteger("Roll No.","Enter Roll No for finding records")
            if rno>100:
                rno=800-rno
            if studb8>=rno:
                r='B'+'%d'%(800+rno)
                ot=""
                ot=dfs8['A-Sem8'].iloc[rno,:]
                messagebox.showinfo("Student Info","Info-\n%s"%(ot))
            else:
                raise ValueError("Roll No is not present")
        
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def HMI():#FOR HMI
    global studa8
    global studb8
    if studa8==0 and studb8==0:
        studa8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV A")
        studb8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV B")
        init8(studa8,studb8)
    messagebox.showinfo("Welcome","This is HMI")
    sub="HMI"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca8[sub],div)
        ot+=" And total students in the class are %d"%studa8 
        messagebox.showinfo("GOTCHA",ot)
        hmia[0]=leca8[sub]
        for i in range(0,lec):
            for j in range (1,studa8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa8[j]))
                if(s=='P'or s=='p'):
                    hmia[j]+=1
        dfa8[sub]=hmia
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb8[sub],div)
        ot+=" And total students in the class are %d"%studb8 
        messagebox.showinfo("GOTCHA",ot)
        hmib[0]=lecb8[sub]
        for i in range(0,lec):
            for j in range (1,studb8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob8[j]))
                if(s=='P'or s=='p'):
                    hmib[j]+=1               
        dfb8[sub]=hmib
    
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def DC():#FOR DC
    global studa8
    global studb8
    if studa8==0 and studb8==0:
        studa8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV A")
        studb8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV B")
        init8(studa8,studb8)
    messagebox.showinfo("Welcome","This is DC")
    sub="DC"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca8[sub],div)
        ot+=" And total students in the class are %d"%studa8 
        messagebox.showinfo("GOTCHA",ot)
        dca[0]=leca8[sub]
        for i in range(0,lec):
            for j in range (1,studa8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa8[j]))
                if(s=='P'or s=='p'):
                    dca[j]+=1               
        dfa8[sub]=dca
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb8[sub],div)
        ot+=" And total students in the class are %d"%studb8 
        messagebox.showinfo("GOTCHA",ot)
        dcb[0]=lecb8[sub]
        for i in range(0,lec):
            for j in range (1,studb8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob8[j]))
                if(s=='P'or s=='p'):
                    dcb[j]+=1               
        dfb8[sub]=dcb
    
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def OPT4(): #FOR OPT4
    global studa8
    global studb8
    if studa8==0 and studb8==0:
        studa8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV A")
        studb8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV B")
        init8(studa8,studb8)
    messagebox.showinfo("Welcome","This is OPT4")
    sub="OPT4"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca8[sub],div)
        ot+=" And total students in the class are %d"%studa8 
        messagebox.showinfo("GOTCHA",ot)
        opt4a[0]=leca8[sub]
        for i in range(0,lec):
            for j in range (1,studa8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa8[j]))
                if(s=='P'or s=='p'):
                    opt4a[j]+=1               
        dfa8[sub]=opt4a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb8[sub],div)
        ot+=" And total students in the class are %d"%studb8 
        messagebox.showinfo("GOTCHA",ot)
        opt4b[0]=lecb8[sub]
        for i in range(0,lec):
            for j in range (1,studb8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob8[j]))
                if(s=='P'or s=='p'):
                    opt4b[j]+=1               
        dfb8[sub]=opt4b
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def ILO2(): #FOR ILO2
    global studa8
    global studb8
    if studa8==0 and studb8==0:
        studa8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV A")
        studb8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV B")
        init8(studa8,studb8)
    messagebox.showinfo("Welcome","This is ILO2")
    sub="ILO2"
    div=simpledialog.askstring("DIVISION","Enter Div")
    if div=='a'or div=='A':  #FOR div A
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        leca8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(leca8[sub],div)
        ot+=" And total students in the class are %d"%studa8 
        messagebox.showinfo("GOTCHA",ot)
        ilo2a[0]=leca8[sub]
        for i in range(0,lec):
            for j in range (1,studa8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnoa8[j]))
                if(s=='P'or s=='p'):
                    ilo2a[j]+=1               
        dfa8[sub]=ilo2a
    #FOR div b
    elif div=='b' or div=='B':                                                                                                                                                              
        lec=simpledialog.askinteger("Lecture","Enter Total lecture")
        lecb8[sub]+=lec
        ot="FETCHED INFO >>>> Total there are %d lectures happened in DIV %s." %(lecb8[sub],div)
        ot+=" And total students in the class are %d"%studb8 
        messagebox.showinfo("GOTCHA",ot)
        ilo2b[0]=lecb8[sub]
        for i in range(0,lec):
            for j in range (1,studb8+1):
                s=simpledialog.askstring("For %s lect %d"%(sub,i+1)," For rollno. %s \n'P' or 'A'?"%(rnob8[j]))
                if(s=='P'or s=='p'):
                    ilo2b[j]+=1               
        dfb8[sub]=ilo2b
    else:
         messagebox.showinfo("ERROR","Invalid Division")
def Bifercate8():#FOR BIFERCATION BASED ON FINAL PERCENTAGE
    for i in range (1,studa8+1):
        if totpera8[i]>=75:
            studin8Aa.append(rnoa8[i])
        elif totpera8[i]>=60:
            studin8Ab.append(rnoa8[i])
        elif totpera8[i]>=50:
            studin8Ac.append(rnoa8[i])
        else:
            studin8Ad.append(rnoa8[i])
    for i in range (1,studb8+1):
        if totperb8[i]>=75:
            studin8Ba.append(rnob8[i])
        elif totperb8[i]>=60:
            studin8Bb.append(rnob8[i])
        elif totperb8[i]>=50:
            studin8Bc.append(rnob8[i])
        else:
            studin8Bd.append(rnob8[i])
    if rad_val.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin8Aa:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in A-Sem8",ot)
    if rad_val1.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin8Ab:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in A-Sem8",ot)
    if rad_val2.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin8Ac:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=50 & <60 in A-Sem8",ot)
    if rad_val3.get()==1:
        ot=()
        ot="List of the students having attendance <50\n" 
        for i in studin8Ad:
            ot+="%s\n"%(i) 
        messagebox.showinfo("<50 in A-Sem8",ot)
    if rad_val4.get()==1:
        ot=()
        ot="List of the students having attendance >=75\n" 
        for i in studin8Ba:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=75 in B-Sem8",ot)
    if rad_val5.get()==1:
        ot=()
        ot="List of the students having attendance >=60 & <75\n" 
        for i in studin8Bb:
            ot+="%s\n"%(i) 
        messagebox.showinfo(">=60 & <75 in B-Sem8",ot)
    if rad_val6.get()==1:
        ot=()
        ot="List of the students having attendance >=50 & <60\n" 
        for i in studin8Bc:
            ot+="%s\n"%(i)
        messagebox.showinfo(">=50 & <60 in B-Sem8",ot)
    if rad_val7.get()==1:
        ot="List of the students having attendance <50\n" 
        for i in studin8Bd:
            ot+="%s\n"%(i)
        messagebox.showinfo("<50 in B-Sem8",ot)
    studin8Aa.clear()
    studin8Ab.clear()
    studin8Ac.clear()
    studin8Ad.clear()
    studin8Ba.clear()
    studin8Bb.clear()
    studin8Bc.clear()
    studin8Bd.clear()
def Sem8GUI():
    w1=Label(root,text="SEM8").grid(row=3,column=2)  
    w1=Label(root,text="BIFERCATE DIV A").grid(row=3,column=1)  
    radio1=Checkbutton(root,text=">=75",variable=rad_val).grid(row=4,column=1)
    radio2=Checkbutton(root,text=">=60&<75",variable=rad_val1).grid(row=5,column=1)
    radio3=Checkbutton(root,text=">=50&<60",variable=rad_val2).grid(row=6,column=1)
    radio4=Checkbutton(root,text="<50",variable=rad_val3).grid(row=7,column=1)
    w2=Label(root,text="BIFERCATE DIV B").grid(row=3,column=5)
    radio5=Checkbutton(root,text=">=75",variable=rad_val4).grid(row=4,column=5)
    radio6=Checkbutton(root,text=">=60&<75",variable=rad_val5).grid(row=5,column=5)
    radio8=Checkbutton(root,text=">=50&<60",variable=rad_val6).grid(row=6,column=5)
    radio8=Checkbutton(root,text="<50",variable=rad_val7).grid(row=7,column=5)
    but=Button(root,text="BIFERCATE",command=Bifercate8).grid(row=8,column=2)
def percentage8(): #FOr FINDING FINAL TOTAL PERCENTAGE
    global studa8
    global studb8
    if studa8==0 and studb8==0:
        studa8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV A")
        studb8=simpledialog.askinteger("SEM-8","Enter no. of students in DIV B")
        init8(studa8,studb8)
    totleca8[0]=hmia[0]+dca[0]+opt4a[0]+ilo2a[0]
    totlecb8[0]=hmib[0]+dcb[0]+opt4b[0]+ilo2b[0]
    if not(totlecb8[0]==0 and totleca8[0]==0):
        for i in range (1,studa8+1):
            totleca8[i]=hmia[i]+dca[i]+opt4a[i]+ilo2a[i]
            if(totleca8[0]>0):
                totpera8[i]=100*(totleca8[i]/totleca8[0])
        for i in range (1,studb8+1):
            totlecb8[i]=hmib[i]+dcb[i]+opt4b[i]+ilo2b[i]
            if(totlecb8[0]>0):
                totperb8[i]=100*(totlecb8[i]/totlecb8[0])
    else:
        raise ValueError("SHEETS ARE EMPTY, FIRST ENTER SOME DATA")
def display8(): #FOR SAVING AND WRITING IN THE EXCEL SHEET
    percentage8()
    df=pd.DataFrame(dfa8)
    df1=pd.DataFrame(dfb8)
    writer=pd.ExcelWriter("SEM8.xlsx",engine="xlsxwriter")
    dfs={'A-Sem8':df,'B-Sem8':df1}
    for sheetname in dfs.keys():
        dfs[sheetname].to_excel(writer,sheet_name=sheetname,index=False)
        print("WRITTEN in "+sheetname)
    writer.save()
    for sheetname in dfs.keys():
        w=pd.read_excel("SEM8.xlsx",sheet_name=sheetname)
        print(w)
def change_dropdown(*args):
    if var.get()=="Sem3":
        Sem3GUI()
    if var.get()=="Sem4":
        Sem4GUI()
    if var.get()=="Sem5":
        Sem5GUI()
    if var.get()=="Sem6":
        Sem6GUI()
    if var.get()=="Sem7":
        Sem7GUI()
    if var.get()=="Sem8":
        Sem8GUI()
#HOME GUI
menu=Menu(root)
root.config(menu=menu)
choices=["Sem3","Sem4","Sem5","Sem6","Sem7","Sem8"]
var=StringVar()
var.set("Sem3")
w1=Label(root,text="BIFERCATE").grid(row=2,column=1)
popmenu=OptionMenu(root,var,*choices).grid(row=2,column=2)
var.trace('w',change_dropdown)
def EXIT():
    exit()
def AboutUs():
    messagebox.showinfo("About Us","It is a Second Year Python project\nMade By:\nAbhishek Yadav(B468)\nKashyap Vyas(B465)")
#SEM3
submenu=Menu(menu)
menu.add_cascade(label="Sem3", menu=submenu)
submenu.add_command(label="AM3",command=AM3)
submenu.add_separator()
submenu.add_command(label="DM",command=DM)
submenu.add_separator()
submenu.add_command(label="DS",command=DS)
submenu.add_separator()
submenu.add_command(label="DLDA",command=DLDA)
submenu.add_separator()
submenu.add_command(label="ECCF",command=ECCF)
submenu.add_separator()
submenu.add_command(label="OOPM",command=OOPM)
submenu.add_separator()
submenu.add_command(label="Display",command=display3)
submenu.add_separator()
submenu.add_command(label="Clear",command=clear3)
submenu.add_separator()
submenu.add_command(label="Search",command=Search3)
submenu.add_separator()
submenu.add_command(label="Exit",command=EXIT)

#SEM4
submenu=Menu(menu)
menu.add_cascade(label="Sem4", menu=submenu)
submenu.add_command(label="AM4",command=AM4)
submenu.add_separator()
submenu.add_command(label="COA",command=COA)
submenu.add_separator()
submenu.add_command(label="OS",command=OS)
submenu.add_separator()
submenu.add_command(label="CG",command=CG)
submenu.add_separator()
submenu.add_command(label="AOA",command=AOA)
submenu.add_separator()
submenu.add_command(label="OSTL",command=OSTL)
submenu.add_separator()
submenu.add_command(label="Display",command=display4)
submenu.add_separator()
submenu.add_command(label="Clear",command=clear4)
submenu.add_separator()
submenu.add_command(label="Search",command=Search4)
submenu.add_separator()
submenu.add_command(label="Exit",command=EXIT)

#SEM5
submenu=Menu(menu)
menu.add_cascade(label="Sem5", menu=submenu)
submenu.add_command(label="MIC",command=MIC)
submenu.add_separator()
submenu.add_command(label="DBMS",command=DBMS)
submenu.add_separator()
submenu.add_command(label="CN",command=CN)
submenu.add_separator()
submenu.add_command(label="TCS",command=TCS)
submenu.add_separator()
submenu.add_command(label="OPT1",command=OPT1)
submenu.add_separator()
submenu.add_command(label="Display",command=display5)
submenu.add_separator()
submenu.add_command(label="Clear",command=clear5)
submenu.add_separator()
submenu.add_command(label="Search",command=Search5)
submenu.add_separator()
submenu.add_command(label="Exit",command=EXIT)

#SEM6
submenu=Menu(menu)
menu.add_cascade(label="Sem6", menu=submenu)
submenu.add_command(label="SE",command=SE)
submenu.add_separator()
submenu.add_command(label="CSS",command=CSS)
submenu.add_separator()
submenu.add_command(label="DWM",command=DWM)
submenu.add_separator()
submenu.add_command(label="SPCC",command=SPCC)
submenu.add_separator()
submenu.add_command(label="OPT2",command=DLO)
submenu.add_separator()
submenu.add_command(label="Display6",command=display6)
submenu.add_separator()
submenu.add_command(label="Clear",command=clear6)
submenu.add_separator()
submenu.add_command(label="Search",command=Search6)
submenu.add_separator()
submenu.add_command(label="Exit",command=EXIT)

#SEM7
submenu=Menu(menu)
menu.add_cascade(label="Sem7", menu=submenu)
submenu.add_command(label="DSIP",command=DSIP)
submenu.add_separator()
submenu.add_command(label="MCC",command=MCC)
submenu.add_separator()
submenu.add_command(label="AISC",command=AISC)
submenu.add_separator()
submenu.add_command(label="ILO1",command=ILO1)
submenu.add_separator()
submenu.add_command(label="OPT3",command=OPT3)
submenu.add_separator()
submenu.add_command(label="Display",command=display7)
submenu.add_separator()
submenu.add_command(label="Clear",command=clear7)
submenu.add_separator()
submenu.add_command(label="Search",command=Search7)
submenu.add_separator()
submenu.add_command(label="Exit",command=EXIT)

#SEM8
submenu=Menu(menu)
menu.add_cascade(label="Sem8", menu=submenu)
submenu.add_command(label="HMI",command=HMI)
submenu.add_separator()
submenu.add_command(label="DC",command=DC)
submenu.add_separator()
submenu.add_command(label="OPT4",command=OPT4)
submenu.add_separator()
submenu.add_command(label="ILO2",command=ILO2)
submenu.add_separator()
submenu.add_command(label="Display",command=display8)
submenu.add_separator()
submenu.add_command(label="Clear",command=clear8)
submenu.add_separator()
submenu.add_command(label="Search",command=Search8)
submenu.add_separator()
submenu.add_command(label="Exit",command=EXIT)

submenu=Menu(menu)
menu.add_cascade(label="About Us", menu=submenu)
submenu.add_command(label="About Us",command=AboutUs)

root.mainloop()
