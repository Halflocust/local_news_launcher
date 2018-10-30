# Launches a News24 article: Asks the user for a topic and lets the user select an article from a list of articles displayd on that topic

import bs4 as bs 
import requests
import webbrowser

res = requests.get("https://www.news24.com/SouthAfrica")

soup = bs.BeautifulSoup(res.text,"html.parser")

articles = soup.find_all(class_ = "col300 news_item ")

article_data = {}


def news_getting(context):
	timmy = 0
	global article_data
	for i in range(len(articles)):
		links = articles[i].find_all("a")
		for item in range(len(links)):
			if context.lower() in links[item].get_text().lower():
				timmy += 1
				article_data[timmy] = [i,item]
				print("{})  {}".format(timmy, links[item].get_text()))
			else:
				pass
	return timmy


def set_choice(choice):
	article = article_data[choice]
	return article


def selecting_article(choice):
	articles_choice = int(choice[0])
	links_choice = int(choice[1])
	links = articles[articles_choice].find_all("a")
	final_link = links[links_choice]["href"]
	return final_link


def run_this():
	print("Enter a topic on local news that you would like to look up on News24 (e.g. Cape Town)")
	choice = input("")
	print("Select a number from the list below and hit the Enter key\n")
	if news_getting(choice) == 0:
		print("That is not a topic in today's local news")
		run_this()

	else: 
		choice = input("")
		try:
			choice = int(choice)
		except:
			choice = ""
		while choice not in article_data.keys():
			print("You did not select an input from the list. Select a number from the list above")
			try:
				choice = int(input(""))
			except:
				choice = ""
		article_selected = set_choice(choice)
		link = selecting_article(article_selected)
		webbrowser.open(link)


run_this()

