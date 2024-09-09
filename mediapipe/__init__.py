"""
=========================================================
Módulo MediaPipe (mediapipe/__init__.py)
=========================================================
Este arquivo inicializa o módulo MediaPipe e facilita a importação dos componentes-chave, como o rastreador de mãos (HandTracker),
o detector de gestos (GestureDetector), e as configurações (config).
"""

# Importa os componentes essenciais do módulo mediapipe
from .hand_tracking import HandTracker
from .gesture_detection import GestureDetector
from .config import SENSIBILITY, DEAD_ZONE, PERIODO_CAPTACAO
