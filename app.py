from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OFF_BASE = 'https://world.openfoodfacts.net'
# fetch products by name
OFF_API_PRODUCT = OFF_BASE + '/cgi/search.pl?search_terms={name}&search_simple=1&action=process&json=1'
# or try
OFF_API_PRODUCT_2 = OFF_BASE + '/cgi/search.pl'
# fetch product by barcode:
OFF_API_BARCODE = OFF_BASE + '/api/v2/product/{barcode}'


@app.route('/home')
def home():
    return "Welcome!"

@app.route('/api/search')
def search_products():
    query = request.args.get('q', '')
    params = {
        'search_terms': query,
        'search_simple': 1,
        'action': 'process',
        'json': 1,
    }
    response = requests.get(OFF_API_PRODUCT, params=params)
    return jsonify(response.json())


@app.route('/api/barcode/<barcode>')
def get_product_by_barcode(barcode):
    response = requests.get(OFF_API_BARCODE.format(barcode))
    return jsonify(response.json())


# the if statement with __name == '__main__' means that this code block will only be executed if the script is run directly (not imported as a module in another script).
if __name__ == '__main__':
    app.run(debug=True)


# usar o codigo da API do professor como exemplo pra add produtos à base


# Open Food Facts API
# criar codigo para consulta de dados na base de dados da API e outro pra Open Food Facts API.
# https://openfoodfacts.github.io/openfoodfacts-server/api/ - documentacao do OFF API




























# If you submit the product's nutritional values and category, you'll get the Nutri-Score.
# If you submit the product ingredients, you'll get the NOVA group (about food ultra-processing), additives, allergens, normalized ingredients, vegan, vegetarian…
# If you submit the product's category and labels, you'll get the Eco-Score (a rating of the product's environmental impact)




# Referências

# A API da Open Food Facts opera com base na Open Database License: https://opendatacommons.org/licenses/odbl/1-0/
# The individual contents of the database are available under the Database Contents License(https://opendatacommons.org/licenses/dbcl/1-0/).
# Product images are available under the Creative Commons Attribution ShareAlike license (https://creativecommons.org/licenses/by-sa/3.0/deed.en). They may contain graphical elements subject to copyright or other rights that may, in some cases, be reproduced (quotation rights or fair use).

