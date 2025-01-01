import re   ### for regex expressions
from nltk.corpus import stopwords ### NLTK for NLP taskss 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def prepreoccessing(text):
  text=text.lower()
  text=re.sub('[^a-zA-Z]',' ',text )
  text=word_tokenize(text)
  stop_word=set(stopwords.words('english'))
  filter=[i for i in text if i not in stop_word]
  steem=PorterStemmer()
  stemmed_tokens=[steem.stem(i) for i in filter]
  stemmed_tokens=' '.join(stemmed_tokens)
  return stemmed_tokens
