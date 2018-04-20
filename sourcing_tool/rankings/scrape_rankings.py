from bs4 import BeautifulSoup
from fuzzywuzzy import process
import requests
import sys

from universities.models import UnivBaseTable

# get list of all universities to match unit ids to names
all_universities = UnivBaseTable.objects.values('unitid','school_name')
univ_dict = {univ['school_name']: univ['unitid'] for univ in all_universities}
univ_names = [univ['school_name'] for univ in all_universities]

# url for us news and world report dat
base_url = 'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data'

f = open('rankings.txt', 'w', encoding='utf-8')

# set range to number of pages to scrape from us news
for i in range(1,10):
    # get html for page i
    url = base_url + '/page+' + str(i)
    html = requests.get(url).text

    # parse html
    soup = BeautifulSoup(html, 'html.parser')

    # add row for each valid tr tag
    for row in soup.find_all('tr'):
        # get rank
        rank_raw = row.find(class_='rankscore-bronze')
        if rank_raw:
            rank_text = rank_raw.text
            rank = ''.join(filter(lambda x: x.isdigit(), rank_text))
            if rank:
                f.write(rank)
                f.write(',')
                # get name
                name = row.find(class_='school-name')
                if name:
                    name_text = name.text
                    f.write('"' + name_text + '"')
                    f.write(',')
                    # get university id
                    # NOTE: This is not perfect! Take a look at the results to make sure they look right
                    match = process.extractOne(name_text, univ_names)
                    match_id = univ_dict[match[0]]
                    f.write(str(match_id))
                    f.write(',')
                else:
                    f.write('null,null')
                f.write('\n')

f.close()
