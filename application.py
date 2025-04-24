import os
import logging
from flask import Flask, request, render_template
from math_utils import add, subtract

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def calculator():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    operation = request.args.get("operation")
    result = None

    logger.info(f"Request received: a={a}, b={b}, operation={operation}")

    if a is not None and b is not None and operation:
        try:
            if operation == "add":
                result = add(a, b)
            elif operation == "subtract":
                result = subtract(a, b)
            else:
                logger.warning(f"Invalid operation: {operation}")
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            result = "Error occurred."

    return render_template("index.html", result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
