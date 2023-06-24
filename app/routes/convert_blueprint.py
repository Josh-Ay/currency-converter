from flask import Blueprint, jsonify, request
from app.tool import ConvertTool
from app.tool import SUPPORTED_CURRENCIES

convert_blueprint = Blueprint('convert_blueprint', __name__, static_folder='', template_folder='')


@convert_blueprint.get('/')
def convert_currency():
    # getting the required query parameters: 'amount', 'inputCurrency', 'outputCurrency'
    amount, input_currency, output_currency = request.args.get('amount'), request.args.get(
        'inputCurrency'), request.args.get('outputCurrency')

    # checking if any query param was left out
    if any(param is None for param in [amount, input_currency, output_currency]):
        return jsonify(
            "'amount', 'inputCurrency', 'outputCurrency' query parameters are required"), 400

    list_of_currencies = list(SUPPORTED_CURRENCIES.keys())
    list_of_currencies_as_str = ', '.join(list_of_currencies)

    if input_currency not in list_of_currencies or output_currency not in list_of_currencies:
        return jsonify(f'Unsupported currency passed. Only {list_of_currencies_as_str} are supported'), 400

    try:
        amount_as_float = float(amount)
    except ValueError:
        return jsonify('Amount must be a valid number.'), 400

    if amount_as_float < 0:
        return jsonify('Amount must be greater than 0.'), 400

    if input_currency == output_currency:
        return jsonify({
            "input_amount": amount_as_float,
            "value": amount_as_float,
            "rate": 1,
            "base_currency": input_currency,
            "base_currency_name": SUPPORTED_CURRENCIES[f'{input_currency}'],
            "result_currency": output_currency,
            "result_currency_name": SUPPORTED_CURRENCIES[f'{output_currency}'],
        }), 200

    tool = ConvertTool(amount_as_float, input_currency, output_currency)

    # getting the results
    result = tool.get_results_from_web()

    if 'error' in result:
        return jsonify(result['error']), result['code']

    return jsonify(result), 200
