def apresentar_pecas(arquivo_pecas, er):
  with open(arquivo_pecas, "r")as arquivo:
    for linha in arquivo:
      chave, valor=linha.strip().split(':')
      print(f'{chave}: R${valor}')
  with open(er, "r") as arquivo:
    for linha in arquivo:
      print(linha)
