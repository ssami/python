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


def cleanHtml( text ):
    pattBreaks = re.compile('<\/?br>')
    pattBreaks.sub('\n', text)
    pattBreaks = re.compile('<\/?p>')
    pattBreaks.sub('\n', text)
    f1 = open('debug1.txt', 'w')
    f1.write(text)
    pattBreaks = re.compile('\.|\?|\!\"')
    pattBreaks.sub('\n', text)
    f2 = open('debug2.txt', 'w')
    f2.write(text)
    pattTags = re.compile('<.*?>')
    pattTags.sub('', text)
    f3 = open('debug3.txt', 'w')
    f3.write(text)
    
    return text.split('\n')


#links = findAllLinks("http://www.chris-granger.com/resume/")
#for i in links:
#    print "This url is: ", i


origText = requests.get('http://docs.python.org/2/library/re.html').content
cleanText = cleanHtml(origText)
