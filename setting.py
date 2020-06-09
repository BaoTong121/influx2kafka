influxdb_host = '192.168.8.36'
influxdb_port = 8086
influxdb_user = 'root'
influxdb_database= 'tax'
influxdb_pass = ''
# influxdb_sql = 'select * from taxKeywordCount where time > now() - 5m'
influxdb_sql = 'select * from taxKeywordCount'