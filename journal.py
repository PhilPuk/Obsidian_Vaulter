from hmac import new
from logger_config import logger
from obsidian_time import my_Time
from obsidian_config import ObsidianConfig
from pathlib import Path
from template import my_Template

class Journal:
    def __init__(self):
        self._obsidian_journal_path = ObsidianConfig().getVaultPath() / "Journal"
        self._obsidian_journal_year_path = self._obsidian_journal_path / str(my_Time.getCurrentYear())
        self._obsidian_journal_month_path = self._obsidian_journal_year_path / str(my_Time.getCurrentMonthName())
        self._journal_page_template = my_Template.getJournalPageTemplate

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
        file_path = self._obsidian_journal_month_path / file_title
        if not file_path.exists():
            with open(file_path, 'a') as new_page:
                new_page.write(self._journal_page_template)
        
def main():
    logger.info("Starting journal creation")
    Journal().newJournalMonth()
    logger.info("Exiting journal creation")

if __name__ == "__main__":
    main()
