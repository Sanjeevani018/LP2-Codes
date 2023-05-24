print("Hi,I'm Chatty Yor CareerCounselling Chatbot /n I will help you Choose best branch For you after 12")
print("Select the Stream You are Intrested in: ")
def menu():
    print("1. Science")
    print("2. Comerce")
    print("3. Diploma")
    print("4. Arts")
menu()
option=(int(input("Enter your Option")))
while option!=0:
        if option==1:
           print("great choice: you can go further for engineering or medical")
           break;
        elif option==2:
          print("great choice: you can go for BCOM ,CA,CS,BBA can be a good concern option for you")
          break;
        elif option==3:
          print("great choice:you can do any kind of engineeringDiploma,Fashion Design Diploma,Biotech,food tech and any kind of Architecture etc.")
          break;
        elif option==4:
          print("great choice: Sociology,BA,BMS,BHM")
          break;
        else:
          print("Invalid")
          break;
        
        n2=input("So,What have you think so far? What is your interest?:")
          
        print("Thank you for using me.I hope I can help you further.See you")
