import csv  

catagory_UNOS = []

# given an attorney UNO return their highest answered catagory 
def expertise(attorney_UNO):
    common_catagory_UNO = ''
    return find_catagory_name(common_catagory_UNO) 

# given a catagory UNO return the name of the catagory 
def find_catagory_name(catagory_UNO):
    catagory_name = ''
    return catagory_name

# Given an attorney UNO returns a list of all catagory UNOS connected to the questions they have answered
def cases(attorney_UNO): 
    with open('test-data/test-questions.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:

           if(row[9] == attorney_UNO):
               catagory_UNOS.append(row[3])
              # print('these should be the same: ' + row[9] + ' and ' + attorney_UNO)
               print('catagory UNO' + row[3])
               print(catagory_UNOS)
    print(catagory_UNOS)
    return catagory_UNOS


cases('FA34142B-1575-4720-981C-2D28C3560137')