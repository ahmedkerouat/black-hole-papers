import arxiv

file_path = "source/current_number.txt"
with open(file_path, "r") as file:
    current_number = int(file.read().strip())
next_number = current_number + 1
with open(file_path, "w") as file:
    file.write(str(next_number))

query = 'title="black hole"'
search = arxiv.Search(query=query,max_results=next_number, sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Ascending)

all_results = list(search.results())
print(len(all_results))
result = all_results[-1]

title = result.title
authors = ', '.join(author.name for author in result.authors)
abstract = result.summary
date = str(result.published).split(" ")[0]

print(f"Title: {title}")
print(f"Authors: {authors}")
print(f"Abstract: {abstract}")
print(f"Date: {date}")




