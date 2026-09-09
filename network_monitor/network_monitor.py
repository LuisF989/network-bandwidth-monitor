import time
import psutil
import os

def bytes_to_human(n_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if n_bytes < 1024.0:
            return f"{n_bytes:.2f} {unit}"
        n_bytes /= 1024.0
    return f"{n_bytes:.2f} PB"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def monitor_network(interval: int = 1):
    print("Iniciando monitor de red... Obteniendo datos de las interfaces.")
    time.sleep(1)

   
    net_io = psutil.net_io_counters()
    bytes_sent_prev = net_io.bytes_sent
    bytes_recv_prev = net_io.bytes_recv

    try:
        while True:
            time.sleep(interval)
            clear_screen()

          
            net_io_now = psutil.net_io_counters()
            bytes_sent_now = net_io_now.bytes_sent
            bytes_recv_now = net_io_now.bytes_recv

           
            upload_speed = (bytes_sent_now - bytes_sent_prev) / interval
            download_speed = (bytes_recv_now - bytes_recv_prev) / interval

            
            bytes_sent_prev = bytes_sent_now
            bytes_recv_prev = bytes_recv_now

           
            print("==================================================")
            print("         MONITOR DE ANCHO DE BANDA EN TIEMPO REAL ")
            print("==================================================")
            print(f" Velocidad de Descarga : {bytes_to_human(download_speed)}/s")
            print(f" Velocidad de Carga    : {bytes_to_human(upload_speed)}/s")
            print("--------------------------------------------------")
            print(f" Total Descargado (Sesión) : {bytes_to_human(bytes_recv_now)}")
            print(f" Total Subido (Sesión)     : {bytes_to_human(bytes_sent_now)}")
            print("==================================================")
            print("Presiona Ctrl + C para detener el monitoreo.")

    except KeyboardInterrupt:
        print("\n\n[!] Monitoreo finalizado por el usuario.")

if __name__ == "__main__":
    monitor_network(interval=1)
