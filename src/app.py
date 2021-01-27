from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

from utils.helper import read_config
import datetime

from constants import SECRET_FILE_PATH, SUCCESS_RESPONSE, NOT_COMPLETED_STATUS


_secret_config = read_config(SECRET_FILE_PATH)
_database_config = _secret_config['database']

app = Flask(__name__)

app.config['MYSQL_DB'] = _database_config['mysql_db']
app.config['MYSQL_HOST'] = _database_config['mysql_host']
app.config['MYSQL_USER'] = _database_config['mysql_user']
app.config['MYSQL_PASSWORD'] = _database_config['mysql_password']

mysql = MySQL(app)

created_by = 'user_id'  #This has to the login ID of the user


@app.route('/update_status', methods=['POST'])
def update_status():
    time = datetime.datetime.today()
    time = time.isoformat()
    print(time)
    request_data = request.json
    name = request_data['name']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE todo set STATUS='COMPLETED',MODIFIED_DATE=%s where NAME=%s",(time,name)) 
    SUCCESS_RESPONSE['data'] = "Successful"  
    mysql.connection.commit()
    cursor.close()
    return SUCCESS_RESPONSE

@app.route('/fetch_category')
def fetch_category():

    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT CATEGORY FROM todo_category''')
    row_headers=[x[0] for x in cursor.description]
    row_values = cursor.fetchall()
    json_data = []
    for row_value in row_values:
        json_data.append(dict(zip(row_headers,row_value)))
    SUCCESS_RESPONSE['data'] = json_data
    return SUCCESS_RESPONSE


@app.route('/add_category', methods=['POST'])
def add_category():

    request_data = request.json
    name = request_data['name']
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT CATEGORY FROM todo_category''')
    row_values = cursor.fetchall()
    for row_value in row_values:
        if name in row_value[0]:
            return {"status_code": 409,"data": "Category already exists",}
    cursor.execute("INSERT INTO todo_category(CATEGORY) VALUES(%s)",(name,))
    mysql.connection.commit()
    cursor.close()
    SUCCESS_RESPONSE['data'] = "Successful"
    return SUCCESS_RESPONSE

@app.route('/add_todo', methods=['POST'])
def add_todo():
    request_data = request.json
    name = request_data['name']
    category=request_data['category']
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT ID,CATEGORY FROM todo_category''')
    row_values = cursor.fetchall()
    for row_value in row_values:
        if category in row_value[1]:
            cursor.execute("INSERT INTO todo(name, status, created_by,CATEGORY_ID) VALUES(%s, %s, %s,%s)",(name, NOT_COMPLETED_STATUS,created_by,row_value[0]))
            mysql.connection.commit()
            cursor.close()
            SUCCESS_RESPONSE['data'] = "Successful"
            return SUCCESS_RESPONSE

    return {"status_code": 400,"data": "Category does not exists",}

@app.route('/fetch_todo')
def fetch_todo():

    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM todo''')
    row_headers=[x[0] for x in cursor.description]
    row_values = cursor.fetchall()
    json_data = []
    for row_value in row_values:
        json_data.append(dict(zip(row_headers,row_value)))
    SUCCESS_RESPONSE['data'] = json_data
    return SUCCESS_RESPONSE

if __name__ == '__main__':
    app.run(debug=True)