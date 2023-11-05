# Currency converter API
Lightweight API for converting currencies.

Live API Link: <a href='https://ayoolaa.pythonanywhere.com' target='_blank' rel='noreferrer noopener'>Currency converter</a>

### Table of Contents
- [Supported Currencies](#supported-currencies)
- [How to use](#how-to-use)
- [Sample Response](#sample-response)

### Supported Currencies
- Nigerian Naira (NGN)
- United States Dollar (USD)


### How to use
#### GET Currency rate
``https://ayoolaa.pythonanywhere.com/?amount=50&inputCurrency=USD&outputCurrency=NGN``

<table>
<thead>
    <tr>
        <td>PARAMS</td>
        <td>DESCRIPTION</td>
    </tr>
</thead>
<tbody>
    <tr>
        <td>amount</td>
        <td>Amount you will like to convert</td> 
    </tr>
    <tr>
        <td>inputCurrency</td>
        <td>Currency that you are converting from</td> 
    </tr>
    <tr>
        <td>outputCurrency</td>
        <td>Currency that you are converting to</td> 
    </tr>
</tbody>
</table>

### Sample Response
```json
{
  "base_currency": "USD",
  "base_currency_name": "United States Dollar",
  "input_amount": 50.0,
  "rate": 760.3872,
  "result_currency": "NGN",
  "result_currency_name": "Nigerian Naira",
  "value": 38019.36
}
```
