print(r"""



                                                            ██╗   ██╗   ██╗   ██╗ ██████╗ ██╗██████╗ 
                                                             ██║ ██╔╝   ██║   ██║██╔═══██╗██║██╔══██╗
                                                              ████╔╝    ██║   ██║██║   ██║██║██║  ██║
                                                             ██╔═██╗    ██║   ██║██║   ██║██║██║  ██║
                                                            ██ ║  ██╗   ╚██████╔╝╚██████╔╝██║██████╔╝
                                                             ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝╚═════╝
                                                                         ░░ X   V O I D ░░           
                                                                     [ TERMINAL EDITION v1.1 ]
""")

input("""





                                                                press enter to enter the VOID...




















""")

array1 = ['.' , '.' , '^' , '.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,]
array2 = ['.' , '.' , '.' , '.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,]
array3 = ['.' , '.' , '.' , '.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,'.' ,]
array4 = ['x' , 'x' , 'x' , 'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'.' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
array5 = ['x' , 'x' , 'x' , 'x' ,'N' ,'x' ,'.' ,'x' ,'.' ,'x' ,'N' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
array6 = ['x' , 'x' , 'x' , '.' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,]


z = 0
q = 0
l = 1






def load() :
        print("""


















                """)
        if l == 5 :
            print(" " * 58 + 'FINAL LEVEL : ░░ M O T H E R  S H I P ░░')
        print(" " * 58 + '  '.join(array6))
        print(" " * 58 + '  '.join(array5))
        print(" " * 58 + '  '.join(array4))
        print(" " * 58 + '  '.join(array3))
        print(" " * 58 + '  '.join(array2))
        print(" " * 58 + '  '.join(array1))
        print("""













        """)
load()

while True :
    while z < 16:
        e = input(" " * 54 + 'move using a , d and s to shoot and enter to confirm ')
        if e == 'a':
            pos = array1.index('^')
            array1[pos] = '.'
            apos = pos - 1
            array1[apos] = '^'
            load()
        elif e == 'd' :
            pos = array1.index('^')
            array1[pos] = '.'
            apos = pos + 1
            array1[apos] = '^'
            load()
        elif e == 's' :
            pos = array1.index('^')

            array2[pos] = '.'
            array3[pos] = '.'
            if array4[pos] == 'Y' :
                array4[pos] = 'W'
            elif array4[pos] == 'W' :
                array4[pos] = 'N'
            elif array4[pos] == 'N' :
                array4[pos] = 'x'
            else :
                array4[pos] = '.'


            if array5[pos] == 'Y' :
                array5[pos] = 'W'
            elif array5[pos] == 'W' :
                array5[pos] = 'N'
            elif array5[pos] == 'N' :
                array5[pos] = 'x'
            else :
                array5[pos] = '.'


            if array6[pos] == 'Y' :
                array6[pos] = 'W'
            elif array6[pos] == 'W' :
                array6[pos] = 'N'
            elif array6[pos] == 'N' :
                array6[pos] = 'x'
            else :
                array6[pos] = '.'
            load()
        z = 1
        if array6.count('.') == 16 and array5.count('.') == 16 and array4.count('.') == 16 :
            z = array6.count('.')
    else:
        while q < 4 :
            info = ' '
            if l == 1 :
                info = '''
                the x is commonly known as the x plens
                they are weak but fast plens
                '''
            elif l == 2 :
                info = '''
                the N is known as the thunderstein
                they have decent armor but not the best
                '''
            elif l == 3 :
                info = '''
                the W are the battlecruisers 
                they are heavily armored and are control centers
                for the other plens
                '''
            elif l == 4 :
                info = 'nothing here but the next battle WILL be hard'
            
            print("""
            //scan
            //exit
            //next
            """)
            s = input('/')
            if s == 'scan':
                print(info)
                s = input('/')
            elif s == 'exit':
             print("exited")
            elif s == 'next':
                print('loading...')
                l+=1
                if l == 2 :
                    

                    z = 0
                    
                    array4 = ['x' , 'x' , 'x' , 'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
                    array5 = ['x' , 'x' , 'x' , 'x' ,'N' ,'N' ,'N' ,'x' ,'x' ,'x' ,'N' ,'x' ,'x' ,'x' ,'x' ,'N' ,]
                    array6 = ['x' , 'x' , 'N' , 'x' ,'x' ,'x' ,'x' ,'N' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
                    load()
                    break
                elif l == 3 :

                    z = 0
                    
                    array4 = ['x' , 'x' , 'x' , 'W' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
                    array5 = ['x' , 'x' , 'x' , 'x' ,'N' ,'N' ,'N' ,'x' ,'x' ,'x' ,'N' ,'x' ,'x' ,'x' ,'x' ,'N' ,]
                    array6 = ['x' , 'x' , 'x' , 'x' ,'x' ,'x' ,'x' ,'N' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
                    load()
                    break
                elif l == 4 :
                    z = 0
                    
                    array4 = ['x' , 'x' , 'x' , 'W' ,'x' ,'x' ,'N' ,'x' ,'x' ,'W' ,'N' ,'x' ,'x' ,'x' ,'N' ,'x' ,]
                    array5 = ['N' , 'x' , 'x' , 'x' ,'N' ,'W' ,'N' ,'x' ,'x' ,'x' ,'N' ,'W' ,'x' ,'N' ,'x' ,'N' ,]
                    array6 = ['x' , 'N' , 'W' , 'x' ,'N' ,'x' ,'x' ,'N' ,'x' ,'x' ,'N' ,'x' ,'x' ,'x' ,'x' ,'x' ,]
                    load()
                    break
                elif l == 5 :
                    z = 0
                    
                    array4 = ['x' , 'x' , 'x' , 'W' ,'x' ,'.' ,'.' ,'Y' ,'.' ,'.' ,'N' ,'x' ,'x' ,'x' ,'N' ,'x' ,]
                    array5 = ['N' , 'x' , 'x' , 'x' ,'N' ,'.' ,'W' ,'Y' ,'W' ,'.' ,'N' ,'W' ,'x' ,'N' ,'x' ,'N' ,]
                    array6 = ['x' , 'N' , 'W' , 'x' ,'N' ,'.' ,'Y' ,'.' ,'Y' ,'.' ,'N' ,'x' ,'x' ,'x' ,'x' ,'x' ,]

                    load()
                    break
                elif l > 5 :
                    print('congraculations on saving earth !!!')
