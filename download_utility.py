from base_scraper import IRS_Scraper, FormNotFoundError
import requests
import os

class YearsNotFoundError(Exception):
    pass


class Download_Utility(IRS_Scraper):

    def __init__(self, form_name: str, start_year: int, end_year: int):
        super().__init__(form_name)
        self.desired_years = self.create_list_of_str_years(start_year, end_year)
        self.available_years = self.find_available_years()
        self.year_url_tuples = self.create_year_url_tuple()
        self.missing_years = self.find_missing_years()
        

    def create_list_of_str_years(self, start_year, end_year):
        years = []
        while start_year <= end_year:
            years.append(str(start_year))
            start_year += 1
        return years[::-1]

    def find_available_years(self):
        available_years = [result.find(class_='EndCellSpacer').text.strip() for result in self.form_results if result.find(class_='EndCellSpacer').text.strip() in self.desired_years]
        if len(available_years) == 0:
            raise YearsNotFoundError
        else:
            return available_years

    def find_missing_years(self):
        missing_set = set(self.desired_years).symmetric_difference(set(self.available_years))
        missing_years = list(missing_set)
        return missing_years


    def fetch_pdf_urls(self):
        urls= [result.find("a")["href"] for result in self.form_results if result.find(class_='EndCellSpacer').text.strip() in self.available_years]
        return urls

    def create_year_url_tuple(self):
        urls = self.fetch_pdf_urls()
        zipped = zip(self.available_years, urls)
        year_url_tuple = list(zipped)
        return year_url_tuple

    def create_form_directory(self):
        os.makedirs(f'{self.form_name}', exist_ok=True)
        
    def write_pdf_files(self):
        self.create_form_directory()
        for pair in self.year_url_tuples:
            try:
                path = f'{self.form_name}/{self.form_name}-{pair[0]}.pdf'
                r = requests.get(pair[1])
                with open(path, 'xb') as file:    
                    pdf = r.content
                    file.write(pdf)
            except FileExistsError:
                print(f"The filepath {path} already exists")
                print("Continuing download....")
                pass

    def run_download_utility(self):
        if self.missing_years:
            print(f"The years {self.missing_years} are not available. Downloading the available years...")    
        self.write_pdf_files()
        print("Files download complete")


