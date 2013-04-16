import web

urls = (
	'/', 'index', 
	'/second', 'hithere'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index : 
	def GET(self) : 
		greeting = ""
		return render.index(greeting = greeting)

class hithere : 
	def GET(self) : 
		sayhi = "We greet you a second time!" 
		return sayhi
	def POST(self): 
		data = web.data()
		print "Oh so here you submitted %r!" % data

if __name__ == "__main__" : 
	app.run()

