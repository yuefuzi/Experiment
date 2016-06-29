# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:56:22 2016

@author: Chang
"""

import sqlite3 as lite
import pandas as pd

con = lite.connect('/Users/Chang/getting_started.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df =pd.DataFrame(rows, columns=cols)
    
    print(df.head(9))
    
 