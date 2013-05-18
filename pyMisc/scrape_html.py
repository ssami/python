import requests, re

#### Learning how to do regexes in Python


def findAllLinks( url ) :
  """Finding all the links in a document"""
  r = requests.get(url);
  p = re.compile('<a.*?>.*?</a>')
  match = p.findall(r.content)
  links = []
  for i in match:
    links.append(i)

  return links


## Need to remove script-related stuff too
def cleanHtml( text ):
    pattBreaks = re.compile('<\/?br>', re.I|re.M|re.S)
    text = pattBreaks.sub('\n', text)
    pattBreaks = re.compile('<\/?p>', re.I|re.M|re.S)
    text = pattBreaks.sub('\n', text)
    f1 = open('debug1.txt', 'w')
    f1.write(text)
    pattBreaks = re.compile('\.|\?|\!\"', re.I|re.M|re.S)
    text = pattBreaks.sub('\n', text)
    f2 = open('debug2.txt', 'w')
    f2.write(text)
    pattTags = re.compile('<.*?>', re.I|re.M|re.S)
    text = pattTags.sub('', text)
    f3 = open('debug3.txt', 'w')
    pattTags = re.compile('<script.*?>.*<\/script>', re.I|re.M|re.S)
    text = pattTags.sub('', text)
    f3.write(text)   
    return text.split('\n')


#links = findAllLinks("http://www.chris-granger.com/resume/")
#for i in links:
#    print "This url is: ", i


origText = requests.get('http://docs.python.org/2/library/re.html').content
cleanText = cleanHtml(origText)
#print cleanText
