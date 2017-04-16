#!/bin/env python3
# -*- coding:utf8 -*-
#author:gaoxueliang
#document:mysql status.
import mysql.connector
conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='213456',database='db1')
cursor = conn.cursor()
cursor.execute('show global status;')
data = cursor.fetchall()
print(data)
conn.commit()
cursor.close()
conn.close()
