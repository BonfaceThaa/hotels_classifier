import requests
from bs4 import BeautifulSoup as soup
from time import sleep

scraper_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# html = requests.get('https://www.tripadvisor.com/Hotels-g294206-Kenya-Hotels.html', headers=scraper_headers)
# hotels_soup = soup(html.content, features="html.parser")
#
# hotels = {}
#
# for hotel in hotels_soup.findAll('div', {'class': 'listItem'}):
#     hotel_title = hotel.find('a', 'property_title prominent')
#     hotel_link = 'https://www.tripadvisor.com' + hotel_title['href']
#     hotel_name = hotel_title.string.lstrip()
#     reviews_num = hotel.find('a', 'review_count').string
#     hotels[hotel_name] = [hotel_link, reviews_num]

# Test data
hotel_reviews = {'Golden Tulip Westlands Nairobi': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d9567504-Reviews-Golden_Tulip_Westlands_Nairobi-Nairobi.html',
    '465 reviews'], 'Palacina Residence & Suites': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d595117-Reviews-Palacina_Residence_Suites-Nairobi.html',
    '438 reviews'], 'Crowne Plaza Nairobi Airport': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d13991898-Reviews-Crowne_Plaza_Nairobi_Airport-Nairobi.html',
    '890 reviews'], 'Villa Rosa Kempinski Nairobi': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d4091780-Reviews-Villa_Rosa_Kempinski_Nairobi-Nairobi.html',
    '1,315 reviews'], 'Radisson Blu Hotel & Residence, Nairobi Arboretum': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d17756145-Reviews-Radisson_Blu_Hotel_Residence_Nairobi_Arboretum-Nairobi.html',
    '266 reviews'], 'ibis Styles Hotel Westlands Nairobi': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d12858053-Reviews-Ibis_Styles_Hotel_Westlands_Nairobi-Nairobi.html',
    '753 reviews'], 'Hemingways Nairobi': [
    'https://www.tripadvisor.com/Hotel_Review-g12559418-d3511538-Reviews-Hemingways_Nairobi-Karen_Nairobi.html',
    '967 reviews'], 'Four Points by Sheraton Nairobi Airport': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d13109932-Reviews-Four_Points_by_Sheraton_Nairobi_Airport-Nairobi.html',
    '458 reviews'], 'Sankara Nairobi, Autograph Collection by Marriott': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d1860203-Reviews-Sankara_Nairobi_Autograph_Collection_by_Marriott-Nairobi.html',
    '1,360 reviews'], 'Hilton Garden Inn Nairobi Airport': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d12817722-Reviews-Hilton_Garden_Inn_Nairobi_Airport-Nairobi.html',
    '387 reviews'], 'The Sands at Nomad': [
    'https://www.tripadvisor.com/Hotel_Review-g775870-d594546-Reviews-The_Sands_at_Nomad-Diani_Beach_Ukunda_Coast_Province.html',
    '641 reviews'], 'Ole Sereni': [
    'https://www.tripadvisor.com/Hotel_Review-g294207-d1586993-Reviews-Ole_Sereni-Nairobi.html', '1,830 reviews'],
                 'Fairview Hotel': [
                     'https://www.tripadvisor.com/Hotel_Review-g294207-d302822-Reviews-Fairview_Hotel-Nairobi.html',
                     '1,497 reviews'], 'Trademark Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d13996430-Reviews-Trademark_Hotel-Nairobi.html',
        '507 reviews'], 'The Majlis Resort': [
        'https://www.tripadvisor.com/Hotel_Review-g488098-d1587136-Reviews-The_Majlis_Resort-Manda_Island_Coast_Province.html',
        '349 reviews'], 'Nyali Sun Africa Beach Hotel & Spa': [
        'https://www.tripadvisor.com/Hotel_Review-g294210-d3376913-Reviews-Nyali_Sun_Africa_Beach_Hotel_Spa-Mombasa_Coast_Province.html',
        '279 reviews'], 'Acacia Premier Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g317064-d8470988-Reviews-Acacia_Premier_Hotel-Kisumu_Nyanza_Province.html',
        '366 reviews'], 'Sentrim Castle Royal Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294210-d657305-Reviews-Sentrim_Castle_Royal_Hotel-Mombasa_Coast_Province.html',
        '150 reviews'], 'Cysuites Apartment Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d19359720-Reviews-Cysuites_Apartment_Hotel-Nairobi.html',
        '32 reviews'], 'The Panari Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d621998-Reviews-The_Panari_Hotel-Nairobi.html',
        '452 reviews'], 'La Maison Royale Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d7149423-Reviews-La_Maison_Royale_Hotel-Nairobi.html',
        '510 reviews'], 'PrideInn Hotel Mombasa': [
        'https://www.tripadvisor.com/Hotel_Review-g294210-d3605026-Reviews-PrideInn_Hotel_Mombasa-Mombasa_Coast_Province.html',
        '885 reviews'], 'Tamarind Tree Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d12996078-Reviews-Tamarind_Tree_Hotel-Nairobi.html',
        '545 reviews'], 'The Zehneria Portico Nairobi': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d7104649-Reviews-The_Zehneria_Portico_Nairobi-Nairobi.html',
        '557 reviews'], 'Azure Airport Hotel & Convention Center': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d19914287-Reviews-Azure_Airport_Hotel_Convention_Center-Nairobi.html',
        '83 reviews'], 'Best Western Plus Meridian Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d640508-Reviews-Best_Western_Plus_Meridian_Hotel-Nairobi.html',
        '897 reviews'], 'The Boma Nairobi': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d3344579-Reviews-The_Boma_Nairobi-Nairobi.html',
        '975 reviews'], 'Nairobi Serena Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d302552-Reviews-Nairobi_Serena_Hotel-Nairobi.html',
        '1,051 reviews'], 'Blue Marlin Beach Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g775870-d4599705-Reviews-Blue_Marlin_Beach_Hotel-Diani_Beach_Ukunda_Coast_Province.html',
        '118 reviews'], 'Ngong Hills Hotel': [
        'https://www.tripadvisor.com/Hotel_Review-g294207-d8095384-Reviews-Ngong_Hills_Hotel-Nairobi.html',
        '56 reviews']}

# loop through test and generate reviews pagination links
for k, v in hotel_reviews.items():
    hotel_link = v[0]
    hotel_reviews_count = v[1]
    hotel_reviews_count = hotel_reviews_count.split(' ')[0]
    hotel_reviews_count = int(hotel_reviews_count.replace(',',''))
    reviews_pages = []
    reviews_total_pages = hotel_reviews_count//5
    i = 0
    while i < reviews_total_pages:
        i += 5
        reviews_pages.append(i)
    tmp_hotel_link = hotel_link.split('Reviews')
    for i in reviews_pages:
        review_page_link = tmp_hotel_link[0] + 'Reviews-or' + str(i) + tmp_hotel_link[1] + '#REVIEWS'
        review_html = requests.get(review_page_link, headers=scraper_headers)
        sleep(5)
        hotel_reviews_soup = soup(review_html.content, features="html.parser")
        for review in hotel_reviews_soup.findAll('div', {'class': '_2wrUUKlw _3hFEdNs8'}):
            review_title = review.find('a', 'ocfR3SKN').string
            review = review.find('q').string
            review_date = review.find('span', '_34Xs-BQm').text[14:]
