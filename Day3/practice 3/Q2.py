"""
Q2. Particle with highest probability

[KOR]
일련의 실험을 수행한 후, 특정 다섯 종류의 아원자 입자(subatomic particles)를 탐지할 확률을 {str: float} 딕셔너리 형태로 다음과 같이 저장했다.
> {'neutron': 0.55, ‘proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}

이러한 딕셔너리를 변수(argument)로 받아 탐지 가능성이 가장 큰 입자를 리턴하는 함수를 작성하시오. 입자가 발견될 확률이 같은 경우는 없다.

[ENG]
Probabilities of detecting each subatomic particles are given in the form of dictionary.
> {'neutron': 0.55, ‘proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}

Implement a function that returns the particle with the highest probability. There is no case that the probability is the same among different particles.([1, 2, 3, 1])
> {1}

ex1 - P2({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14})
> 'neutron'

ex2 - P2({'neutron': 0.11, 'proton': 0.21, 'meson': 0.05, 'muon': 0.09, 'neutrino': 0.12})
> 'proton'
"""

# 2. 

def P2(dict : dict) -> str :
  key_list = []
  value_list = []
  for key, value in dict.items() :
    key_list.append(key)
    value_list.append(value)
  max_value= max(value_list)
  max_value_idx = value_list.index(max_value)
  max_key = key_list[max_value_idx]
  # return key_list[max_value_idx]
  return max_key

P2({'neutron' : 0.55, 'proton' : 0.21, 'meson' : 0.03, 'muon' : 0.07, 'neutrino' : 0.14})
P2({'neutron' : 0.11, 'proton' : 0.21, 'meson' : 0.05, 'muon' : 0.09, 'neutrino' : 0.12})

# dict.keys()
# dict.values()