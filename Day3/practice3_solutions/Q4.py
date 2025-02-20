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

def menu(filename : str) -> list[list]:
    # Write your code here
    out_list = []
    with open(filename, 'r') as menu_txt:
        line = menu_txt.readline()
        while line:
            line = line.split()
            out_list.append(line)
            line = menu_txt.readline()
            
    return out_list

def reverse_menu(filename: str) -> list:
    # Write your code here
    reverse_list = []
    with open(filename, 'r') as menu_txt:
        line = menu_txt.readline()
        while line:
            line = line.strip() # removes newline return
            reverse_list.insert(0, line)
            line = menu_txt.readline()
            
    return reverse_list