# CS50 Final Project: Global Open-Source News
This project is a webpage where that allows users to search and view news from nearly every corner of every country in over 100 languages. The idea behind the project is my belief that the world will benefit from non-traditional news sources. This project provides the accessibility to find these non-traditional news sources, completely unabridged.

# Features:

•	Python

•	Django

•	CSS

•	Geojson

•	Sqlite3

•	Flask

•	BS4

•	additional small libraries or packages

# How the webpage works?

GDELT uses verbal conflict variables to quantify their data. Conflict variables are keywords that are queried throughout global news sources, and indicate that a conflict event has taken place. Various counties are color-coded, which quantifies the degree of conflict events (herein, data density) in the news for that country.

The webpage contains 4 html pages; Index, Map View, Article View, and Contact Us. The Index page, called Latest News, shows an interactive World map. When a user hovers over a country, the country name and data density display in the top right corner of the map. Clicking on the country will open a pop-up and display URL sources to any recent articles containing a conflict event.

The Map View page also displays an interactive map, with an added search bar at the top of the page. The functionality of this page is to input a keyword, such as “technology”, and the interactive map will update to reflect the data density to which that keyword has been found within news sources for that country. Clicking on the country will open a pop-up and display URL sources to any recent articles containing that keyword.

The Article View page displays various news articles from around the World. The articles are generated based on the amount of verbal conflict variables found within the article. There is also a search bar located at the top of this page. Typing a keyword will update the page to populate news articles in which that keyword has been found.

Finally, the Contact Us page displays a map and fillable information fields. The map is interactive, but defaults to the location this project was created, Alexandria, VA. The fillable fields include; Name, Email, Subject, and a larger Message box. Once the fields are filled, a user can click “Send Message Now” which will generate and send an email to the page owner.

# API Integration

This webpage utilizes multiple API’s provided by the Global Database of Events, Language, and Tone (GDELT) Project. There are two main API’s that provide functionality to the webpage; the Visual Global Knowledge Graph and the Event Database.

Visual Global Knowledge Graph:
- Time Range: December 2015 – Present
- Update Interval: Every 15 minutes
- Source: Worldwide news imagery, with all annotations performed by Google Cloud Vision API
- Download / Documentation: http://blog.gdeltproject.org/gdelt-visual-knowledge-graph-vgkg-v1-0-available/

Event Database:
- Time Range: February 2015 – Present (Will extend back to 1979 by Fall 2016)
- Update Interval: Every 15 minutes
- Source: Worldwide news coverage in 100 languages, 65 are live machine translated at 100% volume
- Download / Documentation: http://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/

When a user utilizes the keyword search, this initializes a GET request of the keyword. Then a URL GET request is forwarded to the GDELT API, which queries that keyword. The response to that request is returned and integrated with Json/Geojson to show on the webpage.

# How to launch application
1.	Check that you have Node version 8+
2.	Clone the code: `git clone` https://github.com/afox1987/CS50-final-project.git
3.	Run command prompt in the folder and run `npm install` to install all dependencies
4.	Once installed run command `npm start`
5.	In your browser go to localhost:3000
6.	Enjoy the project!
