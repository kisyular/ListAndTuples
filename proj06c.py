
while True: 
    try:
        opened_file = open( "Data_full.txt", 'r')
        break
    except FileNotFoundError :
        print("file not found in the specified directory")
        break
    except NameError:
        print("wrong name entry")
        break

create_tuple=[]


#prompt the user to enter the N-Warmest month
while True :    
#prompt the user again if enters a float
    try :
        number_warmest =(input("enter the number of warmest months "))
        number_warmest=int(number_warmest)
            
#if the user enters a negative integer, prompt user again
        if number_warmest < 0:
            print("enter only positive number, try again")
            continue
        
    #check if the number is absolute
        elif number_warmest == 0:
            print("the program will always print ONLY the highest temperature \
    if you enter '0' ")
            break
        elif number_warmest > 0:
            break
    except ValueError:
        print("wrong entry, try again")
        continue

  
line = opened_file.readline()
year_months_list = line.split()

#initiate a for loop
for line in opened_file :
    ln_list=line.strip().split()
#create a list for the year    
    year=(ln_list[0])
    
#the program will slice the line and create the months list
    January=int(ln_list[1])
    February=int(ln_list[2])
    March=int(ln_list[3])
    April=int(ln_list[4])
    May=int(ln_list[5])
    June=int(ln_list[6])
    July=int(ln_list[7])
    August=int(ln_list[8])
    September=int(ln_list[9])
    October=int(ln_list[10])
    November=int(ln_list[11])
    December=int(ln_list[12])
    

    
#create a list of both year, month and the highest temperature.   
    January_full_data=(January,year, year_months_list[1])
    February_full_data=(February,year, year_months_list[2])
    March_full_data=(March, year, year_months_list[3])
    April_full_data=(April,year, year_months_list[4])
    May_full_data=(May,year, year_months_list[5])
    June_full_data=(June,year, year_months_list[6])
    July_full_data=(July,year, year_months_list[7])
    August_full_data=(August,year, year_months_list[8])
    September_full_data=(September,year, year_months_list[9])
    October_full_data=(October,year, year_months_list[10])
    November_full_data=(November, year, year_months_list[11])
    December_full_data=(December, year, year_months_list[12])
    
    
#create a tuple of all the months
    create_tuple.append(January_full_data) 
    create_tuple.append(February_full_data) 
    create_tuple.append(March_full_data)
    create_tuple.append(April_full_data)
    create_tuple.append(May_full_data)
    create_tuple.append(June_full_data)
    create_tuple.append(July_full_data)
    create_tuple.append(August_full_data)
    create_tuple.append(September_full_data)
    create_tuple.append(October_full_data)
    create_tuple.append(November_full_data)
    create_tuple.append(December_full_data)
    
create_tuple.sort(reverse=True)

i=0
for elements in create_tuple:
    print("{:4s} {:3s} {:3d} ".format(elements[1], elements[2], elements[0]))
    i+=1
    if i > number_warmest-1:
        break
    
    
