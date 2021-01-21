from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

from utils.helper import read_config

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

@app.route('/add_todo', methods=['POST'])
def add_todo():
    """
    Get the new task to be added and insert into the table.

    Args:
        name: task name.

    Returns:
        Success reponse, if success. Else, error reponse with the error message
    """

    request_data = request.json
    name = request_data['name']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO todo(name, status, created_by) VALUES(%s, %s, %s)",(name, NOT_COMPLETED_STATUS, created_by))
    mysql.connection.commit()
    cursor.close()

    return SUCCESS_RESPONSE

@app.route('/fetch_todo')
def fetch_todo():
    """
    Retrieve all todos from the table

    Args:
        No arguments passed

    Returns:
        Success reponse with data, if success. Else, error reponse with the error message
    """
    print("aaa")
    cursor = mysql.connection.cursor()
    print("bbb")
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