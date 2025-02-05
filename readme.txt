scrap: When it works its awesome for developers and users.
scrap: When it doesnt work simply remove the s!
scrap: run it with "python3 .scrap/scrap.py"
collaberators: rhhen122, pyromanic
info:
to run scrap cd into the directory and run the "python3 scrap/scrap.py"
in the terminal!
install:
to add scrap to yur own project simply cd in to the folder of the project.
"git clone" the repo and then cd into "scrap", then remove the .git folder with "rm -rf .git"
configure:
to configure scrape go into the "info.py" file!
you should see something like this:


# If there is a "*" next to it it is required
name = ("scrap") # This is the name of the scrap *
author = ("vimp") # This is the name of the author *
maintainer = ("rhhen122") # This is the name of the maintainer
version = ("1") # This is the version *
# Below here are important files! dont touch!

readme = ("cat readme.txt")

name indicates the name of the project
author is the author of the project
maintainer indicates the main person responsible for the project, eg. maintaining it!
version indicates the version that scrap is installed to on this project, eg. 1 2 3.5 ect