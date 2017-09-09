import sqlite3
import datetime,time
from configs import *
import threading
tomorrow = datetime.date.today()+datetime.timedelta(days=1)
tomorrow = datetime.datetime.strftime(tomorrow,'%Y-%m-%d')
def count():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    sql1 = "SELECT user_id,starttime,endtime,build,room,seat from whu_seat_get_seat where date=\'%s\'" % tomorrow
    cursor = c.execute(sql1).fetchall()
    count = len(cursor)
    conn.close()
    return count
def main():
    print(tomorrow)
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    sql1 = "SELECT user_id,starttime,endtime,build,room,seat from whu_seat_get_seat where date=\'%s\'" % tomorrow
    row = c.execute(sql1).fetchone()
    user_id = row[0]
    starttime = row[1]
    endtime = row[2]
    build_id = str(row[3])
    room_id = str(row[4])
    seat_num = str(row[5].zfill(3))
    seat = getSeatid(seat_num,Seats[build_id][room_id])
    starttime = getTimeid(starttime)
    endtime = getTimeid(endtime)
    sql2 = "SELECT username,password from whu_seat_get_person where id=%s" % user_id
    person = c.execute(sql2).fetchall()
    Username = person[0]
    Password = person[1]
    Token = getToken(Username,Password)
    result = bookSeat(Token,starttime,endtime,seat,tomorrow)
    if result['status']=='success' or result['status']=='已有1个有效预约，请在使用结束后再次进行选择':
        print('预约成功!')
        print(result['data']['location'])
        print(result['data']['onDate'],result['data']['begin'],result['data']['end'])
    elif result['status']=='fail':
        print(result['message'])
        if result['message']=='登录失败: 用户名或密码不正确':
            Token = getToken(Username,Password)
        for i in range(1,11):
            result = bookSeat(Token,starttime,endtime,seat,tomorrow)
            if result['message']=='登录失败: 用户名或密码不正确':
                Token = getToken(Username,Password)
            if result['status']=='success' or result['status']=='已有1个有效预约，请在使用结束后再次进行选择':
                print('预约成功!')
                if 'data' in result:
                    print(result['data']['location'])
                    print(result['data']['onDate'],result['data']['begin'],result['data']['end'])
            elif result['message']=='预约失败，请尽快选择其他时段或座位':
                print('座位已被抢走了。。。')
            else:
                print(result['message'])
                time.sleep(0.3)
    else:
        print('出现未知错误!')
    conn.close()

def getSeat():
    threads = []
    nloops = count()
    print('共有座位: %d 个' % count)
    for i in nloops:
        t = threading.Thread(target=main)
        threads.append(t)
    for i in nloops:
        threads[i].join()