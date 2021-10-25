file = open("C:/Users/bmm1/Dat120_Ovning9/Øving 9 Prosjekt del 1/sporsmaalsfil.txt", encoding="UTF8") 
Qst = []
Correct = []
alt = []
alt0 = {}
   
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
            alt0[alt[dot[0]:dot[8]]] = [1]
    
    
    
    
    
    