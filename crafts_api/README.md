Hello all! Welcome to my first (but probably not my last) FastAPI project. 

In addition to making my way through the Flatiron School's Software Engineering Bootcamp, I am keeping busy with one million real-life, hands-on, creative projects. 

My goal with this FastAPI debut has been to bring some order to my to-do list. I love to learn, and I am always finding new skills to add to my belt. But between my sewing nook, planting station(s), fabric room, crafting corner, and kitchen counters, projects tend to fall between the cracks. Imagine that! 

Storing and organizing my project lists in one place is a step towards my goal of DIY EVERYTHING! 

I hope that this glimpse into my non-computer life inspires you to dive into a craft of your own. 


More on how I developed this API using FastAPI:

To begin this project, I installed Poetry. Poetry installs packages in Python and sets up the necessary files and dependencies for a project. Running the 'new' command in Poetry sets up a project folder with poetry.lock, pyproject.toml, and README.md files, as well as 'project' and 'tests' folders. I had never seen the file type '.toml' before; it stands for "Tom's Obvious, Minimal Language." This file is meant to make dependency management easier to edit and interact with as a developer. Within the 'project' folder, there existed a pychache folder. 

Once this basic setup was complete, I created my Python files: main.py and project_data.py. 

project_data.py:
I was not yet ready to set up a database, so my data comes from a simply python file. I've created a list of dictionaries to contain data on my various projects. Each project is represented by one dictionary in the list. 

main.py:
Once I imported FastAPI and set my app = FastAPI(), I was ready to start making requests and defining classes. 

My GeneralProject class defines the 'general' format for a project dictionary. I require a number of details(attributes) to be present so that each of my projects can be as specific and well-outlined as possible. I defined methods that conditionally add even more attributes to each project instance. 

I wrote a validator function to ensure that the 'completion status' of each project has valid input.

I've written GET requests for initial load and for a search feature. I developed my search feature so that when you enter a keyword, this function filters through the values of every dictionary in my PROJECTS list and returns a list of dictionaries whose values contain that keyword. In order to make my API SUPER searchable, this keyword could be present in ANY of the values of that dictionary item. 

Finally(so far), I have written a POST request so that new projects can be added to my API. These new projects are instances of the General Project class. 

My first basic FastAPI is complete. Now to create a database!



