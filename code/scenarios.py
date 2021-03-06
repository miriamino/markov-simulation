from random import random
from supermarket import Supermarket
from tiles import SupermarketMap
from utils.constances import MARKET, TILES

def go_to_next_minute(supermarket, adding_prob = 0):
  '''
  simulate next minute
  '''
  if random() < adding_prob:
    supermarket.add_new_customers()
  supermarket.remove_exitsting_customers()
  supermarket.print_customers()
  supermarket.next_minute()
  return supermarket

def simulate_normal_day(prob_of_new_customer = 0.6):
  '''
  simulate a normal day in the supermarket
  '''
  supermarket = Supermarket()

  # from 7 - 21 in minutes
  closing_time = (21 - 7) * 60

  while supermarket.minutes < closing_time:
    go_to_next_minute(supermarket, prob_of_new_customer)


def simulate_n_customers(n):
  '''
  Simulate n customers that start together in the store.
  No new customers are added over time.
  The simulation ends once all are checked out.
  '''
  supermarket = Supermarket()
  for _ in range(n):
    supermarket.add_new_customers()

  while len(supermarket.customers) > 0:
    go_to_next_minute(supermarket)

  # supermarket.save_dataframe()


def draw_simulate_n_customers(n):
  '''
  Simulate n customers that start together in the store.
  Draw their progression through the market.
  No new customers are added and the simulation stops once they all reached the checkout.
  '''
  market = SupermarketMap(MARKET, TILES)
  supermarket = Supermarket(market)
