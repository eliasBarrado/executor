import krakenex
import configparser
import time
import logConf

logger = logConf.getLogger(__name__)

config = configparser.ConfigParser()

config.read('api.config')

#k = krakenex.api.API(config['kraken']['key'], config['kraken']['secret'])
k = krakenex.api.API(config['claudia']['key'], config['claudia']['secret'])


def market_order_sell(volume, pair, leverage = 'none'):
	order = k.query_private('AddOrder', {'pair': pair , 'type': 'sell' , 'ordertype' : 'market', 'volume': str(volume) , 'starttm' : '0', 'leverage': str(leverage)}) 
	logger.info(order)
	return order

def market_order_buy(volume , pair, leverage = 'none'):
	order =  k.query_private('AddOrder', {'pair': pair , 'type': 'buy' , 'ordertype' : 'market', 'volume': str(volume) , 'starttm' : '0' , 'leverage': str(leverage)})
	logger.info(order)
	return order

def limit_order_sell(volume, price, pair, leverage = 'none'):
	order = k.query_private('AddOrder', {'pair': pair , 'type': 'sell' , 'ordertype' : 'limit', 'price': str(price) , 'volume': str(volume) , 'starttm' : '0' , 'leverage': str(leverage)})
	logger.info(order)
	return order

def limit_order_buy(volume, price, pair, leverage = 'none'):
    order = k.query_private('AddOrder', {'pair': pair , 'type': 'buy' , 'ordertype' : 'limit', 'price': str(price) , 'volume': str(volume) , 'starttm' : '0' , 'leverage': str(leverage)})
    logger.info(order)
    return order

def get_leverage_profits():
	info = k.query_private('OpenPositions', {'docalcs': True})
	profit = 0
	for order in info['result']:
		localProfit = info['result'][order]['net']
		profit = profit + float(localProfit)
	print(profit)
	return profit

def get_balance():
	balance = k.query_private('Balance')
	logger.info(balance['result'])
	return balance

def get_open_orders():
	info = k.query_private('OpenOrders')
	if(info['error'] != []):
		logger.error(info['error'])
	else:
		logger.info(info['result'])

def get_price(pair):
	c = get_ticker_info(pair)
	if(c['error'] != []):
		logger.error(c['error'])
		c = get_ticker_info(pair)
	c = float(c['result'][pair]['c'][0])
	logger.info('{}: {}'.format(pair,c))
	return c

def print_open_positions():
	info = k.query_private('OpenPositions', {'docalcs': True})['result']
	for order in info:
		a = info[order]
		print('{0} {1:.5s} {2:.5s}'.format(a['pair'], a['cost'], a['net']))
	
def get_ticker_info(pair):
	try:
		info = k.query_public('Ticker', {'pair': pair})
	except BaseException as error:
		logger.error(error)
		time.sleep(2)
		info = get_ticker_info(pair)
	
	return info

def get_OHLC_info(pair, interval=1440):
	info = k.query_public('OHLC', {'pair': pair, 'interval': interval, 'since': '1413699200'})
	
	if( info['error'] != []):
		return info['error']

	return info['result'][pair]

def get_server_time():
	info = k.query_public('Time')
	info = info['result']['unixtime']
	print(info)
	return info



