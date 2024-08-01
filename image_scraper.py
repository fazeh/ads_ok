import requests
from bs4 import BeautifulSoup
from nevarneyox import qasok


# URL = "https://stock.adobe.com/az/contributor/211076316/Vugar" 
URL = 'https://stock.adobe.com/az/search?creator_id=211076316&filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfetch_excluded_assets%5D=1&filters%5Bcontent_type%3Aimage%5D=1&order=relevance&safe_search=1&limit=100&search_page=18&load_type=page&search_type=pagination&get_facets=0'
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html.parser') 
   
data_content_ids = set()
for element in soup.find_all(attrs={"data-content-id": True}):
    # parent_div = soup.find('div', class_='search-result-cell')
    # print(element)
    if_image = element.find('div', itemtype='https://schema.org/ImageObject')
    if if_image:
        data_content_ids.add(element["data-content-id"])

for data_content_id in data_content_ids:
    print('sending asset: ' + str(data_content_id))
    qasok(data_content_id)



# reveal_turn.run_sel()