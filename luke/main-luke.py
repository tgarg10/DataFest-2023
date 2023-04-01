import csv  


# given an attorney UNO return their highest answered catagory 
def expertise(attorney_UNO):
    common_catagory_UNO = ''
    return find_catagory_name(common_catagory_UNO) 


# given a list of strings, returns the most common string. 
def most_common_catagory(strings):
    return max(set (strings), key=strings.count)


subcatagory_frequency = {}

# given a list of subcatagories, returns a dict where the key is the subcatagory and the value is its frequency 
def build_subcatagory_frequency(lst): 
    for i in lst:
        subcatagory_frequency[i] = lst.count(i)
    return subcatagory_frequency


# Given an attorney UNO returns a list of all subcatagories they have answered 
def build_subcatagories(attorney_UNO):
    subcatagories  = []

    with open('test-data/test-questions.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
             if(row[9] == attorney_UNO):
               subcatagories.append(row[6])
              # print('these should be the same: ' + row[9] + ' and ' + attorney_UNO)
              #print('catagory UNO: ' + row[6])
               #print(subcatagories)
    #print(subcatagories)
    return subcatagories 


#print( most_common_catagory(build_subcatagories('FA34142B-1575-4720-981C-2D28C3560137')))

print(build_subcatagory_frequency (build_subcatagories ('FA34142B-1575-4720-981C-2D28C3560137')))