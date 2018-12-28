from flask import Flask
import datastore

app = Flask(__name__)


@app.route('/_ah/start')
def start():
	"""Initializes app"""
	print('Call to /_ah/start')
	while(True):
		strategies = datastore.getOpenStrategies()
		for st in strategies:
			st.checkAndExecute()
		time.sleep(10)

    
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
