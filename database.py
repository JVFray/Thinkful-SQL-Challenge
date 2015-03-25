import sqlite3 as lite
import pandas as pd 

con = lite.connect('getting_started.db')

with con:

	cur = con.cursor()
	cur.execute("SELECT city FROM weather WHERE warm_month = 'July' ")

	rows = cur.fetchall()
  	df = pd.DataFrame(rows)

  	print df 

