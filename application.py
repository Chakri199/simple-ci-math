import os
from flask import Flask, request, render_template
from math_utils import add, subtract

app = Flask(__name__)

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

    return render_template("index.html", result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
