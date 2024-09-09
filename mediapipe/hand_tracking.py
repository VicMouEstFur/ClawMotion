"""
=========================================================
Hand Tracking Module (hand_tracking.py)
=========================================================
Este arquivo contém a implementação do rastreamento da mão usando a biblioteca MediaPipe. Ele é responsável por capturar a 
posição da mão direita e calcular as coordenadas X, Y e Z.

Utilidade:
- Detecta a presença da mão direita no campo de visão da câmera.
- Calcula a posição da mão nos eixos X (horizontal), Y (vertical) e Z (profundidade).
- Fornece essas coordenadas para outros módulos, como o de detecção de gestos e controle da garra mecânica.

Funcionalidades:
- Inicializa o rastreador de mãos utilizando a solução de rastreamento de mãos do MediaPipe.
- Processa o vídeo em tempo real e retorna as coordenadas da mão direita, ou retorna 'None' se a mão não for detectada.

Este módulo é fundamental para a captação de movimentos que serão espelhados pela garra mecânica.
"""
