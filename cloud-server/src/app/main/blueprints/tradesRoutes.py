from flask import Blueprint, request
from ..modules.Trades import Trades
from  ...types.orders import MarketOrder
from alpaca_trade_api.entity import Order

tradeRoutes = Blueprint('tradeRoutes',  __name__, url_prefix='/trade')



@tradeRoutes.route('/market-order-percentage', methods=['POST'])
def marketOrderPercentage():
    '''
    Executes a market order for a trade for a quantity based off a percentage of the portfolio.
    This is a post request that requires the following data:
        {
            symbol: "SPY",
            side: "BUY",
            qty: 0.2 #this value gets treated a a percentage
            price: 321.0 #this is used to calculatehow many shares we can buy
        }
    '''
    post = request.get_json()
    #first get the amount of equity in the portfolio
    equity = float(Trades.getAccount().equity)
    #create the market order
    order = MarketOrder(symbol=post['symbol'], side=post['side'], qty=int(equity * post['qty'] / post['price']))
    resp: Order = Trades.placeTrade(order)
    # we want to return the raw json of the Order object
    return resp._raw, 200


    



