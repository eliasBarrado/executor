class Ticker:
	def __init__(self, tickerEntity):
		self.a = tickerEntity['a']  # ask array(<price>, <whole lot volume>, <lot volume>) 
		self.b = tickerEntity['b']  # bid array(<price>, <whole lot volume>, <lot volume>)
		self.c = tickerEntity['c']  # last trade closed array(<price>, <lot volume>)
		self.h = tickerEntity['h']  # high array(<today>, <last 24 hours>)
		self.l = tickerEntity['l']  # low array(<today>, <last 24 hours>)
		self.o = tickerEntity['o']  # today's opening price
		self.p = tickerEntity['p']  # volume weighted average price array(<today>, <last 24 hours>)
		self.t = tickerEntity['t']  # number of trades array(<today>, <last 24 hours>)
		self.v = tickerEntity['v']  # volume array(<today>, <last 24 hours>)

	def getPrice(self):
		return float(self.c[0])