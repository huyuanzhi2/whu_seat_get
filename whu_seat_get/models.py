from django.db import models
import time
import datetime
build_choices = (('1','信息科学分馆'),('2','工学分馆'),('3','医学分馆'))
room_choices = (('1','-----信息科学分馆-----'), ('14', '3C创客-双屏电脑（20台）(20)'), ('13', '3C创客-电子资源阅览区（20台）(20)'), ('4', '一楼3C创客空间(110)'), ('5', '一楼创新学习讨论区(64)'), ('15', '创新学习-MAC电脑（12台）(12)'), ('16', '创新学习-云桌面（42台）(42)'), ('7', '二楼东自然科学图书借阅区(92)'), ('6', '二楼西自然科学图书借阅区(92)'), ('10', '三楼东社会科学图书借阅区(84)'), ('12', '三楼自主学习区(188)'), ('8', '三楼西社会科学图书借阅区(88)'), ('11', '四楼东图书阅览区(80)'), ('9', '四楼西图书阅览区(88)'),('2','-----工学分馆-----'), ('19', '201室+东部自科图书借阅区(81)'), ('31', '205室+中部电子阅览室笔记本区(52)'), ('29', '2楼+中部走廊(20)'), ('32', '301室+东部自科图书借阅区(76)'), ('33', '305室+中部自科图书借阅区(130)'), ('34', '401室+东部自科图书借阅区(81)'), ('35', '405室+中部期刊阅览区(98)'), ('44', '个人研修室Ⅰ(0)'), ('45', '个人研修室Ⅱ(0)'), ('46', '个人研修室Ⅲ(0)'), ('47', '个人研修室Ⅳ(0)'), ('48', '个人研修室Ⅴ(0)'), ('49', '团体研修室Ⅵ(0)'), ('50', '团体研修室Ⅶ(8)'), ('37', '501室+东部外文图书借阅区(76)'), ('38', '505室+中部自科图书借阅区(176)'), ('3','-----医学分馆-----'), ('18', '202中文科技图书借阅A区(37)'), ('20', '204数字参考书借阅区(134)'), ('21', '302中文科技图书借阅B区(34)'), ('23', '305科技期刊阅览区(110)'), ('24', '402中文文科图书借阅区(34)'), ('25', '405电子阅览室(112)'), ('26', '502外文图书借阅区(32)'), ('28', '503培训教室(78)'), ('27', '506医学人文阅览区(87)'))
class Person(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)

class Seat(models.Model):
    def __unicode__(self):
        return self.user
    user = models.ForeignKey(Person,null=True)
    build = models.CharField(max_length=50,null=True,choices=build_choices)
    room = models.CharField(max_length=100,null=True,choices=room_choices)
    seat = models.CharField(max_length=30,null=True)
    date = models.DateField(default=datetime.date.today()+datetime.timedelta(days=1),null=True)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)
    email = models.EmailField(blank=True,max_length=254,null=True)
    is_book = models.NullBooleanField(blank=True,default=0,null=True)