#!/bin/env python
import pymysql
import random
import concurrent
from concurrent.futures import ThreadPoolExecutor
import time

# user,password is 'temporary'
def connect(host,user,password,database):
	conn = pymysql.connect(
		host = host,
		user = user,
		password = password,
		database = database,
		cursorclass = pymysql.cursors.DictCursor
	)
	return conn


# insert
def _insert(conn,table,values):
	try:
		with conn.cursor() as cursor:
			sql = f"insert into {table} values ({values})"
			#print(sql)
			conn.begin()
			cursor.execute(sql)
			conn.commit()
	except Exception as e:
		print(e)

def single_insert(conn,table,values):
	_insert(conn,table,values)

# handling at thread
def _multi_insert(table,values):
	con = connect(_HOST,_USER,_PASSWORD,_DATABASE)
	with con:
		_insert(con,table,values)

def multi_insert(threads,table,values):
	exe = ThreadPoolExecutor(threads)
	with exe:
		futures = {exe.submit(_multi_insert,table,values) for _ in range(threads)}
		for future in futures:
			future.result()


if __name__ == "__main__":
	_COUNT = 10000
	_THREADS = 10
	_HOST = "localhost"
	_USER = "neko"
	_PASSWORD = "cat"
	_DATABASE = "hello"
	_TABLE = "animal"
	_DATA = f'{random.randint(0,1000000)},"neko"'
	print("----------- single thread ------------")
	start = time.time()
	for _ in range(_COUNT):
		conn = connect(_HOST,_USER,_PASSWORD,_DATABASE)
		with conn:
			single_insert(conn,_TABLE,_DATA)
	end = time.time() - start
	print(f'elapsed time => {end}[s]')
	print("----------- multi thread ------------")
	start = time.time()
	conn = connect(_HOST,_USER,_PASSWORD,_DATABASE)
	for _ in range(int(_COUNT/_THREADS)):
		multi_insert(_THREADS,_TABLE,_DATA)
	end = time.time() - start
	print(f'elapsed time => {end}[s]')
