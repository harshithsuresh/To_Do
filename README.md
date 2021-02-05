
## Prerequisites

-   Python 3.6
-   MySQL 5.7


## Setting up

    Create a database and table with the following character set and collation.
        Refer src/database/
    Clone the repository.
    Create the virtual environment using anaconda.
        conda create -n todo python=3.6
    Activate the anaconda virtual environment.
        conda activate todo
    Install all the required packages in your virtual environment.
        pip install -r requirements.txt
    Update the database values in etc/config/secrets.ini.
    Run Flask server (inside src directory) with
        python app.py
    Access the APIs with.
        localhost:5000/fetch_todo	(fetch all the tasks)
        localhost:5000/add_todo		(add new task)
		localhost:5000/add_category   (add new category)
		localhost:5000/update/status (update the task status to completed|not_completed) negate the current status
		localhost:5000/update/category (to change the existing todo category)
		localhost:5000/fetch_category (to get category list)
		localhost:5000/delete   		(to delete the todo task)
		