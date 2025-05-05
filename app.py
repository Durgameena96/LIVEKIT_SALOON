from flask import Flask, render_template, request, redirect, url_for, jsonify
from firebase_init import db
from datetime import datetime

app = Flask(__name__)

""" Connects to Firestore (db)
Queries the help_requests collection
Filters documents where status == "pending"
Passes that data to the template """

@app.route('/')
def index():
    docs = db.collection('help_requests').where('status', '==', 'pending').stream()
    requests = [doc.to_dict() | {'id': doc.id} for doc in docs]
    return render_template('index.html', requests=requests)

@app.route('/respond/<id>', methods=['POST'])
def respond(id):
    answer = request.form['response']
    db.collection('help_requests').document(id).update({
        'status': 'resolved',
        'response': answer,
        'resolved_at': datetime.utcnow().isoformat(),
        'handled_by': 'supervisor_001'  # Placeholder ID
    })
    print(f"[Texted back customer] Answer: {answer}")
    return redirect(url_for('index'))

@app.route('/api/pending')
def api_pending():
    docs = db.collection('help_requests').where('status', '==', 'pending').stream()
    requests = [doc.to_dict() | {'id': doc.id} for doc in docs]
    return jsonify(requests)

@app.route('/history')
def history():
    docs = db.collection('help_requests').where('status', '!=', 'pending').stream()
    requests = [doc.to_dict() for doc in docs]
    return render_template('history.html', requests=requests)

if __name__ == '__main__':
    app.run(debug=True)
