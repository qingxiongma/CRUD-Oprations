"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from flaskr import app
import sqlite3 as sql
from flaskr.forms import ContactForm, StudentForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', title='Contact us', form = form )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/newstudent/', methods = ['GET', 'POST'])
def newstudent():
    msg = "" 
    form = StudentForm()
    if form.validate_on_submit():
        nm = form.name.data
        ph = form.phone.data
        em = form.email.data
        ad = form.address.data
         
        with sql.connect("student.db") as conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO students VALUES (?,?,?,?)",(nm,ph,em,ad) )
            conn.commit()

        flash("The student is added.", "success")
        return redirect(url_for('studentlist'))    

            
    return render_template('add_student.html', title='New Student', form = form )

@app.route('/studentlist/')
def studentlist():
    with sql.connect("student.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        return render_template("list_student.html", rows=rows)

@app.route('/studentdetail/<string:id>', methods=['GET'])
def detail(id):
    with sql.connect("student.db") as conn:
        cur = conn.cursor()
        cur.execute('select * from students where name=?', (id,))
        detail = cur.fetchone()
        return render_template('student_detail.html', detail = detail )

@app.route('/studentupdate/<string:id>', methods=['GET', 'POST'])
def update(id):
    with sql.connect("student.db") as conn:
        cur = conn.cursor()
        cur.execute('select * from students where name=?', (id,))
        old_data = cur.fetchone()
        form = StudentForm()
        if form.validate_on_submit():
            t = (form.phone.data, form.email.data,form.address.data, id)
            with sql.connect("student.db") as conn:
                curs = conn.cursor()
                curs.execute("update students set phone =?, email = ?, address =? where name = ?", t)
                conn.commit()
                flash("The record is edited.", "success")
                return redirect(url_for('studentlist'))

        form.name.data = old_data[0]
        form.phone.data = old_data[1]
        form.email.data = old_data[2]
        form.address.data = old_data[3]
        return render_template('add_student.html', form = form )

@app.route('/studentdelete/<string:id>')
def delete(id):
    with sql.connect("student.db") as conn:
        cur = conn.cursor()
        cur.execute('delete from students where name=?', (id,))
        conn.commit()
        form = StudentForm()
        flash("The record is deleted.", "success")
        return redirect(url_for('studentlist'))