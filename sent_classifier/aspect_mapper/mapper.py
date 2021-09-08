hotel_aspects = {
    'value': ['value', 'price'],
    'location': ['location', 'place'],
    'room': ['room', 'size', 'bathroom'],
    'cleanlinesss': ['cleanliness', 'cleaning'],
    'sleep_quality': ['sleep', 'bed', 'bedroom'],
    'service': ['service', 'staff', 'waiter'],
    'facility': ['facility', 'wifi', 'pool', 'gym'],
    'food_quality': ['food', 'drink', 'dish', 'wine', 'salad']
}

# topic 1
topic_one = ['good', 'staff', 'rooms', 'stay', 'room', 'food', 'great', 'service', 'well', 'friendly', 'nairobi',
             'best', 'clean',
             'nice', 'breakfast', 'place', 'time', 'one', 'back', 'restaurant', 'helpful', 'comfortable', 'excellent',
             'pool',
             'stayed', 'business', 'location', 'also', 'amazing']

# topic 2
topic_two = ['good', 'great', 'staff', 'service', 'food', 'rooms', 'friendly',
             'restaurant', 'room', 'place', 'stay', 'nairobi', 'nice', 'would', 'well', 'really', 'breakfast', 'one',
             'airport',
             'clean', 'recommend', 'time', 'stayed', 'pool', 'also', 'bar', 'like', 'visit', 'excellent']

# topic 3
topic_three = ['staff', 'food', 'place', 'service', 'room', 'nice', 'great', 'good', 'stay', 'would', 'clean',
               'friendly', 'rooms',
               'nairobi', 'excellent', 'well', 'best', 'time', 'back', 'breakfast', 'airport', 'definitely',
               'experience',
               'comfortable,''one', 'us', 'really', 'visit', 'stayed']

# topic 4
topic_four = ['staff', 'good', 'rooms', 'room', 'excellent', 'great', 'friendly', 'food', 'stayed', 'well', 'nairobi',
              'stay', 'clean',
              'nice', 'time', 'service', 'one', 'place', 'night', 'breakfast', 'us', 'would', 'comfortable',
              'beautiful', 'airport',
              'pool', 'back', 'lovely', 'also']

# topic 5
topic_five = ['staff', 'food', 'good', 'service', 'hotel', 'rooms', 'great', 'room', 'stay', 'friendly', 'place',
              'excellent', 'well',
              'clean', 'amazing', 'back', 'nice', 'restaurant', 'recommend', 'stayed', 'would', 'really', 'wonderful',
              'enjoyed',
              'nairobi', 'definitely', 'spacious', 'us', 'experience', 'time']

# topics_list = [topic_one, topic_two, topic_three, topic_four, topic_five]
topics_dict = {
    'topic_one': topic_one,
    'topic_two': topic_two,
    'topic_three': topic_three,
    'topic_four': topic_four,
    'topic_five': topic_five
}

aspect_score_dict = {}

for k, v in topics_dict.items():
    topic_aspect_score_list = []
    for i, j in hotel_aspects.items():
        aspect_score = 0
        for aspect in j:
            topic_score = 0
            aspect_list = []
            for l in v:
                if aspect == l:
                    aspect_list.append(l)
                    topic_score = len(aspect_list)
                    aspect_score += topic_score
        topic_aspect_score_list.append({i : aspect_score})
    aspect_score_dict[k] = topic_aspect_score_list

# print(aspect_score_dict)

for k,v in aspect_score_dict.items():
    print(v)
    new_dict = {}
    for i in v:
        new_dict.update(i)
    highest_aspect = max(new_dict, key=new_dict.get)
    print(highest_aspect)

