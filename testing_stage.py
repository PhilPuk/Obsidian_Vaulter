from pathlib import Path
from logger_config import logger
from obsidian_time import my_Time
from obsidian_config import ObsidianConfig

obs_config = ObsidianConfig()

def createMonthCollectorPage(month: int=my_Time.getCurrentMonth(), year: int=my_Time.getCurrentYear()):
    pass

def FillMonthWithDateEntries(month: int=my_Time.getCurrentMonth(), year: int=my_Time.getCurrentYear()):
    #TO DO check if already exists and if so, do not fill
    journal_path = obs_config.getVaultPath() / "Journal"
    current_year_path = journal_path / str(my_Time.getCurrentYear())
    current_month_path = current_year_path / str(my_Time.getMonthName(month))
    current_month_path.mkdir(parents=True, exist_ok=True)

    current_month_file_path = current_month_path / f"{my_Time.getMonthName(month)} {my_Time.getCurrentYear()}.md"
    print("Current month file path: ", current_month_file_path)
    with open(current_month_file_path, 'a') as f:
        for day in range(my_Time.getDaysAmountInMonth(month, year)):
            date = f"{day + 1}.0{month}.{year} {my_Time.getDayName(year, month, day + 1)}"
            f.write(f"\n[[{date}]]\n")

FillMonthWithDateEntries(month=8)