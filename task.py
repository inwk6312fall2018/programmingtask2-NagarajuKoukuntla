def list_crimes():#function for list of unique crime numbers
 data = open("Crime.csv","r") # reading data from csv
 d = dict()
 lot = []
 for line in data:
    line=line.strip()
    array = line.split(',')
    lot.append(array[-1])  #appending data (only crime name data to list)
 for i in lot: #looping list
    if(i not in d):  #checking list data in dictinary
      d[i]=1         # if no exists appending  
    else:
      d[i]+=1           # if  exists adding count value
 print ("{:<8} {:<25}".format('Key','Label'))# tabular format 
 for k, v in d.items():   # printing tabular format
    label= v
    print("{:<8} {:<15}".format(k, label))
       
 
list_crimes()    # calling function
  
