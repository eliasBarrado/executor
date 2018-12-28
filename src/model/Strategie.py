import public
import datastore
from model import Order

import krakenex
import configparser

config = configparser.ConfigParser()
config.read('../config.txt')

k = krakenex.api.API(config['executor']['key'], config['executor']['secret'])

class Strategie:

	def __init__(self, strategieEntity):
		self.id      = strategieEntity.id
		self.status  = strategieEntity['status']
		self.trigger = strategieEntity['trigger']
		self.action  = strategieEntity['action']

	def checkTrigger(self):
		return eval(self.trigger)

	def executeAction(self):
		"""Executes action and changes status value in datastore"""
		entity = self.toEntity()
		entity['status'] = 'executed'
		datastore.client.put(entity)

		return eval(self.action)

	def checkAndExecute(self):
		if(self.checkTrigger()):
			return self.executeAction()


	def toEntity(self):
		key    = datastore.client.key('Strategie', self.id)
		entity = datastore.client.get(key)

		return entity



	
	
	





