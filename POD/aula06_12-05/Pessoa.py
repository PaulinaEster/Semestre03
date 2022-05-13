
class Pessoa:
  def __init__(self, id, nome, sobrenome, idade):
    self.id = id
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

  def getId(self):
    return self.id
  
  def getNome(self):
    return self.nome

  def getSobrenome(self):
    return self.sobrenome

  def getIdade(self):
    return self.idade

  def setId(self, id):
    self.id = id
  
  def setNome(self, nome):
    self.nome = nome

  def setSobrenome(self, sobrenome):
    self.sobrenome = sobrenome

  def setIdade(self, idade):
    self.idade = idade

  