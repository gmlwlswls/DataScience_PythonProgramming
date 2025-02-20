"""
[Optional] Q5. Read csv

Write a function that reads a csv file and returns a dictionary of columns where each value is a list containing the data for that column.

print("contacts.csv \n")
with open("contacts.csv",'r') as grades:
    print(grades.read())

contacts.csv 

Name,Age,Email
Alice,30,alice@example.com
Bob,25,bob@example.com
Charlie,35,charlie@example.com
Dana,28,dana@example.com
Eve,22,eve@example.com

read_csv('contacts.csv')


"""
def read_csv(filename: str) -> dict:
    # Write your code here
    csv_dict = dict()
    
    with open(filename, 'r') as csv:
        header = csv.readline()
        header = header.strip().split(',')

        csv_dict = {col: [] for col in header}
        
        line = csv.readline()
        while line:
            line = line.strip().split(',')
            for i in range(len(header)):
                csv_dict[header[i]].append(line[i])
            line = csv.readline()
    return csv_dict