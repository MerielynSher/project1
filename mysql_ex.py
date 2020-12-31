# mysql installation tutorial : https://www.dev2qa.com/how-to-use-mysql-on-mac/

# **** (use if needed) **** python set to 3.7.3 in mac: https://opensource.com/article/19/5/python-3-default-mac

# Python mysql tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp

# mysql installation tutorial : https://www.dev2qa.com/how-to-use-mysql-on-mac/

# **** (use if needed) **** python set to 3.7.3 in mac: https://opensource.com/article/19/5/python-3-default-mac

# Python mysql tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp

# TODO : design table schema, put resources/customer_rating_movies into 6 tables in local mysql database using python programming
import mysql.connector
import csv
import numpy as np

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='',
  database='customer_ratings'
)