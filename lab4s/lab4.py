from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_modified_response():
    # Вызываем REST API и получаем ответ
    response = requests.get('http://www.mocky.io/v2/5c7db5e13100005a00375fda')
    
    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()
        
        # Заменяем пробелы на нижнее подчёркивание в поле 'result'
        modified_result = data['result'].replace(' ', '_')
        
        # Формируем измененный ответ
        modified_response = {'result': modified_result}
        
        # Возвращаем измененный ответ в формате JSON
        return jsonify(modified_response)
    
    # Если запрос не был успешным, возвращаем ошибку
    return jsonify({'error': 'Failed to retrieve data'})

if __name__ == '__main__':
    app.run()
