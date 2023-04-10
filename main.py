import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://www.basketball-reference.com/teams/LAL/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with the team performance data
team_table = soup.find("table", {"id": "team_and_opponent"})

# Extract the team performance data from the table
team_data = []
for row in team_table.tbody.find_all("tr"):
    row_data = []
    for cell in row.find_all(["th", "td"]):
        row_data.append(cell.text)
    team_data.append(row_data)

# Print the team performance data
print(team_data)