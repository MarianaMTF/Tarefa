def nova_peca(arquivo_pecas, er):
    lista_1=[]
    lista_2=[]
    peca=input("digite a peça que deseja trocar ou vender:")     
    valor=float(input("digite o valor da peça:"))
    mer=input("informe o ER da peça:")
    lista_1.append(mer)
    dicionario={"peça": peca, "valor": valor}
    lista_2.append(dicionario)
    with open(arquivo_pecas, "a")as arquivo:
        for pecas in lista_2:
            for peca, valor in pecas.items():
                arquivo.write(f'{peca}: {valor}')
    with open(er, "a")as arquivo:
        for er in lista_1:
            arquivo.write(er)
    return arquivo_pecas, modelo_ER
