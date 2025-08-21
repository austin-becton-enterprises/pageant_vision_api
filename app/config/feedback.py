"""
    "Missing error handling for environment variables in session.py.",
    "Inconsistent types for date/time fields.",
    "Types: grant_time in Access is a DateTime, but in AccessRemoved it's a String. This inconsistency could cause issues.",
    "Types: Some fields are str but represent timestamps or integers. Consider using datetime or int where appropriate for clarity and validation.",
    "Unimplemented Sections: Many CRUD sections are just comments. Make sure to implement these as needed.",
    "Testing: Write tests for your CRUD operations and models.",

    "Error Handling: If a record is not found, None is returned, which is fine, but you may want to raise HTTP exceptions in your API layer.",
    "Consider using a .env loader (like python-dotenv) for local development.",


"""