import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as soup
from time import sleep

# from database import insert_hotel
from sent_classifier.database.database import insert_hotel

# configurations
BASE_URL = 'https://www.tripadvisor.com'

scraper_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


def scrap_tripadvisor(url: str):
    url = urljoin(BASE_URL, url)

    # 1. Fetching data from TripAdvisor
    html = requests.get(url, headers=scraper_headers)
    hotels_soup = soup(html.content, features="html.parser")

    # 2. Extract data from HTML soup
    for hotel in hotels_soup.findAll('div', {'class': 'listItem'}):
        hotel_title = hotel.find('a', 'property_title prominent')
        hotel_link = urljoin(BASE_URL, hotel_title['href'])
        hotel_name = hotel_title.string.lstrip()
        reviews_num = hotel.find('a', 'review_count').string

        # 3. Data storage
        insert_hotel(hotel_name, reviews_num, hotel_link)


# # loop through test and generate reviews pagination links
# for k, v in hotel_reviews.items():
#     hotel_link = v[0]
#     hotel_reviews_count = v[1]
#     hotel_reviews_count = hotel_reviews_count.split(' ')[0]
#     hotel_reviews_count = int(hotel_reviews_count.replace(',',''))
#     reviews_pages = []
#     reviews_total_pages = hotel_reviews_count//5
#     i = 0
#     while i < reviews_total_pages:
#         i += 5
#         reviews_pages.append(i)
#     tmp_hotel_link = hotel_link.split('Reviews')
#     for i in reviews_pages:
#         review_page_link = tmp_hotel_link[0] + 'Reviews-or' + str(i) + tmp_hotel_link[1] + '#REVIEWS'
#         review_html = requests.get(review_page_link, headers=scraper_headers)
#         sleep(5)
#         hotel_reviews_soup = soup(review_html.content, features="html.parser")
#         for review in hotel_reviews_soup.findAll('div', {'class': '_2wrUUKlw _3hFEdNs8'}):
#             review_title = review.find('a', 'ocfR3SKN').string
#             review = review.find('q').string
#             review_date = review.find('span', '_34Xs-BQm').text[14:]

scrap_tripadvisor('/Hotels-g294206-Kenya-Hotels.html')