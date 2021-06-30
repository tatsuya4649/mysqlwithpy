#!/bin/env python
import pymysql
import random
import time

# Connection to MySQL Server 
# Host,User,Password,Database
def connection():
	conn = pymysql.connect(
		host='localhost',
		user='neko',
		password='cat',
		database='hello',
		cursorclass=pymysql.cursors.DictCursor
	)
	return conn

# Insert DATA operation into connection DATABASE
def insert(table,scheme,data_array):
	with conn.cursor() as cursor:
		sql = f"insert into {table} ({scheme}) values ({data_array})"
		print(sql)
		# not autocommit
		conn.begin()
		cursor.execute(sql)

# Select DATA operation from connection DATABASE
def select(table):
	with conn.cursor() as cursor:
		sql = f"select * from {table}"
		print(sql)
		# result have 'row count(= affected row)'
		result = cursor.execute(sql)
		print(result)
		# if get per row, fetchone() => return dict
		print(cursor.fetchone())
		# if get all, fetchall() => return array 
		print(cursor.fetchall())

if __name__ == "__main__":
	print("Hello World")
	conn = connection()
	with conn:
		print("----------------")
		select("animal")
		print("----------------")
