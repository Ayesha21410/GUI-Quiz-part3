from tkinter import *

#We will need this when we create our randomiser method that will pick up questions randomly
import random

names_list = [] 
#global variable questions_answers  will hold both questions and their answers and create our questions and answers dictionary key and value
global questions_answers
#asked list variable, so each time a question is displayed in the quiz, its added to it, so randomiser method does not duplicate it.
asked = []



# Dictionary has key of numbers (for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers  = {
    1: ["What must you do when you see blue and red flashing lights behind you?", 
        #item 1, index 0 is the question 
        'Speed up to get out of the way', # item 2, index 1 will be first choice
        'Slow down and drive carefully', # item 3, index 2 will be second choice
        'Slow down and stop', # item 4, index 3 will be third choice
        'Drive on as usual', # item 5, index 4 will be fourth choice
        'Slow down and stop' #item 6, index 5 will be the right answer statement we need to display the right statement if the user enters wrong choice 
        ,3], #item 7, index 6 will be the positionof the right answer (index where right  right answer sits),this will be our check if answer is correct or no


    2: ["You may stop on a motorway only:",'if their is an emergency','To let down or pickup pssenger', 'to mak a U-turn','to stop and take a photo','if their is an emergency',1],
  
    3: ["When coming up to the padestrian crossong without a rasied traffic island,what must you do? :",'Speed up before padestrians cross','Stop and give way to padestrian to any part of the crossing', 'Sound the horn on your vehicle to warn the padestrians','Slow down to 30kmh','Stop and give way to padestrian to any part of the crossing',2],
  
    4: ["Can you stop on a bus stop in a private motor vehicle?",'only between midnight and 6am','Under no circumstances', 'When drooping off pasenger','Only if it is less than 5 minutes','Under no circumstances',2],
    
    5: ["What is the maximum speed you may drive i9f you have a 'space saver wheel' fitted? (km/h) ",'70km/h','100km/h so you do not hold up traffic', '80km/h and if the wheel spacer displays a lower limit that appplies','90km/h','80km/h and if the wheel spacer displays a lower limit that appplies',3],
    
    6: ["When folllowing another vehicle on a dusty road you should:",'Speed up to get passed','Turn your vehicles windscreeen wipers on', 'Stay back from the dust cloud','Turn you vehicles heighlights on','Stay back from the dust cloud',3],
  
    7: ["What does the sign contaning letters LSZ mean:",'Low safety zone','Low stability zone', 'Low star zone','Limited speed zone','Limited speed zone',4],

    8: ["What the speed you are allowed to pass a school bus that has stooped to let stuedents get on or off?",'20km/h','30km/h', '70km/h','10km/h','20km/h',1],

    9: ["What is the maximum distance a load may extend infront of the car?",'2 meters forward of the front edge of the front seat','4 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat','2.5 meters foeward of the front edge of the front seat','3 meters forward of the front edge of the front seat',3],
    
    10: ["To avoid being blinded by the heighlights of another vahicle coming forwards you what should you do?",'Look to the left of the road','Look to the center of the road', 'Look to the right of the road','Keep your eyes closed','Look to the left of the road',1]

}

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif  qnum not in asked:
         randomiser()
  
  
  

  

  
    
  
  
  
    
#class QuizStarter to start the Quiz by taking the participant’s name and storing it in a list, will contain frame, label, entry and button widgets

class QuizStarter:
    def __init__(self, parent):
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent, 
        bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()
      
        #label widget for our heading
        self.heading_label= Label(self.quiz_frame, 
        text="NZ Road Rules", bg=background_color)
        self.heading_label.grid(row=0)
        
        #Label for user name prompt
        self.user_label= Label(self.quiz_frame, 
        text="Please enter your name below:",
        bg=background_color)
        self.user_label.grid(row=1)

        #users input is taken by an Entry widget
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)
        #continue button
        self.continue_button= Button(self.quiz_frame, 
        text="continue", bg="pink",command= 
        self.name_collection)
        self.continue_button.grid(row=3,pady=20)
      
    def name_collection(self):
      name=self.entry_box.get()
      names_list.append(name)
      print(names_list)
      self.quiz_frame.destroy()
      Quiz(root)
class Quiz:
   def __init__(self, parent):
        #color selection
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent, 
        bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        #call randomiser before listing questions
        randomiser()
        #questions
        self.question_label=Label(self.quiz_frame, text= questions_answers[qnum][0], font=("Tw Cen MT","16"),bg=background_color)
        self.question_label.grid(row=0, padx=10,pady=10)

        #Hold the value of Radio buttons
        self.var1=IntVar()
        
        #Radiobutton1
        self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
        self.rb1.grid(row=1, sticky=W)
      #Radiobutton2
        self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
        self.rb2.grid(row=2, sticky=W)
     #Radiobutton3
        self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
        self.rb3.grid(row=3, sticky=W)
     #Radiobutton4
        self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
        self.rb4.grid(row=4, sticky=W)

     
     #confirm button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="pink")
        self.confirm_button.grid(row=5)
     
     

        
     
  


#*******Starting point of program *******#

if __name__=="__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root) #instantiation, making an instance of the class QuizStarter to create the frame with its widget, passing root as j 
    root.mainloop()#so the window doesnt dissappear

