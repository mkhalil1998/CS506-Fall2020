import csv 
def read_csv_file(path):   #Declare function to read file
    matrix=[]                  #Initalize matrix              
    with open (path,'r') as file:   #open the csv file  
        reader = csv.reader(file)   #Read content of csv file
    for row in reader:          #Position content of csv file in rows
        line =[]
    for item in row:        #For each item in the row place it as list of list 
        if item.isdigit():
            line.append(int(item))
        else: 
            line.append(item)
        matrix.append(line)
    return(matrix)                  #Return the matrix 


