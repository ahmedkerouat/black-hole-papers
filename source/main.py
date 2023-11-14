import arxiv
from datetime import datetime

query = 'title="black hole"'
search = arxiv.Search(query=query, sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Ascending)

# Get the oldest article
oldest_article = next(search.results())

title = oldest_article.title
authors = ', '.join(author.name for author in oldest_article.authors)
abstract = oldest_article.summary
date = str(oldest_article.published).split(" ")[0]

print(f"Title: {title}")
print(f"Authors: {authors}")
print(f"Abstract: {abstract}")
print(f"Date: {date}")
