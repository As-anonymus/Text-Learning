
# Download nltk
# import nltk
# nltk.download()


from nltk.corpus import stopwords
sw = stopwords.words("english")

sw[0]
sw[10]

# Count how many stop words
len(sw)



from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")
stemmer.stem("responsivity")
stemmer.stem("unresponsive")









