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

>{'Name': ['Alice', 'Bob', 'Charlie', 'Dana', 'Eve'],
 'Age': ['30', '25', '35', '28', '22'],
 'Email': ['alice@example.com',
  'bob@example.com',
  'charlie@example.com',
  'dana@example.com',
  'eve@example.com']}

"""
# 5. 
from typing import TextIO

def read_csv(csv_file : TextIO) -> dict :
  contacts_dict= {}
  name_list= []
  age_list= []
  email_list= []
  with open(csv_file, 'r') as input_file :
    first_line= input_file.readline()
    first_line = first_line.strip()
    key_list = first_line.split(',')
    
    contents_line= input_file.readlines() # 둘째줄로 커서 이동
    for line in contents_line :
      line= line.strip()
      value_list = line.split(',')
      name_list.append(value_list[0])
      age_list.append(value_list[1])
      email_list.append(value_list[2])
    
    total_list= [name_list, age_list, email_list]
    
    for i, key in enumerate(key_list) :
      contacts_dict[key] = total_list[i]    
  return contacts_dict
    