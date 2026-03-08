from auth.login import login_bp
from auth.register import register_bp
from auth.logout import logout_bp
from database.db import get_connection

from flask import Flask, request, render_template, session, redirect
import pickle
import numpy as np

app = Flask(__name__)

app.secret_key = "supersecretkey"

# register auth routes
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(logout_bp)

# load ML model
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("label_encoder.pkl", "rb"))


@app.route("/")
def home():

    # user must login first
    if "user" not in session:
        return redirect("/login")

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    hemoglobin = float(request.form["hemoglobin"])
    rbc = float(request.form["rbc"])
    platelets = float(request.form["platelets"])
    mcv = float(request.form["mcv"])
    mch = float(request.form["mch"])
    mchc = float(request.form["mchc"])
    pdw = float(request.form["pdw"])

    features = np.array([[hemoglobin, rbc, platelets, mcv, mch, mchc, pdw]])

    prediction = model.predict(features)

    disease = encoder.inverse_transform([prediction[0]])[0]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (username, hemoglobin, rbc, platelets, mcv, mch, mchc, pdw, result)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user"],
        hemoglobin,
        rbc,
        platelets,
        mcv,
        mch,
        mchc,
        pdw,
        disease
    ))

    conn.commit()
    conn.close()

    # values for chart
    blood_values = [
        hemoglobin,
        rbc,
        platelets,
        mcv,
        mch,
        mchc,
        pdw
    ]

    return render_template(
        "result.html",
        prediction=disease,
        blood_values=blood_values
    )


@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/login")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM predictions WHERE username=? ORDER BY created_at DESC",
        (session["user"],)
    )

    rows = cursor.fetchall()

    conn.close()

    return render_template("history.html", rows=rows)


@app.route("/delete/<int:id>")
def delete_prediction(id):

    if "user" not in session:
        return redirect("/login")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM predictions WHERE id=? AND username=?",
        (id, session["user"])
    )

    conn.commit()
    conn.close()

    return redirect("/history")


if __name__ == "__main__":
    app.run(debug=True, port=8000)