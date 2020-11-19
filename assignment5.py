"""
Jordan Phillips
Agile UNO Module 5
Strings and Lists

""" 

# Import exit from system package
from sys import exit


# Import requests library
import requests

 
# Create new dictionary
site_data = {}


# Use open context manager
with open("sites.csv", "r") as infile:

    # Read contents of csv
    data = infile.read()

    # Split based on commas to create a new list called "sites"
    sites = data.split(",")

    
# Create a for loop to retrieve data from the list we've created above
for site in sites:
    print(site)
    site_data[site] = requests.get(site)

 

# Print dictionary data using a for loop and f string format

for key, value in site_data.items():
    print(f"\n{key}:{value}")

 
# 1
#######################################################################

"""
Using string slicing, print out each URL extension below.
"""

# Loop through all items in the list of sites
for site in sites:


    # Slice the last three
    print(site[-1:-3])

# 2
#######################################################################

"""
Print any sites that end with .com below.
"""

# Loop through all items in the list of sites
for site in sites:

    # Use if statement to identify strings containing "com"
    if ".com" in site:
        print(site)

 
# 3
#######################################################################

"""

Convert all site names to upper case and print
"""

for site in sites:
    print(site.upper())

 

# 4
#######################################################################

"""
Add a new site to the list using the input() method to get the name of the
site from the user. Reverse the order of the list and print.
"""

# Append user response to the end of the list of sites
sites.append(input("Please enter a URL."))


# Print list in reverse order
sites.reverse()
print(f"sites reversed are {sites} ")

 

# 5
#######################################################################

"""
Print out 'server' attribute of response of the URL requests of the items
from the list.
"""

for key in site_data.keys():
    for key, value in site_data[key].headers.items():
        if key == 'Server':
            print(f"{key} : {value}")

 

# 6
#######################################################################

"""
Exit using sys module's exit function
"""

exit()
