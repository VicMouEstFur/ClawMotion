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
from .config import SENSIBILITY, DEAD_ZONE

class GestureDetector:
    def __init__(self):
        """
        Inicializa o detector de gestos e define a posição inicial como [0, 0, 0].
        A posição inicial é usada para calcular o movimento em relação ao ponto de origem.
        """
        self.current_position = [0, 0, 0]

    def detect_movement(self, new_position):
        """
        Detecta o movimento da mão, calcula o vetor de movimento e aplica a sensibilidade e a zona morta.

        Parâmetros:
        - new_position: Lista [x, y, z] com a nova posição da mão capturada pelo rastreamento.

        Retorna:
        - Vetor de movimento ajustado pela sensibilidade e zona morta.
        """
        # Calcula a diferença entre a nova posição e a posição atual (vetor de movimento)
        movement_vector = [
            new_position[0] - self.current_position[0],  # Diferença em X
            new_position[1] - self.current_position[1],  # Diferença em Y
            new_position[2] - self.current_position[2],  # Diferença em Z (profundidade)
        ]

        # Aplica o fator de sensibilidade ao vetor de movimento
        movement_vector = [v * SENSIBILITY for v in movement_vector]

        # Aplica a zona morta para ignorar movimentos muito pequenos
        movement_vector = [
            v if abs(v) > DEAD_ZONE[i] else 0  # Se o valor for menor que a zona morta, ignora o movimento
            for i, v in enumerate(movement_vector)
        ]

        # Atualiza a posição atual da mão
        self.current_position = new_position

        # Retorna o vetor de movimento ajustado
        return movement_vector