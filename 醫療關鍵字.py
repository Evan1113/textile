from googlesearch import search

query = "機能布料-"

for j in search(query, stop=5, pause=2.0): 
	print(j)