from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.get('/<operation>')
def calculate(operation):
    """ Takes two numbers and performs given operation and returns
    the result as the body """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    if operation == 'add':
        return f'<body>{add(a, b)}</body>'
    elif operation == 'sub':
        return f'<body>{sub(a, b)}</body>'
    elif operation == 'mult':
        return f'<body>{mult(a, b)}</body>'
    else:
        return f'<body>{div(a, b)}</body>'


