import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost",
							user="webviewer",
							passwd="webview",
							db="ffxi_findall")
	c = conn.cursor()
	
	return c, conn