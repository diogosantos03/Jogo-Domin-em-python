



#                                                                     >>DIOGO SANTOS<<

import BBdomino



pecaComparacao=['Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q','Q']
pecaDomino=[['P','P'],['Y','Y'],['T','T'],['H','H'],['O','O'],['N','N'],['$','$'],
             ['P','Y'],['Y','T'],['T','H'],['H','O'],['O','N'],['N','$'],['P','T'],
             ['Y','H'],['T','O'],['H','N'],['O','$'],['P','H'],['Y','O'],['T','N'],
             ['H','$'],['P','O'],['Y','N'],['T','$'],['P','N'],['Y','$'],['P','$']]

#------------------------------------------------------------
BBdomino.DistribuicaoPeca(pecaDomino,pecaComparacao)
#chama a funçao que sorteia as peças.
#---------------------------------------------------------------------------------
jogador1=pecaComparacao[0:7]
jogador2=pecaComparacao[7:14]#dividindo sete peças p/ cada que estão na lista pecadomino e add em pecacomparação
jogador3=pecaComparacao[14:21]
jogador4=pecaComparacao[21:28]
#-------------------------------------------------------------

PRINT=BBdomino.entrada()#chama a fun... com os prints de entrada
#---------------------------------------------------------------
print('\n\n\nSuas peças são essas:',jogador1)










ultimajogada1=[]
jogadores=['play2','play3','play4']


name=str.upper(input('\n\nDigite seu nome:'))
jogadores.insert(0,name)
#----------------------
jogada=str.upper(input('\n\nSe quiser saber das regras digite REGRAS.\n\nVai iniciar jogando qual peça?\n\nDigite uma peça que tenha em mãos: '))
ganhador=[]

cont=0
pare=0
#-----------------------------------------------------------------------------------------------------------------------------------------------
play1=[['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q']]
play2=[['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q']]
play3=[['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q']]#Esse elementos serão substituidos pelos elementos de jogador1,2,3 e 4.
play4=[['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q'],['Q','Q']]
#---------------------------------------------------------------------------------------------------------------------------------------------
while(jogada!='SAIR')and(pare<=0):
    PecaJogada=[]
    add=[]
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    add.append(jogada[:1])
    add.append(jogada[1:2])#add a primeira e seg.. letra digitada a list ADD e depois a list PECAJOGADA
    PecaJogada=[add]#-----------------------------------------------------------------------------------------------------------------------------                                                                
    if(jogada=='REGRAS'):
        Regras=BBdomino.regras()
        jogada=str.upper(input('vai iniciar jogando qual peça?'))
    elif(PecaJogada[0] not in jogador1):#tratamento de erros.
        print('Vc não tem essa peça!')
        jogada=str.upper(input('vai iniciar jogando qual peça?'))
    else:#---------------------------------------------------------------------------------------------------------------------------------------------
        cont+=1
        if(cont==1):#add os elementos de uma lista p/ outra.
            for q in range(len(jogador1)):
                play1[q]=jogador1[q]
#-----------------------------------------------------------------------------------------------------------------------------------------------------
            for s in range(len(play1)):
                if(play1[s]==PecaJogada[0]):
                    ultimajogada1.append(play1[s])
                    play1.remove(PecaJogada[0])#---
                    break
                else:
                    PecaJogada[0].reverse()
                    if(play1[s]==PecaJogada[0]):
                        ultimajogada1.append(play1[s])
                        play1.remove(PecaJogada[0])#---
                        break
    #-------------------------------------------------------------------------------------------------------------------------------------
        if(cont>1):#Apartir da segunda jogada, virá para esse bloco.
            if(PecaJogada[0][0]==ultimajogada1[(len(ultimajogada1)-1):len(ultimajogada1)][0][1]):#compara a estremidade das peças jogadas à direita.
                print(ultimajogada1[(len(ultimajogada1)-1):len(ultimajogada1)][0])
                if(PecaJogada[0] not in play1):
                    print('não digite invertido')
                else:
                    ultimajogada1.append(PecaJogada[0])                   
                    play1.remove(PecaJogada[0]) 
                
            elif(PecaJogada[0][1]==ultimajogada1[(len(ultimajogada1)-1):len(ultimajogada1)][0][1]):#compara a estremidade das peças jogadas à direita.
                if(PecaJogada[0] not in play1):
                   print('não digite invertido')
                else:
                    play1.remove(PecaJogada[0])
                    PecaJogada[0].reverse()
                    ultimajogada1.append(PecaJogada[0])
            
            elif(PecaJogada[0][0]==ultimajogada1[0][0]): #compara a estremidade das peças jogadas à esquerda.            
                if(PecaJogada[0] not in play1):
                   print('não digite invertido')
                else:
                    play1.remove(PecaJogada[0])
                    PecaJogada[0].reverse()
                    ultimajogada1.insert(0,PecaJogada[0])
                
            elif(PecaJogada[0][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                if(PecaJogada[0] not in play1):
                   print('não digite invertido')
                else:
                    ultimajogada1.insert(0,PecaJogada[0])
                    play1.remove(PecaJogada[0])
    #-------------------------------------------------------------------------------------------------------------------------------------------------                           
                          
        if(len(play1)==0):#aqui ira comparar se o jogador ainda tem peças, contar para o fim do loop e add o nome do jogador a uma lista que sera exibida o
            pare+=1#nome dele, se caso for o vencedor.
            ganhador.append(jogadores[0])
    #----------------------------------------------------------------------------------------------------------------------------------------------------        
        if(cont==1):#add os elementos de uma lista p/ outra.
            for g in range(len(jogador2)):
                play2[g]=jogador2[g]
         
#-------------------------------------------------------------------------------------------------------------------------------------------
        for d in range(len(play2)):
            if(play2[d][0]==ultimajogada1[len(ultimajogada1)-1][1]):#compara a estremidade das peças jogadas à direita.
                print(play2[d],'play2')
                ultimajogada1.append(play2[d])
                del(play2[d])
                break
            elif(play2[d][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                print(play2[d],'play2')
                ultimajogada1.insert(0,play2[d])
                del(play2[d])
                break
            else:#acima irá comparar as estremidades das peças que ja foram jogadas, se não for compatível com a peça do play2, fará a intrução abaixo.
                play2[d].reverse()
                if(play2[d][0]==ultimajogada1[len(ultimajogada1)-1][1]):#compara a estremidade das peças jogadas à direita.
                    print(play2[d],'play2')
                    ultimajogada1.append(play2[d])
                    del(play2[d])
                    break
                elif(play2[d][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                    print(play2[d],'play2')
                    ultimajogada1.insert(0,play2[d])
                    del(play2[d])
                    break
   #----------------------------------------------------------------------------------------------------------------------------  
        if(len(play2)==0):#aqui ira comparar se o jogador ainda tem peças, contar para o fim do loop e add o nome do jogador a uma lista que sera exibida o
            pare+=1#nome dele, se caso for o vencedor.
            ganhador.append(jogadores[1])
    #---------------------------------------------------------------------------------------------------------------          
        if(cont==1):#add os elementos de uma lista p/ outra.
            for o in range(len(jogador3)):
                play3[o]=jogador3[o]
#-----------------------------------------------------------------------------------------------------------------------------
        for f in range(len(play3)):
            if(play3[f][0]==ultimajogada1[len(ultimajogada1)-1][1]):#compara a estremidade das peças jogadas à direita.
                print(play3[f],'play3')
                ultimajogada1.append(play3[f])
                del(play3[f])
                break
            elif(play3[f][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                print(play3[f],'play3')
                ultimajogada1.insert(0,play3[f])
                del(play3[f])
                break
            else:#acima irá comparar as estremidades das peças que ja foram jogadas, se não for compatível com a peça do play3, fará a intrução abaixo.
                play3[f].reverse()
                if(play3[f][0]==ultimajogada1[len(ultimajogada1)-1][1]):#compara a estremidade das peças jogadas à direita.
                    print(play3[f],'play3')
                    ultimajogada1.append(play3[f])
                    del(play3[f])
                    break
                elif(play3[f][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                    print(play3[f],'play3')
                    ultimajogada1.insert(0,play3[f])
                    del(play3[f])
                    break
#-------------------------------------------------------------------------------------------------------------------
        if(len(play3)==0):#aqui ira comparar se o jogador ainda tem peças, contar para o fim do loop e add o nome do jogador a uma lista que sera exibida o
            pare+=1#nome dele, se caso for o vencedor.
            ganhador.append(jogadores[2])
    #---------------------------------------------------------------------------------------------------------------
        if(cont==1):#add os elementos de uma lista p/ outra.
            for w in range(len(jogador4)):
                play4[w]=jogador4[w]
#-------------------------------------------------------------------------------------------------------------------------
        for h in range(len(play4)):
            if(play4[h][0]==ultimajogada1[len(ultimajogada1)-1][1]):#compara a estremidade das peças jogadas à direita.
                print(play4[h],'play4')
                ultimajogada1.append(play4[h])
                del(play4[h])
                break
            elif(play4[h][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                print(play4[h],'play4')
                ultimajogada1.insert(0,play4[h])
                del(play4[h])
                break
            else:#acima irá comparar as estremidades das peças que ja foram jogadas, se não for compatível com a peça do play2, fará a intrução abaixo.
                play4[h].reverse()
                if(play4[h][0]==ultimajogada1[len(ultimajogada1)-1][1]):#compara a estremidade das peças jogadas à direita.
                    print(play4[h],'play4')
                    ultimajogada1.append(play4[h])
                    del(play4[h])
                    break
                elif(play4[h][1]==ultimajogada1[0][0]):#compara a estremidade das peças jogadas à esquerda.
                    print(play4[h],'play4')
                    ultimajogada1.insert(0,play4[h])
                    del(play4[h])
                    break
#---------------------------------------------------------------------------------------------------------------------
        if(len(play4)==0):#aqui ira comparar se o jogador ainda tem peças, contar para o fim do loop e add o nome do jogador a uma lista que sera exibida o
            pare+=1#nome dele, se caso for o vencedor.
            ganhador.append(jogadores[3])
#--------------------------------------------------------------------------------------------------------------------
        print('\n\n\nPeças jogadas:',ultimajogada1)
        print('\n\nSuas peças',name,play1,'\n\n')
        jogada=str.upper(input('Digite mais uma peça: '))
if(jogada=='SAIR'):
    print('\n\n\nVocê acabou de sair, volte sempre!') #Saída jogo.
else:
    print('\n\n\n',ganhador[0],'é o vencedor!')
         
#--------------------------------------------------------------------------------------------------------------------
