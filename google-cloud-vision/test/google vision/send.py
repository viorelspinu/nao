import base64
import requests
import json

URL = "https://vision.googleapis.com/v1/images:annotate?key=YOUR_TOKEN"

#image to base64, which is a long long text
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read())

#make api call
def image_request(image_path):
    data = {
            "requests":[
                        {
                        "image":{
                            "content":encode_image(image_path)
                                },
                        "features":[
                                    {
                                    "type":"LABEL_DETECTION", #other options: LABEL_DETECTION FACE_DETECTION LOGO_DETECTION CROP_HINTS WEB_DETECTION
                                    "maxResults": 10
                                    }
                                   ]
                        }
                    ]
}
    r = requests.post(URL, json = data)
    return r.text


#arg = path of image
def main(argv):
    api_answer = json.loads(image_request(argv[1]))
    try:
        rows = api_answer['responses'][0]['labelAnnotations']
    except:
        print(file_to_proccess)
        print(api_answer)
    data = []
    for item in rows:
        data.append([item['mid'], item['description'], item['score'], item['topicality']])

    # save somewhere the data list...

if __name__ == "__main__":
    main(sys.argv)