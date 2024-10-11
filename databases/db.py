import pymysql

db_host = 'bd-grupo-3.cbm0w8aki8h0.us-east-1.rds.amazonaws.com'
db_user = 'grupo3'
db_password = 'grupo3123'

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_password
    )
    print("Connection ok")
except Exception as err:
    print("Error: ", err)
    connection = None

def add_activities(name_activity, start_time, end_time, duration, date_activity, description_activity, responsible, project):
    instruction_sql = "INSERT INTO db_grupo3.work_activities(name_activity, start_time, end_time, duration, date_activity, description_activity, responsible, project) VALUES ('"+name_activity+"', '"+start_time+"', '"+end_time+"', '"+duration+"', '"+date_activity+"', '"+description_activity+"', '"+responsible+"', '"+project+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("Activity added")
    except Exception as err:
        print("Error", err)