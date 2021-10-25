class Quiz:
    def __init__(self,question, alt, correct):
        self.question = question
        self.alt = alt
        self.correct = correct
        self.s =""
        for a in range(len(self.alt)):
            self.s =self.s+str(a+1)+". "+self.alt[a]+"\n" 
            
    def corect_ansrer_txt(self):
        print("correct anser is: "+self.alt[self.correct-1])
           
    def __str__(self):
        return "{self.question}\n{self.s}".format(self=self)
  
if __name__=="__main__":    
    file = open("C:/Users/bmm1/Dat120_Ovning9/Øving 9 Prosjekt del 1/sporsmaalsfil.txt", encoding="UTF8") 
    Qst = []
    Correct = []
    alt = []
    altL = {}   
    Score1 = 0
    Score2 = 0       
# Split all the diffrent parts of the questions from  the text file into lists             
    for line in file:
            end = line.find(":")
            Qst.append(line[0:end])
            Correct.append(int(line[end+2:end+3])+1)
            Start_alt = line.find("[")
            End_alt = line.find("]")
            alt.append(line[Start_alt+1:End_alt])
    file.close()
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
            altL[q+1,b+1] = [str_alt[dot[b]+2:dot[b+1]]]
        list1 = []
        for t in range(len(dot)-1):
            str_altL=altL[q+1,t+1]
            list1 = list1 + str_altL
        Qst1= Quiz(Qst[q], list1, Correct[q])
        print(Qst1)
        lenD = len(dot)-1
        anser1 = int(input(f"Player 1 select anser from 1 to {lenD} \n"))
        anser2 = int(input(f"Player 2 select anser from 1 to {lenD} \n"))
        Qst1.corect_ansrer_txt()
        if anser1 == Correct[q]:
            Score1+=1
            Txt1 = "Correct"
        else: 
            Txt1 = "Wrong"
        if anser2 == Correct[q]:
            Score2+=1
            Txt2 = "Correct "
        else: 
            Txt2 = "Wrong"
        print(f"\nPlayer 1: {Txt1}")
        print(f"Player 2: {Txt2} \n")
    print(f"Score player 1:{Score1}")    
    print(f"Score player 2:{Score2} \n") 
    if Score1>Score2 :
        print("Player 1 won")
    elif Score1<Score2:
        print("Player 2 won")
    else:
        print("It's a tie!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        