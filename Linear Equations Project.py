import time

#store number of variables and equations in an array
def takeDs():
    time.sleep(1)
    eq=int(input("\nplease enter the number of equations:")) #rows
    vr=int(input("please enter the number of variables:")) #columns-1
    Ds=[eq,vr]
    return Ds

#taking the elements from the user
def takeEle(Dimensions):# dimensions of the method before
    arr=[] # the augmented matrix
    numOfEqu=Dimensions[0]
    numOfVar=Dimensions[1]
    for i in range(numOfEqu):
        row=[]
        print("Equation number: ",i+1)
        for j in range(numOfVar): #entering the variables in each row without absloute term 
            row.append(float(input(f'Enter coeffitient of variable number {j+1}: ')))
        row.append(float(input(f'Enter the absloute term: '))) # entering the constant of the equation
        arr.append(row) #appending variables and the constant of each row in the augmented matrix
    print("The augmanted matrix of your linear system:")
    for i in range(len(arr)):
        print(arr[i])
    return arr         

#searching for a zeros row
def zerosRow(arr):
    zRow=False # tell me if the row is zeros row or not
    for i in range(len(arr)): # go seaarch for each row
        for j in range(len(arr[0])): # search in each element of that row
            if arr[i][j] == 0:
                zRow=True # will be true till it find an element doesn't equal to zero
            else:
                zRow=False # if there at least one element of a row doesn't equal to zero
                break # go out og the loop 
        if zRow==True: # if it = true then it will return zrow if not then it will loop for the second row and so on
            return zRow      
        

#Define the first non-zero column in the matrix
def nZeroCol(arr):
    for column in range(len(arr[0])): #طول عدد العناصر اللي في الصف هو عدد الاعمده 
        for row in range(len(arr)):# بلف على كل عنصر في العمود 
            if arr[row][column] != 0: #لو مش بيساوى صفر برجع العمود دا رقم كام
                return column        

#the first element != 0 by interchanging rows
def arrangeMat(arr,nonz):# take the augmatrix and the output of the method before that return the first non zero col
    if arr[0][nonz] == 0:# في حالة ان اول عنصر في العمود الغير صفري يساوى 0
        for r in range(1,len(arr)):
            if arr[r][nonz] == 1: # لو لقيت في العمود الغير صفري دا عنصر يساوي 1 ببدل الصف اللي فيه 1 دا مع اول صف
                arr[0],arr[r]=arr[r],arr[0]
                time.sleep(1)
                print(f'\nTo make a leading we interchanged rows number 0 and {r+1}')
                time.sleep(1)
                print("\nThe augmented matrix after interchanging rows: ")
                for i in range(len(arr)):
                    print(arr[i])
                return None #  اللي فوق مدخلش على اللي بعدها(for loop)عشان لو خلصت ال 
        for r in range(1,len(arr)):
            if arr[r][nonz] != 0: # في حالة مفيش عناصر بتساوي 1 في العمود دا ف انا هكون محتاجه اي عنصر وخلاص بس يكون لا يساوي 0
                arr[0],arr[r]= arr[r],arr[0]
                time.sleep(1)
                print(f"\nTo make the first element of the non zero column doesn't equal 0, we interchanged rows number 0 and{r+1}")          
                time.sleep(1)
                print("\nThe augmented matrix after interchanging rows: ")
                for i in range(len(arr)):
                    print(arr[i])
                return None

#takes the array which first element !=0 and != 1, make the first equals to 1 if it doesn't
#doing that by multiplying the whole row by the multiplicative inverse of the first element
def makeL(arr,n):# taking the augmatrix and the non zero col
    bleading = arr[0][n] # بحط اول عنصر دا في متغير
    if bleading !=1:
        time.sleep(1)
        print("\nMake a leading in the row by multiplying the whole row by the multiplicative inverse of the first nonzero element")
        for i in range(len(arr[0])): # بتعدي على كل العناصر بتاع اول صف
            arr[0][i] *= 1/bleading # بضرب كل عنصر في الصف دا في المعكوس الضربي بتاع اول عنصر 
        time.sleep(1)
        print("\nThe augmented matrix:")
        for i in range(len(arr)):
            print(arr[i])

#making all elements under the leading equal zero
def zeros_UL(arr,n):
    for tR in range(1,len(arr)):# starting from the sec row that it always under the first row that has a leading
        x = -arr[tR][n]# بعمل متغير بحط فيه قيمة المعكوس الجمعي بتاع العناصر اللي تحت الليدينج
        if x != 0:# في حالة ان العنصر اللي تحت الليدينج لا يساوى صفر   
            time.sleep(1)
            print(f"\nmultiply each element of the first row by {x} and add it to the row number {tR+1}\n\nThe resulting augmented matrix:")
            for i in range (len(arr[0])):
                arr[tR][i]=(arr[0][i]*x)+arr[tR][i] # بضرب كل عنصر في الصف الاول بالمعكوس الجمعي بتاع العنصر اللي تحت الليدينح اللي انا عاوزه اصفره وبجمعه على الصف اللي بعده
            time.sleep(1)
            for i in range(len(arr)):
                print(arr[i])

#move the first col from the old matrix to a new one to repeat the steps
def delFirstRow(old,new):#  كأني ظللت اول صف عشان اعيد العمليات من الاول على الصفوف اللي بعد كدا ف هنقله من المصفوفه القديمه لمصفوفه جديده
    print('\nMove the first row from the main to another matrix and repeat the steps if possible')
    new.append(old.pop(0))  

#بعد ما كل الخطوات اتكررت على كل الصفوف في المصفوفة بتاعتي و اتنقلت من المصفوفة الفديمه للجديده
#check the last row
# 0 = "there's no sol", 1 =" there's a unique sol", 2 ="there's infinity sol"
def check_LR(newArr):
    if newArr[len(newArr)-1][len(newArr[0])-2] == newArr[len(newArr)-1][len(newArr[0])-1] == 0: # لو العنصر اللي قبل الاخير بيساوي العنصر الاخير بيساوي صفر
        return 2 # infinity sol
    elif newArr[len(newArr)-1][len(newArr[0])-2] == 0 and newArr[len(newArr)-1][len(newArr[0])-1] != 0: # لو العنصر اللي قبل الاخير بيساوي صفر و العنصر الاخير لا يساوي صفر 
        return 0 # no sol
    else:
        return 1 # unique sol

# بعد ما اتأكدت ان اخر صف يخلي فيه حل   
# input : matrix in row echlon form
# output: matrix in reduced row echlon form
# make all elements above the leading equal zero              
def zeros_AL(newArr):
    for lRow in range(len(newArr)-1,0,-1):# ببدأ من الاخر 
        for tR in range(lRow): # بعمل نفس اللي عملته في الميثود اللي كانت بتخلي العناصر اللي تحت الليدينج بصفر
            x = -newArr[tR][lRow]
            if x != 0:
                time.sleep(1)
                print(f"\nmultiply each element of the row number {lRow+1} by {x} and add it to the row number {tR+1}\n\nThe resulting augmented matrix:")
                for i in range(len(newArr[0])):
                    newArr[tR][i]=(newArr[lRow][i]*x) + newArr[tR][i]
                time.sleep(1)
                for i in range(len(newArr)):
                    print(newArr[i])    

#extact variables value from the matrix
def varsOutput(newArr):
    time.sleep(1)
    print("\nThe variables values: ")
    for i in range(len(newArr)): # go for each row
        time.sleep(1)             # باخد رقم كل صف مع اخر عمود دايما لانه اللي بيكون فيه فيمة الثابت 
        print(f'x{i+1} = {round(newArr[i][len(newArr[i])-1],2)}') #بقرب الناتج لاقرب علامتين عشريتين
    time.sleep(1)
    return 'Done!'    

def solve():
    Ds = augMatrix = newMat = []
    print("\nWelcome to my project.")
    Ds = takeDs()
    augMatrix=takeEle(Ds) # هنا بدخل عناصر في المصفوفه اللي عملتها
    while augMatrix != []:
        if zerosRow(augMatrix) == True: #لو لقيت صف صفري بقوله ان عندي عدد لا نهائي و بقفل على كدا
            time.sleep(1)
            return "\nThere are infintly solutions!"
        time.sleep(1)
        print("\nThe augmented matrix to solve:")
        for i in range(len(augMatrix)): # هيطبع المصفوفه اللي هيحلها 
            print(augMatrix[i])
        n = nZeroCol(augMatrix) #هخزن اللي هيطلع من الميثود دي في متغير 
        arrangeMat(augMatrix,n) # هخلي اول عنصر مبيساويش صفر
        makeL(augMatrix,n) # بخلي اول عنصر ب 1
        zeros_UL(augMatrix,n) # بصفر العناصر اللي تحت الليدينج
        time.sleep(1)
        delFirstRow(augMatrix,newMat) # بشيل اول صف بنقله من المصفوفه بتاعتي لمصفوهف جديده عشان يعيد العمليات تاني
    time.sleep(1)                     # لحد ما المصفوفه بتاعتي تبقا فاضيه و الجديده تبقا كامله
    print("\nThe matrix in the row-echlon from:")
    for i in range(len(newMat)):
        print(newMat[i]) # بطبع المصفوفه الجديده اللي هي بقت في r.e.f
    if check_LR(newMat) == 0: # بعمل check لو لقيت اللي بيطلع منا الميثود ب 0 يبقا معنديش حل
        time.sleep(1)
        return "\nThere's no solution!"
    elif check_LR(newMat) == 2:
        return "\nThere are infinity solutions!"
    else: # لو حاجه تانيه غير ال 0 و 2 
        zeros_AL(newMat) # هبعتله المصفوفه في الميثود اللي بتخلي العناصر اللي فوق الليدينج كمان ب صفر و بيبقا عندي مصفوفة في الr.r.e
        return varsOutput(newMat) # بطلع القيم بتاعتي بقا


print(solve())               


                    