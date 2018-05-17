

#---------------------------Menu---------------------------

option = "string"

while option != "3":
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")
        
      
    
    option = input("Please choose an option:")
        
        
    if option == "1":
        f  = open('questions.txt', 'r')
        lines = f.read().split('\n')
        f.close()
        
        score = 0
        
        for line in lines[:-1]:
            question,answer= line.split("|")
            guess = input(question)
            if guess == answer:
                print("You're right :-)")
                score += 1
                print("Your score is: ")
                print(score)
                
                
            else:
                print("You're wrong!")
        
    
        
    if option == "2":
        question = input("Please type the question that you want to add: \n")
        answer = input("Please type the answer you want to add: \n")
        setString = question + "|" + answer + "\n"
            
        f  = open('questions.txt', 'a')
        f.write(setString)
        f.close()
            
    
      
            
        
        
    
