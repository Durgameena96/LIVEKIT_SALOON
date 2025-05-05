

I have installed the following: 
pip install livekit
pip install livekit-api
pip install firebase-admin


After installed Generated the LIVEKIT_API_KEY and LIVEKIT_API_SECRET from Livekit portal.
And i have installed firebase for the storage.

I have created the project with following structure

my-salon-agent/
│
├── agent.py            # Main AI logic
├── knowledge_base.py   # Simple Q&A storage
├── help_request.py     # Help request DB model
|___app.py              # To handle API calls for storage, history, pending requests from UI
├── .env                # LIVEKIT API keys and url
├── firebase_init.py    # To Initialize firebase configuration and certificate
|__ templates           # For the UI screen with html and app calls
└── README.md
