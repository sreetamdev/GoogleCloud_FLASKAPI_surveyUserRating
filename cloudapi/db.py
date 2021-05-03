{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# fetching libraries from packages \n",
    "import os\n",
    "import pymysql\n",
    "from flask import jsonify\n",
    "\n",
    "# retrieving value for the variables by referncing the app.yaml file\n",
    "user_db = os.environ.get('CLOUD_SQL_USERNAME')  \n",
    "password_db = os.environ.get('CLOUD_SQL_PASSWORD')\n",
    "name_db = os.environ.get('CLOUD_SQL_DATABASE_NAME')\n",
    "connection_name_db = os.environ.get('CLOUD_SQL_CONNECTION_NAME')\n",
    "\n",
    "\n",
    "def open_conn():\n",
    "    \"\"\"initialises the cloud MYSQL connection and returns the MYSQL connection\"\"\"\n",
    "    \n",
    "    connect_name = '/cloudsql/{}'.format(connection_name_db)  # sql connection object\n",
    "    \n",
    "    try:\n",
    "        # initiates the gcloud \n",
    "        if os.environ.get('GAE_ENV') == 'standard':\n",
    "            connection = pymysql.connect(user=user_db, password=password_db,\n",
    "                                unix_socket=connect_name, db=name_db,\n",
    "                                cursorclass=pymysql.cursors.DictCursor\n",
    "                                )\n",
    "            \n",
    "    except pymysql.MySQLError as e:\n",
    "        print(e)\n",
    "        \n",
    "    return connection\n",
    "\n",
    "def get_rating():\n",
    "    \"\"\"initialises the cloud MYSQL connection and returns the MYSQL connection\"\"\"\n",
    "    connection = open_conn()\n",
    "    with connection.cursor() as cursor:\n",
    "        search_result = cursor.execute('SELECT * FROM survey_report;') # executes the select statement to fetch data from MYSQL data table within our google cloud database\n",
    "        survey = cursor.fetchall()\n",
    "        \n",
    "        if search_result > 0:  # control statement that checks if they get any values for the database table in google cloud\n",
    "            got_survey_report = jsonify(survey)\n",
    "        else:\n",
    "            got_survey_report = 'No Ratings in Database'\n",
    "    connection.close()\n",
    "    return got_survey_report # the GET request response \n",
    "\n",
    "def add_rating(report):\n",
    "    connection = open_conn()\n",
    "    with connection.cursor() as cursor:\n",
    "        # executes the insert statement to provide data to MYSQL database table within our google cloud database\n",
    "        cursor.execute('INSERT INTO survey_report (Channel, Rating) VALUES(%s, %d)', (report[\"Channel\"], report[\"Rating\"]))\n",
    "    connection.commit()\n",
    "    connection.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
