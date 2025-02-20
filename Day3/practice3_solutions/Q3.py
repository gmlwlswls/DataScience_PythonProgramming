"""
Q3. Check dictionary of dictionaries

[KOR]
때때로 프로그래머들은 value가 딕셔너리로 이루어진 “Dictionary of dictionaries”를 간단한 데이터베이스로 이용한다. key가 문자열(string)이고 value가 딕셔너리 형태인 “Dictionary of dictionaries”를 다음과 같이 나타낼 수 있고, 이때 value는 “inner dictionary”라 한다. “Dictionary of dictionaries”를 변수(argument)로 받아 “inner dictionaries”가 모두 같은 key 값을 가지면 1, 아니면 0을 리턴하는 함수를 작성하시오.

! 조건
1. 딕셔너리가 비어있는 경우는 없음
2. 모든 value는 딕셔너리로 되어있음
3. value의 value는 딕셔너리 형태가 아님

[ENG]
"Dictionary of dictionaries" refer to a dictionary that has values that are dictionaries as well. Here we have keys of strings and values of dictionaries, which we call "inner dictionary". Take "Dictionary of dictionaries" as input argument. Return 1 if all "inner dictionaries" have the exact same keys, else 0.

! Condition
1. input dictionaries are not empty
2. All values are dictionaries
3. Values of a value is not a dictionary

{ 'jgoodall' : {'surname' : 'Goodall',
                'forename' : 'Jane',
                'born' : 1934,
                'died' : None,
                'notes' : 'primate researcher',
                'author' : ['In the Shadow of Man','The Chimpanzees of Gombe']},
    'rfranklin' : {'surname' : 'Franklin',
                'forename' : 'Rosalind',
                'born' : 1920,
                'died' : 1957,
                'notes' : 'contributed to discovery of DNA'},
    'rcarson' : {'surname' : 'Carson',
                'forename' : 'Rachel',
                'born' : 1907,
                'died' : 1964,
                'notes' : 'raised awareness of effects of DDT',
                'author' : ['Silent Spring'] }}

ex1 - P3({'a': {'aa':123, 'ab': [1,2]}, 'b': {'aa': 'bb', 'ab': 'cc'}})
> 1 (Explanation: All values have the same keys, {'aa', 'ab'}.)

ex2 - P3({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
> 0

"""

def P3(dct: dict) -> int:
    ### Write code here ###
    ref = set(list(dct.values())[0].keys())
    
    for inner_dct in dct.values():
        inner_key = set(inner_dct.keys())
        if inner_key != ref:
            return 0
    return 1
    ### End of your code ###