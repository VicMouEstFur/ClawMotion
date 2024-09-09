# ClawMotion - In Air Mechanic Claw Controller Through Computational Vision

ClawMotion é um projeto que visa controlar uma garra mecânica utilizando visão computacional para detectar gestos e movimentos das mãos no ar. Usando a biblioteca MediaPipe para rastreamento de mãos e o protocolo MQTT para comunicação em tempo real, o projeto captura movimentos da mão direita e espelha esses gestos na garra mecânica. O controle do sistema pode ser iniciado com `Ctrl+Q` e parado com `Q`.

## Descrição do Projeto

O ClawMotion é dividido em duas partes principais:

1. **Captação de Dados com MediaPipe e Python**
   - A primeira etapa consiste em usar a biblioteca MediaPipe para rastrear a mão direita e detectar movimentos nos eixos X (esquerda/direita), Y (cima/baixo), e Z (frente/trás). O tamanho da mão na tela é usado para estimar a profundidade (eixo Z).
   - Se a mão esquerda estiver visível, a leitura da mão direita é pausada. Quando a mão esquerda sair do campo de visão, a posição da mão direita é considerada a posição inicial (0, 0, 0).

2. **Controle da Garra Mecânica com MQTT**
   - A segunda etapa envolve a conversão dos dados captados em vetores de movimento e envio desses dados para o controlador da garra mecânica via MQTT.
   - O vetor de movimento inclui as coordenadas X, Y, Z e um valor booleano que indica se a mão está aberta (para abrir a garra) ou fechada (para fechar a garra).

## Principais Funcionalidades
- **Rastreamento de Mão Direita**: Detecta a posição da mão direita em tempo real e calcula um vetor de movimento.
- **Controle da Garra**: Baseado no vetor capturado, a garra mecânica realiza movimentos espelhados da mão.
- **Sensibilidade Ajustável**: Permite modificar a sensibilidade dos movimentos para uma resposta mais precisa ou mais suave.
- **Zona Morta**: Implementa uma zona morta para evitar movimentos não intencionais.
- **MQTT em Tempo Real**: O sistema utiliza o protocolo MQTT para transmissão eficiente dos dados de movimento.
- **Teclado de Controle**: `Ctrl+Q` para iniciar e `Q` para parar a execução do programa.

---

## Pastas e Arquivos do Projeto

### mediapipe/
#### hand_tracking.py
Responsável pela captura de dados da mão utilizando MediaPipe. Detecta a posição da mão e retorna as coordenadas X, Y, Z.

#### gesture_detection.py
Detecta os gestos e movimentos da mão direita com base nas posições captadas. Calcula o vetor de movimento levando em consideração a sensibilidade e a zona morta.

#### config.py
Arquivo de configuração contendo valores importantes como sensibilidade, zona morta e período de captação.

### mqtt/
#### mqtt_publisher.py
Responsável por publicar os dados de movimento e estado da garra no broker MQTT, permitindo o controle remoto da garra mecânica.

#### mqtt_config.py
Arquivo de configuração para o MQTT. Contém informações sobre o endereço do broker e o tópico para publicação.

### Outros Arquivos
#### main.py
O arquivo principal que executa o projeto. Coordena a captação de dados com MediaPipe, o cálculo dos vetores de movimento e a publicação via MQTT. A execução pode ser controlada com `Ctrl+Q` para iniciar e `Q` para parar.

#### requirements.txt
Lista de dependências necessárias para o funcionamento do projeto, que podem ser instaladas com o comando `pip install -r requirements.txt`.

---

## Tutorial de Instalação

Para rodar o ClawMotion em seu ambiente local, siga os passos abaixo:

### 1. Instale o Python 3.x
Verifique se o Python está instalado em sua máquina. Você pode verificar digitando o seguinte comando no terminal:

```bash
python --version
