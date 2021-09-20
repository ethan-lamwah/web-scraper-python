import requests
import time
from bs4 import BeautifulSoup

def find_jobs():
    url = "https://pythonjobs.github.io/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_list_section = soup.find("section", class_ ="job_list")
    job_list = job_list_section.find_all("div", class_="job")
    for job in job_list:        
        title = job.h1.a.text.strip()
        location = job.find("i", class_="i-globe").parent.text.strip()
        company_name = job.find("i", class_="i-company").parent.text.strip()
        post_date = job.find("i", class_="i-calendar").parent.text.strip()
        contract_type = job.find("i", class_="i-chair").parent.text.strip()
        detail = job.p.text.strip()
        read_more = job.find("a", class_="go_button")["href"]
        print("{:<16} {:<20}".format("Job Title:", title))
        print("{:<16} {:<20}".format("Location:", location))
        print("{:<16} {:<20}".format("Post by:", company_name))
        print("{:<16} {:<20}".format("Post on:", post_date))
        print("{:<16} {:<20}".format("Contract Type:", contract_type))
        print("{:<16} {:<20}".format("Read more:", url + read_more[1:]))
        print("{:<16} {:<20}".format("Detail:", detail))
        print()

    print(f"{len(job_list)} Jobs Found.")

if __name__ == '__main__':
    while True:
        find_jobs()        
        time_wait_min = 1
        time_wait_sec = time_wait_min * 60
        print(f"Waiting {time_wait_sec} Seconds...")
        time.sleep(time_wait_sec)