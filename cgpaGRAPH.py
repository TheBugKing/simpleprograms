from matplotlib import pyplot as plt  #importing pyplot from matplot pakage


again=True  #assigning a boolean for main loop
print("This python program will visualize your academic perfomance in a graph (in form of line or point) \n")

while again==True: # main loop runs tile again is true
    view=input("""" type 'plot' visualize your performance as line in the graph \n
        type 'scatter' visualize your performance as point in the graph          :""").lower()    #asking user the type of graph


    if (view == 'bar' or view=='scatter' or view== 'plot'):  #verifying the correct input
        name=input("Enter your name \n")     #user name

        rollno=int(input("Enter your roll number\n")) #user roll no

        totalsem=int(input("Enter toltal number semesters\n")) # total semesters

        allsem=[sem for sem in range(1,totalsem+1)]  #getting total sequence of the semester eg. 8 - [1,2,3,....,8]
        grade=list()                                  #list created for grade

        for cgpa in allsem:                             #getting cgpa per semester
            grade.append(float(input(f"Enter CGPA obtained in {cgpa}th semester :\t"))) #appending cgpa per semester to grade list


        plt.title(f"Performance of {name} roll no: {rollno} ") #graph title
        plt.xlabel(" Total semesters")  #x axis label
        plt.ylabel("Grade points obtained")# y axis label

        # ploting according to user specified graph

        if view=='plot':
            plt.plot(allsem,grade)
            plt.show()
        if view=='scatter':
            plt.scatter(allsem,grade)
            plt.show()

        #asking user if he/she wants to enter new graph
        ans=input("Do you want to Enter new data or record (Y/N)").upper()

        #while loop condition setting
        if (ans=='N'):
            again=False
        else:
            again=True

    else:
        print("\n error  please type correctly")




