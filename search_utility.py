from base_scraper import IRS_Scraper

class Search_Utility(IRS_Scraper):
    
    def __init__(self, form_name):
        super().__init__(form_name)
        self.title = self.fetch_form_title()
        self.min_year = 0
        self.max_year = 0
        self.find_min_max_year()

    def fetch_form_title(self):
        return self.form_results[0].find(class_='MiddleCellSpacer').text.strip()

    def find_year_range(self):
        years = [result.find(class_='EndCellSpacer').text.strip() for result in self.form_results if result.find(class_='LeftCellSpacer').text.strip() == self.form_name]
        return years

    def find_min_max_year(self):
        years = self.find_year_range()
        years.sort()
        self.min_year = years[0]
        self.max_year = years[-1]

    def to_dict(self):
        return {
        "form_name": self.form_name,
        "title": self.title,
        "min_year": self.min_year,
        "max_year": self.max_year
        }

