from . import buy_blueprint

@buy_blueprint.route('/api/buy')
def buy_stock():
    # implement buying stock
    return 'Buying stock...'
