
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
        localhost:5000/fetch_todo
        localhost:5000/add_todo
		localhost:5000/add_category   (add new category)
		localhost:5000/update_status (update the task status completed)
		localhost:5000/fetch_category (to get category list)
		