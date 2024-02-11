# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def display():
    hotel = [{'hotel_name': "hotel name", 'hotel_description':"wonderful!", 'rating_value': 5, 'hotel_image':"https://media-cdn.tripadvisor.com/media/photo-s/1c/02/78/ba/romance-istanbul-hotel.jpg",'price_range': '$', 'review_count': 2024,'hotel_url': "https://www.tripadvisor.com/Hotel_Review-g293974-d8364987-Reviews-Romance_Istanbul_Hotel-Istanbul.html"}]
    #example data

    for x in range(len(hotel)):
        hotelName = hotel[x]['hotel_name']
        hotelDescription = hotel[x]['hotel_description']
        hotelImage = hotel[x]['hotel_image']
        priceRange = hotel[x]['price_range']
        ratingValue = hotel[x]['rating_value']
        reviewCount = hotel[x]['review_count']
        hotelUrl = hotel[x]['hotel_url']
        #reason = decoder_results
        

        with st.container(border=True):
            col1, col2 = st.columns([0.6,0.4])
            with col1:
                st.markdown(hotelName)
                st.markdown("**Price:** {} |  **Rating:** {}:star: | {:,} reviews".format(priceRange, ratingValue, reviewCount))
                st.markdown(hotelDescription)
                #st.markdown("Why we chose this for you: " + reason)
                st.page_link(hotelUrl, label = "***Interested?***")
            with col2:
                st.image(hotelImage)

def run():
    st.set_page_config(
        page_title="Hotels",
    )

    with st.container(border=True):
      st.markdown('<h1 style="text-align: center; color: #89CFF0; font-family: sans-serif;">Paris Hotel Finder</h1>', unsafe_allow_html=True)

    data = st.text_input('Find a hotel that fits:',placeholder='Search...')

    #results = import from other file
    results = {1,2,3}

    if results == {}:
        st.error("Hmm.. no results found. Search again?")
    else:
        display()


if __name__ == "__main__":
    run()