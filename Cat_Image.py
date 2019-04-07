import io, urllib.request, json, requests

def returnImage():
    with urllib.request.urlopen("https://api.thecatapi.com/v1/images/search") as randomURL:
        image = json.loads(randomURL.read().decode())[0]["url"]
        imageFile = io.BytesIO(requests.get(image).content)
    return imageFile