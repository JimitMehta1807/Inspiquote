from PIL import Image
import requests
import random
import urllib.request as url
from os import environ

UNSPLASH_ACCESS_KEY = environ["UNSPLASH_ACCESS_KEY"]

class GetImage:
    
    def get_unsplash_img(self,query_word = 'motivation'):
        """
        Gets images from Unsplash and downloads+resizes it.
        @param query_word - ranked word
        returns list of metrics
        """
        try:
            orientation = random.choice(['landscape','portrait'])
            if orientation == "landscape":
                response = requests.get('https://api.unsplash.com/photos/random',
                            headers={'Authorization':'Client-ID '+UNSPLASH_ACCESS_KEY},params={'query':query_word,'orientation':orientation})
                img_data = response.json()
                img_url = img_data['urls']['raw'] + "&fit=max&w=1200&h=675"
            else:
                response = requests.get('https://api.unsplash.com/photos/random',
                            headers={'Authorization':'Client-ID '+UNSPLASH_ACCESS_KEY},params={'query':query_word,'orientation':orientation})
                img_data = response.json()
                img_url = img_data['urls']['raw'] + "&fit=max&w=640&h=960"

            img_author = img_data['user']['name']
            img_twitter_username = img_data['user']['twitter_username']
            img_name = '/app/bg images/' + query_word+ '.jpg'
            url.urlretrieve(img_url,img_name)

            return [img_author,img_twitter_username,orientation]
        except:
            logger.error("Image fetching error")

#Change the img_name variable to the local path