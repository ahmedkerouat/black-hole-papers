import urllib.request as ur
import feedparser
from datetime import datetime

# Base api query url
base_url = 'http://export.arxiv.org/api/query?'

# get last paper index
file_path = "current_number.txt"
with open(file_path, "r") as file:
    current_number = int(file.read().strip())
next_number = current_number + 1
with open(file_path, "w") as file:
    file.write(str(next_number))

# Search parameters
search_query = 'all:black+hole' # search for black hole
start = next_number                      # start at the last paper index + 1
total_results = next_number + 1              # want one result
results_per_iteration = 1       # one result at a time

for i in range(start,total_results,results_per_iteration):
    
    
    query = 'search_query=%s&start=%i&max_results=%i&sortBy=submittedDate&sortOrder=ascending' % (search_query,
                                                         i,
                                                        results_per_iteration)

    # perform a GET request using the base_url and query
    response = ur.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)

    # Run through each entry, and print out information
    for entry in feed.entries:

        title = f"[{entry.title}]({entry.id})"
        authors = ', '.join(author.name for author in entry.authors)
        abstract = entry.summary.replace("\n", " ") #remove line breaks
        date = str(entry.published).split(" ")[0]
        datetime_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        date = datetime_object.strftime('%Y-%m-%d')
        
        # write into the readme
        readme_path = "README.md"
        new_paper_info = f"| {title} | {authors} | {date} | {abstract} |\n"

        with open(readme_path, "r") as readme_file:
            readme_content = readme_file.readlines()
        papers_index = readme_content.index("## License\n")

        readme_content.insert(papers_index -1, new_paper_info)
        with open(readme_path, "w") as readme_file:
            readme_file.writelines(readme_content)