from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.BloodPressure=StringVar()
        self.HowToUseMedicine=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        # ===============================Data Frame ========================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                  font=("times new roman",12,"bold"),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)
        dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                  font=("times new roman",12,"bold"),text="Prescription")
        dataframeright.place(x=990,y=5,width=460,height=350)

        # ================================Buttons Frame==============================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        # ===============================Details Frame=========================================================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # ===========================================================dataframeleft===========================================================
        lblNameTablet=Label(dataframeleft,text="Names Of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(dataframeleft,textvariable=self.Nameoftablets,font=("arial",12,"bold"),
                                   width=33)
        comNameTablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Amlodipine","Ativan")
        comNameTablet.grid(row=0,column=1)

        lblref=Label(dataframeleft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeleft,textvariable=self.ref,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(dataframeleft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(dataframeleft,textvariable=self.Dose,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablet=Label(dataframeleft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablet.grid(row=3,column=0,sticky=W)
        txtNoOftablet=Entry(dataframeleft,textvariable=self.Numberoftablets,font=("arial",12,"bold"),width=35)
        txtNoOftablet.grid(row=3,column=1)

        lblLot=Label(dataframeleft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(dataframeleft,textvariable=self.Lot,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(dataframeleft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(dataframeleft,textvariable=self.Issuedate,font=("arial",12,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(dataframeleft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(dataframeleft,textvariable=self.ExpDate,font=("arial",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(dataframeleft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(dataframeleft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(dataframeleft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(dataframeleft,textvariable=self.SideEffect,font=("arial",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(dataframeleft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(dataframeleft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(dataframeleft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(dataframeleft,textvariable=self.BloodPressure,font=("arial",12,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(dataframeleft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataframeleft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(dataframeleft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(dataframeleft,textvariable=self.HowToUseMedicine,font=("arial",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(dataframeleft,textvariable=self.PatientId,font=("arial",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(dataframeleft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(dataframeleft,textvariable=self.nhsNumber,font=("arial",12,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(dataframeleft,textvariable=self.PatientName,font=("arial",12,"bold"),width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(dataframeleft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(dataframeleft,textvariable=self.DateOfBirth,font=("arial",12,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(dataframeleft,textvariable=self.PatientAddress,font=("arial",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)

        # ================================Dataframe right====================================================
        self.txtPrescription=Text(dataframeright,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        # ========================Buttons====================================================================
        btnPrescription=Button(Buttonframe,text="Prescription",font=("arial",12,"bold"),bg="green",fg="white",width=23,padx=2,pady=3)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",font=("arial",12,"bold"),bg="green",fg="white",width=23,padx=2,pady=3)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update ",font=("arial",12,"bold"),bg="green",fg="white",width=23,padx=2,pady=3)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",font=("arial",12,"bold"),bg="green",fg="white",width=23,padx=2,pady=3)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",font=("arial",12,"bold"),bg="green",fg="white",width=23,padx=2,pady=3)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",font=("arial",12,"bold"),bg="green",fg="white",width=23,padx=2,pady=3)
        btnExit.grid(row=0,column=5)

        # ==========================================================Table===================================
        # =======================================================ScrollBar==================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate",
                                                              "dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

# =============================Functionality Declaration=============================================
        def iPrescriptionDate(self):
            if self.Nameoftablets.get()==""or self.ref.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.Numberoftablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                     
                ))
                conn.commit()
                conn.close()

root=Tk()
ob=Hospital(root)
root.mainloop()