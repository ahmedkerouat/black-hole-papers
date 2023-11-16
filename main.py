import arxiv

file_path = "current_number.txt"
with open(file_path, "r") as file:
    current_number = int(file.read().strip())
next_number = current_number + 1
with open(file_path, "w") as file:
    file.write(str(next_number))

query = 'title="black hole"'
search = arxiv.Search(query=query,max_results=next_number, sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Ascending)

all_results = list(search.results())
result = all_results[-1]

title = f"[{result.title}]({result.entry_id})"
authors = ', '.join(author.name for author in result.authors)
abstract = result.summary.replace("\n", " ") #remove line breaks
date = str(result.published).split(" ")[0]

readme_path = "README.md"
new_paper_info = f"| {title} | {authors} | {date} | {abstract} |\n"

with open(readme_path, "r") as readme_file:
    readme_content = readme_file.readlines()
papers_index = readme_content.index("## License\n")

readme_content.insert(papers_index -1, new_paper_info)
with open(readme_path, "w") as readme_file:
    readme_file.writelines(readme_content)

