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

#@app.route("/choose/<name>")
#def choose_member(name=None):
 #   if name == None:
  #      return redirect(url_for('login'))
   # groupnum = util.get_group(str(name))
    #periodnum = util.get_period(str(name))
    #gmembers = []
    #gmembers.append(util.get_groupMembers(groupnum,periodnum))
    #return render_template("choose.html", name=name, groupnum=groupnum, periodnum=periodnum,gmembers=gmembers)

@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate_page(name=None):
    if name == None:
        return redirect(url_for('login'))
    names = util.get_group_members(str(name))
    emails = names
    if request.method == "GET":
        #print names, emails
        return render_template("rate_page.html",qlist=qlist,names=names, emails=emails)
    else:
        group_members = util.get_group_members(name)
        counta = 0
        for member in group_members:
            tmpscore = []
            countb = 0
            for q in qlist:
                tmp = str(request.form["emails[%d]:Button %d" %(counta,countb)])
                countb = countb + 1
                tmpscore.append(tmp)
            group = util.get_group(str(group_members[counta]))
            util2.save_rating(str(group_members[counta]),str(name),tmpscore,group)
            util2.get_rating(str(group_members[counta]))
            counta = counta + 1

        flash("Ratings Sent!!!")
        return redirect(url_for('user_page',name=name))


@app.route("/results")
@app.route("/results/<name>")
def view_results(name=None):
    if name == None:
        return redirect(url_for('login'))
    A,S = util2.get_rating(str(name))

    #tempScores = S
    #scoreSum = 0
    #scoreLength = S.len
    #for score in S:
    
    #Compiling statistics for author by author scores.
    tempScores = S
    #print tempScores
    sums = []
    for scoreList in tempScores:
        tmpInt = 0
        for rating in scoreList:
            tmpInt = tmpInt + int(rating)
        sums.append(tmpInt)
    #print sums
    lengths = [len(x) for x in S]
    #print lengths
    means = [int(sums[x]/lengths[x]) for x in range(len(S))]
    #print means
 
    return render_template("results.html", name=name,A=A,S=S,qlist=qlist, means=means)


if __name__ == "__main__":
    app.debug = True
    app.run(port=7010)
