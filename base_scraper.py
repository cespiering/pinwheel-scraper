#Attempting object model

import requests
from bs4 import BeautifulSoup

class FormNotFoundError(Exception):
    pass



class IRS_Scraper:
    BASE_URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"


    BASE_PARAMS = {
        "resultsPerPage": '200',
        "sortColumn": "sortOrder",
        "indexOfFirstRow": "0",
        "criteria": "formNumber",
        "isDescending": "false",
    }

    def __init__(self, form_name) -> None:
        self.form_name = form_name
        self.set_query_string_parameter()
        self.soup_results = self.create_soup()
        self.form_results = self.limit_soup_to_form_name()


    def set_query_string_parameter(self):
        self.BASE_PARAMS["value"] = self.form_name

    def create_soup(self):
        response = requests.get(self.BASE_URL, params=self.BASE_PARAMS)
        soup = BeautifulSoup(response.content, "html.parser")
        soup_results = soup.find_all(class_=['even','odd'])
        return soup_results

    def limit_soup_to_form_name(self):
        form_results = [result for result in self.soup_results if result.find(class_='LeftCellSpacer').text.strip() == self.form_name]
        if len(form_results) == 0:
            raise FormNotFoundError
        else:
            return form_results


