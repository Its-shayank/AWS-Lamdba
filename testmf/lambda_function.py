from __future__ import print_function

import json
import pymysql

print('Loading function')


def lambda_handler(event, context):
    pid = event['pid']
    if type(pid) == type(2):
        conn = pymysql.connect(host='172.XXX.XXX.XXX', port=3306, user='testuser', password='password', db='testDB')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Persons where PersonID = %s"%pid)
        print(cur.description)
        res = []
        print(cur.description)
        print()
        for row in cur:
            res.append(row)
        cur.close()
        conn.close()
        return res
    else:
        res = ["Please send valid value!!!!"]
        return res