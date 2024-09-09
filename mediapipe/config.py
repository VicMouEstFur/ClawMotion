"""
=========================================================
Configurações do Projeto (config.py)
=========================================================
Este arquivo contém as configurações globais do projeto. Ele define parâmetros como a sensibilidade dos movimentos, a zona morta 
e o período de captação de dados. Essas configurações são usadas em todo o projeto para ajustar o comportamento dos módulos de 
detecção de gestos e controle da garra.

Utilidade:
- Permite ajustar a sensibilidade dos movimentos, influenciando o quanto a garra se move em resposta aos gestos da mão.
- Define a zona morta, que evita a detecção de movimentos muito pequenos ou involuntários.
- Especifica o intervalo de tempo entre as capturas de posição da mão, controlando a frequência de atualização do sistema.

Funcionalidades:
- Facilita a personalização do comportamento do sistema sem a necessidade de alterar diretamente o código dos módulos.
- Fornece parâmetros que são utilizados em várias partes do projeto, garantindo consistência no processamento dos dados.

Este arquivo é importante para permitir ajustes finos no funcionamento do sistema de controle da garra.
"""
