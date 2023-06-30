# to read and execute the file named hello.py in the main.py filer from the same directory 
# exec(open('hello.py').read())  

# command line arguments in python 
"""
    --> py hello.py  
        to run file hello.py 

now we can also pass in some arguments after py hello.py 
for e.g. py hello.py 123
we can pass in as many params as we want 
to access this 123 we need to import sys 
"""

import sys 

print('hello')
print('total parameters ', len(sys.argv))

"""
    it will always give num of param as n+1 
    as it considers the hello.py as 1st param

"""
print(sys.argv[0])
print(sys.argv[1])
print(type(sys.argv[1])) # strig 

"""
touch app.py --> create a new file named app.py 
gedit app.py --> edit app.py 

py -m venv env --> create virtual env 

.\env\Scripts\activate --> activate virtual env 
.\env\Scripts\deactivate.bat --> deactivate

pip freeze --> to show all the installed packages 
pip freeze > requirements.txt --> create requirements.txt
"""