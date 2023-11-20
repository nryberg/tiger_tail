import duckdb
import pandas as pd

# Connect to the database
con = duckdb.connect(database='tracks.db', read_only=True)
sql = 'SELECT distinct station, time_zone FROM track_history'
df = con.execute(sql).fetchdf()

for ind in df.index:
    print(df['station'][ind], df['time_zone'][ind])
    sql = 'SELECT title, count(*) FROM track_history WHERE station = \'' + df['station'][ind] + '\''
    sql += ' GROUP BY title ORDER BY count(*) DESC LIMIT 10'
    df2 = con.execute(sql).fetchdf()
    print(df2.head(10))

con.close()
