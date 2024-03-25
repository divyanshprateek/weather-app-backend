from pydantic import BaseModel
from typing import List, Optional, Dict
from flask import Flask, jsonify, make_response

class ZipCodeModel(BaseModel):
    zip_codes: List[str]


class WeatherResponseModel:

    def __init__(self, payload, status=200, success=True, headers=None) -> None:
        self.payload = payload
        self.status = status
        self.headers = headers or {}
        self.success = success
    
    def create_response(self):

        response_data = {
            'success': self.success,
            'data': self.payload
        }

        response = make_response(jsonify(response_data), self.status)
        for key, value in self.headers.items():
            response.headers[key] = value
        
        return response