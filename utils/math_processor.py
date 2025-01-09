import requests

def extract_math_from_image(image_path):
    # Replace 'your_app_id' and 'your_app_key' with MathPix credentials
    url = "https://api.mathpix.com/v3/text"
    headers = {
        "app_id": "your_app_id",
        "app_key": "your_app_key"
    }
    with open(image_path, 'rb') as image_file:
        response = requests.post(url, headers=headers, files={"file": image_file})
    return response.json()
