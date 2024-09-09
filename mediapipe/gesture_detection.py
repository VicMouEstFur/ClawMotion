"""
=========================================================
Gesture Detection Module (gesture_detection.py)
=========================================================
Este arquivo é responsável por detectar os gestos da mão direita com base nas coordenadas capturadas pelo rastreamento de mãos. 
Ele calcula um vetor de movimento que será usado para mover a garra mecânica, considerando a sensibilidade configurada e a zona 
morta para evitar movimentos indesejados.

Utilidade:
- Interpreta as mudanças de posição da mão direita e gera um vetor de movimento.
- Aplica ajustes de sensibilidade para personalizar a resposta da garra aos movimentos da mão.
- Ignora pequenos movimentos baseados na zona morta configurada, garantindo que apenas gestos intencionais sejam reconhecidos.

Funcionalidades:
- Detecta a direção e a magnitude do movimento da mão.
- Atualiza a posição atual da mão para calcular movimentos contínuos.

Este módulo é essencial para traduzir os movimentos físicos da mão em comandos digitais que controlam a garra mecânica.
"""
