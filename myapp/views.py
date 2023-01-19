from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from App import db, app
from models import Department
@app.route('/')
def Index():
    all_departments = Department.query.all()
    return render_template('index.html', departments = all_departments)

@app.route('/insert', methods = ['GET'])
def GetInsert():
    return render_template('insert.html')


@app.route('/insert', methods = ['POST'])
def Insert():
    if request.method == 'POST':
        name = request.form['name']
        my_data = Department(name)
        db.session.add(my_data)
        db.session.commit()
        flash('Department Inserted')
        return redirect(url_for('Index'))
        
if __name__ == "__main__":
    app.run(debug=True)
