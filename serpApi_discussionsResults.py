from serpapi import GoogleSearch
import csv

input_filename = 'keywords.csv'

output_filename = 'forum_results.csv'

def get_forum_results(keyword):
        params = {
            'engine': 'google',
            'q': keyword,
            'api_key': '[YOUR API KEY]',
            'location': 'United States',
            'google_domain': 'google.com',
            'gl': 'us',
            'hl': 'en',
            "device": "mobile",
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        discussions_and_forums = results["discussions_and_forums"]
        return discussions_and_forums

keywords = []
with open(input_filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip the header if there is one
    for row in reader:
        keywords.append(row[0])

with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for keyword in keywords:
        print(keyword)
        try:
            discussionresults = get_forum_results(keyword)
            for i in discussionresults:
                title = i['title']
                print(title)
                link = i['link']
                date = i['date']
                domain = i['source']
                writer.writerow([keyword,title,link,date,domain])
        except:
            continue
