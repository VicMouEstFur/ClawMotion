"""
=========================================================
Configurações do MQTT (mqtt_config.py)
=========================================================
Este arquivo contém as configurações relacionadas ao protocolo MQTT. Ele define o endereço do broker MQTT, o tópico utilizado 
para a comunicação e quaisquer outros parâmetros necessários para estabelecer e manter a conexão com o broker.

Utilidade:
- Armazena as configurações do broker MQTT, como o endereço IP e a porta de conexão.
- Define o tópico para publicação, permitindo que a garra mecânica receba os dados corretamente.
- Centraliza as configurações do MQTT para facilitar a manutenção e ajustes futuros.

Funcionalidades:
- Facilita a configuração e alteração do broker MQTT sem necessidade de modificar outros arquivos no projeto.
- Garante que as informações de conexão e comunicação estejam centralizadas e organizadas.

Este arquivo é importante para garantir que o sistema de controle da garra esteja conectado corretamente ao broker MQTT.
"""
# Endereço do broker MQTT (pode ser o IP local ou o endereço de um servidor MQTT remoto)
BROKER = 'localhost'  # Substitua por 'seu.broker.mqtt' ou o IP do seu broker

# Tópico no qual os dados de movimento serão publicados
TOPIC = 'garra/movimentos'