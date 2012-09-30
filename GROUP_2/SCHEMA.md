database 

a shelf 

this will be a dictionary filled with names of people / email addresses to avoid name conflict

-in the first few spots on the list important information not pertaining to ratings will be held
-the list will then be filled with Ratings.

Utils.py will interact with the database

_____________________________________________________________________________
rating.py

this will be the item appended to the list attached to a name in the database


 Each rating will have: 

-a list of ints corresponding to the answers of the questions
-the Group the person was in / project description
-their role in the project
-the author of the review(encoded)

these will act as 'tags' in a sense to help us sort the data later.

should we use methods? or should we directly acsess the variables.

METHODS:
get_score():
	will return the list containing the scores

get_authorID():
	will return the unique authorID

get_group/project():
	return group or project string	

NOTES:
-once ratings are seperated from the parent, I don't think they'll be able to be found again. This can prevent publicity of names while still allowing for mass comparisons

______________________________________________________________________________

utils.py

the class that is used to interact with the database.

the parameters for save_rate will be filled out using temporary variables assigned based on radiobuttons checked as well as textboxes for names that are on the TEMPLATE.

save_ratings(target,score[],target_group):
	-this will create a rating and append it to d{target}'s list.
	-if we can find a way to stay logged in, we can eliminate some text fields
	-should we store some of the data for parameters in the database?

get_ratings(target):
	-this method is a shortcut for getting all the ratings a person has.
	-this will return a list of the ratings that target has.
	-another method will be used to print or interact with the method

NOTES:
      -Different methods to display the scores
      -Compare scores
__________________________________________________________________________________

app.py



@HOME():

this will be where you login with your email and anything else we want to include on the home page

login(username):
	 will check your email address from a text and take you to your USERPAGE if you exsist on the list.

it will use the HOME_TEMPLATE
 
  ----------

@USERPAGE():


this will be where you view your own ratings, or choose to write a review for someone else.


view_ratings(username=user loggedin):
	-pulls out ratings for your own username, you will not be able to view other people's ratings.

have button for going to @REVIEWPAGE():

it will use the USERPAGE_TEMPLATE
  ----------

@REVIEW PAGE():

Submit():
	-this will take the variables from the radio buttons or text fields and use them for parameters in save_ratings() 
	-this will check to make sure all fields are filled out, an incorrectly filled out form will not save  arating.

it will use REVIEW_TEMPLATE
_______________________________________________________________________________________________________

HOME_TEMPLATE

HTML FILE

variables:
username - a text box

buttons:
submit - login

_____________________________________________________________________________________________________

USERPAGE_TEMPLATE

HTML FILE

when wanted will display your ratings

variables:
a list that can be sent INPUT of RATINGS that will then be printed out

buttons:
review - takes you to the review page

_____________________________________________________________________________________________________

REVIEW_TEMPALTE

HTML FILE

this is the template for the review questions

variables:

radioboxes- for questions (QUESTION1,QUESTION2)
textboxes - for TARGET's name

both of these will be requested from the app.py

buttons
SUBMIT-attempt to submit review.
CANCEL-back to userpage.
_______________________________________________________________________________________________________



