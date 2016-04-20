###################################################
#Algortihm
# Title for the graph and labels for the axes
#Create and display the plot
#initiate a while True loop
#Prompt the user to enter the name of the file to be opened
#open the file for "reading"
#tell user the file was opened successfully
#The program will raise an error and exception if the file does not exist
# The program will halt if the file is not found
#initiate x to an empty list
#initiate y to an empty list    
#initiate a for loop so as to iterate through the file a couple times
#split the lines found in the file
#append the item in index[0] to x list
#append the item in index[1] to y list
#call function drwa_graph to plot graph
#initiate function main to call upon the work_file and close the file

import pylab

def draw_graph( x, y ):
    '''Plot x vs. y (lists of numbers of same length)'''

#Title for the graph and labels for the axes
    pylab.title( "Change in Global Mean Temperature" )
    pylab.xlabel( "Year" )
    pylab.ylabel( "Temperature Deviation" )

# Create and display the plot
    pylab.plot( x, y )
    pylab.show()

def open_file() :
#initiate a while True loop

    while True:
#Prompt the user to enter the name of the file to be opened
        input_file = input( "Enter the name of the file to open: " )
        try:
#open the file for "reading"
#tell user the file was opened successfully
            opened_file = open( input_file, 'r')
            print( "File open successful:", input_file )
            break
#The program will raise an error and exception if the file does not exist
# The program will halt if the file is not found
        except FileNotFoundError:
            print("file not found, program halted")
            break
    while True :
        try:
            return opened_file
        except UnboundLocalError:
            break
                    
def work_file( input_file):
#initiate x to an empty list
#initiate y to an empty list
    x=list()
    y=list()
#initiate a for loop so as to iterate through the file a couple times
    while True:
        try:
            for line in input_file:
                        #split the lines found in the file
                split_line=line.split()
#append the item in index[0] to x list
#append the item in index[1] to y list
                x.append(split_line[0], )
                y.append(split_line[1], )
            if len(x)==0:
                print("file empty")
                break
            graph=draw_graph(x, y)
            print(graph)
            break
        except TypeError:
            break

#call function drwa_graph to plot graph
#initiate function main to call upon the work_file and close the file
def main(): 

    opened_file=open_file()
    work_file(opened_file)
    while True:
        try:
            opened_file.close()
            break
        except AttributeError:
            break
main()

#ask why it prints (none) after the graph.
