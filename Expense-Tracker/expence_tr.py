import sqlite3 as db
from datetime import date
import datetime
from docopt import docopt
from tabulate import tabulate


usage = '''
Daily expense tracker

Usage:
    test.py init
    test.py show
    test.py <expense_name> <amount>
    test.py <week_count>
    '''


def init():
    conn = db.connect("expense.db")  # creation of a new database named expense
    cur = conn.cursor()

    sql = '''
    create table if not exists expenses_table(
        expense_name string,
        amount number,
        date2 string
    )'''

    cur.execute(sql)
    conn.commit()


def user_info():
    year=2020
    month=8
    day=1
    user_info.weeks_no = int(input("Number of weeks:"))
    # today = date.today()
    today=datetime.date(year,month,day)
    print(today)
    past = datetime.timedelta(weeks=user_info.weeks_no)
    past_day = today - past
    # print(past_day)
    return past_day, today


def log(expense_name, amount):
    # dates = date.today()
    dates=datetime.datetime.strptime('2020-08-01','%y-%m-%d')
    # week_dates= str(date.today().weekday())
    conn = db.connect("expense.db")
    cur = conn.cursor()

    sql = ''' 
    insert into expenses_table values(
        '{}',
         {},
        '{}'

    )'''.format(expense_name, amount, dates)

    cur.execute(sql)
    conn.commit()


def dis(name=None):
    conn = db.connect("expense.db")
    cur = conn.cursor()

    sql = '''
    select * from expenses_table join (select sum(amount) sumtotal from expenses_table) join (select sum(amount) sumtotal from expenses_table)
    '''.format(name)
    cur.execute(sql)
    results = cur.fetchall()
    return results


def dis1(today, past_day):
    conn = db.connect("expense.db")
    cur = conn.cursor()


    sql='''select sum(amount) from expenses_table where date2 between '2020-07-30' and '2020-08-20' '''

    # sql = "select sum(amount) from expenses_table where date2 between {} and {}".format(today.strftime('%Y-%m-%D'), past_day.strftime('%Y-%m-%D'))
    cur.execute(sql)
    results = cur.fetchall()
    return results


args = docopt(usage)

if args['init']:
    init()

if args['show']:
    results = dis()
    print(tabulate(results, headers=[
          "Name", "Amount", "date", "Week duration", "Daily total", "Weekly total"], tablefmt="pretty"))

if args['<expense_name>']:
    try:
        amount = float(args['<amount>'])
        log(args['<expense_name>'], amount)
    except:
        print(usage)

# if args['total_amount']:
var1, var2 = user_info()
results = dis1(var1, var2)
print(results)
# print (tabulate(results,headers=["Name","Amount","date","Week duration", "Daily total","Weekly total"],tablefmt="pretty"))
