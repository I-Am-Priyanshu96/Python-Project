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