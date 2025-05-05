# agent.py

from knowledge_base import get_answer
import uuid

def handle_incoming_call(question, customer_id):
    print(f"Received question from customer {customer_id}: {question}")
    answer = get_answer(question)
    if answer:
        print(f"AI Response: {answer}")
    else:
        print("AI: Let me check with my supervisor and get back to you.")
        create_help_request(question, customer_id)

def create_help_request(question, customer_id):
    print(f"[Help Request Created] Customer {customer_id}: {question}")
    # Here, you would insert this into your database (e.g., Firebase, DynamoDB)

if __name__ == "__main__":
    customer_id = str(uuid.uuid4())
    question = input("Simulate call - ask your question: ")
    handle_incoming_call(question, customer_id)
