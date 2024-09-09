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
import time
import cv2
import keyboard  # Biblioteca para detectar teclas pressionadas

# Importa os componentes do módulo mediapipe
from mediapipe import HandTracker, GestureDetector, PERIODO_CAPTACAO

# Importa os componentes do módulo MQTT
from mqtt import MQTTPublisher, BROKER, TOPIC

def get_frame_from_camera():
    """
    Função para capturar o frame da câmera em tempo real.
    Retorna o frame capturado pela webcam.
    """
    cap = cv2.VideoCapture(0)  # Usa a câmera padrão
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar imagem da câmera.")
        return None
    return frame

def check_if_hand_is_open(frame):
    """
    Função simulada para determinar se a mão está aberta ou fechada.
    (Esta função precisaria ser implementada corretamente usando a detecção da mão aberta.)
    
    Retorna:
    - True se a mão estiver aberta.
    - False se a mão estiver fechada.
    """
    # Simulação: sempre retornando True para simplificar
    return True

def main():
    print("Pressione Ctrl+Q para iniciar e Q para parar.")
    
    # Aguarda o usuário pressionar Ctrl+Q para iniciar
    keyboard.wait('ctrl+q')

    # Inicializa os componentes do sistema
    hand_tracker = HandTracker()
    gesture_detector = GestureDetector()
    mqtt_publisher = MQTTPublisher()

    print("Iniciando o controle da garra. Pressione 'Q' para parar.")

    # Inicia a captura de frames da câmera
    cap = cv2.VideoCapture(0)  # Usa a câmera padrão

    try:
        while True:
            # Verifica se a tecla 'q' foi pressionada para interromper a execução
            if keyboard.is_pressed('q'):
                print("Encerrando o programa.")
                break

            # Captura o frame da câmera
            ret, frame = cap.read()
            if not ret:
                print("Falha ao capturar imagem da câmera.")
                continue

            # Obtém a posição da mão direita
            hand_position = hand_tracker.get_hand_position(frame)
            
            if hand_position:
                # Detecta o vetor de movimento com base na posição da mão
                movement_vector = gesture_detector.detect_movement(hand_position)
                # Verifica se a mão está aberta ou fechada
                is_open = check_if_hand_is_open(frame)
                # Cria um array de dados para enviar via MQTT
                data = movement_vector + [is_open]
                # Publica os dados no broker MQTT
                mqtt_publisher.publish_data(data)
            
            # Pausa por um período definido (em segundos)
            time.sleep(PERIODO_CAPTACAO)

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")

    finally:
        # Libera a câmera quando o programa terminar
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
