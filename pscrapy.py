#!/usr/bin/python3
#!/usr/bin/python

from  bs4  import BeautifulSoup
import requests
import time
import csv 
from datetime import date



def timesjobs(si,keyword,exp):

  url=f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=AEROSPACE&txtLocation=India&cboWorkExp1=1"
  html_text = requests.get(url).text
  soup =BeautifulSoup(html_text,'lxml')
  jobs0 = soup.find_all('header',class_='srp-header clearfix')
  for indexno,job0 in enumerate(jobs0):
    luceneResult = (job0.find('span').text.strip()).split()
    luceneResultSize=luceneResult[0]
    print(luceneResultSize[0])



  Portal = "timesjobs"
  today = str(date.today())
  path=(f"{today}.csv")
  f = open(path,'a',newline='')
  writer = csv.writer(f)
  writer.writerow(["SN","Portal","Job_Tittle","Experince","Company_Name","location","Job Skill","Date_Post","More_Info"])
  url=f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&txtLocation=India&cboWorkExp1={exp}&luceneResultSize={luceneResultSize}"
  html_text = requests.get(url).text
  print(url)
  soup =BeautifulSoup(html_text,'lxml')
  jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
  for indexno,job in enumerate(jobs):
      Date_Post = job.find('span',class_='sim-posted').text.replace(' ','').strip()
      company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','').replace('(MoreJobs)','')
      company_name = company_name.strip()
      more_info =job.header.h2.a['href'].strip()
      job_tittle = job.header.h2.a.text.strip()
      si_number = si +(indexno+1)
      sino ="TJ"+str(si_number)
      Exper =job.find("li").text.replace('card_travel','').strip()
      locationj =job.find("span").text.strip()
      Job_skill =job.find("span",class_="srp-skills").text.strip()
      writer.writerow([sino,Portal,job_tittle,Exper,company_name,locationj,Job_skill,Date_Post,more_info])
  f.close()   
  return(si_number)    




if __name__ == "__main__":
    set_no = 1
    set_serial_no = timesjobs(set_no,"cybersecurity","1") 





