import random

def DistribuicaoPeca(pecaDomino,pecaComparacao):
    domino=0
    quant=28
    while(domino<quant):
        sorteio=random.randint(0,27)
        if(pecaComparacao[sorteio]=='Q'):
            pecaComparacao[sorteio] = pecaDomino[domino]
            domino+=1
    return pecaComparacao

    

def regras():
    print('''   =>O jogo é composto por 28 peças não repetidas, com dois símbolos cada.
   =>Você jogará com três jogadores simulados pelo computador.
   =>Você e os demais jogadores, receberão sete peças cada,
      que foi escolhida aleatoriamente pelo computador.
   =>Você que vai iniciar a partida jogando uma de suas peças.
   =>A partir dessa jogada, cada jogador deverá, em sua vez, escolher uma
      de suas peças para dar continuidade ao jogo. Só serão permitidas
      peças que contenham pelo menos um dos símbolos presentes nas
      extremidades. Cada peça deverá ser posicionada de modo que os
      símbolos iguais fiquem juntos.
   =>Caso o jogador não tenha nenhuma peça com nenhum dos símbolos das
     extremidades, ele perderá sua vez e só poderá jogar na rodada seguinte.
   =>O vencedor será o jogador que conseguir posicionar todas as suas
     peças antes de seus adversários.''')
def entrada():
    print('''       ['P', 'Y']['Y', 'T']['T', 'H']['H', 'O']['O', 'N']
                              PYTHON
   \n\n                   BEM VINDO AO JOGO DE DOMINO''')

