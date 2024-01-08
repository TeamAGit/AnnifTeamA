from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# A function that writes the lists with scraped data to a csv file.
def write_data_to_csv(uids, disciplines, titles, keywords_chains, table_of_contents, rvks):
	df = pd.DataFrame({"UID": uids,
					"Discipline": disciplines,
					"Title": titles,
					"Keywords": keywords_chains,
					"Content": table_of_contents,
					"RVK(s)": rvks})

	df.to_csv("extracted_th-wildau_records.csv", index=False)

# Create empty lists where we put in our data.
uids = []
disciplines = [] 
titles = []
keywords_chains = []
table_of_contents = []
rvks = []

# Start with 1 as parameter.
start = 1

try:
	# Since we do not know the exact number of current documents, make an infinite loop. 
	while True:
		url = f"https://solrproxy-wilbert-test.kobv.de/wilbertselect?access=w21%234lCUb&fq=search_space:theses&index=internal&q=*:*&rows=10&start={start}"
		
		time.sleep(1)
		soup = BeautifulSoup(requests.get(url).text, features="xml")

		# Check if all documents are retrieved by comparing start value with number of found records.
		max_publications = int(soup.find("result").get("numFound"))
		print(max_publications)
		print(start)
		# When start higher than the total of publications, write data to file and leave loop.
		if start > max_publications:
			print("No further documents found.")
			write_data_to_csv(uids, disciplines, titles, keywords_chains, table_of_contents, rvks)
			break


		for i, doc in enumerate(soup.find_all("doc")):
			print(f"Publication No {i+1} of starting point {start}")

			# We retrieve the intern IDs to have an unique identifier.
			try:
				uid = doc.find("arr", {"name": "identnr"}).text.strip()
				print(uid)
				uids.append(uid)
			except:
				print("No ID")
				uids.append(None)

			# "Abstract" means research field.
			try:
				discipline = doc.find("arr", {"name": "abstract"}).text.strip()
				print(discipline)
				disciplines.append(discipline)
			except:
				print("No discipline")
				disciplines.append(None)

			try:
				title = doc.find("arr", {"name": "titel"}).text.strip().replace("\n", "|")
				print(title)
				titles.append(title)
			except:
				print("No title")
				titles.append(None)

			# Fetch and prepare keywords as a keyword chain. Use pipes for separation.
			try:
				keyword_chain = doc.find("arr", {"name": "schlagwort"}).text.strip().replace("\n", "|")
				print(keyword_chain)
				keywords_chains.append(keyword_chain)
			except:
				print("No keywords")
				keywords_chains.append(None)

			# Fulltext means table of content. 
			try:
				table_of_content = doc.find("arr", {"name": "fulltext"}).text.strip().replace("\n", "")
				print(table_of_content)
				table_of_contents.append(table_of_content)
			except:
				print("No content")
				table_of_contents.append(None)

			# Sometimes, there is more than one RVK classification signature. Use pipes for separation.
			try:
				rvk = doc.find("arr", {"name": "rvk"}).text.strip().replace("\n", "|")
				print(rvk)
				rvks.append(rvk)
			except:
				print("No RVK")
				rvks.append(None)

		# When finished, increment by 1.
		start += 1

# For test purposes: If ctrl+c is pressed, program will be cancelled and data will be written to csv.
except KeyboardInterrupt:
	print(f"KeyboardInterrupt detected.")
	write_data_to_csv(uids, disciplines, titles, keywords_chains, table_of_contents, rvks)


			
 





