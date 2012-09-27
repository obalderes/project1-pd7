Group 7UP
=========

* * *

## SCHEMA ##

Shelf containing a dictionary of "projects" and a dictionary of "people"

PROJECTS
    1. each project contains a dictionary of "groups"
    1. each group contains a dictionary of "members" 
    1. each member has a name(first,last), and an email adress, and a dictionary of feedback
    1.each entry in feedback is a list of length 4, with room for the period,group,score,and comments.

PEOPLE
    1. each person has a name(first,last) an email adress, and a dictionary of "projects1"
    1.Projects1 is a dictionary that contains a list of groups
    1. each group contains a dictionary of "groupmems"
    1. each groupmem has a name(first,last), an email adress, and list of questions. (It refers to the member within projects)
    1. each question is a list of length 4, with room for one score and one comment (project# and group# are automatically added)

The basic idea is that in our program a user will search themselves up to get their own scores through "PROJECTS," and they will give feedback to to others through the "PEOPLE" dictionary.

