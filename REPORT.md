# Relatório

O Mundo de Wumpus é um  jogo antigo de computador considerado um ambiente artificial que fornece grande motivação para o raciocínio lógico.

Baseado em um agente que explora uma caverna, o ambiente consiste de compartimentos conectados por passagens sendo que em um desses compartimentos está o Wumpus: um monstro que devora qualquer um que entrar em seu compartimento. Para piorar a situação, alguns dos compartimentos possuem abismos que engolem qualquer um que entrar neles, menos o Wumpus que é muito grande para cair. A única motivação para o agente permanecer nesse ambiente é a caçada pelo ouro. O Wumpus pode ser morto pelo agente por uma flecha mas este possue somente uma chance de atirar.

Com isso, foi desenvolvido um programa para simular o mundo do Wumpus, na linguagem **Python**. Para implementar o mundo foi usado uma lista de tamanho fixo, e se determinava a posição do ouro e do Wumpus de maneira aleatória utilizando a biblioteca **random** do Python. Nas posições adjacentes ao Wumpus era preenchido a característica do **Fedor** e às adjacentes aos poços era preenchido a **Brisa**. O jogador pode perceber essas características se estiver na sala correspondente e tomar uma decisão.

Portanto, foi possível implementar o simulador do mundo Wumpus com as características propostas, percebendo cada sala com um vetor de estados dos sensores e reagindo a cada estado de uma maneira diferente.