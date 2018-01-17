from flask import Flask, render_template, request
import pyodbc
import configparser

config = configparser.ConfigParser()
config.read('denta_config.ini')

show_last_count = config['WebServer']['ShowLastEntries']
connection_string = config['WebServer']['DBConnectionString']

app = Flask(__name__)


@app.route('/test')
def show_test():
    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT dateadd(day,datediff(day,1,GETDATE()),0)")

    entries = cursor.fetchall()
    print(entries)

@app.route('/fullsearch', methods=['GET'])
def show_fullsearch():
    name = request.args.get('name')
    name1 = name
    name2 = name
    try:
        name1, name2 = name.split(' ')
    except Exception:
        pass

    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT top 30 "
                   "imgInfo.chart AS chart, imgInfo.C_Date AS cdate, (injek.name + ' ' + injek.name_F) AS name "
                   "FROM imgInfo LEFT JOIN injek ON imgInfo.chart = injek.chart "
                   "WHERE injek.name LIKE '%" + name +"%' OR injek.name_F LIKE '%" + name +"%' "
                   "OR injek.name LIKE '%" + name1 +"%' OR injek.name_F LIKE '%" + name2 +"%' "
                   "OR injek.name LIKE '%" + name2 +"%' OR injek.name_F LIKE '%" + name1 +"%' "
                   "ORDER  BY imgInfo.C_Date DESC")


@app.route('/search', methods=['GET'])
def show_search():
    name = request.args.get('name')
    name1 = name
    name2 = name
    try:
        name1, name2 = name.split(' ')
    except Exception:
        pass

    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT top 30 "
                   "imgInfo.chart AS chart, imgInfo.C_Date AS cdate, (injek.name + ' ' + injek.name_F) AS name "
                   "FROM imgInfo LEFT JOIN injek ON imgInfo.chart = injek.chart "
                   "WHERE injek.name LIKE '%" + name +"%' OR injek.name_F LIKE '%" + name +"%' "
                   "OR injek.name LIKE '%" + name1 +"%' OR injek.name_F LIKE '%" + name2 +"%' "
                   "OR injek.name LIKE '%" + name2 +"%' OR injek.name_F LIKE '%" + name1 +"%' "
                   "ORDER  BY imgInfo.C_Date DESC")

    entries = cursor.fetchall()

    return render_template('main.html', entries=entries)

@app.route('/month')
def show_month():
    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT  "
                   "imgInfo.chart AS chart, imgInfo.C_Date AS cdate, (injek.name + ' ' + injek.name_F) AS name "
                   "FROM imgInfo LEFT JOIN injek ON imgInfo.chart = injek.chart "
                   "WHERE dateadd(day,datediff(day,0,imgInfo.C_Date),0) > dateadd(day,datediff(day,31,GETDATE()),0)"
                   "ORDER  BY imgInfo.C_Date DESC")

    entries = cursor.fetchall()

    return render_template('main.html', entries=entries)

@app.route('/week')
def show_week():
    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT  "
                   "imgInfo.chart AS chart, imgInfo.C_Date AS cdate, (injek.name + ' ' + injek.name_F) AS name "
                   "FROM imgInfo LEFT JOIN injek ON imgInfo.chart = injek.chart "
                   "WHERE dateadd(day,datediff(day,0,imgInfo.C_Date),0) > dateadd(day,datediff(day,7,GETDATE()),0)"
                   "ORDER  BY imgInfo.C_Date DESC")

    entries = cursor.fetchall()

    return render_template('main.html', entries=entries)

@app.route('/yesterday')
def show_yesterday():
    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT "
                   "imgInfo.chart AS chart, imgInfo.C_Date AS cdate, (injek.name + ' ' + injek.name_F) AS name "
                   "FROM imgInfo LEFT JOIN injek ON imgInfo.chart = injek.chart "
                   "WHERE dateadd(day,datediff(day,0,imgInfo.C_Date),0) = dateadd(day,datediff(day,1,GETDATE()),0)"
                   "ORDER  BY imgInfo.C_Date DESC")

    entries = cursor.fetchall()

    return render_template('main.html', entries=entries)


@app.route('/')
def show_entries():
    db_connection = pyodbc.connect(connection_string)
    cursor = db_connection.cursor()
    cursor.execute("SELECT top " + show_last_count +
                   "imgInfo.chart AS chart, imgInfo.C_Date AS cdate, (injek.name + ' ' + injek.name_F) AS name "
                   "FROM imgInfo LEFT JOIN injek ON imgInfo.chart = injek.chart "
                   "ORDER  BY imgInfo.C_Date DESC")

    entries = cursor.fetchall()

    return render_template('main.html', entries=entries)


if __name__ == '__main__':
    app.run()
