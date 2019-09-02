#Hagman 1.1
#Once per run working beta
#Made by Aleksa Crveni
#Sredi globale gde ne treba
#Resi resetovanje txtboxa
import tkinter
from tkinter import * 
 # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import messagebox
top = tkinter.Tk()
top.geometry("600x650") #velicina prozora
#button click funckija
index =0#index za funkcije
game_start = False #boolean koji se proverava prilikom input_btn klika
hidden_word ='' #ovde se storuje skrivena rec
x_Slova = 20 #x koordinate za slova koja su iskoriscena
y_Slova = 450#y koordinate za slova koja su iskoriscena
final_word_guess = 3 #broj pkusaja za finalnu rec
C = Canvas(top, bg = "White", height = 590, width = 600) #pravljenje kanavsa sa crtanje
used_chars = [] #lista za koriscene karaktere
label_dict = {} #dicionary za skrivenu rec i labele
#label['text'] = 'Test1' menjanje teksta u labelu
word_len=0 #poveceava se kada pogodis slovo u reci(broj pogodjenih slova)
slovo =''
#_input_btn click event
def btnClick():  
    if(game_start == True): #proverava da li je skrivena rec zadata
        slovo1 = str(txt_box.get()) #slovo/rec koju korisnik unosi da pogodi
        slovo = str(slovo1.upper())            
        if(slovo.isalnum):
            if(len(slovo) >0 and len(slovo) == 1):#proverava da li je rec ili slovo #zameni test sa slovom da ne moram stalno da pozivam upper() ,proveri da li je broj...           
                if(slovo not in used_chars):#ako slovo nije iskoriceno vec    
                    global x_Slova
                    global y_Slova
                    global final_word_guess
                    global label_dict
                    global word_len
                    global hidden_word
                    #ovo radi samo zameni ifelse
                    if(slovonot in hidden_word):#ako slovo nije u trazenoj reci
                        global index
                        funcList[index]() #pozivanje funkcije za isctavanje
                        index += 1      
                        C.create_text(x_Slova,y_Slova,anchor=W,text=slovo.upper())#ispisvanje slova na kanvasu
                        x_Slova += 10 #pomeranje pozicije slova
                        used_chars.append(slovo)#dodavanje u listu iskoriscenih slova
                        if(x_Slova >= 220):#pomeranje u novi rec
                            y_Slova += 15
                            x_Slova = 20
                        if(index == 7):#proverava da li je iscrtan hangman
                            messagebox.showinfo('Obavestenje!','Kraj igre')      
                    else:#ako je slovo u trazenoj reci    
                        for key in label_dict:#prolazi kroz kljuceve u dictionariju(labele)
                            if(label_dict.get(key) == slovo):#uzima key sa tim slovom
                                key['text'] = slovo#ispisiuje slovo
                                word_len +=1#poveceava broj pogodnjenih slova
                                if(word_len == len(hidden_word)): #kada pogodis rec
                                    messagebox.showinfo('Obavestenje','Kraj igre')                                
                        C.create_text(x_Slova,y_Slova,anchor=W,text=slovo)#isctavanje slova
                        x_Slova += 10#pomeranje
                        used_chars.append(slovo)#dodavanje u listu
                        if(x_Slova >= 220):#pomeranje u novi red
                            y_Slova += 15
                            x_Slova = 20
                else:#ako je slovo vec iskoriceno
                    messagebox.showinfo('Obavestenje','Slovo iskorisceno')
                #pogadjanje finalne reci
            elif(len(slovo) >1):#ako je koirsinik uneo rec
                if(final_word_guess > 0): #ako ima jos pokusaja da pogodi celu rec
                    final_word_guess -= 1 #smanjuje broj pokusaja
                    if(slovo == hidden_word): #ako je pogodio
                        for key in label_dict: #prolazanje kroz dict uz pomoc kljuceva
                            key['text'] = label_dict[key] #ispisavanje reci
                        messagebox.showinfo('Obavestenje','Pogodili ste trazenu rec!')
                                #reset logika ovde ide
                    elif(slovo != hidden_word): #ako rec nije trazena rec
                        messagebox.showinfo(f'Obavestenje','Trazena rec nije '+ str(slovo) + '\nOstalo vam je jos ' + str(final_word_guess) + ' pokusaja')
                else:#ako nema presoalih pokusaja
                    messagebox.showinfo('Obavestenje','Iskoristili ste sve pokusaje za finalnu rec')
            else: #ako dugme pritisnuto sa praznim texboom
                messagebox.showinfo('Obavestenje','Unesite zeljeno slovo')
        #ako unesna rec/slovo sadrzi broj/cifru
        else:
            messagebox.showinfo('Unesena rec/slovo ne sme da sadrzi broj')
    else: #ako pokusa da unese slovo bez sakrivene reci unesene
        messagebox.showinfo('Obavestenje','Morate uneti skrivenu rec prvo!')

input_btn = Button(top ,text = "Unesi", command = btnClick)# input btn
 #prozor,text,pozivanje funkcije na klik(prakticno pravljenje eventa)
input_btn.place(x = 435,y = 615)
input_btn.width=50 
txt_box_label = Label(top,text='Vase slovo/rec:')#label za input txtbox
txt_box_label.place(x=300, y=597)
txt_box = Entry(top,text = 'Chose a charakter') #input txtbox
txt_box.place(x = 300, y = 620)#pozicija

def ResetButtonClick():
    global index
    global game_start
    global hidden_word
    global x_Slova
    global y_Slova
    global final_word_guess
    global used_chars
    global label_dict
    global word_len
    global C
    global x_Labela
    global slovo
    slovo =''
    index =0#index za funkcije
    game_start = False #boolean koji se proverava prilikom input_btn klika
    hidden_word ='' #ovde se storuje skrivena rec
    x_Slova = 20 #x koordinate za slova koja su iskoriscena
    y_Slova = 450#y koordinate za slova koja su iskoriscena
    final_word_guess = 3 #broj pkusaja za finalnu rec
    
    for key in label_dict:
        key.destroy() #kompetno unistavnje labela
    
    used_chars.clear() #lista za koriscene karaktere
    label_dict.clear()  #dicionary za skrivenu rec i labele
    print(len(label_dict))
    #prodji kroz lib i obrisi sve kljuceve
    #label['text'] = 'Test1' menjanje teksta u labelu
    word_len=0 #poveceava se kada pogodis slovo u reci(broj pogodjenih slova)
    C.delete('all') #ciscenje kavnas
    DrawStart()
    C.pack()
    x_Labela = 40
    messagebox.showinfo('Obavestenje','Igra uspesno resetovana')

reset_btn = Button(top,text='Reset', command = ResetButtonClick ) #reset btn
reset_btn.place(x = 500, y = 615)
reset_btn_label = Label(top,text='Resetuj igru')
reset_btn_label.place(x = 500, y=597)
x_Labela = 40#x koordinate za postavljanje labela
#start btn click event
def StartGame():
    #start game logic 
    test = str(hidden_word_txtbox.get()) #uzimanje inputa
    if(len(test) > 1): #proveravanje da li je rec
        global hidden_word
        hidden_word = test.upper()
        global game_start
        game_start = True #postavnjae game_starta na true
        messagebox.showinfo('Obavestenje','Rec sacuvana!')
        global label_dict
        
        for i in range(len(hidden_word)): #pravljenje laebla
            global x_Labela          
             #x koorde
            y_Labela = 400#y lkoorde
            name = Label(top,text='_') #pravljenje labela
            name.place(x=x_Labela,y=y_Labela) #koordiante labela
            label_dict[name] = hidden_word[i] #unosenje labela sa vrednoscu
            x_Labela += 18
        #tip: nazivi labela su automatski generisani pocinju sa .!label , .!label2..
    else:#ako nije rec
        messagebox.showinfo('Obavestenje','Rec mora biti duza od jednog slova')

hidden_word_txtbox = Entry(top) #hidden word txbox
hidden_word_txtbox.place(x=20,y=620)
start_btn = Button(top,text='Start',command= StartGame)#start btn 
start_btn.place(x=150,y=615)
hidden_word_txtbox_label = Label(top,text='Skrivena rec:')#hidden word label
hidden_word_txtbox_label.place(x=20,y=597)


#test func   
def DrawShape(self,index):
    self.create_line(40,40,200,30,fill='black')
    #self je objekat koji pasujem sa kojim mogu da radim sta hocu 
#iscrtavanje postolja
def DrawStart():
    C.create_line(20,20,150,20,width=2,fill='black') #x1,y1,x2,y2
    C.create_line(150,20,150,40,width=2,fill='black')
#isctavanje glave
def DrawHead():
    C.create_oval(120,40,180,100,width=2,outline='black')#gornji levi  i donji desni ugao ,glava
    C.create_oval(138,60,146,68,fill='black')#levo oko
    C.create_oval(154,60,162,68,fill='black')#desno oko   
#iscrtavanje vrata
def DrawNeck():
    C.create_line(150,100,150,140,width=2,fill='black')#vrat
#iscrtavanje tela
def DrawBody():
    C.create_line(150,140,150,250,width=2,fill='black')#telo
#isctavanje leve ruke 
def DrawLArm():
    C.create_line(150,140,90,200,width=2,fill='black')#leva ruka
def DrawRArm():
    C.create_line(150,140,210,200,width=2,fill='black')#desna ruka
def DrawRLeg():   
    C.create_line(150,247,100,350,width=2.5,fill='black')#desna noga
def DrawLLeg():
    C.create_line(150,247,200,350,width=2.5,fill='black')#leva noga    
funcList = [DrawHead,DrawNeck,DrawBody,DrawLArm,DrawRArm,DrawLLeg,DrawRLeg]#lista funkcija za iscrtavanje




DrawStart()
C.pack()
top.mainloop() #poziva mainloop

