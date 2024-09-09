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
