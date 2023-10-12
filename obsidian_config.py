from pathlib import Path
from logger_config import logger

class ObsidianConfig:
    def __init__(self):
        self._vault_path = Path("C:/Users/Phil/Documents/Obsidian/Zettelkasten/X")

    def getVaultPath(self):
        return self._vault_path