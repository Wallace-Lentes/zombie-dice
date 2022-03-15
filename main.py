import random
#Nome do jogo.
print("Zombie Dice")
#Regras do jogo.
print("REGRAS: Este jogo inclui estas regras, 13 dados e um tubo para guardá-los. Você precisa marcar seus pontos de alguma maneira. Dois ou mais jogadores podem jogar."
      "\n O primeiro jogador será aquele que venceu a última partida ou a pessoa que falar Céééééérebros da maneira mais zumbi possível."
      "\n No seu turno, agite o tubo e pegue 3 dados, sem olhar. Role os dados."
      "\n Cada um deles representa uma pobre vítima a ser atacada. Os dados vermelhos são os mais difíceis. Os verdes são os mais fáceis e os amarelos são médios."
      "\n Os dados possuem 3 símbolos:"
      "\n Cérebro – Você devorou o cérebro de sua vítima. Separe os dados de Cérebro na sua esquerda."
      "\n Espingarda – Sua vítima revidou! Separe os dados de Espingarda na sua direita."
      "\n Pegadas – Sua vítima escapou. Fique com os dados de Pegadas na sua frente. Se você escolher rolar dados novamente, você vai re-rolar esses dados, juntamente com novos dados suficientes para rolar sempre 3 dados."
      "\n Se você tiver 3 dados com a face da Espingarda virada para cima na mesa, em qualquer momento, seu turno acabou. Caso contrário, você pode optar por parar e marcar pontos ou continuar."
      "\n Se você decidir parar, marque 1 ponto por cada Cérebro que você tem, e coloque todos os dados de volta no tubo. O próximo jogador inicia seu turno."
      "\n Se você escolher continuar, você não devolve os dados ao tubo. Sempre que você rolar dados, você vai rolar três por vez. Primeiro, você deverá pegar todas as Pegadas que estejam à sua frente, depois, pegue dados suficientes do tubo (se for preciso) até completar três e role-os novamente."
      "\n Depois de pegar novos dados, você não pode decidir parar...você tem que rolar."
      "\n Separe os Cérebros e as Espingardas como explicado acima. Se você rolar a terceira Espingarda seu turno acaba e você não marca pontos. Caso contrário, você pode parar e marcar pontos, ou rolar os dados novamente..."
      "\n Se você não tiver 3 dados sobrando no tubo, anote quantos Cérebros você tinha e coloque esses dados de volta no tubo (mantenha as Espingardas na mesa). É só continuar..."
      "\n Jogue até alguém chegar a 13 Cérebros. Termine a rodada (todos devem jogar o mesmo número de turnos). Quem tiver devorado mais Cérebros até o ¬final dessa rodada é o vencedor. Se houver um empate, os líderes (apenas) jogam uma rodada de desempate."
)
print("Bem-vindos ao jogo!")

# Definir quantidade de no minimo 2 jogadores.
numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input("Digite quantidade de jogadores: "))

    if numJogadores < 2:
        print("Necessario ao menos 2 jogadores")

#Dar nome aos jogadores, sendo iniciado conforme as regras.
print("Iniciar o jogo com quem falou 'Cérebros' da maneira mais zumbi possível ou vencedor da ultima partida.")
listaJogadores = []
for i in range(numJogadores):
    nome = input("Informe o nome do jogaodr: " + str(i + 1) + ":")

    listaJogadores.append(nome)
print(listaJogadores)


#Os lados dos dados são "C= cerebro, P= passo, T= tiro."
from random import randint
dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"
#os 13 dados dentro do copo.
copoDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
             dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
             dadoVermelho, dadoVermelho, dadoVermelho]

#Mostrar os dados e os suas faces.
print("Quantidade de dados e seus lados:")
print(copoDados)
print("Sendo 13 dados com as faces 'C= cerebros, P= passos, T= tiros.'")

#Comando para dar inicio ao jogo.
str(input("Pressione 'Enter' para dar inicio ao jogo:"))
print("jogo iniciado.")

#Tabela de pontuação
dadosSorteados = []
jogadorAtual = 0
espingardas = 0
cerebros = 0
pegadas = 0
while True:
    print("Turno do jogador(a): {}".format( listaJogadores[jogadorAtual] ))
    str(input("Pressione 'S' para sortear dados do copo: ")).strip().upper()

    for i in range(0, 3, 1):
        numSorteado = random.randint(0,12)
        dadoSorteado = copoDados[numSorteado]

        if dadoSorteado == "CPCTPC":
            corDado = "Verde"
        elif dadoSorteado == "TPCTPC":
            corDado = "Amarelo"
        else:
            corDado = "Vermelho"
        print("A cor do " + str(i + 1) +" dado sorteado foi: {}".format(corDado))
        dadosSorteados = dadoSorteado

    print("Sortear faces dos dados " + str(input("Pressione 'S' para jogar dados: ")).strip().upper())
    print("Faces sorteadas foram: ")

    for i in range(0,3,1):
        faceSorteada = random.choice(dadosSorteados)
        if faceSorteada == "C":
            print("Cérebro- Você comeu um Cérebro!!!")
            cerebros = cerebros +1
        elif faceSorteada == "T":
            print("Espingarda- você levou um Tiro!!!")
            espingardas = espingardas + 1
        else:
            print("Pegada- Sua vitima escapou!!!")
            pegadas = pegadas + 1

    print("Pontuação atual.")
    print("Cérebros: {}".format(cerebros))
    print("Tiros: {}".format(espingardas))
    print("Passos: {}".format(pegadas))

#Se o jogador deciidir continuar jogando
    continuarTurno = str(input("Para continuar jogando dados pressione 'S' ou pressione 'N' para parar: ")).strip().upper()

#Caso jogador decida parar sua vez, passar para o proximo jogador.
    if continuarTurno == "N":
        jogadorAtual = jogadorAtual + 1
        dadosSorteados = []
        espingardas = 0
        cerebros = 0
        pegadas = 0
        if jogadorAtual == len(listaJogadores):
            print("Primeira parte para semana 4 finalizada!")
            break
        else:
            print("Iniciando rodada com jogador atual: ")
            dadosSorteados = []


