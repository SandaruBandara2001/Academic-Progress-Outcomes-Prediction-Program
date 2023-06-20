# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1866979
# Date: 30.11.2021

progress=trailer=retriever=exclude=0

def star (total ):
    for i in range (total):
        print ('*',end = '')
        
while True:
    while True:

        def range_ch(x):                #checking range of credits
            if not x in range (0,121,20):
                print (" Out of range ")
                return True
            
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
                print ("Integer required ")
                continue

        if (pss+defer+ fail) == 120:        #calculate total of the credits
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
                    
        print ("would you like to input another set of data ? ")
            
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

    print ("_"*50)
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
    print ("_"*50)
    break
    
