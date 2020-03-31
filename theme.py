import pandas as pd
theme = pd.read_csv("Theme.csv")
theme_list = []
theme_to_list = theme.values.tolist()
for value in theme_to_list:
    for i in value:
        i = i[1:-1].split(",")
        theme_list += i
theme_list
