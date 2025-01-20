import socket

def log(message):
    """Функция для вывода логов с отметкой времени."""
    import datetime
    now = datetime.datetime.now()
    print(f"{now} - {message}")

def run_server():
    """Основная функция сервера."""
    log("Запуск сервера")
    sock = socket.socket()
    sock.bind(('localhost', 9090))
    sock.listen(1)
    log("Начало прослушивания порта 9090")
    
    try:
        while True:  # Бесконечный цикл для принятия новых подключений
            conn, addr = sock.accept()
            log(f"Подключение клиента: {addr}")
            
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        log(f"Отключение клиента: {addr} (соединение разорвано)")
                        break  # Клиент разорвал соединение
                    
                    decoded_data = data.decode('utf-8')
                    log(f"Прием данных от клиента {addr}: {decoded_data.strip()}")
                    
                    if decoded_data.strip().lower() == 'exit':
                       log(f"Отключение клиента: {addr} (получена команда exit)")
                       break  # Клиент отправил "exit"
                       
                    response_data = data.upper()
                    conn.send(response_data)
                    log(f"Отправка данных клиенту {addr}: {response_data.decode('utf-8').strip()}")

            except Exception as e:
                log(f"Ошибка при обработке клиента: {e}")
            finally:
                conn.close()
                
    except KeyboardInterrupt:
        log("Остановка сервера (пользователем)")
    except Exception as e:
        log(f"Ошибка сервера: {e}")
    finally:
        sock.close()
        log("Остановка сервера (завершение)")


if __name__ == "__main__":
    run_server()