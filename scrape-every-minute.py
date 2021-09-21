import requests
import time
from bs4 import BeautifulSoup

print("Put some skill that your are not familiar with")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    url = "https://pythonjobs.github.io/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_list_section = soup.find("section", class_ ="job_list")
    job_list = job_list_section.find_all("div", class_="job")
    for index, job in enumerate(job_list):  
        tags = job["data-tags"]      
        if unfamiliar_skill not in tags:
            # *set encoding to solve 'illegal multibyte sequence'
            with open(f'posts/{index}.txt', 'w+', encoding="utf-8") as f:
                title = job.h1.a.text.strip()
                location = job.find("i", class_="i-globe").parent.text.strip()
                company_name = job.find("i", class_="i-company").parent.text.strip()
                post_date = job.find("i", class_="i-calendar").parent.text.strip()
                contract_type = job.find("i", class_="i-chair").parent.text.strip()
                detail = job.p.text.strip()
                read_more = job.find("a", class_="go_button")["href"]
                f.write("{:<16} {:<20} \n".format("Job Title:", title))
                f.write("{:<16} {:<20} \n".format("Tags:", tags))
                f.write("{:<16} {:<20} \n".format("Location:", location))
                f.write("{:<16} {:<20} \n".format("Post by:", company_name))
                f.write("{:<16} {:<20} \n".format("Post on:", post_date))
                f.write("{:<16} {:<20} \n".format("Contract Type:", contract_type))
                f.write("{:<16} {:<20} \n".format("Read more:", url + read_more[1:]))
                f.write("{:<16} {:<20} \n".format("Detail:", detail))
            print(f'File saved: {index}')
                # print("{:<16} {:<20}".format("Job Title:", title))
                # print("{:<16} {:<20}".format("Tags:", tags))
                # print("{:<16} {:<20}".format("Location:", location))
                # print("{:<16} {:<20}".format("Post by:", company_name))
                # print("{:<16} {:<20}".format("Post on:", post_date))
                # print("{:<16} {:<20}".format("Contract Type:", contract_type))
                # print("{:<16} {:<20}".format("Read more:", url + read_more[1:]))
                # print("{:<16} {:<20}".format("Detail:", detail))
                # print()
            

    # print(f"{len(job_list)} Jobs Found.")

if __name__ == '__main__':
    while True:
        find_jobs()        
        time_wait_min = 1
        time_wait_sec = time_wait_min * 60
        print(f"Waiting {time_wait_sec} Seconds...")
        time.sleep(time_wait_sec)