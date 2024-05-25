from git import Repo
from openai_client import ansver_gpt

def main():
    repo = Repo(".")
    
    git_full_text = ""

    for untracked_file in repo.untracked_files:
        with open(untracked_file, 'r') as file:
            content = file.read()
            git_full_text += f"Содержимое файла {untracked_file}:\n"
            git_full_text += content + "\n"
    
    changed_files = [item.a_path for item in repo.index.diff(None)]
    for changed_file in changed_files:
        with open(changed_file, 'r') as file:
            content = file.read()
            git_full_text += f"Содержимое файла {changed_file}:\n"
            git_full_text += content + "\n"

    commit_name = ansver_gpt(git_full_text)

    repo.index.add(repo.untracked_files + changed_files)

    print("Your`s commit name is : ", commit_name)

    repo.index.commit(commit_name)
    
if __name__ == "__main__":
    main()