#!/bin/env python
import pymysql

def connect(host,user,password,):
	conn = pymysql.connect(
		host = host,
	)
	return conn

def single_insert(table,values):

def multi_insert(threads,table,values):

if __name__ == "__main__":
	_THREADS = 10
