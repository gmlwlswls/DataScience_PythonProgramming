"""
Q4. Café menu

Write two functions to read a cafe's menu from a text file (menu.txt) and return a list of menu.

* menu - returns list of lists
* reverse_menu - returns a list of strings in reverse order

print("menu.txt \n")
with open("menu.txt",'r') as menu_txt:
    print(menu_txt.read())

menu.txt 

Americano 3.66 4.11 4.56
CafeLatte 4.11 4.56 5.00
CafeMocha 4.55 5.00 5.45
DecafeCaffeLatte 4.38 4.82


menu('menu.txt')

>[['Americano', '3.66', '4.11', '4.56'],
  ['CafeLatte', '4.11', '4.56', '5.00'],
  ['CafeMocha', '4.55', '5.00', '5.45'],
  ['DecafeCaffeLatte', '4.38', '4.82']

reverse_menu('menu.txt')

>['DecafeCaffeLatte 4.38 4.82',
  'CafeMocha 4.55 5.00 5.45',
  'CafeLatte 4.11 4.56 5.00',
  'Americano 3.66 4.11 4.56']

"""

# 4. 

from typing import TextIO
# 1) 
def menu(file_path : TextIO) -> list :
  with open(file= file_path, mode= 'r') as file :
    lines = file.readlines()
    lst_of_lsts = []
    for line in lines :
      line= line.strip() # 양 옆 공백 제거
      line= line.strip('\n')
      line= line.split(sep= ' ')
      lst_of_lsts.append(line)
  return lst_of_lsts

menu('menu.txt')

# 2)
def reverse_menu(file_path : TextIO) -> list :
  with open(file= file_path, mode= 'r') as file :
    lines = file.readlines()
    lines_list = []
    for line in lines :
      line= line.strip()
      line= line.strip('\n')
      lines_list.append(line)
      lines_list.reverse() # list에 바로 반영
  return lines_list

# reverse : list 함수
# reversed : 파이썬 내장 함수

reverse_menu('menu.txt')