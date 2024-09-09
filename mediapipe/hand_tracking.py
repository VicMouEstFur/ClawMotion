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
import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        """
        Inicializa o rastreador de mãos usando MediaPipe e configura o ambiente de rastreamento.
        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,  # Detecta apenas uma mão
                                         min_detection_confidence=0.7)
        self.mp_drawing = mp.solutions.drawing_utils  # Utilitário para desenhar a mão nas imagens

    def get_hand_position(self, frame):
        """
        Processa o frame da câmera e detecta a posição da mão direita.

        Parâmetros:
        - frame: Frame de vídeo capturado pela câmera.

        Retorna:
        - Vetor [x, y, z] representando a posição da mão direita (se detectada).
        - None se nenhuma mão for detectada.
        """
        # Converte o frame de BGR (usado pelo OpenCV) para RGB (usado pelo MediaPipe)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Processa o frame para detectar as mãos
        results = self.hands.process(frame_rgb)

        # Verifica se há alguma mão detectada
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Desenha os pontos da mão no frame (opcional)
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # Coleta as coordenadas de um ponto chave (neste caso, o ponto central da palma da mão)
                x = hand_landmarks.landmark[0].x  # Coordenada X
                y = hand_landmarks.landmark[0].y  # Coordenada Y
                z = hand_landmarks.landmark[0].z  # Coordenada Z (aproximada, usada para profundidade)

                # Converte as coordenadas relativas para coordenadas absolutas (pixel)
                h, w, _ = frame.shape
                x_abs = int(x * w)  # Coordenada X em pixels
                y_abs = int(y * h)  # Coordenada Y em pixels
                z_abs = z  # A profundidade em Z é mantida como está (sem conversão para pixels)

                return [x_abs, y_abs, z_abs]

        return None  # Retorna None se nenhuma mão for detectada