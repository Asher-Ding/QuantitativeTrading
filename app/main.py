from price_watcher import PriceWatcher

price_watcher = PriceWatcher()
while True:
    price_watcher.watch_price('BTC-USD')
    price_watcher.watch_price('ETH-USD')
    