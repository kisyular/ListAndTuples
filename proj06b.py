###########################################################
#Algorithm
#initiate the program to open the file
#prompt the user to enter the file name
#open the file for writing mode
#prompt the user to enter the first starting year
#the program compares if entered_year matches any of the following
#if the user enters "all", output the everything
#if the user enters "alL", output the everything
#if the user enters "aLL", output the everything
#if the user enters "L", output the everything
#if the user enters "alL", output the everything
#if the user enters "alL", output the everything
            #initiate the program to open the file
try:
    opened_file = open( "Data_full.txt", 'r')
except FileNotFoundError :
    print("file not found in the specified directory")
except NameError:
    print("wrong name entry")


            #prompt the user to enter the file name

file_name=input("please enter the name of the output file  ")

while True :
    if file_name.find("txt")!= -1:
        print("file", file_name, "created and ready to be written")
        break
    elif file_name.find("txt")== -1:
        print("always add extension \".txt\" to the end of your output name,\
 file", file_name, "cannot be created")
        break
            #open the file for writing mode
output_file=open(file_name, "w")
opened_file.readline()

            #prompt the user to enter the first starting year
entered_year=input("please enter the year to check:  ")


            #the program compares if entered_year matches any of the following
            #if the user enters "all", output the everything
if entered_year=="all"  : 
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        total=sum(ln_list[1:])
        average=round(total/12, 0)
        avg_int=int(average)
        year=ln_list[0]
        output_form= ("{:4d} {:4d}\n".format(year, avg_int))
        output_file.write(output_form)
        
        
            #if the user enters "alL", output the everything
elif entered_year=="alL"  :
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        total=sum(ln_list[1:])
        average=round(total/12, 0)
        avg_int=int(average)
        year=ln_list[0]
        output_form= ("{:4d} {:4d}\n".format(year, avg_int))
        output_file.write(output_form)
        
        
             #if the user enters "aLL", output the everything
elif entered_year=="aLL"  :
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        total=sum(ln_list[1:])
        average=round(total/12, 0)
        avg_int=int(average)
        year=ln_list[0]
        output_form= ("{:4d} {:4d}\n".format(year, avg_int))
        output_file.write(output_form)
        
        
            #if the user enters "ALL", output the everything
elif entered_year=="ALL"  :
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        total=sum(ln_list[1:])
        average=round(total/12, 0)
        avg_int=int(average)
        year=ln_list[0]
        output_form= ("{:4d} {:4d}\n".format(year, avg_int))
        output_file.write(output_form)
        
        
            #if the user enters "All", output the everything
elif entered_year=="All"  :
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        total=sum(ln_list[1:])
        average=round(total/12, 0)
        avg_int=int(average)
        year=ln_list[0]
        output_form= ("{:4d} {:4d}\n".format(year, avg_int))
        output_file.write(output_form)
        
        
            #if the user enters "ALl", output the everything
elif entered_year=="ALl"  :
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        total=sum(ln_list[1:])
        average=round(total/12, 0)
        avg_int=int(average)
        year=ln_list[0]
        output_form= ("{:4d} {:4d}\n".format(year, avg_int))
        output_file.write(output_form)
        
        
            #the program will check if entered_year is numeric
elif entered_year.isnumeric():
    
            #the program will let the user know if the entry is out of range
    if int(entered_year) < 1879:
        print("out of range (1880-2014), empty", file_name, "has been created")
    if int(entered_year) > 2014:
        print("out of range (1880-2014), empty", file_name, "has been created")
    entered_year=int(entered_year)
    
            
            #the program will prompt the user to enter number of years
            #the program will check if the it is absolute number
    count_years=int(input("please enter years to count up to: "))
    count_years=abs(count_years-1)
            #initiate counter=0 and increment it based on the code below
    counter=0
    for line in opened_file:
        ln_list=line.strip().split()
        ln_list=[int(values) for values in ln_list]
        year=ln_list[0]
        while True:
            if count_years==0:
                print("only",entered_year, "has been printed in", file_name)
                break
            
        if year==entered_year or counter >0:
             total=sum(ln_list[1:])
             average=round(total/12, 0)
             avg_int=int(average)
             output_form= ("{:4d} {:4d}\n".format(year, avg_int))
             
             counter=counter + 1
             output_file.write(output_form)

            
            #break if the counter is greater than years to count
        if counter>count_years:
            break


            #the program tells user if entered_year is incorrect
else:
    print("your entry year","'",entered_year,"'", " is not among the choices \
empty", file_name, "has been created (if you didn't add extension '.txt' \
your", file_name, " file was not created")

            #close the both files
opened_file.close()
output_file.close()
