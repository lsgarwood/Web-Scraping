- Scraping a practice website (home.html) to get to grips with idea, whihc will just be kept in same directory
- Going to use beautifulsoup4 and lxml libraries
- Then will move onto storing whta we have scraped
- We will be working with file objects in this tutorial
- using open() we will give it the html file name we want to scrape and specify that we only want to read the file with 'r', and use it as html_file variable
- apply the read() method on the html_file variable, and print that content
- run main.py and you should see the html content from the file

----------------------

- use prettify on that content to make it clearer
- make a new instance of the beautifulSoup library, and give it content and a parser: we will use lxml
- print whats in that soup variable, with prettify method, make sit nicer to read

- how to grab specific information: use inbuilt methods of BS
- create a variable and use soup.find('h5'), giving it a string to look for, .find() will give you the first element and stops
- now try .find_all('h5') will bring back a list
    `[<h5 class="card-title">Python for beginners</h5>, <h5 class="card-title">Python Web Development</h5>, <h5 class="card-title">Python Machine Learning</h5>]`
- we can now iterate over the list and bring back each of the courses using a for loop
- now on each element of the list we can use the .text method:
    `Python for beginners
     Python Web Development
     Python Machine Learning`

-------------------------

- Now lets return each of the course cards ('div') and get the price ('a') out of each one
- make a course_cards variable and use the find_all method on soup, filter the results on 'class=card'
- Then for each course cards we can look for the course name and course price with a for loop
- So for each course in the list, we can get the name of the course with .text and the price with .text.split

-----------------------------



