file = open("C:/Users/bmm1/Dat120_Ovning9/Øving 9 Prosjekt del 1/sporsmaalsfil.txt", encoding="UTF8") 
Qst = []
Correct = []
alt = []
alt0 =[]
class Quiz:
    def __init__(self,question, alt, correct):
        self.question = question
        self.alt = alt
        self.correct = correct
        self.s =""
        for a in range(len(self.alt)):
            self.s =self.s+str(a+1)+" "+self.alt[a]+"\n" 

    def check_anser(self, anser):
       if anser == self.correct:
           print("Correct \n")
       else:
           print("Wrong \n")
    
    def corect_ansrer_txt(self):
        print("correct anser is: "+self.alt[self.correct-1])
           
    def __str__(self):
        return "{self.question}\n{self.s}".format(self=self)
   
# Split all the diffrent parts of the questions from  the text file into lists             
for line in file:
        end = line.find(":")
        Qst.append(line[0:end])
        Correct.append(line[end+2:end+3])
        Start_alt = line.find("[")
        End_alt = line.find("]")
        alt.append(line[Start_alt+1:End_alt])
            
file.close()


if __name__=="__main__":
    for q in range(len(Qst)):
        str_alt = alt[q]
        find = 0
        dot = []
        dot.append(-2)
        while find != -1:
            find = str_alt.find(",",find+1)
            dot.append(find)
        dot.pop()
        dot.append(len(str_alt))
        for b in range(len(dot)-1):
            alt0.append(str_alt[dot[b]+2:dot[b+1]])    
        alt0.append(q+2)
    Qst1= Quiz(Qst[q], alt0, Correct[q])
    
n =1
['strg%s' % n] = 'Hello'    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    