# setting up essential variables
#input_string = input()
priority_list = [['*','/'],['+','-','%'],['==','<=','>=','<','>','!=']]
opperation_list = ['*','/','+','-','%','=','<','>','!=','==','<=','>=','(',')']
process_order = 1


# Input Preprocessing functions:

#a function to convert string into a list of characters
def convert(string):
    list1=[]
    list1[:0]=string
    return list1

# a function that turns brackets in our input list into a sub-list
def bracketting(l):
    itteration = 1
    while True:
        try:
            o = l.index("(")
            tol = 0
            b = []
            #print(f"the index to be removed is: {o}")
            del l[o]
            while True:
                if l[o]!= ')':
                   # print(f"input list is now:{l}")
                    if l[o] =="(":
                        tol+=1
                    b.append(l[o])
                    del l[o]
                elif l[o] == ")" and tol == 0:
                    del l[o]
                    l.insert(o, b)
                    break
                elif l[o] == ")" and tol>0:
                    tol-=1
                    b.append(l[o])
                    del l[o]
            itteration+=1
        except:
            break


# a recursive function to turn multiple brackets into a sub-list of lists
def transfiguration(l):
    bracketting(l)
    for element in l:
        if type(element) == type(list()):
            transfiguration(element)



#================================================ Step 1: Process the input into a useful format ============================================
#converting the input string into a list
def cleaning_input(input_string):
    input_string = convert(input_string)

    # removing all empty spaces from our string
    try:
        while True:
            input_string.remove(" ")
    except ValueError:
        pass

    # attatcing all separated numbers into one number
    input_list = []
    s = ''
    for element in input_string:
        
        if element in opperation_list:
            input_list.append(s)
            input_list.append(element)
            s = ''
        
        else:
            s = s+element
    if s != '':
        input_list.append(s)

    # removing empty element from list because of unknown error
    while True:
        try:
            a = input_list.index("")
            input_list.remove(input_list[a])
        except:
            break

    #now we need to stitch logical opperations like >=, == and <= together 
    try:
        for i in range(len(input_list)-1):
            if input_list[i] == '=' and input_list[i+1] == '=':
                input_list[i] = input_list[i]+input_list[i+1]
                input_list.remove(input_list[i+1])

            elif input_list[i] == '>' and input_list[i+1] == '=':
                input_list[i] = input_list[i]+input_list[i+1]
                input_list.remove(input_list[i+1])
            
            elif input_list[i] == '<' and input_list[i+1] == '=':
                input_list[i] = input_list[i]+input_list[i+1]
                input_list.remove(input_list[i+1])
    except:
        pass
        


    print(f"Input List: {input_list}")

    #turning all brackets into lists for later processing

    transfiguration(input_list)


    print(f"transfigured Input List: {input_list}")

    return input_list

#input_list = cleaning_input(input_string)


#now everything is complete and ready for processing!!



#================================================ Step 2: Now is the real start of the project ============================================



# Input processing Functions

def get_value(x,opperand,y):
        x = float(x)
        y = float(y)
        if opperand == "+":
            return x+y
        elif opperand == "-":
            return x-y
        elif opperand == "*":
            return x*y
        elif opperand == "/":
            return x/y
        elif opperand == "%":
            return x%y
        elif opperand == ">":
            return x>y
        elif opperand == "<":
            return x<y
        elif opperand == ">=":
            return x>=y
        elif opperand == "<=":
            return x<=y
        elif opperand == "!=":
            return x!=y
        elif opperand == "==":
            return x==y

# a function that solves any statement based on the global priority list
def solve_statement(l):
    global priority_list
    global process_order
    try:
        for i in range(len(l)):
            if l[i] in priority_list[0]:
                x = l[i-1]
                o = l[i]
                y = l[i+1]
                val = get_value(x,o,y)
                del l[i-1]
                del l[i-1]
                del l[i-1]
                l.insert(i-1, val)
                print(f"process{process_order}: {x} {o} {y} -> {val}")
                process_order+=1

    except:
        print(l)
        pass
    try:
        for i in range(len(l)):
            if l[i] in priority_list[1]:
                x = l[i-1]
                o = l[i]
                y = l[i+1]
                val = get_value(x,o,y)
                del l[i-1]
                del l[i-1]
                del l[i-1]
                l.insert(i-1, val)
                print(f"process{process_order}: {x} {o} {y} -> {val}")
                process_order+=1
    except:
        print(l)
        pass
    
    try:
        for i in range(len(l)):
            if l[i] in priority_list[2]:
                x = l[i-1]
                o = l[i]
                y = l[i+1]
                val = get_value(x,o,y)
                del l[i-1]
                del l[i-1]
                del l[i-1]
                l.insert(i-1, val)
                print(f"process{process_order}: {x} {o} {y} -> {val}")
                process_order+=1
    except:
        print(l)
        pass
    
    return l[0]

#a function that takes the transfigured input list and solves the problem given in the list from left to right
def solve_problem(l):
    for i in range(len(l)):
        if type(l[i]) == type(list()):
            l.insert(i,solve_problem(l[i]))
            del l[i+1]
        
    return solve_statement(l)
    
    




#print(f"solution: {solve_problem(cleaning_input(output))}")
