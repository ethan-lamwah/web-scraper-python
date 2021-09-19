# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:47:03 2021

@author: Ethan
"""
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# Find element by ID
results = soup.find(id="ResultsContainer")
print(results.prettify())

# Find Elements by Class Name
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # Extract Text from HTML elements
    # strip() superfluous whitespace
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
# Find elements by Class Name and Exact Text Content
python_jobs = results.find_all("h2", string = "Python")
print(len(python_jobs))

# Find elements by Class Name and Text Content by passing lambda function
python_jobs = results.find_all("h2", string = lambda x: "python" in x.lower())
print(len(python_jobs))

# Accessing .parent elements
python_job_elements = [
    job.parent.parent.parent for job in python_jobs
]
print(python_job_elements)
