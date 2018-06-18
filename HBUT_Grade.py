import requests
from bs4 import BeautifulSoup,element
import os

checkimg = 'http://run.hbut.edu.cn/Account/GetValidateCode'
StuGrade = 'http://run.hbut.edu.cn/StuGrade/Index'
g_20171 = '?SemesterName=20171&SemesterNameStr=2017学年%20第一学期'
g_20162 = '?SemesterName=20162&SemesterNameStr=2016学年%20第二学期'
g_20161 = '?SemesterName=20161&SemesterNameStr=2016学年%20第一学期'

file = open('grade.txt','w+')
session  = requests.Session()
headers = {
    'Referer' : 'http://run.hbut.edu.cn/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
}

def getHtmlText(SemesterName,payload):
    login_url = 'http://run.hbut.edu.cn/Account/LogOnForJson?Mobile=1&UserName=%s&Password=%s&Role=Student'%(payload['UserName'],payload['Password'])
    session.get(login_url,headers = headers)
    if SemesterName=='1':
        SemesterName = g_20161
    if SemesterName=='2':
        SemesterName = g_20162
    if SemesterName=='3':
        SemesterName = g_20171
    grade_url = StuGrade+SemesterName
    stugrade = session.get(grade_url,headers=headers)
    return stugrade.text


def GetFromText(txt):
    form = []
    soup = BeautifulSoup(txt,'html.parser')
    for tr in soup.find('table').children:
        try:
            if isinstance(tr,element.Tag):
                tds = tr('td')
                s1 = tds[1].string
                s2 = tds[4].string
                s3 = tds[5].string
                form.append([''.join(s1.split()),''.join(s2.split()),''.join(s3.split())])
        except:
            continue
    return form

def printgrade(ulist,num):
    tplt = "{0:{3}^25}\t{1:^10}\t{2:^10}\n"
    print(tplt.format("课程","学分","成绩",chr(12288)))
    file.write(tplt.format("课程","学分","成绩",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        file.write(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    try:
        payload = {
        'UserName': input('请输入账号：'),
        'Password': input('请输入密码：'),
        'Role':'Student',
        }
        print('大一上： 1')
        print('大一下： 2')
        print('大二上： 3')
        SenesterName = input('请输入查询的学期：')
        txt = getHtmlText(SenesterName,payload)
        form = GetFromText(txt)
        printgrade(form,len(form));
    except :
        print("Error")
    finally:
        file.close()

main()
