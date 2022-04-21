import emoji
from conf import username, languages_count, layout_value, theme_value, print_checkout, pinned_repos, pin_repos
from conf import show_icons_value, private_count_value, custom_titles_list, p_align, exclude_value, exclude_1, exclude_2

text_file = open("public_repos.txt", "r")
lines = text_file.readlines()
public_repos = []
for i in lines: public_repos.append(i[:-1])
print(f"\n{username.capitalize()} public repositories:")
print("--------------------------------")
for i in public_repos: print(f"{i}")
print("--------------------------------")

### DONT CHANGE ###
exclude = "&exclude_repo"
theme = f"&theme={theme_value}"
private_count = f"&count_private={private_count_value}"
language_count = f"&langs_count={languages_count}"
layout = f"&layout={layout_value}"
show_icons = f"&show_icons={show_icons_value}"
base_url = "https://github-readme-stats.vercel.app/api"
github_profile = f"https://github.com/{username}/"
ahref = f'<a href="{github_profile}">'
top_languages_url = f"{base_url}/top-langs/?username={username}{layout}{theme}{private_count}{language_count}"
p_tag = f"<p vertical-align:{p_align}>\n"
p_r = "%20projects"
projects = []
for i in custom_titles_list: projects.append(f"{i}{p_r}")
###################

###################
if not exclude_value:
    exclude_list = f"{top_languages_url})]"
    stats = [f"{top_languages_url}&custom_title=My%20top%20languages"]
else:
    exclude_list = [exclude_1, exclude_2]
    custom_titles = []
    sep_url = []
    stats = []
    for i in projects: custom_titles.append(f"&custom_title={i}")
    for i in range(len(custom_titles)): sep_url.append(f"{top_languages_url}{exclude_list[i]}{custom_titles[i]}")
    for i in sep_url: stats.append(i)
###################

github_stats = f"{base_url}?username={username}{show_icons}{theme}"
repos = []

for i in pinned_repos:
    repos.append(
        f"[![Readme Card]({base_url}/pin/?username={username}&repo={i}{theme})]({github_profile}{i})")
readme_script = "[Check out the script I made for this README.md file](https://github.com/juhamikael/juhamikael/blob/main/makefile.py)"
school_projects = 0

###############
with open('README.md', 'w') as f:
    f.write(f"### Hi, I'm Juha {emoji.emojize(':wave:')} \n")
    f.write(p_tag)
    for i in stats:
        if school_projects == 0:
            ahref = f'<a href="{github_profile}schoolProjects">'
        elif school_projects == 1:
            ahref = f'<a href="{github_profile}?tab=repositories">'

        f.write(f'{ahref}<img src="{i}"/>\n')
        school_projects += 1

    ahref = f'<a href="{github_profile}">'
    f.write(f'{ahref}<img src="{github_stats}"/>\n')
    f.write("</p>\n\n")

    if pin_repos:
        f.write("## Currently working with:")
        f.write("\n")
        for i in repos:
            f.write(i)
            f.write("\n")

    # Can be deleted
    if print_checkout:
        f.write(f"\n\n## {readme_script}\n")

######################
