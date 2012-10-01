Our main data structure will be a dictionary keyed by email.
Each email will be keyed to a list that contains its owner's
full name, period, group, a list of people whom they've worked with
(the only people allowed to rate them), and a dictionary keyed by
all the projects the person has worked on. Each project entry will
contain its own dictionary of people who worked on it, keyed by email,
and all the ratings given by the original person to those people.

It's probably better explained like this:
{email : [first, last, period, current group, [people previously and/or currently in same group], {project number : {person : rating}}]}