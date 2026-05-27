# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():

#     if request.method == "GET":
#         return "Server Running"

#     data = request.get_json()

#     # print(data)   # VERY IMPORTANT FOR DEBUGGING

#     unit_currency = data['queryResult']['parameters']['unit-currency'][0]

#     source_currency = unit_currency['currency']
#     amount = unit_currency['amount']

#     target_currency = data['queryResult']['parameters']['currency-name']

#     print("Source Currency:", source_currency)
#     print("Amount:", amount)
#     print("Target Currency:", target_currency)

#     return "Hello"


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        return "Server Running"

    data = request.get_json()

    unit_currency = data['queryResult']['parameters']['unit-currency'][0]

    source_currency = unit_currency['currency']
    amount = unit_currency['amount']

    target_currency = data['queryResult']['parameters']['currency-name'][0]

    print("Source Currency:", source_currency)
    print("Amount:", amount)
    print("Target Currency:", target_currency)

    # Frankfurter API URL
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={source_currency}&to={target_currency}"

    response = requests.get(url)
    result = response.json()

    converted_amount = result['rates'][target_currency]

    print("Converted Amount:", converted_amount)

    # Dialogflow response
    return jsonify({
        "fulfillmentText":
        f"{amount} {source_currency} is equal to {converted_amount} {target_currency}"
    })


if __name__ == "__main__":
    app.run(debug=True)