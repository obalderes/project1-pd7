from flask import Flask

from flask import request, render_template, url_for, redirect, flash

from ivan_smirnov import util
import util2

app = Flask(__name__)
app.secret_key = 'Whatever'

qlist = open("questions.txt","r").readlines()

@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        #assert username != ""
        #assert password != ""
        #flash("User " + username)
        if util.verifylogin(username, password):
            return redirect(url_for('user_page', name = username))
        else:
            flash("Sorry, incorrect login information for user %s"%(username))
            return redirect(url_for('login'))

#So frustrated. This is an important note to self, David. When you use url_for, the String input is the name of the method of the page, not it's actual URL. Agh!

@app.route("/home")
@app.route("/home/<name>", methods = ['GET', 'POST'])
def user_page(name=None):
    if name == None:
        return redirect(url_for('login'))
    
    if request.method == "GET":
        return render_template("user_page.html", name=name)
    else:
        button = request.form['button']
        if button == 'Rate':
            return redirect(url_for('rate_page', name=name))
        elif button == 'View':
            return redirect(url_for('view_results', name=name))


@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate_page(name=None):
    if name == None:
        return redirect(url_for('login'))
    if request.method == "GET":
        return render_template("rate_page.html",qlist=qlist)
    else:
        tmpscore =[]
        count = 0
        for n in qlist:
            tmp = str(request.form["Button %d" %count])
            tmpscore.append(tmp)
            count = count + 1
        
        uname = request.form['student_rated']
        
        assert uname != ""
        group = util.get_group(str(uname))
        print group
        util2.save_rating(str(uname),str(name),tmpscore,group)
        util2.get_rating(str(name))

        flash("Rating Sent!!!")
        return redirect(url_for('user_page',name=name))



@app.route("/results")
@app.route("/results/<name>")
def view_results(name=None):
    if name == None:
        return redirect(url_for('login'))
    A,S = util2.get_rating(str(name))
    return render_template("results.html", name=name,A=A,S=S,qlist=qlist)


if __name__ == "__main__":
    app.debug = True
    app.run()
