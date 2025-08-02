# Reading Space Booking Web App using Flask

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import uuid

app = Flask(__name__)

# Dummy in-memory databases
seats = [
    {"id": "1", "room": "A", "number": "A1", "type": "Silent", "active": True},
    {"id": "2", "room": "A", "number": "A2", "type": "Silent", "active": True},
    {"id": "3", "room": "B", "number": "B1", "type": "Group", "active": False},
]

slots = [
    {"id": "101", "date": "2025-08-02", "start": "10:00", "end": "12:00", "total": 2, "available": 1},
    {"id": "102", "date": "2025-08-02", "start": "14:00", "end": "16:00", "total": 2, "available": 2},
]

bookings = []
students = []
payments = []

@app.route('/')
def index():
    return render_template("index.html", slots=slots, seats=seats)

@app.route('/book', methods=["POST"])
def book():
    student = request.form.get("name")
    seat_id = request.form.get("seat")
    slot_id = request.form.get("slot")
    payment_method = request.form.get("payment")

    booking_id = str(uuid.uuid4())[:8]
    bookings.append({
        "booking_id": booking_id,
        "student": student,
        "seat_id": seat_id,
        "slot_id": slot_id,
        "payment_method": payment_method,
        "paid": True if payment_method != "Cash" else False
    })
    payments.append({
        "booking_id": booking_id,
        "amount": 100,
        "method": payment_method,
        "status": "Paid" if payment_method != "Cash" else "Pending"
    })
    return redirect(url_for("index"))

@app.route('/admin')
def admin():
    return render_template("admin.html", bookings=bookings, payments=payments)

if __name__ == '__main__':
    app.run(debug=True)