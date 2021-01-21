
## Prerequisites

-   Python 3.6
-   MySQL 5.7


## Setting up

-   Create a database and table with the following character set and collation.
    -   Refer src/database/
-   Install all the required packages in your virtual environment.
    -   pip install -r requirements.txt
-   Update the database values in etc/config/secrets.ini
-   Run Flask server (inside src directory) with
    -   _python app.py_
-   Access the APIs with.
    -   _localhost:5000/fetch_todo_
    -   _localhost:5000/add_todo_
