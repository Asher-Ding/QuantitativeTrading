from . import sell_blueprint

@sell_blueprint.route('/api/sell')
def sell_stock():
    # Implement selling stock
    return 'Selling stock...'
