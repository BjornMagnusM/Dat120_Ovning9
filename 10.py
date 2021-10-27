class Quiz:
    def __init__(self,question, alt, correct):
        self.question = question
        self.alt = alt
        self.correct = correct
        self.s =""
        for a in range(len(self.alt)):
            self.s =self.s+str(a+1)+". "+self.alt[a]+"\n" 
    def corect_ansrer_txt(self):
        return "correct anser is:{self.alt[self.correct-1]}".format(self=self)
    def __str__(self,*args,**kwargs):
        return "{self.question}\n{self.s}".format(self=self)

class Player: 
    def __init__(self,name,Score):
        self.score=0
        self.name=name
    def Correct(self):
        self.score+=1
    def Print_Score(self):
        print(f"{self.name} score is {self.score}")  
        return self.score        
    def __str__(self):
        return "{self.name}".format(self=self)
    
def Add_players(Player_Nr):
    List_of_players=[]
    for l in range(Player_Nr):
        p=Player(input(f"Player{l+1}s name?"),0)
        List_of_players.append(p)
    return List_of_players   

if __name__=="__main__":    
    file = open("C:/Users/bmm1/Dat120_Ovning9/sporsmaalsfil.txt", encoding="UTF8")  
    Nr_players = int(input("Select number of players"))
    PlayerL = Add_players(Nr_players)
    ScoreL = []
    
    for line in file:
        line = line.replace("[", "").replace("]","")
        Qst_Ans = line.split(":")
        Alt = Qst_Ans[2].replace(" ","").split(",")
        Qst_Ans.pop()
        int(Qst_Ans[1])
        CorrectWrongL = []
        Qst= Quiz(Qst_Ans[0], Alt, Qst_Ans[1])
        print(Qst)
        for a in range(Nr_players):
            anser = int(input(f"{PlayerL[a]} select your anser"))
            Correct = int(Qst_Ans[1])
            if anser == Correct+1:
                PlayerL[a].Correct()
                CorrectWrongL.append("Correct")
            else:
                CorrectWrongL.append("Wrong")
        print(f"Correct anser is {Alt[Correct]}")
        for z in range(len(CorrectWrongL)):
            print(f"{PlayerL[z]}'s anser is {CorrectWrongL[z]}")
        print("")
    for d in range(len(PlayerL)):
        SL = PlayerL[d].Print_Score()
        ScoreL.append(SL)
    max_value = max(ScoreL)
    max_index = ScoreL.index(max_value)
    print(f"{PlayerL[max_index]} won")














    