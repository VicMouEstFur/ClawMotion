"""
=========================================================
MQTT Publisher (mqtt_publisher.py)
=========================================================
Este arquivo implementa a lógica para publicar os dados de movimento e o estado da garra mecânica no broker MQTT. Ele é 
responsável por enviar os vetores de movimento calculados e o status da garra (aberta ou fechada) para o dispositivo que 
controla a garra.

Utilidade:
- Publica os dados capturados de movimento da mão em tempo real para o broker MQTT.
- Permite que o controlador da garra receba os vetores de movimento para espelhar os gestos da mão.
- Suporta comunicação assíncrona, ideal para sistemas IoT e dispositivos distribuídos.

Funcionalidades:
- Estabelece conexão com o broker MQTT configurado.
- Publica os dados de movimento periodicamente ou conforme as alterações são detectadas.
- Garante que a comunicação seja estável e confiável para o controle da garra mecânica.

Este arquivo é crucial para a transmissão em tempo real dos dados de controle para a garra mecânica via MQTT.
"""

import paho.mqtt.client as mqtt
from mqtt.mqtt_config import BROKER, TOPIC

class MQTTPublisher:
    def __init__(self):
        """
        Inicializa o cliente MQTT e conecta-se ao broker especificado.
        """
        self.client = mqtt.Client()  # Cria o cliente MQTT
        self.client.connect(BROKER)  # Conecta ao broker usando o endereço especificado em mqtt_config.py

    def publish_data(self, data):
        """
        Publica os dados capturados (vetor de movimento e status da garra) no tópico MQTT especificado.

        Parâmetros:
        - data: Lista contendo as coordenadas X, Y, Z e o estado da garra (aberta/fechada).

        O vetor de dados é convertido em string e enviado para o tópico MQTT definido.
        """
        message = ",".join(map(str, data))  # Converte o array de dados em uma string, separada por vírgulas
        self.client.publish(TOPIC, message)  # Publica a mensagem no tópico MQTT
        print(f"Dados publicados: {message}")  # Imprime os dados publicados para referência