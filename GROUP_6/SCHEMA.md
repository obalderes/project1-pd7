#Schema and Designs
##Schema
###"Pointers"
	-all of the emails are stored in a list, and the index of the email becomes the ID number
	-log in with email and use indexOf() to get the internal ID
	-send the internal ID to the database to get data
</br>
###"Database"
####Structure
	-A shelve of information, comments and groups
		-Information (list)
			-name
			-email
			-currentgroup
			(profile picture is stored in profilepictures/[id#].png)
		-Comments(list of list)
			-id[] (id of the commenter is not displayed, but kept to allow editing)
			-ratings[] (0 to 5 stars)
			-titles[] (a short phrase summarizing the comment)
			-content[] (the comment itself)
			-timestamp[] (in POSIX time, used to display comments in order) 
####Methods
	-avg() average of all ratings
	-getComments(id) returns the entire comments list for the specified 
	-leaveComment(idofreceiver, id,rating,title,comment) check the IDs and store the comment into the shelve with a timestamp
	-changeGroup(group) changes the currentgroup

##Design sketches
![Homepage](Design-sketches/Homepage.png)Project name subject to change<br />
![Dashboard](Design-sketches/Dashboard.png)<br />
![Group](Design-sketches/Group.png)<br />
![Browse](Design-sketches/Browse.png)<br />
![Account](Design-sketches/Account.png)<br />