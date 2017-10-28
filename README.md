## 湖北工业大学教务系统查分、查课表小程序
运行该小程序需安装requests和bs4库，还需要安装能操作excel的xlwt库

``` shell
pip install requests
pip install bs4
pip install xlwt
```
``` shell
python HBUT_Grade.py //查分
python HBUT_Schedule.py //查课表
```

现在该程序不能自动识别验证码，需手动在控制台输入二维码，然后输入学号和密码即可查询，作者本人大二，所以现在可支持查询大一两个学期和大二上的成绩，成绩会自动保存在本地。<br>
由于课表不好格式化输出，如需查课表，程序会生成一个excel文件，然后直接查看即可