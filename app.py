import tkinter as tk
import requests

#make an API call
url = "http://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#convert the responses object o a dictionary

response_dict = r.json()

#process results
print(response_dict.keys())
print(f"Total repos: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

print("explore info about the repos")
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("Examine the first repo")
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):print(key)

#Tkinker GUI
root = tk.Tk()
text = tk.Text(root)

text.insert(tk.INSERT, f'\nKeys: {len(repo_dict)}') 
text.insert(tk.INSERT, keyOut) 
text.pack()

root.mainloop()