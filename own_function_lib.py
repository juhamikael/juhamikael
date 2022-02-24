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