from tkinter import filedialog
import tkinter as tk
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# specify the URL
url = 'https://www.basketball-reference.com/teams/LAL/2023.html'

# send a GET request to the URL
response = requests.get(url)

# parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the table containing player stats
table = soup.find('table', {'id': 'per_game'})

# extract the relevant columns from the table
columns = ['Player', 'Pos', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA','2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
rows = []
for tr in table.find_all('tr')[1:]:
    row = [td.get_text() for td in tr.find_all('td')]
    rows.append(row)

# create a pandas DataFrame from the rows and columns
df = pd.DataFrame(rows, columns=columns)

# clean the data by converting columns to numeric types
df['G'] = pd.to_numeric(df['G'])
df['GS'] = pd.to_numeric(df['GS'])
df['MP'] = pd.to_numeric(df['MP'])
df['FG'] = pd.to_numeric(df['FG'])
df['FGA'] = pd.to_numeric(df['FGA'])
df['FG%'] = pd.to_numeric(df['FG%'])
df['3P'] = pd.to_numeric(df['3P'])
df['3PA'] = pd.to_numeric(df['3PA'])
df['3P%'] = pd.to_numeric(df['3P%'])
df['2P'] = pd.to_numeric(df['2P'])
df['2PA'] = pd.to_numeric(df['2PA'])
df['2P%'] = pd.to_numeric(df['2P%'])
df['eFG%'] = pd.to_numeric(df['eFG%'])
df['FT'] = pd.to_numeric(df['FT'])
df['FTA'] = pd.to_numeric(df['FTA'])
df['FT%'] = pd.to_numeric(df['FT%'])
df['ORB'] = pd.to_numeric(df['ORB'])
df['DRB'] = pd.to_numeric(df['DRB'])
df['TRB'] = pd.to_numeric(df['TRB'])
df['AST'] = pd.to_numeric(df['AST'])
df['STL'] = pd.to_numeric(df['STL'])
df['BLK'] = pd.to_numeric(df['BLK'])
df['TOV'] = pd.to_numeric(df['TOV'])
df['PF'] = pd.to_numeric(df['PF'])
df['PTS'] = pd.to_numeric(df['PTS'])

# remove the 'Pos' column
df.drop(columns=['Pos'], inplace=True)

print(df)

# get the current working directory
cwd = os.getcwd()

# create a tkinter root window
root = tk.Tk()
root.withdraw()

# open a save dialog window to choose where to save the file
file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', initialdir=cwd, title='Save Excel file', filetypes=(
    ('Excel files', '*.xlsx'), ('All files', '*.*')))

# export the cleaned data to an Excel file
df.to_excel(file_path, index=False)