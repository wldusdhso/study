from ccfs import ccfs
from cgi import parse_qs

def application(environ, start_response):
	try: request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except valueError: request_body_size = 0
    
	request_body = environ['wsgi.input'].read(request_body_size)
	d = parse_qs(request_body)
    
	sentence = d.get('sentence'.encode(), [''])[0]
	character = d.get('character'.encode(), [''])[0]

	status = '200 OK'
	response_body = ccfs.Ccfs(sentence, character).getJson()

	response_headers = [
		('Content-Type', 'application/json'),
		('Content-Length', str(len(response_body)))
	]

	start_response(status, response_headers)
	return [response_body.encode()]
