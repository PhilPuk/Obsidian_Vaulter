from journal import main as journal_main
from library import main as library_main
from backup import Backup

if __name__ == "__main__":
    Backup().createBackupOfVault()
    
    journal_main()
    library_main()
