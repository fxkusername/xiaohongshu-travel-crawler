import requests
import json
from datetime import datetime

class XiaohongshuPublisher:
    def __init__(self, title, content, images, tags):
        self.title = title
        self.content = content
        self.images = images
        self.tags = tags
        self.publish_url = 'https://xiaohongshu.com/api/publish'

    def auto_fill_publish_page(self):
        # Prepare the data for the request
        payload = {
            'title': self.title,
            'content': self.content,
            'images': self.images,
            'tags': self.tags,
            'date_time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Make the API request to publish the content
        response = requests.post(self.publish_url, json=payload)

        if response.status_code == 200:
            print('Content published successfully!')
            return response.json()
        else:
            print('Failed to publish content:', response.status_code, response.text)
            return None

# Example usage:
# publisher = XiaohongshuPublisher(
#     title='My Travel Journey',
#     content='Exploring the beauty of the world!',
#     images=['image1.jpg', 'image2.jpg'],
#     tags=['travel', 'adventure']
# )
# publisher.auto_fill_publish_page()