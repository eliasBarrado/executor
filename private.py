import krakenex
k = krakenex.api.API('','')

pairs = {
	'XBT-ETC': 'XETCXXBT',
	'XBT-EUR': 'XXBTZEUR',
	'XBT-USD': 'XXBTZUSD',
	'XBT-LTC': 'XLTCXXBT'
}

PAIR = pairs['XBT-USD']

def market_order_sell(volume , leverage = 'none'):
	order = k.query_private('AddOrder', {'pair': PAIR , 'type': 'sell' , 'ordertype' : 'market', 'volume': str(volume) , 'starttm' : '0', 'leverage': str(leverage)}) 
	print(order)
	return order
def market_order_buy(volume , leverage = 'none'):
	order =  k.query_private('AddOrder', {'pair': PAIR , 'type': 'buy' , 'ordertype' : 'market', 'volume': str(volume) , 'starttm' : '0' , 'leverage': str(leverage)})
	print(order)
	return 
def limit_order_sell(volume, price, leverage = 'none'):
	order = k.query_private('AddOrder', {'pair': PAIR , 'type': 'sell' , 'ordertype' : 'limit', 'price': str(price) , 'volume': str(volume) , 'starttm' : '0' , 'leverage': str(leverage)})
	print(order)
	return order
def limit_order_buy(volume, price, leverage = 'none'):
    order = k.query_private('AddOrder', {'pair': PAIR , 'type': 'buy' , 'ordertype' : 'limit', 'price': str(price) , 'volume': str(volume) , 'starttm' : '0' , 'leverage': str(leverage)})
    print(order)
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
	print(balance['result'])
	return balance
def get_open_orders():
	info = k.query_private('OpenOrders')
	if(info['error'] != []):
		print(info['error'])
	else:
		print(info['result'])
def get_price():
	c = k.query_public('Ticker', {'pair': PAIR})
	c = float(c["result"][PAIR]['c'][0])
	print(c)
	return c
def print_open_positions():
	info = k.query_private('OpenPositions', {'docalcs': True})['result']
	for order in info:
		a = info[order]
		print('{0} {1:.5s} {2:.5s}'.format(a['pair'], a['cost'], a['net']))
	

