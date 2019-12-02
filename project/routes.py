from flask import render_template, url_for, flash, redirect,request
from project import app,db
from project.forms import RegistrationForm, LoginForm, SubmitForm
from project.models import User
from flask_login import login_user,current_user,logout_user,login_required
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)


posts = [
    {
        'title': 'Lesson 1',
        'content': 'Alphabets from A->M',
        'lesson':'A B C D E F G H I J K L M',
        'number' : '1'
    },
    {
        'title': 'Lesson 2',
        'content': 'Alphabets from N>Z',
        'lesson' : 'N O P Q R S T U V W X Y Z',
        'number' : '2'
    },
        {
        'title': 'Lesson 3',
        'content': 'A Simple Word',
        'lesson' : 'Happy',
        'number' : '3'
    },
    {
        'title': 'Lesson 4',
        'content': 'Simple Words',
        'lesson' : 'Good Bad Right Wrong',
        'number' : '4'
    },
        {
        'title': 'Lesson 5',
        'content': 'Simple Words',
        'lesson' : 'Hello, World',
        'number' : '5'
    },
    {
        'title': 'Lesson 6',
        'content': 'Simple Sentence',
        'lesson' : 'I am learning to type.',
        'number' : '6'
    },
        {
        'title': 'Lesson 7',
        'content': 'Simple Sentence',
        'lesson' : 'Hi, my name is John.',
        'number' : '7'
    },
    {
        'title': 'Lesson 8',
        'content': 'Intermediate Sentence',
        'lesson' : 'Python is a good programming language.',
        'number' : '8'
    },
    {
        'title': 'Lesson 9',
        'content': 'Good Sentence',
        'lesson' : 'The sky, at sunset, looked like a carnivorous flower.',
        'number' : '9'
    },
    {
        'title': 'Lesson 10',
        'content': 'Difficult Sentence',
        'lesson' : 'No matter what you are going through, there is a light at the end of the tunnel.',
        'number' : '10'
    }
]


@app.route("/")
@app.route("/welcome", methods = ['GET','POST'])
def welcome():
    return render_template('welcome.html')


@app.route("/lessons")
@login_required
def lessons():
    return render_template('lessons.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('lessons'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created for "+ str(form.username.data),'success')
        return redirect(url_for('login'))
    return render_template('register.html', title= 'Register', form = form)

@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('lessons'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and  user.password == form.password.data:
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            flash("You have been logged in succesfully",'success')
            return redirect(next_page) if next_page else redirect(url_for('lessons'))
        else:
            flash("Login Unsuccesful.Please check your email and password!",'danger')
    return render_template('login.html', title= 'Login', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('welcome'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title= 'Account')



@app.route("/lesson1", methods = ['GET','POST'])
def lesson1():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[0]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 1",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[0]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[0]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
            engine.runAndWait()
    return render_template('lesson1.html',title = 'Lesson 1',form = form, posts=posts)

@app.route("/lesson2", methods = ['GET','POST'])
def lesson2():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[1]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 2",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[1]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[1]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
            engine.runAndWait()
    return render_template('lesson2.html',title = 'Lesson 2',form = form, posts=posts)

@app.route("/lesson3", methods = ['GET','POST'])
def lesson3():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[2]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 3",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[2]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[2]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
            engine.runAndWait()
    return render_template('lesson3.html',title = 'Lesson 3',form = form, posts=posts)

@app.route("/lesson4", methods = ['GET','POST'])
def lesson4():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[3]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 4",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[3]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[3]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
            engine.runAndWait()
    return render_template('lesson4.html',title = 'Lesson 4',form = form, posts=posts)

@app.route("/lesson5", methods = ['GET','POST'])
def lesson5():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[4]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 5",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[4]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[4]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
            engine.runAndWait()
    return render_template('lesson5.html',title = 'Lesson 5',form = form, posts=posts)

@app.route("/lesson6", methods = ['GET','POST'])
def lesson6():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[5]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 6",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[5]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[5]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
    return render_template('lesson6.html',title = 'Lesson 6',form = form, posts=posts)

@app.route("/lesson7", methods = ['GET','POST'])
def lesson7():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[6]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 7",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[6]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[6]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
    return render_template('lesson7.html',title = 'Lesson 7',form = form, posts=posts)

@app.route("/lesson8", methods = ['GET','POST'])
def lesson8():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[7]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 8",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[7]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[7]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
    return render_template('lesson8.html',title = 'Lesson 8',form = form, posts=posts)

@app.route("/lesson9", methods = ['GET','POST'])
def lesson9():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[8]['lesson']:
            engine.say("Good Job")
            engine.runAndWait()
            flash("You have finished lesson 9",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[8]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[8]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
    return render_template('lesson9.html',title = 'Lesson 9',form = form, posts=posts)

@app.route("/lesson10", methods = ['GET','POST'])
def lesson10():
    form = SubmitForm()
    if form.validate_on_submit():
        if form.answer.data == posts[9]['lesson']:
            engine.say("Good Job")
            engine.say("You have succesfully finished the course! Congrats")
            engine.runAndWait()
            flash("You have finished lesson 10 and with that you have succesfully completed this course!",'success')
            return redirect(url_for('lessons'))
        else:
            count =0
            l1 = [ch for ch in form.answer.data]
            l2 = [char for char in posts[9]['lesson']]
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    count +=1
            engine.say("Wrong Answer!")
            acc = str(((count*100.0)/len(posts[9]['lesson'])))
            flash("Wrong Answer,Try Again!  Your Accuracy rate was " + acc + "%",'danger')
            engine.say("Your Accuracy Rate was" + acc + "percent")
            engine.say("You have typed the following text")
            for char in form.answer.data:
                if char == " ":
                    engine.say("space")
                elif char == ".":
                    engine.say("full stop")
                elif char == ",":
                    engine.say("comma")
                elif char == "/":
                    engine.say("forward slash")
                elif char == ":":
                    engine.say("colon")
                elif char == ";":
                    engine.say("semi colon")
                elif char == "'":
                    engine.say("apostrophe")
                else:
                    engine.say(char)
    return render_template('lesson10.html',title = 'Lesson 10',form = form, posts=posts)
























