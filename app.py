from flask import Flask, request, render_template_string
from math_utils import add, subtract

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; }
        input, select, button { padding: 10px; margin: 5px; }
        .result { font-size: 20px; color: green; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="get">
        <input type="number" name="a" placeholder="Enter first number" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
        </select>
        <input type="number" name="b" placeholder="Enter second number" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <div class="result">
            Result: {{ result }}
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def calculator():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    operation = request.args.get("operation")
    result = None

    if a is not None and b is not None and operation:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
