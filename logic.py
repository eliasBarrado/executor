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


def start_trailing(start_price, volume, trailing, order, pair, leverage = 'none'):

	logger.info("StartPrice = {}, Volume = {}, Trailing = {}, Order = {}, Pair = {}, Leverage = {}".format(start_price, volume, trailing, order, pair, leverage))

	while True:

		price = private.get_price(pair)
		
		if(order == 'buy'):
			if(price < start_price):
				return trailing_stop(volume, trailing, order, pair, leverage)

		if(order == 'sell'):
			if(price > start_price):
				return trailing_stop(volume, trailing, order, pair, leverage)

		time.sleep(5)



