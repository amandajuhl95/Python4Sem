#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pandas as pd
import pymysql

app = Flask(__name__)

cnx = pymysql.connect(
    user="dev", password="ax2", host="127.0.0.1", port=3307, db="python"
)


@app.route("/ipaddress/api/info", methods=["GET"])
def get_info():
    df = pd.read_sql("SELECT * FROM week9", con=cnx)
    info = df.to_dict("records")
    return jsonify({"info": info})


if __name__ == "__main__":
    app.run(debug=True)

