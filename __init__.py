from influxdb import InfluxDBClient
from src import setting
user = setting.influxdb_user
host = setting.influxdb_host
database = setting.influxdb_database
port = setting.influxdb_port
sql = setting.influxdb_sql
client = InfluxDBClient('192.168.8.36', 8086, 'root', '', 'tax')



def influx2kafka(client):
    result = client.query(sql)
    print(result)


if __name__ == '__main__':
    influx2kafka(client)