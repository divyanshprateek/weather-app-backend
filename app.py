from flask import Flask, request, jsonify, Blueprint
from concurrent.futures import ThreadPoolExecutor
from weather_app.models import ZipCodeModel, WeatherResponseModel
from weather_app.controller import  WeatherController
from flask_pydantic import validate
from flask_cors import CORS, cross_origin

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=20)
cors = CORS(app)
host = ['http://localhost:3000']
@app.route("/api/v1/health")
def health():
    return jsonify({ 'success': True, 'message': 'Health check complete'})

@app.before_request 
def before_request(): 
    headers = { 'Access-Control-Allow-Origin': host, 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' } 
    if request.method == 'OPTIONS' or request.method == 'options': 
        return jsonify(headers), 200

@app.route("/api/v1/fetch_weather_data", methods=["POST", "OPTIONS"])
@validate(body=ZipCodeModel)
@cross_origin()
def get_zip_codes(body: ZipCodeModel):
    weather_controller = WeatherController(body.zip_codes)
    data = weather_controller.get_weather_response()
    resp = WeatherResponseModel(payload=data)

    return resp.create_response()

if __name__ == '__main__':
    app.run(debug=False, port=5000)