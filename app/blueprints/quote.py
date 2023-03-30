from . import quote_blueprint

@quote_blueprint.route('/api/quote')
def get_quote():
    # implement getting quote data
    return 'Getting quote data...'
