#Function to check if the co-ordinates value that is entered is a float 
def check_float(prompt):
    while True:
        value = input(prompt)

        #Check if the value entered in Q or no. If 'Q" then exit
        if value.strip() == 'Q' or value.strip() == 'q':
            return 'q'
        
        # check if the value entered is a negative value. If it is negative then ignore the negative just take the value
        if value.startswith('-'):
            num = value[1:]
        else:
            num = value

        #check if it a float value then allow only one decimal point value
        if num.replace('.','',1).isdigit():
            return float(num)
        else:
            print("Invalid input.")    

def main():
    myList=[]

    print("Enter the 3D point(enter q or Q to exit): \n")

    while True:
        name = input("\nEnter Point Name: ")
        if name.strip() == 'q' or name.strip() == 'Q':
            break
        if not name.strip():
            print("The point name cannot be empty")
            continue
        
        #Take the input value for X and check if it a float value
        x = check_float("Enter the value of X: ")
        if x=='q':
            break

        #Take the input value for Y and check if it a float value
        y = check_float("Enter the value of Y: ")
        if y=='q':
            break
        
        #Take the input value for Z and check if it a float value
        z = check_float("Enter the value of Z: ")
        if z=='q':
            break

        myList.append([name,(x,y,z)])

    #Check if there are atleast 2 points in the list to compute the distance betwwen the points
    if len(myList) <2:
        print("Insufficient points to compute distances.")
        return
    
    #Print the results
    newList = []
    print("\nResults: ")

    #calculate the distance between the points in the list
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            name1, coorinates1= myList[i]
            x1, y1, z1 = coorinates1
            name2, coorinates2 = myList[j]
            x2, y2, z2 = coorinates2
            distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
            dis = f"Distance between {name1} and {name2}"
            newList.append([dis, round(distance, 3)])
            print(f"{dis} is {distance:.3f}")

    print("\nDistance List: ")
    print(newList)


if __name__ == "__main__":
    main()