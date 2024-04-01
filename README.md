# GoogleDiscussionsSerp
The script uses the GoogleSearch class from the serpapi library to fetch forum results for each keyword.

It iterates over the list of keywords retrieved from the input CSV file and sends a request to the SERP API for each keyword.

The retrieved forum results are then written into a new CSV file.


**Example**
![Laptop SERP](example.png)


For this search item, we would import this keyword: "Best laptops for graphic design", and get 3 rows with each discussion result in its own csv row:
- keyword, title, link, date (if any but usually not), source (aka domain)
- *Best laptops for graphic design, What are some good laptops for ... - Reddit, https://www.reddit.com/r/graphic_design/..., Reddit.com*
- *Best laptops for graphic design, Laptop for Graphic Designers?, https://www.graphicdesignforum.com/t ... , https://www.graphicdesignforum.com/*
- *Best laptops for graphic design, What laptop do you use for work? ... - Reddit, https://www.reddit.com/r/graphic_design/ ..., Reddit.com*



**Libraries:**
Serp API, CSV

**Description:**

1. Obtain API Key: You need to obtain an API key from [SERP API](https://serpapi.com/) and replace [YOUR API KEY] in the script with your actual API key.

2. Prepare Input CSV: Create a CSV file (keywords.csv by default) containing the list of keywords. Each keyword should be listed in a separate row on the first column. Save it in the same folder as the script.

3. Run the script. 

