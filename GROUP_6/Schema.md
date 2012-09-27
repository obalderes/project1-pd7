Schema
======
"Pointers"
----------
	-all of the emails are stored in a list, and the index of the email becomes the ID number</br>
	-log in with email and use indexOf() to get the internal ID</br>
	-send the internal ID to the database to get data</br>
</br>
"Database"
----------
	-A shelve of lists of lists</br>
		-Rating(int[]),Comments(str[]),Groups(int[])</br>
			-The ratings would be in range(0,5)</br>
			-The comments will be formatted as id|title|content. The ID is used to allow editing comments and won't be displayed</br>
			-Groups keeps a record of which groups this person has been in, the newest group is appended to the end of the list</br>
	-avg() average of ratings
	-
