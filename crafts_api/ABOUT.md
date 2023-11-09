
To begin this project, I installed Poetry. Poetry installs packages in Python and sets up the necessary files and dependencies for a project. Running the 'new' command in Poetry sets up a project folder with poetry.lock, pyproject.toml, and README.md files, as well as 'project' and 'tests' folders. I had never seen the file type '.toml' before; it stands for "Tom's Obvious, Minimal Language." This file is meant to make dependency management easier to edit and interact with as a developer. Within the 'project' folder, there existed a pychache folder. 

Once this basic setup was complete, I created my Python files: main.py and project_data.py. 

project_data.py:
I was not yet ready to set up a database, so my data comes from a simple python file. I'd created a list of dictionaries to contain data on my various projects. Each project is represented by one dictionary in the list. 

main.py:
Once I imported FastAPI and set my app = FastAPI(), I was ready to start making requests and defining classes. 

My GeneralProject class defined the 'general' format for a project dictionary. I require a number of attributes to be passed when instantiating a GeneralProject so that each of my projects can be as specific and detailed as possible. I defined methods that conditionally add even more attributes to each project instance. 

I wrote a validator function to ensure that the 'completion status' of each project has valid input.

I'd written GET requests for initial load and for a search feature. I developed my search feature so that when you enter a keyword, this function filters through the values of every dictionary in my PROJECTS list and returns a list of dictionaries whose values contain that keyword. In order to make my API SUPER searchable, this keyword could be present in ANY of the values of that dictionary item. 

Finally(so far), I had written a POST request so that new projects can be added to my API. These new projects are instances of the General Project class. 

This was all done before I decided to bite the bullet and create a database using SQLAlchemy(SQLite). I want my data to persist, not just to be manually inputted to my python file. Thus began the database tutorial...

I did not have knowledge of database creation before this project. I was able to piece together code using 'The Ultimate FastAPI Tutorial' and explanations from a friendly AI bot. 

Bringing a database into the mix forced me to restructure my files, to rewrite most of my code so that it was accessing data from a database, not a python file. I created the following new files: crud, project_model, database, and api_schemas. 

    crud: where functions are written to access the database directly and perform the preamble to my delete, post, search capabilities. 

    project_model: where I define the Class for a Project and the structure for the database table, directing data to columns.

    database: where I define the database itself with a link, and the concept of a 'session' with variables

    api_schemas: where I define classes for data coming in and out of the API, validating their structures(str, int)

After assuring that each of these files can access the others, I rewrote my get/post/delete/search functions to reference the corresponding functions in crud.py. This allowed respective functions access to the appropriate data. I kept the function that validates a project's completion status because you never know when it may come in handy! 

Finally, I connected my initial Get request to a Jinja2Template. The HTML code is basic but allows very easy communication between the python file and the viewable web-app. I made two pages: one initial index.html that outlines my data in list form, and table.html which outlines the data in a (any guesses?) table! I took more time to do in-file css styling with the table file because I like that view better. 

Overall, I am very proud of this work. I was temporarily hesitant to jump to content that will be covered in the next couple of weeks of my course, but I am glad I moved past that hesitation. It is very satisfying to see the work that I put in be translated to a functional API/database that I will certainly continue to use (and develop). 