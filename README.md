# Web-Scraping

## Practice

Put together from a range of sources, including tutorials from FreeCodeCamp with @jimshapedcoding, W3 schools, Real Python, geeksforgeeks and lots of stackoverflow!!

    ### AdvancedScraper/main.py

    - Hard coded URL and sercah term
    - Writes results into individual .txt files

    ### FileHTMLScraper/main.py

    - Opens a saved html file
    - Then runs BeautfulSoup on that
    - Just print findings to terminal

    ### listUrls/listUrls.py

    - Wanted to try out list urls before adding file of urls...as I think im going to try Scrapy to develop this further...
    - Also trialing a -h file....not qute working as expected yet, but must sleep...

    ### MissionOne/simpleHTML.py

    - Was a trial run for my final scraper
    - Takes in args from command line
    - And simply prints a true or false if search term was found
    - Run command as suggested: `python MissionOne/simpleHTML.py 'https://www.woolwarehouse.co.uk/yarn?brand_nav=39580' '4 Ply'`

    ### ScrapeToCsv/trying_pandas.py

    - Exactly how it sounnds..me trying out pandas....didnt really get to grips with that, not sure its workign quite right but didnt feel like i wanted to de-bug it

    ### ScrapeToCsv/bs.py

    - bs.py - hard coded url and looks for table rows, writes the data to a .csv successfuly
    - just trying out beautifulsoup

    ### Trials/main.py 

    - Was my first attempt/understanding of using sys.argv to get args in from the commandline 
    - run with `python AccessingCLArgs/main.py Python Command Line Arguments`

    ### Trials/trialScraper.py 

    - First go at actaully using an arg as serchTerm from the command line, i was really pleased with this one, as i finally managed to get it to append the findings nicely to a .csv and print a statemnt to terminal telling you what file its written to 
    - run with `python Trials/trialScraper.py '4 Ply'`

    ### laurenScraper.py 

    - This was my final go at Mission One
    - Im please with it, takes in a URL and search term from command line
    - Prints out a statement with how many times it appears in page too
    - Run command as suggested: `python laurenScraper.py 'https://www.woolwarehouse.co.uk/yarn?brand_nav=39580' '4 Ply'`

## User Agent String Research

- whatu.info
- useragentstring.com

- python
    - import requests
    - resp-requests.get('https://whatu.info')
    - print(resp.text)
    - will give you a 'Your user agent:' and you can manipulate that from the command line
    - curl '<website>' will show it as a curl command
    - similarly if you run python script will show python
    - if you do curl -A "a string" 'url' will show what ever string you chose

- browser extensions that will change your user agent string to be whatever you want it to be