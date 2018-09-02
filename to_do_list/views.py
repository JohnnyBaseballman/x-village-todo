from flask import Flask, request, jsonify, render_template

from app import app, db
from models import Record


@app.route("/")
def index():
    return render_template('index.html', title='Accounting')


@app.route("/record", methods=['POST'])
def add_record():
    req_data = request.form
    job = req_data['job']
    deadline = req_data['deadline']
    record = Record(job=job, deadline=deadline)
    db.session.add(record)
    db.session.commit()
    return 'Create Succeeded', 200


@app.route("/record", methods=['GET'])
def get_records():
    records = Record.query.all()
    records_data = [
        {
            'id': record.id,
            'job': record.job,
            'deadline': record.deadline
        }
        for record in records
    ]
    return jsonify(records_data), 200


@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    record_data = {
        'id': record.id,
        'job': record.job,
        'deadline': record.deadline
    }
    return jsonify(record_data), 200


@app.route('/record/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    req_data = request.form
    record = Record.query.filter_by(id=record_id).first()
    record.job = req_data['job']
    record.deadline = req_data['deadline']
    db.session.add(record)
    db.session.commit()
    return 'Update Succeeded', 200


@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    db.session.delete(record)
    db.session.commit()
    return 'Delete Succeeded', 200
