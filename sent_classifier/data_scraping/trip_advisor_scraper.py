from time import sleep

import requests
from requests.adapters import HTTPAdapter
from urllib.parse import urljoin
from urllib3 import Retry
from bs4 import BeautifulSoup as soup

from sent_classifier.database.database import insert_hotel, get_hotels, insert_review, update_hotel_status

# configurations
BASE_URL = 'https://www.tripadvisor.com'

scraper_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


def scrap_hotels(url):
    """
    Function scraping hotels names, reviews and links from Trip Advisor
    :param url: url for a hotel
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


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    """
    Function to configure the session and retries of HTTP requests
    """
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def fetch_html_soup(url):
    """
    Fetch the HTML soup for a single hotel reviews page
    :param url: URL containing hotel reviews
    :return hotel_reviews_soup:
    """
    req = requests_retry_session()
    review_html = req.get(url, headers=scraper_headers)
    sleep(5)
    hotel_reviews_soup = soup(review_html.content, features="html.parser")
    return hotel_reviews_soup


def gen_review_pages(total_hotel_reviews):
    """
    Generate the pagination numbers list for reviews
    :param total_hotel_reviews: total number of reviews for a hotel
    :return reviews_pages: list of url pages for a hotel reviews
    """
    reviews_pages = []
    reviews_total_pages = total_hotel_reviews // 5
    n = 0
    i = 1
    while i < reviews_total_pages + 1:
        n += 5
        reviews_pages.append(n)
        i += 1
    return reviews_pages


def extract_reviews_count(count):
    """
    Extract the number of reviews from raw data
    :param count: total number of reviews in mixed format
    :return hotel_reviews_count: the total number reviews count
    """
    hotel_reviews_count = count.split(' ')[0]
    hotel_reviews_count = int(hotel_reviews_count.replace(',', ''))
    return hotel_reviews_count


def scrap_reviews():
    """
    Function to fetch each hotel and scrap its reviews
    """
    # 1. Fetch data from the database
    hotels = get_hotels()
    print("Hotels from DB:", hotels)
    for hotel in hotels:
        print("Hotel name:", hotel[1])
        hotel_link = hotel[3]

        # 2. Extract the reviews count
        hotel_reviews_count = hotel[2]
        hotel_reviews_count = extract_reviews_count(hotel_reviews_count)

        # 3. Generate reviews pages list
        reviews_pages = gen_review_pages(hotel_reviews_count)

        # 4. Extract part one of review url
        tmp_hotel_link = hotel_link.split('Reviews')

        # 5. loop through the review pages
        for i in reviews_pages:
            print("Pagination number: ", i)
            review_page_link = tmp_hotel_link[0] + 'Reviews-or' + str(i) + tmp_hotel_link[1] + '#REVIEWS'
            hotel_reviews_soup = fetch_html_soup(review_page_link)

            # 6. Loop through reviews in a single review page
            if hotel_reviews_soup:
                for review in hotel_reviews_soup.findAll('div', {'class': '_2wrUUKlw _3hFEdNs8'}):
                    review_title = review.find('a', 'ocfR3SKN').string
                    raw_review_date = review.find('span', '_34Xs-BQm')
                    if raw_review_date is not None:
                        review_date = raw_review_date.text[14:]
                    else:
                        review_date = 'Not available'
                    review = review.find('q').string
                    print(review_title, hotel[1], review_date, review)

                    # 7. Insert review details to the DB
                    insert_review(review_title, hotel[1], review, review_date)

        # 8. update hotel scrapped status to true
        update_hotel_status(hotel[0], 'yes')


# scrap_tripadvisor('/Hotels-g294206-Kenya-Hotels.html')
scrap_reviews()
