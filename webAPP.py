#!/usr/bin/env python
import sqlite3
from os import sep, path

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.debug = True
DATABASE = path.dirname(path.realpath(__file__))+sep+'db'+sep+ 'currencies.db'

def get_db():

	db = sqlite3.connect(DATABASE)
	return db

def query_db(query, args=(), one=False):

	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return rv


@app.route("/", methods=['POST', 'GET'])

def index():

	if request.method == 'GET':

		return render_template("index.html")

	else:
		first_Curr = query_db("select to_usd from currencies where curname='{}'".format(request.form['curname1']))[0][0]
		second_Curr = query_db("select to_usd from currencies where curname='{}'".format(request.form['curname2']))[0][0]
		res = (first_Curr/second_Curr)*float(request.form['cval1'])
		return jsonify(result=round(res,2))


@app.route("/chckrates")

def check_rates():

	curRates = query_db("select to_usd from currencies")
	for i in range(len(curRates)):
		curRates[i] = '{:.5f}'.format(curRates[i][0])
	return render_template("rates.html",arr=curRates)


@app.route("/about-us")

def show_about():

	return render_template("about.html")


@app.route("/contact")

def show_contact():

	return render_template("contact.html")


@app.route("/donate", methods=['POST', 'GET'])

def show_donate():

	if request.method == 'GET':
		return render_template("donate.html")

	else:
		try:
			float(request.form['donation'])
			return render_template("donate.html", thanks="Thank You!")

		except:
			return render_template("donate.html")

if __name__ == '__main__':

	app.run(host='0.0.0.0')
