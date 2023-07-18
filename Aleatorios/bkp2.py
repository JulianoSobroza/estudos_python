import shutil
import schedule
import time

def fazer_backup():
    origem = 'C:\Users\jubso\Documents\Euro Truck Simulator 2'  # Insira o caminho da pasta que deseja fazer o backup
    destino = 'C:\Users\jubso\Documents\bkp do ets'  # Insira o caminho onde deseja salvar o backup
    
    # Cria um arquivo compactado (ZIP) com o conteúdo da pasta de origem
    shutil.make_archive(destino, 'zip', origem)

# Agendamento para fazer o backup a cada 24 horas
schedule.every(24).hours.do(fazer_backup)

while True:
    schedule.run_pending()
    time.sleep(1)