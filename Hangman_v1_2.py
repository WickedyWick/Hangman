#Hagman 1.2
#Fixed bugs from 1.1
 #top.withdraw() #hidujem window
 # self.root.update() za show
 # self.root.deiconify() -||-
import tkinter
from tkinter import * 
 # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import messagebox
import time

top = tkinter.Tk()
top.geometry("600x650") #window size

index =0#index used for drawing functions
game_start = False #true if game started , false otherway
hidden_word ='' #hidden word
x_Slova = 20 #x coords for used letters
y_Slova = 450#y coords for used letters
final_word_guess = 3 #number of tries for final word
C = Canvas(top, bg = "White", height = 590, width = 600) #making canvas
used_chars = [] #list for used letter
label_dict = {} #dicionary for hidden_world key=label value=letter
#label['text'] = 'Test1' menjanje teksta u labelu
word_len=0 #used to track if all letters are used
slovo ='' #letters are stored here

#_input_btn click event
def btnClick():  
    if(game_start == True): #checks if game started
        slovo1 = str(txt_box.get()) #guessed letter/word
        slovo = str(slovo1.upper())          
        if(slovo.isalnum()):
            if(len(slovo) >0 and len(slovo) == 1):          
                if(slovo not in used_chars):#if letter is not used before
                    global x_Slova
                    global y_Slova
                    global final_word_guess
                    global label_dict
                    global word_len
                    global hidden_word
                    if(slovo not in hidden_word):#if letter is not in hidden word
                        global index
                        funcList[index]() #drawing part of the hangman
                        index += 1      
                        C.create_text(x_Slova,y_Slova,anchor=W,text=slovo.upper())#drawing used letter 
                        x_Slova += 10 
                        used_chars.append(slovo)#adding to used letter list
                        if(x_Slova >= 220):
                            y_Slova += 15
                            x_Slova = 20
                        if(index == 7):#checks if hangman is fully draw
                            messagebox.showinfo('INFO!','Game over!')      
                    else:#if letter is in hidden word
                        for key in label_dict: #iterating tru label dictionary
                            if(label_dict.get(key) == slovo):#checks for letter
                                key['text'] = slovo#drawing letter
                                word_len +=1
                                if(word_len == len(hidden_word)): #chekcs if all letters are guessed
                                    messagebox.showinfo('INFO!','Game over!')                                
                        C.create_text(x_Slova,y_Slova,anchor=W,text=slovo)#drawing used letter
                        x_Slova += 10
                        used_chars.append(slovo)#adding to used letter list
                        if(x_Slova >= 220):
                            y_Slova += 15
                            x_Slova = 20
                else:#if letter is used already
                    messagebox.showinfo('INFO!','Letter used already')
            #if user guessed whole word
            elif(len(slovo) >1):
                if(final_word_guess > 0): #checks if user has any guesses left
                    final_word_guess -= 1
                    if(slovo == hidden_word): #if he got the right word
                        for key in label_dict: 
                            key['text'] = label_dict[key] #showing whole word
                        messagebox.showinfo('INFO!','You guessed the right word!')
                    elif(slovo != hidden_word): #if he didnt get the right word
                        messagebox.showinfo(f'INFO!','Hidden word is not '+ str(slovo) + '\nYou have left ' + str(final_word_guess) + ' guesses')
                else:#if user used all final word guesses
                    messagebox.showinfo('INFO!','You used all final word guesses')
            else: #if button is clicked with empty textbox
                messagebox.showinfo('INFO!',' Guess textbox must not be empty!')
        #if guess word has number
        else:
            messagebox.showinfo('INFO!','Your guess must not contain number')
    else: #if user tries to guess when game didnt start
        messagebox.showinfo('INFO!','You must enter hidden word first!')

input_btn = Button(top ,text = "Unesi", command = btnClick)# input btn
input_btn.place(x = 435,y = 615)
input_btn.width=50 
txt_box_label = Label(top,text='Your guess')#input txtbox label
txt_box_label.place(x=300, y=597)
txt_box = Entry(top,text = 'Chose a charakter') #input txtbox
txt_box.place(x = 300, y = 620)

#reset button click event
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
    index =0
    game_start = False 
    hidden_word ='' 
    x_Slova = 20 
    y_Slova = 450
    final_word_guess = 3 
    for key in label_dict:
        key.destroy() 
   
    used_chars.clear() 
    label_dict.clear()  
    word_len=0 
    C.delete('all') 
    DrawStart()
    C.pack()
    x_Labela = 40
    messagebox.showinfo('INFO!','Game reset successful')

reset_btn = Button(top,text='Reset', command = ResetButtonClick ) #reset btn
reset_btn.place(x = 500, y = 615)
reset_btn_label = Label(top,text='Resetuj igru')
reset_btn_label.place(x = 500, y=597)
x_Labela = 40#x coors for labels

#start btn click event
def StartGame():
    #start game logic 
    test = str(hidden_word_txtbox.get()) 
    if(len(test) > 1): #checking if input is word
        global hidden_word
        hidden_word = test.upper()
        global game_start
        game_start = True 
        messagebox.showinfo('INFO!','Hidden word saved!')
        global label_dict
        #creating labels for hidden word letters and pairing values and labels in dict
        for i in range(len(hidden_word)): 
            global x_Labela          
            y_Labela = 400#y coors of labels
            lbl = Label(top,text='_') #creating label
            lbl.place(x=x_Labela,y=y_Labela) 
            label_dict[lbl] = hidden_word[i] #pairing labels and values
            x_Labela += 18     
    else:#if input isn't word
        messagebox.showinfo('INFO!','You must enter word!')

hidden_word_txtbox = Entry(top) #hidden word txbox
hidden_word_txtbox.place(x=20,y=620)
start_btn = Button(top,text='Start',command= StartGame)#start btn 
start_btn.place(x=150,y=615)
hidden_word_txtbox_label = Label(top,text='Skrivena rec:')#hidden word label
hidden_word_txtbox_label.place(x=20,y=597)


#test func   
def DrawShape(self,index):
    self.create_line(40,40,200,30,fill='black')
#drawing stand
def DrawStart():
    C.create_line(20,20,150,20,width=2,fill='black') #x1,y1,x2,y2
    C.create_line(150,20,150,40,width=2,fill='black')

def DrawHead():
    C.create_oval(120,40,180,100,width=2,outline='black')
    C.create_oval(138,60,146,68,fill='black')
    C.create_oval(154,60,162,68,fill='black') 

def DrawNeck():
    C.create_line(150,100,150,140,width=2,fill='black')

def DrawBody():
    C.create_line(150,140,150,250,width=2,fill='black')
def DrawLArm():
    C.create_line(150,140,90,200,width=2,fill='black')
def DrawRArm():
    C.create_line(150,140,210,200,width=2,fill='black')
def DrawRLeg():   
    C.create_line(150,247,100,350,width=2.5,fill='black')
def DrawLLeg():
    C.create_line(150,247,200,350,width=2.5,fill='black')
funcList = [DrawHead,DrawNeck,DrawBody,DrawLArm,DrawRArm,DrawLLeg,DrawRLeg]#draw function list



DrawStart()
C.pack()
top.mainloop() #poziva mainloop

