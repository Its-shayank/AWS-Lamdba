from __future__ import print_function

import json
import pymysql
print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    conn = pymysql.connect(host='127.XXX.XXX.XXX', port=3306, user='user', password='password', db='testDB')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Persons ")
    print(cur.description)
    print()
    for row in cur:
        print(row)
    cur.close()
    conn.close()

    return 'Hello world'
  # Echo back the first key value
    #raise Exception('Something went wrong')
