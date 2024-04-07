import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import Label
import  mysql.connector
import webbrowser
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import *
root = tk.Tk()
root.title("Course Academy")
root.geometry("1346x685")
root.config()


    # Function to handle the "New" button click
def About():
    # Add your logic here for creating a login
    print("about")
    
    main_frame = Frame(bg="#003153")
    # main_frame.pack(fill=BOTH, expand=1)
    main_frame.place(x=0,y=0,width=1346,height=685)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")





    for i in range(20):
        Label(second_frame,  text="About us\n", width =300, font=("arial bold ", 30), fg="white", bg="#003153").pack()
        
        Label(second_frame, text="About us", font=("arial bold", 30), bg="#003153", fg="white").place(x=575, y=5)
        Label(second_frame,  text="Developer :- Abhishek kumar mahto\n Developed on :-14/august/2023\n country region:-india\n Hello everyone this is our official website page and this website helps you to select your \ncourses and book your seat for  registration in our institute we provide offline classes in our institute\n this site is only for registration and confirmed your seat\n below you can see our courses details....  ", font=("arial ", 15), bg="#003153", fg="#F0F8FF").place(x=250, y=110)
        
        
        Label(second_frame,  text=" HTML\n The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser.\n It defines the meaning and structure of web content.\n It is often assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.\n Contained by: Web browser Container for: HTML elements \nDeveloped by: WHATWG \nExtended from: SGML \nExtended to: XHTMLInitial\n release: 1993; 30 years ago\nLatest release: Living Standard", font=("arial bold", 13), bg="#003153", fg="#F0F8FF").place(x=10, y=400)
        Label(second_frame, text=" PYTHON\n Python is a high-level, general-purpose programming language.\n Its design philosophy emphasizes code readability with the use of significant indentation.\n Python is dynamically typed and garbage-collected. \nIt supports multiple programming paradigms, including structured, object-oriented and functional programming.\n Designed by: Guido van Rossum \nDeveloper: Python Software Foundation \nFirst appeared: 20 February 1991; 32 years ago \nOS: Windows, macOS, Linux/UNIX, Android and more\n Paradigm: Multi-paradigm: object-oriented, procedural (imperative), functional, structured, reflective \nPreview release: 3.12.0rc1 / 6 August 2023; 1 day ago \nStable release: 3.11.4 / 7 June 2023; 2 months ago", font=("arial bold", 13), fg="#F0F8FF", bg="#003153"). place(x=430, y=700)
        Label(second_frame, text=" TKINTER\n Tkinter is a Python binding to the Tk GUI toolkit.\n It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.\n Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.\nThe name Tkinter comes from Tk interface. \nProgramming language: Python  \nDeveloper: John Ousterhou", font=("arial bold", 13), bg="#003153", fg="#F0F8FF").place(x=10, y=1050)
        Label(second_frame, text="PL/SQL\nPL/SQL is Oracle Corporation's procedural extension for SQL and the Oracle relational database. \nPL/SQL is available in Oracle Database, Times Ten in-memory database, and IBM Db2.\n Oracle Corporation usually extends PL/SQL functionality with each successive release of the Oracle Database", font=("arial bold", 13), bg="#003153", fg="#F0F8FF").place(x=440, y=1300)

                

    # Function to handle the "Save" button click
def logout(): 
    import customtkinter as ctk
    from PIL import Image, ImageTk
    pict=Frame()
    pict.place(x=0,y=0,width=1346,height=685)
    def show_full_image(event):
        global resized_tk
        
        resized_image = image_original.resize((980,680))
        resized_tk = ImageTk.PhotoImage(resized_image)
        canvas.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor = 'center',
            image = resized_tk)

    # grid layout
    pict.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
    pict.rowconfigure(0, weight = 1)

    # import an image 
    image_original = Image.open('python2.jpg')

    image_tk = ImageTk.PhotoImage(image_original)

    python_dark = Image.open('python_dark.png').resize((30,30))
    python_dark_tk = ImageTk.PhotoImage(python_dark)

    img_ctk = ctk.CTkImage(
        light_image = Image.open('python_dark.png'),
        dark_image = Image.open('python_light.png'))


    button_frame = ttk.Frame(pict)
    button = ttk.Button(button_frame, text = 'Home', image = python_dark_tk, compound = "left",command=home)
    button.pack(padx=5,pady=45)

    button_ctk = ctk.CTkButton(button_frame, text = 'Login', image = img_ctk, compound = 'left',command=login1)
    button_ctk.pack(padx=5,pady = 125)

    button_frame.grid(column = 0, row = 0, sticky = 'nsew')


    canvas = tk.Canvas(pict, background = 'black', bd = 1.5, highlightthickness = 1, relief = 'ridge')
    canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')

    canvas.bind('<Configure>', show_full_image)
    

        

    # Function to handle the "Delete" button click
def login1():
    log=Frame(bg="#003153")
    log.place(x=0,y=0,width=1346,height=685)
    def loginmain():
            username1 = username.get()
            password1 = password.get()


            if username1=='' or  password1=='':
                message.set("fill the empty field!!!",) 
        
            else:
            
                try:
                    print("hello")
                    if username1==None:
                        message.set("inavlid user")
                    else:
                        message.set("login successfully")
                    log1()
                    
                    
                            
                    
                        
                except:
                
                    message.set("login not successfully._.", )


        
            
    global message;
    global username
    global password
    username=StringVar()
    password=StringVar()
    message=StringVar()
    lab1=Label(log, width=220, text="Create an user account" ,font=(' arabic bold', 30), fg='orange' , bg="#003153" ).pack()

    username_label = Label(log, text="username:-",font=('arabic bold',22 ), bg="#003153" , fg="white").place(x=95,y=110)
    username_entry = Entry(log, textvariable=username).place(x=260,y=123)


    password_label = Label(log, text="password:-",font=('arabic bold', 22), bg="#003153", fg="white").place(x=95,y=160)

    password_entry =Entry(log, textvariable=password, show="*").place(x=260,y=172)

    Label(root, textvariable=message, font=("arial bold",12),bg="#003153", fg="red").place(x=149, y=210)
    login_button = Button(log, text="Login", command=loginmain, width=8, height=0,bg="gray", fg="white" , font=("arial bold", 10)).place(x=150, y=240)  
    b3=Button(log,text="<-",command=home)
    b3.place(x=2,y=3)

    


    
# Function to handle the "About" button click
def help():
    help1=Frame(bg="#FAFAD2")
    help1.place(x=0,y=0,width=1346,height=685)



    frame=Frame(help1, bg="#003153", height=20)
    frame.pack(side=TOP, fill=X, )
        
    Button(frame, text="home", command=home, fg="white", bg="#003153", font=(10)).pack(side=RIGHT, padx=10, pady=5)
    Label(help1, text="help center", width=300, fg="#383838", bg="#F8F8FF", font=("arial bold ", 40)).pack()

    frame1=Frame(help1, bg="#003153", height=400)
    frame1.pack( fill=BOTH )
    Label(frame1, text="how to create a account? \n", font=("arial bold", 20), bg="#003153", fg="white" ).place(x=40, y=50)
    Label(frame1, text="how to register for courses?\n", font=("arial bold", 20), bg="#003153", fg="white" ).place(x=470, y=50)
    Label(frame1, text="Any other helps pls contact us\n", font=("arial bold", 20), bg="#003153", fg="white" ).place(x=905, y=50)
    Label(frame1, text="you can create your user account easily\n first click on login button and after that\n you can set your username and password\n and than click on the login button below\n your account is created successfully....\n", font=("arial", 15), bg="#003153", fg="white" ).place(x=25, y=110)
    Label(frame1, text="you want to register than you firstly choose\n your course which are available in\n our websites when you select a course\n you have open a page and this is our regisration \npage you filled your details easily here\n and click the register button your\n registration has been succesfully.....\n", font=("arial", 15), bg="#003153", fg="white" ).place(x=450, y=110)
    Label(frame1, text="contact:- +917986846029 \n\n email:- abhi206070@gmail.com", font=("arial ", 15), bg="#003153", fg="white" ).place(x=935, y=120)
    frame2=Frame(help1, bg="#FAFAD2", height=25)
    frame2.pack(side=BOTTOM, fill=BOTH )
    Label(frame2, text="follow us on :- ", font=("arial", 20), bg="#FAFAD2", fg="black").place(x=960, y=2)
    def web():
        print("")
        webbrowser.open("https://www.instagram.com/itzkabhishek/")
    Button(frame2, text="instagram", command=web, fg="white", bg="#003153", font=(10)).pack(side=RIGHT, fill=X , padx=10 ,pady=10 )
    def web1():
        webbrowser.open("https://www.facebook.com/profile.php?id=100027990383100&mibextid=ZbWKwL")
    Button(frame2, text="facebook", command=web1, fg="white", bg="#003153", font=(10)).pack(side=RIGHT, fill=BOTH, padx=20, pady=10)

   
def registration1():
    regi=Frame(bg="#003153")
    regi.place(x=0,y=0,width=1346,height=685)   
    
    
            
    #defining register function
    def register():
        conn = mysql.connector.connect(user='root', password='Ccit@123', host='localhost', database='firstdata')
        #getting form data
        name1=name.get()
        con1=contact.get()
        email1=email.get()
        dob1=dob.get()
        gen1=gender.get()
        city1=city.get()
        state1=state.get()
        #applying empty validation
        if not name1 or not con1 or not email1 or not dob1 or not gen1 or not city1 or not state1:
            message.set("fill the empty field!!!")
            return
        else:
        # Creating a cursor object using the cursor() method
            cursor = conn.cursor()
        # Preparing SQL query to INSERT a record into the database.
        insert_stmt = (
            "INSERT INTO register (NAME, CONTACT, EMAIL, DOB, GENDER, CITY, STATE)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        if gen1==1:
            data = (name1, con1,email1, dob1, "Male",city1,state1)
        else:
            data = (name1, con1, email1, dob1,"Female", city1, state1)
        try:
            #executing the sql command
            cursor.execute(insert_stmt,data)
            #commit changes in database
            conn.commit()
        except:
            conn.rollback()
        message.set("Stored successfully")
        suc()
        

    #defining Registrationform function
    
    global reg_screen
    
    global  message;
    global name
    global contact
    global email
    global dob
    global gender
    global city
    global state
    name = StringVar()
    contact = StringVar()
    email=StringVar()
    dob=StringVar()
    gender=IntVar()
    city=StringVar()
    state=StringVar()
    message=StringVar()
        #Creating layout of Registration form
    Label(regi,width="300", text="Please enter details below", bg="orange",fg="white", font=("italic bold", 15)).pack()
        #name Label
    Label(regi, text="Name * ", bg="#003153",fg="orange",font=("arabic bold",15)).place(x=20,y=40)
        #name textbox
    Entry(regi, textvariable=name).place(x=110,y=45)
        #contact Label
    Label(regi, text="Contact * ", bg="#003153",fg="orange", font=("arabic bold",15)).place(x=20,y=80)
        #contact textbox
    Entry(regi, textvariable=contact).place(x=110,y=82)

        # email Label
    Label(regi, text="Email * ", bg="#003153", fg="orange", font=("arabic bold",15)).place(x=20, y=120)
        # email textbox
    Entry(regi, textvariable=email).place(x=110, y=122)
        
        # dob label
    Label(regi, text="DOB * ", bg="#003153", fg="orange", font=("arabic bold",15)).place(x=20,y=160)
    Entry(regi, textvariable=dob).place(x=110, y=160)

    # gender Label
    Label(regi, text="Gender * ", bg="#003153", fg="orange", font=("arabic bold",15)).place(x=20, y=200)
    # gender radiobutton
    Radiobutton(regi,text="Male",bg="#003153", fg="orange", variable=gender,value=1).place(x=110,y=200)
    Radiobutton(regi, text="Female",bg="#003153", fg="orange", variable=gender, value=2).place(x=180, y=200)

    # city Label
    Label(regi, text="City * ", bg="#003153", fg="orange", font=("arabic bold",15)).place(x=20, y=240)
    # city combobox
    citychoosen = ttk.Combobox(regi, width=27, textvariable=city)
    citychoosen['values'] = (' Mumbai',
                            ' Bhopal',
                            ' Patna',
                            ' Indore',
                            ' Nagpur',
                            ' Motihari',
                            ' Pune',
                            ' Gwalior',
                            ' Jabalpur',
                            'ludhiana')
    citychoosen.current()
    citychoosen.place(x=110,y=241)

    # state Label
    Label(regi, text="State * ", bg="#003153", fg="orange", font=("arabic bold",15)).place(x=20, y=280)
    # state combobox
    statechoosen = ttk.Combobox(regi, width=27, textvariable=state)
    statechoosen['values'] = (' Madhya Pradesh',
                            ' Maharashtra',
                            ' Bihar',
                            ' Punjab',
                            ' Gujrat',
                            ' Rajsthan'
                            )
    statechoosen.current()
    statechoosen.place(x=110, y=280)
   
    Label(regi, text="",textvariable=message, bg="#003153", fg="red", font=("arabic bold",15)).place(x=95,y=310)
    #Login button
    Button(regi, text="Register", width=10, height=1, bg="orange", fg="white", command=register, font=("arabic bold",15)).place(x=120,y=350)


def suc():
    pass1=Frame(bg="orange")
    pass1.place(x=0,y=0,width=1346,height=685)  
    
    Label(pass1, text="Thank You For Registration..", width=300, font=("arabic bold", 20), bg="orange", fg="black" ).pack()
    Label(pass1, text="Your Course Registration is Successfully\n\n\n\n Your Classes has been Started from Next Week... ", bg="orange", fg="black", font=("arial", 15)). place(x=80, y=150)
    frame=Frame(pass1,bg="gray", height=20)
    frame.pack(side=BOTTOM, fill=Y, )
    ttk.Button(frame, text="view record").pack(side=RIGHT)

def log1():
    cour=Frame(bg="#69359c")
    cour.place(x=0,y=0,width=1346,height=685)    
    
    Label(cour, text="Courses Available", font=("arial bold", 20), width=200, fg="white", bg="black").pack()
    def html():
        Label(cour, text="Duration:- 4 weeks\n Time period :- 1.5 hour\n Fee:- 2000", font=("arial bold", 20), bg="#69359c", fg="#FF0000").place(x=203, y=190)
    frame = ttk.Frame(cour, height=20 )
    frame.pack(side=TOP, fill=X)
    Button(frame, text="HTML", command=html, bg="white",  font=("arial bold", 10)).pack(side=LEFT, padx=5, pady=5)
    def python():
        Label(cour, text="Duration:- 4 weeks\n Time period :- 2.5 hour\n Fee:- 4000", font=("arial bold", 20), bg="#69359c", fg="white").place(x=203, y=190)
    Button(frame, text="PYTHON", command=python, bg="white", font=("arial bold", 10)).pack(side=LEFT, padx=10, pady=5)
    def tkinter():
        Label(cour, text="Duration:- 4 weeks\n Time period :- 2.5 hour\n Fee:- 6000",font=("arial bold", 20),  bg="#69359c", fg="#00FF00").place(x=203, y=190)
    Button(frame, text="TKINTER", command=tkinter, bg="white",  font=("arial bold", 10)).pack(side=LEFT, padx=10, pady=5)
    def plsql():
        Label(cour, text="Duration:- 4 weeks\n Time period :- 1.5 hour\n Fee:- 6000", font=("arial bold", 20),  bg="#69359c", fg="orange").place(x=203, y=190)
    Button(frame, text="PL/SQL", command=plsql, bg="white",  font=("arial bold", 10)).pack(side=LEFT, padx=10, pady=5)
    def chose():
        print("choose")
        bok()
    Button(frame, text="SELECT COURSE", command=chose, bg="white",  font=("arial bold", 15)).pack(side=RIGHT, padx=5, pady=5)
    
def bok():
    bok1=Frame(bg="#003153")
    bok1.place(x=0,y=0,width=1346,height=685)    
    Label(bok1, text="BOOK COURSES" ,width=300, fg="white", bg="#003153", font=("italic bold ", 30)).pack()
    def htm():
        print("")
        registration1()
        
    Button(bok1, text="HTML", command=htm , font=("arial", 20), bg="orange" ).pack(side=LEFT)
    Button(bok1, text="PYTHON", command=htm ,font=("arial", 20) , bg="orange").pack(side=RIGHT)
    Button(bok1, text="TKINTER", command=htm ,font=("arial", 20), bg="orange" ).pack(side=BOTTOM)
    Button(bok1, text="PL/SQL", command=htm ,font=("arial", 20), bg="orange" ).pack(side=TOP)

def suc():
    succ=Frame(bg="orange")
    succ.place(x=0,y=0,width=1346,height=685) 

    Label(succ, text="Thank You For Registration..", width=300, font=("arabic bold", 20), bg="orange", fg="black" ).pack()
    Label(succ, text="Your Course Registration is Successfully\n\n\n\n Your Classes has been Started from Next Week... ", bg="orange", fg="black", font=("arial", 15)). place(x=80, y=150)
    frame=Frame(succ,bg="gray", height=20)
    frame.pack(side=BOTTOM, fill=Y, )
    ttk.Button(frame, text="view record").pack(side=RIGHT)


def home():
    task_bar1 = tk.Frame(bg="#091e42")
    task_bar1.place(x=0,y=0,width=1346,height=685)


    task_bar = tk.Frame(task_bar1,bg="#091e42")
    task_bar.pack(side=tk.TOP, fill=tk.X)
    

    new_button = tk.Button(task_bar, text="About", command=About )
    new_button.pack(side=tk.LEFT, padx=5, pady=5)


    save_button = ttk.Button(task_bar, text="logout", command=logout)
    save_button.pack(side=tk.RIGHT, padx=5, pady=5)

    delete_button = ttk.Button(task_bar, text="login", command=login1)
    delete_button.pack(side=tk.RIGHT, padx=5, pady=5)

    # Create a footer bar
    footer_bar = tk.Frame(root, bg="#003153", height=30)
    footer_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # Create the "About" button and add it to the footer bar
    about_button = ttk.Button(footer_bar, text="help", command=help)
    about_button.pack(side=tk.RIGHT, padx=10)
    def time():
        print("show time")
        import watch
    ttk.Button(footer_bar, text="time", command=time, ).pack(side=tk.RIGHT, padx=10)

    # Create the label to display the footer text
    about_label = tk.Label(footer_bar, text="welcome", fg="white", bg="#003153")
    about_label.pack(side=tk.LEFT)
    
    class App:
	    def __init__(self, master) -> None:

		# Instantiating master i.e toplevel Widget
		    self.master = master

		    Label(self.master, text="Course Academy Ludhiana",bg="#091e42",fg="white",font=("Arial", 25)).pack()
    app=App(root)
        
    


home()
root.mainloop()
