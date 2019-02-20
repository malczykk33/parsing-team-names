from bs4 import BeautifulSoup
import requests
import sys, getopt

argumentList = sys.argv[1:]
unixOptions = "hu:"
gnuOptions = ["help", "url="]

page_url = ''
searched_id = 'page_competition_1_block_competition_tables_7_block_competition_league_table_1_table'
searched_class = 'text team large-link'

def help():
	print('Witaj w programie dla Bialuka. \n Instrukcja użycia programu:')
	print('Program zwraca plik csv z listą drużyn danej ligi. Aby zadziałał poprawnie, potrzebuje jednego argumentu: adresu URL z soccerway.com do ligi')
	print('Program zwróci plik w formacie nazwakrajupoangielsku.csv.')

def get_team_list(page_url):
	page = requests.get(page_url)
	page_soup = BeautifulSoup(page.text, 'html.parser')
	searched_table = page_soup.find(id = searched_id)
	found_table = searched_table.find_all('td', {'class' : searched_class})

	country_name = page_url.split('/')[4]
	output_file_name = country_name + '.csv'

	with open(output_file_name, 'w', newline='') as output_file:
		for line in found_table:
			output_file.write(line.get_text())
			output_file.write('\n')

try:
	arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
	print(str(err))
	sys.exit(2)
if not arguments:
	help()
for currArg, currVal in arguments:
	if currArg in ('-u', '--url'):
		print(('Lista drużyn została zapisana w pliku %s') % (currVal.split('/')[4]+'.csv'))
		get_team_list(currVal)
	else:
		help()


