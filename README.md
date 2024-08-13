# DAPy - Down Apache with Python

DAPy é uma ferramenta Python multifuncional para realizar escaneamento de portas e ataques DDoS em plataformas Linux. 

## Funcionalidades

- **Escaneamento de Portas**: Verifica as portas abertas em um endereço IP alvo dentro de um intervalo de portas especificado pelo usuário.
- **Ataque DDoS**: Executa um ataque DDoS simples em um servidor Apache2, enviando múltiplas requisições para um IP e porta específicos.

## Requisitos

Este script foi desenvolvido em Python 3 e não requer bibliotecas adicionais além das padrão, portanto, não há dependências extras a serem instaladas.

## Instalação

1. Clone este repositório:

   git clone https://github.com/freitasec/dapy.git

2. Navegue até o diretório do repositório:

   cd dapy
   
3. (Opcional) Crie e ative um ambiente virtual:

   python3 -m venv venv
   
   source venv/bin/activate
   
## Uso

1. Execute diretamente o script:

   python3 dapy.py

## Aviso Legal
Este software é destinado exclusivamente para fins educacionais e de teste em ambientes controlados. O uso inadequado, especialmente em ataques DDoS, pode ser ilegal e resultar em graves consequências legais. Use esta ferramenta com responsabilidade e apenas em sistemas para os quais você tenha permissão explícita.
