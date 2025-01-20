import socket

def log(message):
    """Функция для вывода логов с отметкой времени."""
    import datetime
    now = datetime.datetime.now()
    print(f"{now} - {message}")

def run_client():
    """Основная функция клиента."""
    sock = socket.socket()
    try:
        log("Соединение с сервером...")
        sock.connect(('localhost', 9090))
        log("Соединение с сервером установлено")

        while True:
            message = input("Введите сообщение (или 'exit' для завершения): ")
            
            log(f"Отправка данных серверу: {message}")
            sock.send(message.encode('utf-8'))

            if message.lower() == 'exit':
                break

            data = sock.recv(1024)
            if not data:
                log("Разрыв соединения с сервером (сервер закрыл соединение).")
                break
            
            decoded_data = data.decode('utf-8')
            log(f"Прием данных от сервера: {decoded_data}")
    
    except ConnectionRefusedError:
            log("Ошибка соединения: Сервер недоступен или не запущен.")
    except Exception as e:
        log(f"Ошибка клиента: {e}")
    finally:
        sock.close()
        log("Разрыв соединения с сервером (клиент закрыл соединение).")

if __name__ == "__main__":
    run_client()