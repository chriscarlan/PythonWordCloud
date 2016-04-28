# PythonWordCloud
#An easy to use python word cloud with any txt file
#pip install image
#pip install pillow
#pip install word cloud

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.show()
