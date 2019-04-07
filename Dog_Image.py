import io, urllib.request, json

def returnImage():
    with urllib.request.urlopen("https://dog.ceo/api/breeds/image/random") as randomURL:
        image = json.loads(randomURL.read().decode())["message"]
        with urllib.request.urlopen(image) as imageURL:
            imageFile = io.BytesIO(imageURL.read())
    return imageFile