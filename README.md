
# IRS Forms Scraper

IRS Forms Scraper is a collection of two utilities used to scrape the IRS Prior Year Products webpage.

Search_utility.py scrapes the form name, title and year range for any number of IRS Forms

Download_utility.py scrapes the site for a requested year range and downloads the associated PDF files.

## Tech and Specs
* Python 3.9.2
* Library: BeautifulSoup
* Library: requests

## Run Locally

Clone the project

```bash
  $ git clone https://github.com/cespiering/pinwheel-scraper.git
```

Go to the project directory

```bash
  $ cd my-project
```

Install dependencies

```bash
  < set up virtual environment >
  $ pip install requirements.txt
  
```

Run IRS Scraper

```bash
  $ python run.py
```
Follow the prompts in the command line to interact with scraper

## Using the utilities

`Scrape_Utility`

Inputs: command line prompt for form names to search

Outputs: JSON object printed to terminal

Notes: Utility will inform user if any of the requested forms are not found

`Download_Utility`

Inputs: command line prompt for form name, start year and end year

Outputs: files found will download to subdirectories in the project folder

Notes: Utility will inform user of any years missing and any previously downloaded forms


## General Information

I used this project to dive deeper into Object Oriented Programming and to play with custom exceptions. For the scope of this project, I felt comfortable keeping all the files in the same directory. However, if the project were to expand much further I would create a nested file structure. As much as possible, I tried to maintain a separation of concern among the classes/functions and minimize coupling.



