alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
pinguin = r"""
   _~_    
  (o o)   
 /  V  \  
/(  +  )\ 
  ^^ ^^   
"""

M = (alphabet.index((input("Введите фамилию: ")[0].lower())) + 1) % 9 + 1
N = (alphabet.index((input("Введите имя: ")[0].lower())) + 1) % 9 + 1

[print(*(lambda n: [item * n for item in pinguin.split("\n")[1:-1]])(i), sep="\n") for i in (M, N)]