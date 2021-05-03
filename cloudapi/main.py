{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing libraries from packages\n",
    "from flask import Flask, jsonify, request\n",
    "from db import get_rating, add_rating\n",
    "\n",
    "app = Flask(__name__)   # app is a Flask object\n",
    "\n",
    "@app.route('/', methods = ['POST','GET'])  # Both arguments POST to add data and GET to fetch data have been initiated as argument\n",
    "def survey_report():\n",
    "    if request.method == 'POST':  # if control structure for POST \n",
    "        if not request.is_json:\n",
    "            return jsonify({\"msg\": \"Missing JSON in request\"}), 400 \n",
    "        add_rating(request.get_json())\n",
    "        return 'Channel & Rating Added'\n",
    "        \n",
    "    return get_rating()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run() "
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
