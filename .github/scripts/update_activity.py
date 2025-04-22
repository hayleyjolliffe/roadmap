import os
import subprocess
import datetime

readme_file = "README.md"

today = datetime.date.today()
start_date = today - datetime.timedelta(days=7)

commits = subprocess.check_output(
    ["git", "log", "--since='7 days ago'", "--pretty=format:%ad", "--date=short"]
).decode("utf-8").splitlines()

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
commit_dates = {line.strip() for line in commits}

habit_tracker = "| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n|-----|-----|-----|-----|-----|-----|-----|\n"
for i in range(7):
    current_day = start_date + datetime.timedelta(days=i)
    day_str = current_day.strftime("%Y-%m-%d")
    if day_str in commit_dates:
        habit_tracker += "| 🟩 "
    else:
        habit_tracker += "| 🟥 "
    if i == 6:
        habit_tracker += "|\n"
    else:
        habit_tracker += ""

with open(readme_file, "r") as f:
    readme_content = f.readlines()

for i, line in enumerate(readme_content):
    if line.startswith("## Activity"):
        readme_content[i + 1] = habit_tracker

with open(readme_file, "w") as f:
    f.writelines(readme_content)

print("Activity updated successfully.")
