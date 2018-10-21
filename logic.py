import private
import time
import logConf

logger = logConf.getLogger(__name__)

def round_price(price, pair, modifier):

	if(pair != 'USD-USDT'):
		return round(price*modifier,2)

	else:
		return round(price*modifier,4)


def trailing_stop(volume, trailing, order, pair, leverage = 'none'):

	"""
	Trailing stop 

	Keywords arguments:

	volume   -- 
	trailing -- the absolute trailing to be set
	order    -- buy or sell order
	pair     -- 
	leverage --

	"""
	
	logger.info("Volume = {}, Trailing = {}, Order = {}, Pair = {}, Leverage = {}".format(volume, trailing, order, pair, leverage))

	extremePrice = private.get_price(pair)
	logger.info(("Initial price is {}".format(extremePrice)))

	while(True):
		time.sleep(5)
		price = private.get_price(pair)
		logger.info("Price = {}  ExtremePrice = {}".format(price, extremePrice))

		if(order == 'buy'):
			if(price < extremePrice):
				extremePrice = price
				logger.info("ExtremePrice set to {}".format(extremePrice))

			if(price > extremePrice + trailing):
				logger.info("Trailing exceded. Putting buying order...")
				info = private.limit_order_buy(volume, round_price(price, pair, 1.002), pair, leverage)
				return info

		if(order == 'sell'):
			if(price > extremePrice ):
				extremePrice = price
				logger.info("ExtremePrice set to {}".format(extremePrice))

			if(price < extremePrice - trailing):
				logger.info("Trailing exceded. Putting selling order...")
				info = private.limit_order_sell(volume, round_price(price, pair, 0.998), pair, leverage)
				return info





while True:
	price = private.get_price('XETHZUSD')
	if(price > 205):
		trailing_stop(1, 0.75, 'sell','XETHZUSD',5)
	time.sleep(5)



