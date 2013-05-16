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

#links = findAllLinks("http://www.chris-granger.com/resume/")
#for i in links:
#    print "This url is: ", i
