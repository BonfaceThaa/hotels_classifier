# TEMPORAL SENTIMENT CLASSIFICATION OF ONLINE HOTEL REVIEWS IN KENYA
## Overview
Online reviews are increasingly becoming a reference for information for both potential customers
and travelers in Kenya and across the globe. This project aims to develop a temporal and aspect-based sentiment analysis
platform for hotel reviews using Latent Dirichlet Allocation (LDA), aspect mapping and Support
Vector Machines (SVM).

The repo is structured as follows:

```bash
.
├── data
│   ├── hotel_reviews.csv
│   └── kenya_hotels.csv
├── LICENSE.txt
├── notebooks
│   ├── hotel-reviews-topic-modeling-lda.ipynb
│   └── hotels-reviews-exploratory-data-analysis.ipynb
├── README.md
├── reports
│   ├── ldavis_prepared_26
│   └── ldavis_prepared_26.html
├── requirements.txt
├── sent_classifier
│   ├── aspect_mapper
│   │   ├── mapper.py
│   │   └── sentiment_api_updater.py
│   ├── database
│   │   ├── database.py
│   │   └── __init__.py
│   ├── data_scraping
│   │   └── trip_advisor_scraper.py
│   └── __init__.py
└── src
    └── models
```
