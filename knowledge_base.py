# knowledge_base.py

KNOWN_QUESTIONS = {
    "what are your hours": "We are open from 9am to 6pm, Monday to Saturday.",
    "Do you have offers": "Yes, we have various offers. Please check our website for the latest deals.",
    "where are you located": "We are at 123 Main Street, Washington."
}

def get_answer(question):
    normalized = question.lower().strip()
    return KNOWN_QUESTIONS.get(normalized)
