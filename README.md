This project was created on 27 July 2020 as part of the Udacity Programming for Data Science with Python Nanodegree program.

### BikeShare
This project was established to create an interactive interface for the user to request statistical data regarding BikeShare data in 3 US cities.


### Files used
3 data files (.csv) were used as provided by Udacity with data for Chicago, New York City and Washington.

1 code file (.py) is used to create the interactive experience and to provide the requested statistics.

### Credits
This repository was forked from udacity/pdsnd_github. Many thanks go to Richard Kalehoff for the lesson material and instruction videos on git and GitHub.
Similarly many thanks to everyone at Udacity for the course material and the mentor help on Knowledge.

### Built with
Anaconda for the Python Code

Atom for Code editing

Git Bash as terminal for git

### Known bugs - still requires a fix
There is a known bug in the .py code. 
Use case:
In def load_data(), the final question to request whether the user would like to see 5 ros of data. If the sequence to answer these questions is:
Yes followed by No, the output is:
"Goodbye!
Would you like to see 5 rows of raw data? PLease enter Y for Yes, or N to exit"

The while loop needs to be reviewed to resolve this problem and end the loop after "Goodbye!"