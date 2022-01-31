
import json
from search_utility import Search_Utility
from download_utility import Download_Utility, YearsNotFoundError
from input_manager import InputManager
from base_scraper import FormNotFoundError

def run_program():
    input_manager = InputManager()
    utility = input_manager.determine_utility()

    #Running Download Utility
    if utility == "d":
        form_name, start_year, end_year = input_manager.determine_download_inputs()
        try:
            downloader = Download_Utility(form_name, start_year, end_year)
            downloader.run_download_utility()
        except FormNotFoundError:
            print(f"{form_name} not found from run.py") 
        except YearsNotFoundError:
            print("No years found for range given")
    
    #Running Search Utility
    if utility == "s":
        search_results = []
        form_names = input_manager.determine_search_inputs()
        for form_name in form_names:
            try:
                current_search = Search_Utility(form_name)
                search_results.append(current_search.to_dict())
            except FormNotFoundError:
                print(f"{form_name} not found, continuing form search")
                continue
        if search_results:
            print(json.dumps(search_results))
        else:
            print("Your search yielded no results")

if __name__ == "__main__":
    run_program()