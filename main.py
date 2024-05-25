from git import Repo

from openai_client import ansver_gpt

repo = Repo(".")

git_full_text = ""

for untracked_file in repo.untracked_files:
    with open(untracked_file, 'r') as file:
        content = file.read()
        git_full_text += f"Содержимое файла {untracked_file}:\n"
        git_full_text += content + "\n"

commit_name = ansver_gpt(git_full_text)

repo.index.add(repo.untracked_files)

repo.index.commit(commit_name)

print(f"Committed with message: {commit_name}")