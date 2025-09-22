print('---------------------------------------------------------------------------------')
print('-                   GAME ACERTE O DESAFIO DAS 10 PERGUNTAS                      -')
print('-                       DESENVOLVIDO POR HILDEBRANDO                            -')
print('---------------------------------------------------------------------------------')
print(' ')
print('INSTRUÇÕES:')
print('DICA: responda copiando a alternativa e cole na resposta e aperte enter.')
print('Boa Sorte!!! =]')
print(' ')

questions = [
    {
        'question': '1- (Fácil): Qual componente do computador é responsável por processar os dados e executar os programas?',        
        'options': ['Memória RAM', 'CPU', 'Placa-Mãe', 'Fonte de Alimentação', 'Placa de Vídeo'],
        'response': 'CPU',
    },
    {
        'question': '2- (Fácil): Qual tipo de memória é volátil e perde as informações quando o computador é desligado?',
        'options': ['Memória ROM', 'Memória RAM', 'Memória Cache', 'HD', 'SSD'],
        'response': 'Memória RAM',
    },
    {
        'question': '3- (Fácil): Qual das alternativas a seguir é uma forma de armazenamento permanente e não volátil?',
        'options': ['Memória RAM', 'Cache L1', 'SSD', 'Memória Cache L2', 'Registradores do Processador'],
        'response': 'SSD',
    },
    {
        'question': '4- (Fácil): O que é a BIOS em um computador?',
        'options': ['Sistema Operacional', 'Processador Principal', 'O Software de Inicialização do Sistema',
                    'Memória Principal', 'Placa de Vídeo'],
        'response': 'O Software de Inicialização do Sistema',
    },
    {
        'question': '5- (Médio): Qual a principal função da placa-mãe em um computador?',
        'options': ['Armazenar Dados Permanentemente', 'Controlar o Desempenho Gráfico', 
                    'Interligar Todos os Componentes do Computador', 'Refrigeração do Processador',
                    'Prover Fontes de Energia para a CPU'],
        'response': 'Interligar Todos os Componentes do Computadoa',
    },
    {
        'question': '6- (Médio): Qual é a diferença entre a memória DDR3 e DDR4?',
        'options': ['DDR4 tem uma frequência maior e consome menos energia que DDR3', 
                    'DDR3 tem mais capacidade de armazenamento',
                    'DDR4 é mais barata e tem maior latência',
                    'DDR3 é mais rápida que DDR4',
                    'DDR3 é uma memória não volátil, enquanto DDR4 é volátil'],
        'response': 'DDR4 tem uma frequência maior e consome menos energia que DDR3',
    },
    {
        'question': '7- (Médio): O que é a placa de vídeo (GPU) de um computador?',
        'options': ['Um componente de armazenamento de dados',
                    'Um dispositivo que controla as conexões de rede',
                    'Um chip responsável pelo processamento gráfico e exibição de imagens',
                    'A unidade responsável pela execução de cálculos matemáticos',
                    'componente que armazena o sistema operacional'],
        'response': 'Um chip responsável pelo processamento gráfico e exibição de imagens',
    },
    {
        'question': '8- (Médio): O que é o barramento PCIe (Peripheral Component Interconnect Express)?',
        'options': ['Um tipo de memória RAM', 'Uma conexão para unidades de armazenamento externas',
                    'Um protocolo de comunicação entre o processador e os dispositivos de entrada',
                    'Um tipo de conexão de alta velocidade entre a placa-mãe e os componentes como GPU e SSD',
                    'Um modelo de chip para placas-mãe'],
        'response': 'Um tipo de conexão de alta velocidade entre a placa-mãe e os componentes como GPU e SSD',
    },
    {
        'question': '9- (Difícil): Em um processador, o que é a técnica de "Hyper-Threading"?',
        'options': ['Uma técnica que aumenta o número de núcleos físicos do processador',
                    'Uma tecnologia que permite que cada núcleo do processador execute dois threads simultaneamente',
                    'Uma função que melhora a capacidade de refrigeração do processador',
                    'Um recurso que reduz o consumo de energia do processador',
                    'Uma tecnologia usada para melhorar o desempenho gráfico do processador'],
        'response': 'Uma tecnologia que permite que cada núcleo do processador execute dois threads simultaneamente',
    },
    {
        'question': '10- (Difícl): O que é a diferença entre SATA II e SATA III em relação ao armazenamento?',
        'options': ['SATA III oferece maior capacidade de armazenamento que SATA II', 
                    'ATA III oferece uma velocidade de transferência de dados mais alta que SATA II',
                    'SATA II não é compatível com SSDs',
                    'SATA III só pode ser usado com unidades de armazenamento mecânicas',
                    'SATA II e SATA III são idênticos em desempenho, sem diferenças perceptíveis'],
        'response': 'SSD',
    },  
]
 
quest_set = 0
quest_miss = 0
 
for quest_count in range(len(questions)):
    question = questions[quest_count]['question']
    option = questions[quest_count]['options']
    response = questions[quest_count]['response']
    
    print(f'\n{question}\n{option[0]}\n{option[1]}\n{option[2]}\n{option[3]}')
    get_response = input('--> ')
    
    if get_response == response:
        print('\nAcertou')
        quest_set += 1
    else:
        print('\nErrou')
        quest_miss += 1
    
print(f'Você acertou {quest_set} de {len(questions)} perguntas!')
