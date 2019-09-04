from flask import Flask
from flask import request
from flask import make_response

EVENT_API_FIELD_TYPE = "type"
EVENT_API_FIELD_TOKEN = "token"
EVENT_API_FIELD_CHALLENGE = "challenge"

EVENT_API_REQ_TYPE_URL_VERIFICATION = "url_verification"
EVENT_API_REQ_TYPE_EVENT = "event_callback"

AUTH_API_ARG_CODE = "code"
AUTH_API_ARG_STATE = "state"

app = Flask(__name__)

# создали ендпоинт
@app.route('/webhook')
def hello_slack():
    # получили данные из запроса
    request_json = request.get_json(silent=True, force=True)
    # тут ваш код возьмет запрос и вернет в ответ любой dict объект ответа, можно даже пустой
    # примерно так request_json -> response_body_json
    ...
    response_body = json.dumps(response_body_json)
    # упаковали все в корректный респонс
    response = make_response(response_body)
    response.headers['Content-Type'] = 'application/json'
    # и вернули
    return response

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
