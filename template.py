from pathlib import Path
from logger_config import logger

class Template:
    def __init__(self):
        self._template_folder_path = Path(__file__).parent / "templates"
        self._journal_page_template_path = self._template_folder_path / "journal_page_template.md"
        self._book_page_template_path = self._template_folder_path / "book_page_template.md"

    def getJournalPageTemplatePath(self) -> Path:
        return self._journal_page_template_path
    
    def getBookPageTemplatePath(self) -> Path:
        return self._book_page_template_path
    
    def getJournalPageTemplate(self) -> str:
        return self.readTemplateFile(self.getJournalPageTemplatePath())
    
    def getBookPageTemplate(self) -> str:
        return self.readTemplateFile(self.getBookPageTemplatePath())

    def getTemplateFolderPath(self) -> Path:
        return self._template_folder_path

    def readTemplateFile(self, template_file_path: str) -> str:
        '''Reads a template file and returns its content as a string.'''
        try: 
            with open(template_file_path, 'r') as f:
                template_file_content = f.read()
            return template_file_content
        except FileNotFoundError:
            logger.error(f"Template file {template_file_path} not found! Returning empty string")
            return ""
        
my_Template = Template()