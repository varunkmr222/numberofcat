import base64
import requests
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

url="https://firebasestorage.googleapis.com/v0/b/catdetection-a523a.appspot.com/o/cat_04.jpg?alt=media&token=0352162c-a847-4a9f-80bc-0766a6bee73d"
fh=open("image_fetch1.jpg","wb")
fh.write(base64.b64decode(get_as_base64(url)))
fh.close
