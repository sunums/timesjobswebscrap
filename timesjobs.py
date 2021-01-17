from  bs4  import BeautifulSoup
import requests
import time
import csv 
from datetime import date
from header import *


def timesjobs():
    today = str(date.today())
    path=(f"POST/{today}.csv")
    f = open(path,'a',newline='')
    writer = csv.writer(f)
    writer.writerow(["SN", "Job_Tittle","Experince","Company_Name","location","Job Skill","Date_Post","More_Info"])
    url=timesjobhtml()
    html_text = requests.get(url).text
    soup =BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for indexno,job in enumerate(jobs):
        Date_Post = job.find('span',class_='sim-posted').text.replace(' ','')
        company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','').replace('(MoreJobs)','')
        company_name = company_name.strip()
        more_info =job.header.h2.a['href']
        job_tittle = job.header.h2.a.text.strip()
        sino ="TJ"+str(indexno+1)
        Exper =job.find("li").text.replace('card_travel','').strip()
        locationj =job.find("span").text.strip()
        Job_skill =job.find("span",class_="srp-skills").text.strip()
        writer.writerow([sino,job_tittle,Exper,company_name,locationj,Job_skill,Date_Post,more_info])
            # with open(f'POST/indexno.csv','a') as f:
                #  f.write(f"\n si.No:TJ{indexno+1}\n")
                #f.write(f"job_tittle:{job_tittle}\n")
                #f.write(f"Company_Name:{company_name}\n")
                #  f.write(f"Date_Post :{Date_Post.strip()}\n")
            











