import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as soup
from time import sleep

# from database import insert_hotel
from sent_classifier.database.database import insert_hotel, get_hotels, insert_review

# configurations
BASE_URL = 'https://www.tripadvisor.com'

scraper_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


def scrap_hotels(url: str):
    """
    Function scraping hotels names, reviews and links from Trip Advisor
    :param url:
    """
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


# loop through test and generate reviews pagination links
def scrap_reviews():
    """
    Function to fetch each hotel and scrap its reviews
    """
    # 1. Fetch data from the database
    hotels = get_hotels()
    for hotel in hotels:
        hotel_link = hotel[3]

        # 2. Extract the reviews count
        hotel_reviews_count = hotel[2]
        hotel_reviews_count = hotel_reviews_count.split(' ')[0]
        hotel_reviews_count = int(hotel_reviews_count.replace(',',''))

        # 3. Generate reviews pages list
        reviews_pages = []
        reviews_total_pages = hotel_reviews_count//5
        n = 0
        i = 1
        while i < reviews_total_pages + 1:
            n += 5
            reviews_pages.append(n)
            i += 1

        # 4. Extract part one of review url
        tmp_hotel_link = hotel_link.split('Reviews')

        # 5. loop through the review pages
        for i in reviews_pages:
            print("Pagination number: ",i)
            review_page_link = tmp_hotel_link[0] + 'Reviews-or' + str(i) + tmp_hotel_link[1] + '#REVIEWS'
            sleep(5)
            review_html = requests.get(review_page_link, headers=scraper_headers)
            hotel_reviews_soup = soup(review_html.content, features="html.parser")

            # 6. Loop through reviews in a single review page
            for review in hotel_reviews_soup.findAll('div', {'class': '_2wrUUKlw _3hFEdNs8'}):
                review_title = review.find('a', 'ocfR3SKN').string
                review_date = review.find('span', '_34Xs-BQm').text[14:]
                review = review.find('q').string
                print(review_title, hotel[1], review_date, review)

                # 7. Insert review details to the DB
                insert_review(review_title, hotel[1], review, review_date)


# scrap_tripadvisor('/Hotels-g294206-Kenya-Hotels.html')
scrap_reviews()
