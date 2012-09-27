Group 7UP
=========

* * *

## SCHEMA ##

Shelf containing a dictionary of "projects" and a dictionary of "people"

PROJECTS
each project contains a dictionary of "groups"
each group contains a dictionary of "members" 
each member has a name(first,last), and an email adress, and a dictionary of feedback
each entry in feedback is a list of length 4, with room for the period,group,score,and comments.

PEOPLE
each person has a name(first,last) an email adress, and a dictionary of "projects1"
Projects1 is a dictionary that contains a list of groups
each group contains a dictionary of "groupmems"
each groupmem has a name(first,last), an email adress, and list of questions. (It refers to the member within projects)
each question is a list of length 4, with room for one score and one comment (project# and group# are automatically added)

The basic idea is that in our program a user will search themselves up to get their own scores through "PROJECTS," and they will give feedback to to others through the "PEOPLE" dictionary.

