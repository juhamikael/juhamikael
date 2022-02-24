from conf import username
from own_function_lib import return_public_repos, write_public_repos_to_txt

repos = return_public_repos(username)
write_public_repos_to_txt(repos)