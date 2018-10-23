import private
import logging
import logConf
import time

logger = logConf.getLogger(__name__)


#private.get_price('XXBTZUSD')
#private.limit_order_buy(0.1, 9190, 2)
#private.limit_order_buy(5, 0.02161)
#private.limit_order_sell(0.1, 8359.5, 2)
#private.get_leverage_profits()
#private.print_open_positions()
#private.get_balance()

def max_price():
	max_price = private.get_price('XXBTZUSD')
	while True:
		price = private.get_price('XXBTZUSD')
		if(price > max_price):
			max_price = price
			
		print('price = {} max_price = {}'.format(price,max_price))
		time.sleep(1)	


max_price()

