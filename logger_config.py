import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Konfigurieren Sie den Logger auf dem gewünschten Level und dem gewünschten Format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Erstellen Sie einen FileHandler, um Protokolle in eine Datei zu schreiben
file_handler = logging.FileHandler('log.txt')

# Definieren Sie das gewünschte Format für die Log-Datei
file_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

# Fügen Sie den FileHandler zum Logger hinzu
logging.getLogger().addHandler(file_handler)

# Create logger
logger = logging.getLogger('my_logger')
