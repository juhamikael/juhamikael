from own_function_lib import exclude_list

exclude = "&exclude_repo"
text_file = open("public_repos.txt", "r")
lines = text_file.readlines()
public_repos = []
for i in lines: public_repos.append(i[:-1])

for_school_projects = exclude_list(public_repos)
print("Exclude for school: ", for_school_projects)


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
exclude_1 = f"{exclude}={for_school_projects}"
exclude_2 = f"{exclude}=WeatherApp,schoolProjects,self_driving_car_SJOM21"
pinned_repos = ["liigadata_analysis", "MacroCounter"]
###################


