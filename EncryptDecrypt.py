f=open(r'./hi.txt','w')
#lines=f.read()
#print(lines)
pasw = 'pes123'
def writelist():

    LIST=input("enter lines of the file").split(',')
    for line in LIST:
        f.write(line+'\n')

writelist()
f.close()

def fileLineCount():
    f=open(r'./hi.txt','r')
    LIST=f.readlines()
    
    count=0
    for lines in LIST:
        lines=lines.strip()
        test = 0
        for j in lines:
            if j!=' 'and j!='\n' and j!='\t':
                test=1



        #print(lines)
        #print(lines.startswith('#'))
        if test==1:
            if lines.startswith('#')==False:
                count=count+1
                #print (count)
    return count
print('number of lines in this file is',fileLineCount())



def insertline():
    num = 1
    ans = []
    p=')'
    f=open(r'./hi.txt','r')
    LIST=f.readlines()

    for lines in LIST:
        lines=lines.strip()
    
        i=str(num)+p+lines
        ans.append(i)
        num=num+1
    print(ans)

    f=open(r'./hi.txt','w').close()
    for i in ans:
        print(i)
        

        f=open(r'./hi.txt','a')
        f.write(i+'\n')

                   
insertline()

def encryp():

    f=open(r'./hi.txt','r')

    
    LIST=f.readlines()
    x=''
    for lines in LIST:
        input_char="abcdefghijklmnopqrstuvwxyz1234567890-+=#$;,.?/`~*:^%!@&()[]''"
        output_char="+=#$;,.?/`~*:^%!@&()[]''abcdefghijklmnopqrstuvwxyz1234567890-"
        trantab=str.maketrans(input_char,output_char)
        str1 = lines
        x+=str1.translate(trantab)
    f=open(r'./hi.txt','r').close()

    f=open(r'./hi.txt','w')
    f.write(x)
   

encryp()

def decryp():
    
    f=open(r'./hi.txt','r')

    LIST=f.readlines()
    x=''
    for lines in LIST:
        input_char="abcdefghijklmnopqrstuvwxyz1234567890-+=#$;,.?/`~*:^%!@&()[]''"
        output_char="+=#$;,.?/`~*:^%!@&()[]''abcdefghijklmnopqrstuvwxyz1234567890-"
        trantab=str.maketrans(output_char,input_char)
        str1 = lines
        x+=str1.translate(trantab)
    f=open(r'./hi.txt','r').close()
    f=open(r'./hi.txt','w')
    f.write(x)

password = input('Enter your password: ')
if password == pasw:
    decryp()
else: 
    print('Try Again!')
    encryp()