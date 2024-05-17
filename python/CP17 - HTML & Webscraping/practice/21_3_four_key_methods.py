# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

from bs4 import BeautifulSoup
import requests


'''
Basically everything you need to do with scraping can be accomplished with
four methods: 

    - .find('element_name', attrs={'attribute_name' : 'attribute_value'})
        - This finds the first occurence of an element within the html soup that you run it on.
        - So if you run it on the whole page, it will find the first element you specify,
            but if you run it on a subset of the html, it will find the first element you specify in that subset

    - .find_all('element_name', attrs={'attribute_name' : 'attribute_value'})
        - same as .find but gets all the elements within the html soup that you run it on, not just the first.
        - it returns a list, so you either need to loop through the list, or access a specific thing you want like list[2] to get the 3rd thing, etc.

    - .get_text()
        - grabs all the text from whatever html is contained in a soup object. Could be a single element, or multiple elements

    - .get('attribute_name')
        - gets the value of an attribute.
        so if you have <p class="example text">  and you did .get('class') it would return "example text"

'''





'''
To simplify things at first, let's just look at a page for a single book
https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html

'''

# Store the response object, create beautifulsoup object of the url above
response = requests.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
soup = BeautifulSoup(response.content, "html.parser")

# .find method will find the first occurence of an element / tag
# soup.find('tag_name')
# how about you find the first <p> tag and print it out.
# In another line, try finding the title of the page and printing it out

p_tag = soup.find("p")
print(p_tag)
# try printing out just the text using .get_text()


# use soup.find_all('tag_name') to get all occurences of a tag
# try getting all the p tags
all_p_tag = soup.find_all("p")
print(all_p_tag)

title = soup.find("title")
print(title)

# loop through and run .get_text() on all the p tags you found
print(p_tag.get_text())
print(title.get_text()) 

list_p_tags = soup.find_all("p")
print(list_p_tags)
for p_tag in list_p_tags:
    print(p_tag)



print("\n \n ------------- \n")
# find and find_all have a parameter for attrs={'attribute_name' : 'attribute value'}
# this lets you get pretty specific about what we want to find.
# find the first occurence of a div tag with a class attribute that has an id of "product_description"
# store the result in a variable, and then print it out.

specific_div = soup.find('div', attrs={'id': "product_description"}) #could add class tags as well to get indepth with description
print(specific_div)

# when you've stored a specific element that has child tags, you can run any of the methods we've learned
# to grab stuff inside it. For example, on the variable you stored above, run .find and get the "h2" element
print("\n ------------- \n")
h2_element = specific_div.find('h2')
print(h2_element)

# note that if you just wanted the h2 inside of the div with the id of product description, you could just do that 
# all on one line by chaining two finds.
# try to print out the h2 element inside of the   
print("\n ------------- \n")
print(soup.find('div', attrs={'id': "product_description"}).find('h2'))

'''
Why not just do .find('h2')? Sometimes, there are multiple instances of an element on a page,
but you only want a specific one. By first selecting a uniquely defined element (with an id or a class)
and then finding elements that are nested inside it, you can make your web scraping code more robust.

'''

# let's go back to the div class you stored in a variable.
# you can also access a specific tag's attribute values by using square brackets or the .get method
# try printing out the value of "id" using .get()
# then, try printing out the value of "class" using .get()
# get returns the value as a string for all attributes, with the exception of "class". When you use
# "class" it returns a list, since class can potentially have multiple values in a single element.
print("\n ------------- \n")
specific_div = soup.find('div', attrs={'id': "product_description"})
print(specific_div)
print(specific_div.get('id'))
print(specific_div.get('class'))
print(specific_div.get('class')[0]) # because class returns list, you need to use square brackets if you just want the text 

