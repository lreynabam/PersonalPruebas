from flask import Flask, request, jsonify
from primerosCienNumeros import PrimerosCienNumeros

app = Flask(__name__)
number_set = PrimerosCienNumeros()

@app.route('/extract', methods=['POST'])
def extract_number():
    data = request.json
    number = data.get('number')
       
    if not isinstance(number, int) or not (1 <= number <= 100):
        return jsonify({'error': 'El numero debe ser un entero entre 1 y 100.'}), 400

    try:
        number_set.extract(number)
        return jsonify({'message': f'Numero {number} extraido con exito.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/calculate', methods=['GET'])
def calculate_extract():
    try:
        extract_number = number_set.calculate_extract_number()
        return jsonify({'el numero extraido es: ': extract_number})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
