def testval(Num1,Num2,operator): 

    try:
        int(Num1)

    except: 
        return("Error: Numbers must only contain digits.")

    try:
        int(Num2)

    except: 
        return("Error: Numbers must only contain digits.")

    try:
        if len(Num1) > 4 or len(Num2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."

    return ""



def arithmetic_arranger(problems,displaymode=False):
  
    start = True
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
  
    if len(problems) > 5:
      return("Error: Too many problems.")

    for problem in problems:
        IndividualProblem = problem.split()
        Num1 = IndividualProblem[0]
        Num2 = IndividualProblem[2]
        operator = IndividualProblem[1]

        Exception = testval(Num1, Num2, operator)

        if Exception != "":
            return(Exception)

        no1 = int(Num1)
        no2 = int(Num2)

        Spacerequired = max(len(Num1), len(Num2))

        if start == True:
            line1 += Num1.rjust(Spacerequired + 2)
            line2 += operator + ' ' + Num2.rjust(Spacerequired)
            line3 += '-' * (Spacerequired + 2)
            if displaymode == True:
                if operator == '+':
                    line4 += str(no1 + no2).rjust(Spacerequired + 2)
                else:
                    line4 += str(no1 - no2).rjust(Spacerequired + 2)
            start = False
        
        
        else:

            line1 += Num1.rjust(Spacerequired + 6)
            line2 += operator.rjust(5) + ' ' + Num2.rjust(Spacerequired)
            line3 += side_space + '-' * (Spacerequired + 2)
                
            if displaymode == True:
                if operator == '+':
                    line4 += side_space + str(no1 + no2).rjust(Spacerequired + 2)
                else:
                    line4 += side_space + str(no1 - no2).rjust(Spacerequired + 2)
            
    if displaymode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

    return line1 + '\n' + line2 + '\n' + line3
