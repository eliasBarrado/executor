import time
import logging

class Order:
	
	def __init__(self, pair, tipe, ordertype, price, volume, leverage='none'):
		self.pair      = pair
		self.type      = tipe
		self.ordertype = ordertype
		self.price     = price
		self.volume    = volume
		self.leverage  = leverage

	def pushOrder(self, k):
		orderDict = self.constructOrderDict()

		try:
			info = k.query_private('AddOrder', orderDict)

		except Exception as error:
			logging.error(error)
			time.sleep(1)
			info = self.pushOrder(self, k)

		return info

	def constructOrderDict(self):
		orderDict = {}
		orderDict['pair']      = self.pair
		orderDict['type']      = self.type
		orderDict['ordertype'] = self.ordertype
		orderDict['price']     = self.price
		orderDict['volume']    = self.volume
		orderDict['leverage']  = self.leverage

		return orderDict



	