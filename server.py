from flask import Flask
from flask import request
from dotenv import load_dotenv
import stripe
import os

# Load local .env file and assign key
load_dotenv()
stripe.api_key = os.environ.get("SK_TEST_KEY")

app = Flask(__name__)

@app.route("/api/charge", methods = ['POST'])
def charge():
    try:
        content = request.get_json()
        # Print what JSON comes in for the sake of checking
        print(content)

        resp = stripe.Charge.create(
            amount=content['amount'],
            currency="usd",
            source="tok_visa",
            receipt_email=content['receiptEmail'],
        )
        print("Success: %r" % (resp))
        return "Successfully charged", 201
    except Exception as e:
        print(e)
        return "Charge failed", 500

if __name__ == "__main__":
    app.run()

