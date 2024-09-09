"""
=========================================================
Arquivo Principal (main.py)
=========================================================
Este é o arquivo principal do projeto, onde todo o sistema é coordenado. Ele orquestra o rastreamento de mãos, a detecção de 
gestos e a publicação dos dados via MQTT. O programa começa quando o usuário pressiona 'Ctrl+Q' e termina quando 'Q' é pressionado.

Utilidade:
- Controla o fluxo geral do projeto.
- Inicializa os módulos de rastreamento de mão e detecção de gestos.
- Publica os vetores de movimento no broker MQTT em tempo real.
- Permite ao usuário iniciar e parar o programa com atalhos de teclado (Ctrl+Q para iniciar e Q para parar).

Funcionalidades:
- Aguarda o comando do usuário para iniciar o rastreamento e a detecção de gestos.
- Processa as capturas de vídeo e transforma as informações em vetores de movimento.
- Publica os dados via MQTT para que a garra mecânica possa replicar os gestos da mão.

Este arquivo é essencial para o funcionamento do projeto como um todo, unindo os diferentes componentes em uma aplicação coesa.
"""
