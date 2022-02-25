import requests

def return_public_repos(username:str):
    url = f"https://api.github.com/users/{username}/repos"
    request = requests.get(url).json()
    public_repos = []
    for i in request: public_repos.append(i["name"])
    return public_repos

def print_repos(repos:list):
    print(f"YOUR PUBLIC REPOS:\n")
    for i in repos: 
        print(f"{i}\n") 

def write_public_repos_to_txt(repos_list:list):
    with open('public_repos.txt', 'w') as f:
        x = 0
        for i in repos_list: 
            f.write(f"{i}\n") 
            x+=1


def exclude_all_but_one_repo(public_repos:list,repo_to_show:str):
    exclude_list = []
    for i in public_repos:
       if i == str(repo_to_show):
           continue
       else:
           exclude_list.append(f"{i},")
    remove_comma = exclude_list[len(exclude_list)-1]
    remove_comma = remove_comma[:-1]
    exclude_list.pop()
    exclude_list.append(remove_comma)
    string_to_return = ""
    for i in exclude_list:
        string_to_return = string_to_return+i
    return string_to_return


text_file = open("public_repos.txt", "r")
lines = text_file.readlines()
public_repos = []
for i in lines: public_repos.append(i[:-1])