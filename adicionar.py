def adicionar_peca(arquivo_pecas, er):
  lista_1=[]
  lista_2=[]
  while True:
    peca=input("digite a peça que deseja trocar ou vender(digite sair para encerrar):")
    if peca == "sair":
      break
    valor=float(input("digite o valor da peça:"))
    mer=input("informe o ER da peça:")
    lista_1(mer)
    dicionario={"peça":peca, "valor":valor}
    lista_2.append(dicionario)
  with open(arquivo_pecas, "w") as arquivo:
    for pecas in lista_2:
      for peca, valor in pecas.items():
        arquivo.write(f'{peca}: {valor}')
  with open(er, 'w') as arquivo:
    for mer in er:
      arquivo.write(mer)
  return arquivo_pecas, er
