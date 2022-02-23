import emoji
exclude_personal_projects = "&exclude_repo=macro_counter_database,liigadata_analysis,unzipper,make_new_folder,fl_studio_stem_renamer"
exclude_school_projects = "&exclude_repo=WeatherApp,schoolProjects,self_driving_car_SJOM21"

base_url = "https://github-readme-stats.vercel.app/api/top-langs/"
git_hub_readme_stats = "(https://github.com/anuraghazra/github-readme-stats)"
username = "?username=juhamikael"
github_profile = "https://github.com/juhamikael/"
layout = "&layout=compact"

projects = ["School%20projects", "Personal%20projects",
            "School projects", "Personal projects"]

title = [f"![Top Langs on {projects[2]}]", f"[![Top Langs on {projects[3]}]"]

title_school = f"&custom_title={projects[0]}"
title_personal = f"&custom_title={projects[1]}"

theme = f"&theme=dark"
private_count = f"&count_private=true"
language_count = f"&langs_count=3"
line_height = "&line_height=100"

readme_script = "[Check out the script I made to make this README.md file](https://github.com/juhamikael/juhamikael/blob/main/makefile.py)"

school_project_url = f"{base_url}{username}{layout}{exclude_personal_projects}{title_school}{theme}{line_height}{language_count}{private_count}{language_count})]"
personal_project_url = f"{base_url}{username}{layout}{exclude_school_projects}{title_personal}{theme}{line_height}{private_count}{language_count})]"
github_stats = "https://github-readme-stats.vercel.app/api?username=juhamikael&show_icons=true&theme=dark"

readme_pinned_repos = ["liigadata_analysis", "MacroCounter"]

repos = []
for i in readme_pinned_repos:
    repos.append(
        f"[![Readme Card](https://github-readme-stats.vercel.app/api/pin/{username}&repo={i}{theme})]({github_profile}{i})")

print(repos)


stats = [school_project_url, personal_project_url, github_stats]


with open('README.md', 'w') as f:

    f.write(f"### Hi, I'm Juha {emoji.emojize(':wave:')} \n")

    f.write("<p vertical-align:top>")

    for i in stats:
        f.write(f'<a href="{github_profile}"><img src="{i}"/>')
        f.write("\n")
    f.write("</p>\n\n")

    f.write("## Currently Working with:")
    f.write("\n")
    for i in repos:
        f.write(i)
        f.write("\n")

    # Can be deleted
    f.write(f"\n\n## {readme_script}\n")
