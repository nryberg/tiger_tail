import duckdb
import pandas as pd
import os

# Connect to the database
con = duckdb.connect(database='tracks.db', read_only=True)
sql = 'SELECT distinct station, time_zone FROM track_history'
df = con.execute(sql).fetchdf()

# TODO make sure you get the path right
path = '/Users/nick/Documents/GitHub/nryberg/tiger_tail/content/stations'
for ind in df.index:

    station = df['station'][ind]

    station_path = path + '/' + station

    if not os.path.exists(station_path):
        os.makedirs(station_path)

    sql = 'SELECT title, title_ref, artist, artist_ref, count(*) as plays FROM track_history WHERE station = \'' + df['station'][ind] + '\''
    sql += ' GROUP BY title, title_ref,artist, artist_ref ORDER BY count(*) DESC LIMIT 10'
    df2 = con.execute(sql).fetchdf()
    print(df2.head(10))

    track_file = station_path + '/tracks.md'


    with open(track_file, 'w') as f:

        f.write('## Top Ten Tracks' + '\n\n')
        f.write('| Track | Plays |' + '\n')
        f.write('| --- |  ---: |' + '\n')

        for trackindex in df2.index:
            # TODO: patched together MD files

            ref = df2['title_ref'][trackindex]
            title = df2['title'][trackindex]
            count = df2['plays'][trackindex]
            track_link = '[' + title + '](' + ref + ')'
            artist_link = '[' + df2['artist'][trackindex] + '](' + df2['artist_ref'][trackindex] + ')'
            f.write('|' + track_link  + ' by '  + artist_link + '| ' + str(count) + '|\n')

con.close()
