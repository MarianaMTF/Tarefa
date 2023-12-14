from adicionar import adicionar_peca
from adicionar_nova import nova_peca
from apresentar import apresentar_pecas

if __name__ == "__main__":
    arquivo_pecas = "pecas.txt"
    er = "modeloER.txt"
    while True:
        r=int(input("digte 1 para adicionar uma peça e seu valor, 2 para adicionar uma nova peça, 3 para ver as peças, 0 para encerrar:"))
        if r==1:
            adicionar_peca(arquivo_pecas, er)
        elif r==2:
            nova_peca(arquivo_pecas, er)
        elif r==3:
            apresentar_pecas(arquivo_pecas, er)
        elif r==4:
            break
