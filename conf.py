from own_function_lib import exclude_all_but_one_repo
from own_function_lib import public_repos


for_exclude_1 = exclude_all_but_one_repo(public_repos,"schoolProjects")

### CHANGE THESE ##
username = "juhamikael"
languages_count = 4
layout_value = "compact"
theme_value = "dark"
show_icons_value = "true"
private_count_value = "true"  # true / false
custom_titles_list = ["School", "Personal"]
p_align = "top"
exclude_value = True
print_checkout = True
pin_repos = True
exclude_1 = f"&exclude_repo={for_exclude_1}"
exclude_2 = f"&exclude_repo=schoolProjects,WeatherApp"
pinned_repos = ["macroReact_PythonAPI", "liigadata_analysis"]
###################



