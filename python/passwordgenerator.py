LOWER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMS = ['0','1','2','3','4','5','6','7','8','9']
SYMS = ['!','@','#','$','%','^','&','*','(',')']
EXT_SYMS = ['`','~','-','=','[',']','\\',';','\'',',','.','/','_','+','{','}','|',':','\"','<','>','?']


def main():
    length = int(input("How many characters?\n"))
    reqs=getReqs()
    file_name = input("Enter the file name:\n")
    
    
    if reqs == 1:
        generate(LOWER, length, file_name)
    elif reqs == 2:
        generate(NUMS, length, file_name)
    elif reqs == 3:
        generate((LOWER + UPPER), length, file_name)
    elif reqs==4:
        generate((LOWER + NUMS), length, file_name)
    elif reqs==5:
        generate((LOWER + UPPER + NUMS), length, file_name)
    elif reqs==6:
        ext=input("Enter b for basic symbols or e for extended symbols.\n")
        if ext=="b":
            generate((LOWER + SYMS), length, file_name)
        else:
            generate((LOWER + SYMS + EXT_SYMS) ,length, file_name)
    elif reqs==7:
        ext=input("Enter b for basic symbols or e for extended symbols.\n")
        if ext=="b":
            generate((LOWER + UPPER + SYMS), length, file_name)
        else:
            generate((LOWER + UPPER + SYMS + EXT_SYMS) ,length, file_name)
    elif reqs==8:
        ext=input("Enter b for basic symbols or e for extended symbols.\n")
        if ext=="b":
            generate((LOWER + NUMS + SYMS), length, file_name)
        else:
            generate((LOWER + NUMS + SYMS + EXT_SYMS), length, file_name)
    elif reqs==9:
        ext=input("Enter b for basic symbols or e for extended symbols.\n")
        if ext=="b":
            generate((LOWER + UPPER + NUMS + SYMS), length, file_name)
        else:
            generate((LOWER + UPPER + NUMS + SYMS + EXT_SYMS) ,length, file_name)
    
    
def getReqs():
    print("Enter 1 for lowercase letters.")
    print("Enter 2 for numbers.")
    print("Enter 3 for lower and uppercase letters.")
    print("Enter 4 for alphanumeric lowercase.")
    print("Enter 5 for alphanumeric with lower and uppercase.")
    print("Enter 6 for lowercase with symbols.")
    print("Enter 7 for lower and uppercase with symbols.")
    print("Enter 8 for alphanumeric lowercase with symbols.")
    reqs= input("Enter 9 for alphanumeric lower and uppercase with symbols.\n") 
    
    while (int(reqs) < 0 or int(reqs) > 9):
        print("Enter a valid number")
        reqs=getReqs()
        
    return int(reqs)

    
def generate(chars,length, file_name):
    for i in range(1, length+1):
        iterate(chars,i,"",len(chars), file_name)
        
def iterate(chars,i,p,length, file_name):
    if (i==0):
        with open(file_name, 'a') as file:
            file.writelines(p + '\n')
        return
    for j in range(0, length):
        result=p+chars[j]
        iterate(chars, i-1,result,length, file_name)
    return
    
main()
