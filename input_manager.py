

class InputManager:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def determine_utility():
        print("Do you want to search forms or download forms? ")
        return input("Type s for search, d for download: ").lower()

    @staticmethod
    def determine_download_inputs():
        try:
            form_name = input("Enter the name of the form you would like to download: ")
            start_year = int(input("Enter the first year of search range: "))
            end_year = int(input("Enter the last year of search range(inclusive): "))
            return form_name, start_year, end_year
        except ValueError: ##This works
            print("Year values must be integers")
            return InputManager.determine_download_inputs()

    @staticmethod
    def determine_search_inputs():
        form_names = input("Enter all desired forms to search, separated by a comma ex: Form 1, Form 2: ")
        form_names = form_names.split(", ")
        return form_names
