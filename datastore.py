from google.cloud import datastore
import configparser
from model import Ticker
from model import Strategie

config = configparser.ConfigParser()
config.read('config.txt')

client = datastore.Client(project=config['project']['id'])

def getLastTicker():
	key          = client.key('Ticker', 'last')
	tickerEntity = client.get(key)
	ticker       = Ticker.Ticker(tickerEntity)
	return ticker

def getOpenStrategies():
	"""Returns an array of open Strategie Objects"""
	query = client.query(kind='Strategie')
	query.add_filter('status', '=', 'open')

	strategies = []

	for entity in list(query.fetch()):
		strategies.append(Strategie.Strategie(entity))

	return strategies

