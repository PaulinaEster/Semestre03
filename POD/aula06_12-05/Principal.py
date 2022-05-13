
# 1. Em Python, crie uma classe Pessoa, com os atributos id, sobrenome, nome e idade.

# 2.  Em um outro arquivo, crie uma lista de contatos com N objetos Pessoa.

# 3. Utilize o algoritmo Insertion Sort (estudado na aula anterior) para ordenar a lista de contatos por id, idade, nome e sobrenome


from operator import attrgetter
from pprint import pprint
from Pessoa import Pessoa




pessoas = [
  Pessoa(3, "Paula", "Rehbein", 23),
  Pessoa(53, "Paulina", "Rehbein", 89),
  Pessoa(34, "Ranya", "Campanario", 31),
  Pessoa(2, "Emanuela", "Flores", 12)
]



for i in range(len(pessoas)):
 print("nome: ", pessoas[i].nome)

def insertionSortId(v ):
 
 for i in range(1, len(v)):
  key  = v[i].id
 
  j = i - 1
  while j >= 0 and v[j].id > key:
    v[j + 1].setId(v[j].id)
    j -= 1
  v[j + 1].setId(key) 

def insertionSortNome(v ):
 
 for i in range(1, len(v)):
  key  = v[i].getNome()
 
  j = i - 1
  while j >= 0 and v[j].getNome()> key:
    v[j + 1].setNome(v[j].getNome())
    j -= 1
  v[j + 1].setNome(key) 

def insertionSortSobrenome(v ):
 
 for i in range(1, len(v)):
  key  = v[i].getSobrenome()
 
  j = i - 1
  while j >= 0 and v[j].getSobrenome()> key:
    v[j + 1].setSobrenome(v[j].getSobrenome())
    j -= 1
  v[j + 1].setSobrenome(key) 


def insertionSortIdade(v ):
 
 for i in range(1, len(v)):
  key  = v[i].getIdade()
 
  j = i - 1
  while j >= 0 and v[j].getIdade()> key:
    v[j + 1].setIdade(v[j].getIdade())
    j -= 1
  v[j + 1].setIdade(key)  


print("Ordenado por ID")
insertionSortId(pessoas)
for i in range(len(pessoas)):
 print("id: ", pessoas[i].getId())


print("Ordenado por Nome")
insertionSortNome(pessoas)
for i in range(len(pessoas)):
 print("Nome: ", pessoas[i].getNome())


print("Ordenado por Sobrenome")
insertionSortSobrenome(pessoas)
for i in range(len(pessoas)):
 print("Sobrenome: ", pessoas[i].getSobrenome())


print("Ordenado por Idade")
insertionSortIdade(pessoas)
for i in range(len(pessoas)):
 print("Idade: ", pessoas[i].getIdade())