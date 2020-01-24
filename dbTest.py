import pyodbc, json
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

with open('dbConfig.json') as json_data_file:
	credential = json.load(json_data_file)

server = credential['server']
database = credential['database']
username = credential['username']
password = credential['password']

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * from Anime.MyAnimeList.WatchedAnime;") 
row = cursor.fetchone() 
while row: 
    for i in row:
    	print(i)
    row = cursor.fetchone()