"""
=========================================================
Módulo MQTT (mqtt/__init__.py)
=========================================================
Este arquivo inicializa o módulo MQTT e facilita a importação dos componentes chave, como o `MQTTPublisher`.
"""

from .mqtt_publisher import MQTTPublisher
from .mqtt_config import BROKER, TOPIC