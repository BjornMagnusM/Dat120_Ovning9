
class Quiz:
    def __init__(self,question, alt1, alt2, alt3, alt4, correct):
        self.question = question
        self.alt1 = alt1
        self.alt2 = alt2
        self.alt3 = alt3
        self.alt4 = alt4 
        self.correct = correct


    def check_anser(self, anser):
       self.anser = anser
       score = 0
       if anser == self.correct:
           score += 1
           print("Correct \n")
           print("score:",score)
       elif anser > 4 or anser <1 :
           print("you can only anser 1,2,3 or 4 ")
       else:
           print("Wrong \n")
    def __str__(self):
        return " {self.question} \n 1. {self.alt1} \n 2. {self.alt2} \n 3. {self.alt3} \n 4. {self.alt4}".format(self=self)
     
QST1 = Quiz("Whats the capitalt of Norway", "Bergen", "Oslo", "Stavanger", "Trondheim", 2)
QST2  = Quiz("what is the number 1001 form binary to the decimal system", "17", "14", "5","21",1)

print ("Question 1")
print(QST1)
anser1 = int(input("Select anser from 1 to 4 \n"))
QST1.check_anser(anser1)

print ("Question 2")
print(QST2)
anser2 = int(input("Select anser from 1 to 4 \n"))
QST2.check_anser(anser2)






