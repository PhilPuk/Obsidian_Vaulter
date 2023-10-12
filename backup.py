from pathlib import Path
from logger_config import logger
from obsidian_time import Time
from obsidian_config import ObsidianConfig
from shutil import copyfile, copytree

my_Time = Time()

class Backup:
    def __init__(self):
        self._backup_path = ObsidianConfig().getVaultPath().parent / "Backup"
        self._backup_path.mkdir(parents=True, exist_ok=True)

    def createBackup(self, file_path_to_backup: str, backup_path: str, extend_file_name_with_timestamp: bool=True) -> None:
        try:
            backup_path = Path(backup_path)
            file_path_to_backup = Path(file_path_to_backup)
            
            if extend_file_name_with_timestamp:
                file_name = file_path_to_backup.name
                file_name = f"{my_Time.getTimeStamp(format='%Y-%m-%d_%H-%M-%S')}_Backup_{file_name}"
                print("File name: ", file_name)

            if file_path_to_backup.is_dir():
                copytree(file_path_to_backup, backup_path / file_name)
            else:
                copyfile(file_path_to_backup, backup_path / file_name)

            logger.info(f"Created backup of {file_path_to_backup} in {backup_path}")
        except:
            logger.warn(f"Could not create backup of {file_path_to_backup} in {backup_path}")

    def createBackupOfVault(self):
        self.createBackup(ObsidianConfig().getVaultPath(), self._backup_path)