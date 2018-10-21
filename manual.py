import private
import logging
import logConf

logger = logConf.getLogger(__name__)

logger.info('A')


private.get_price('USDTZUSD')
#private.limit_order_buy(0.1, 9190, 2)
#private.limit_order_buy(5, 0.02161)
#private.limit_order_sell(0.1, 8359.5, 2)
#private.get_leverage_profits()
#private.print_open_positions()
#private.get_balance()


	