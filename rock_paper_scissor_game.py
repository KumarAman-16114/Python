import random
l=['rock','paper','scissor']
while True:
    ucount=0
    ccount=0
    print()
    name= input("Enter your name : ")
    ucc=int(input('''
                 Do You Want to play the Game......
                 1. YES
                 2. NO / EXIT\n'''))
    round = int(input("Enter rounds to play : "))
    if ucc==1:
        for i in range(round):
            print('''Select 
                    1. rock
                    2. paper
                    3. scissor\n
                    '''
                  )
            userinput=int(input("Choice : "))
            if userinput==1:
                uc='rock'
            elif userinput==2:
                uc='paper'
            elif userinput==3:
                uc='scissor'
            else:
                print("Invalid choice")
            cc = random.choice(l)
            if cc==uc:
                print(name,"enetered : ",uc)
                print("Computer enetered : ",cc)
                print("Match Tied")
                ucount += 1
                ccount += 1
            # users winning cases
            elif (uc == "rock" and cc == "scissor")or(uc == 'paper' and cc == 'rock')or(uc == 'scissor' and cc =="paper"):
                print("Computer enetered : ",cc)
                print(name,"enetered : ",uc)
                print(name,"Won and Computer Loose")
                print("Better Luck next time....")
                ucount+=1
            # elif (userinput=='rock' and cc == 'paper') or (userinput=='paper' and cc == 'scissor') or (userinput=='scissor' and cc == 'rock'):
            else:
                print(name,"enetered : ",uc)
                print("Computer enetered : ",cc)
                print("Computer Won....",name,"Loose")
                ccount+=1
        if ucount==ccount:
                print("Final Match draw")
                print("Total score of Computer : ",ccount)
                print("Total score  of",name,":" ,ucount) 
        elif ucount>ccount:
                print("You Won the Final Match")
                print("Total score of Computer : ",ccount)
                print("Total score  of",name,":" ,ucount) 
        else:
            print("Final Match won by Computer")
            print("Total score of Computer : ",ccount)
            print("Total score  of",name,":" ,ucount)  
    else:
        break             
            