bal = 10000 ;
attempt = 3 ;
PIN = 1234 ;
lst = [] ;
while attempt >= 1:
    user = int(input("Enter PIN: "))
    if(len(str(user))!=4):
        print("Invalid input")
        continue 
    attempt -= 1 
    if user != PIN:
        if(attempt == 0):
            print("You have no more attempts left and the card is blocked")
            break
        print("Invalid Pin","attempts left: ",attempt)
    else:
        while True :
            print("1. Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            inp = int(input("Enter your choice: "))
            if(0>inp or inp>4):
                print("Invalid input")
                continue ;
            else:
                if(inp == 1):
                    print("Your balance is :",bal,"\n")
                if(inp == 2):
                    amt = int(input("enter amount: "))
                    lst.append("Deposit")
                    lst.append(amt)
                    print("New balance is",bal+amt,"\n")
                    bal+= amt 
                if(inp == 3):
                    amt = int(input("Enter amount: "))
                    if(amt > bal):
                        print("Insufficient balance","\n")
                    else:
                        print("Amount withdrawn successfully",)
                        print("New balance:",bal-amt,"\n")
                        bal -= amt 
                        lst.append("Withdraw")
                        lst.append(amt)
                if(inp == 4):
                    for i in range(len(lst)):
                        if i%2 == 0:
                            print(lst[i],end =":")
                        else:
                            print(lst[i])
                    print("Thank you ! Have a great day\n")

                    break ;
    break

#2
students={"Aman":[85,90,78],"Riya":[92,88,95],"Zoya":[70,65,80]} 
high = 0
for i in students:
    sum = 0
    for j in students[i] :
        sum += j 
        if(sum / 3 >= 85):
            grade="A"
        elif(sum/3 >= 70):
            grade="B"
        elif(sum/3 >= 50):
            grade="C"
        else:
            grade="F"
    if(sum > high):
        st = i
        high = sum 
    print(f"{i} : {sum/3:.2f} , Grade={grade}")
    print("Topper:",st)
while True :
    print("1.Add student")
    print("2.View all")
    print("3.Show Topper")
    print("4.Exit")
    user = int(input("Enter your choice: "))
    if(user == 1):
        stu = input("Enter student name: ")
        if stu in students:
            print("Student already exists!")
            continue 
        lst =[] 
        for i in range(3):
            marks=int(input("Enter marks: "))
            flag = 0
            if(marks>100 or marks < 0):
                print("Invalid input !!")
                flag= 1
                break
            lst.append(marks) 
        students[stu] = lst 
        if(flag == 1):
            continue  
    if (user == 2):
        print(students)
    if(user == 3):
        high = 0
        for i in students:
            sum = 0
            for j in students[i] :
                sum += j 
            if(sum > high):
                st = i
                high = sum 
        print("Topper:",st)
    if user == 4:
        print("Have a great day !")
        break 
