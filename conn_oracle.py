import cx_Oracle


# XE =
#   (DESCRIPTION =
#     (ADDRESS = (PROTOCOL = TCP)(HOST = BLRKEC382015D.ad.infosys.com)(PORT = 1521))
#     (CONNECT_DATA =
#       (SERVER = DEDICATED)
#       (SERVICE_NAME = XE)
#     )
#   )

# if needed, place an 'r' before any parameter in order to address special characters such as '\'.
# dsn_tns = cx_Oracle.makedsn(r'BLRKEC382015D.ad.infosys.com', '1521', service_name='XE')
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')

# if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)

c = conn.cursor()
c.execute('select * from emp') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()