from PIL import Image

im = Image.open("static/welshcorgi.jpg")
im.thumbnail((800, 600))
im.save("static/welshcorgi.jpg")
