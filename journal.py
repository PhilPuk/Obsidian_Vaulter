from logger_config import logger
from obsidian_time import Time
from obsidian_config import ObsidianConfig

my_Time = Time()

class Journal:
    def __init__(self):
        self._obsidian_journal_path = ObsidianConfig().getVaultPath() / "Journal"
        self._obsidian_journal_year_path = self._obsidian_journal_path / str(my_Time.getCurrentYear())
        self._obsidian_journal_month_path = self._obsidian_journal_year_path / str(my_Time.getCurrentMonthName())

    def newJournalMonth(self, month: int=my_Time.getCurrentMonth(), year: int=my_Time.getCurrentYear()):
        self._obsidian_journal_month_path.mkdir(parents=True, exist_ok=True)
        self.createAllJournalMonthPages(my_Time.getDaysAmountInMonth(month, year), month, year)
        logger.info(f"Created new journal month: {my_Time.getCurrentMonthName()} {my_Time.getCurrentYear()}")
        
    def createAllJournalMonthPages(self, daysInMonth: int=0, month: int=my_Time.getCurrentMonth(), year: int=my_Time.getCurrentYear()):
        for day in range(1, daysInMonth + 1):
            week_number = (day - 1) // 7 + 1
            week_folder = self._obsidian_journal_month_path / f"Week {week_number}"
            week_folder.mkdir(parents=True, exist_ok=True)

            file_name = f"{str(day)}.{month}.{year} {my_Time.getDayName(year, month, day)}.md"
            self.newJournalPage(week_folder / file_name)
        logger.info(f"Created all journal pages for {my_Time.getCurrentMonthName()} {my_Time.getCurrentYear()}")

    def newJournalPage(self, file_title: str):
        with open(self._obsidian_journal_month_path.joinpath(file_title), 'a') as f:
            f.write("# Morning\n---\n")
            f.write("\n###### 1.  What am I grateful for?\n   \n")
            f.write("###### 2. What is my most important task today?\n  \n")
            f.write("###### 3. What story-worthy moment happened yesterday?\n   \n")
            f.write("###### 4. How am I feeling right now?\n    \n")
            f.write("###### 5. What's working right now? What could be better?\n    \n")
            f.write("# Noon/Afternoon (12 Uhr/14 Uhr)\n---\n\n")
            f.write("# Evening/Night (16 Uhr)\n---\n\n")
        
def main():
    logger.info("Starting journal creation")
    Journal().newJournalMonth()
    logger.info("Exiting journal creation")

if __name__ == "__main__":
    main()
    