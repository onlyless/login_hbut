import requests
from bs4 import BeautifulSoup
import xlwt
import os

checkimg = 'http://run.hbut.edu.cn/Account/GetValidateCode'
Schedule = 'http://run.hbut.edu.cn/ArrangeTask/MyselfSchedule'
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('MyselfSchedule')
session  = requests.Session()
headers = {
    'Referer' : 'http://run.hbut.edu.cn/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
}

#获取课程表网页
def getHtmlText(payload):
    login_url = 'http://run.hbut.edu.cn/Account/LogOnForJson?Mobile=1&UserName=%s&Password=%s&Role=Student'%(payload['UserName'],payload['Password'])
    session.get(login_url,headers = headers)
    work = session.get(Schedule,headers=headers)
    return work.text

#提取网页中的课程表
def getFormText(string):
    soup = BeautifulSoup(string,'html.parser')
    list = []
    for tr in soup.find('table').children:
        try:
            th = tr('th')[0].string
            if th==None:
                continue
            day1 = tr('td')[0].string
            day2 = tr('td')[1].string
            day3 = tr('td')[2].string
            day4 = tr('td')[3].string
            day5 = tr('td')[4].string
            day6 = tr('td')[5].string
            day7 = tr('td')[6].string
            list.append([th,day1,day2,day3,day4,day5,day6,day7])
        except:
            continue
    return list

#将提取到的课程表写入excel表格中
def WirteXls(list):
    worksheet.write(0,1,"星期一")
    worksheet.write(0,2,"星期二")
    worksheet.write(0,3,"星期三")
    worksheet.write(0,4,"星期四")
    worksheet.write(0,5,"星期五")
    worksheet.write(0,6,"星期六")
    worksheet.write(0,7,"星期日")
    for i in range(len(list)):
        u = list[i]
        for k in range(8):
            worksheet.write(i+1,k,u[k])


def main():
    try:
        payload = {
        'UserName': input('请输入账号：'),
        'Password': input('请输入密码：'),
        'Role':'Student',
        }
        string = getHtmlText(payload)
        string = string.replace('<br />','')
        list = getFormText(string)
        WirteXls(list)
    
    finally:
        workbook.save('MyselfSchedule.xls')

main()
