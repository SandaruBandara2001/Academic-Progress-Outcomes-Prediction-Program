# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1866979
# Date: 02.12.2021

progress=trailer=retriever=exclude=total=0
count1=count2=count3=count4=1
credits_list = []

def star (total ):
    for i in range (total):
        print ('*',end = '')
        
def vertic_histogram(name,count):        #print star in vertical histogram
    if count <= name:
            print ('          *           ', end='')
    else:
            print ('                      ', end='')

def range_ch(x):                #checking range of credits
    if not x in range (0,121,20):
        print (" Input is out of range ")
        return True

while True:
    while True:
   
        try:
            pss = int(input ("Enter your total PASS credits :    " ))
            if range_ch(pss):
                continue

            defer = int(input("Enter your total DEFER credits :    "))
            if range_ch(defer):
                continue

            fail= int(input( "Enter your total FAIL credits :    "))
            if range_ch (fail):
                continue

        except ValueError:                  #cheking data type 
            print (" Integer required ")
            continue

        if (pss + defer + fail) == 120:        #calculate total of the credits
            
            credits_list.append([pss,defer,fail])        #add data to nested list


            if pss==120:
                print ("Progress")
                progress += 1

            elif pss==100:
                print ("Progress (module trailer)")
                trailer += 1
            elif fail>=80:
                print ("Exclude ")
                exclude += 1
            elif pss <100:
                print ("Module retriever ")
                retriever += 1
        else :
            print ("Total incorrect ")
                    
        print ('\n',"would you like to input another set of data ? ")
            
        while True:
            answ = input ( "please enter 'y' for yes or ' q ' quit and see the result ...")
            answ = answ.lower()
            print ()
            if answ == "y" or answ == "q" :
                break
            else:
                print (" invalid input ")
                print()
        if answ == "y":
            continue
        else:
            break

    print ("-"*50)
    print ("Horizontal Histogram ")

    print('Progress',progress,'\t :   ',end ='')
    star(progress)
    print('\nTrailer',trailer,'\t\t :   ',end ='')
    star(trailer)
    print('\nRetriever',retriever,'\t :   ',end ='')
    star(retriever)
    print('\nExclude',exclude,'\t\t :   ',end ='')
    star(exclude )
    print ('\n')
    total=progress+trailer+retriever+exclude
    print (total,"outcomes in total. ")

                
    print ("-"*50,'\n'," Vertical Histogram ")             
    x = max(progress, trailer, retriever, exclude)               #vertical histogram
    print(" Progress",progress,'| Trailer' ,trailer,'| Retriever',retriever,'| Exclude ',exclude)
    for i in range (x):
        vertic_histogram(progress,count1)
        count1 += 1
        vertic_histogram(trailer,count2)
        count2 += 1
        vertic_histogram(retriever,count3)
        count3 += 1
        vertic_histogram(exclude,count4)
        count4 += 1
        print()
    print(total, 'outcomes in total.')
    print ('-'*50)

    for i in range(len(credits_list)):        #print progression outcomes
        if credits_list[i][0]==120:
            print('Progress',end='')
            
        elif credits_list[i][0]==100:
            print('Progress (module trailer)',end='')

        elif credits_list[i][2]>=80:
            print('Exclude',end='')

        else:
            print('Module retriever',end='')
        print (' -' , credits_list[i][0] , ',', credits_list[i][1] , ',' , credits_list[i][2])    
    break




