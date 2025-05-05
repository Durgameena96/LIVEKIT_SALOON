# help_request.py
from firebase_init import db
from datetime import datetime

def create_help_request(question, customer_id):
    help_request = {
        "customer_id": customer_id,
        "question": question,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat(),
        "resolved_at": None,
        "response": None,
        "handled_by": None
    }

    doc_ref = db.collection("help_requests").add(help_request)
    print(f"[Help Request Created] ID: {doc_ref[1].id}")
