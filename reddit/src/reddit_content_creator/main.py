#!/usr/bin/env python
import os
import sys
import warnings
from flask import Flask, request, jsonify
from waitress import serve
import firebase_admin
from firebase_admin import firestore

if os.environ.get('USE_FIRESTORE') == 'True':
    app = firebase_admin.initialize_app()
    db = firestore.client()

from reddit_content_creator.crew import RedditContentCreator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'subreddit': '/r/crewai',
        'post_subject': 'How to use crewai to analyse and generate custom reddit post'
    }
    RedditContentCreator().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'subreddit': '/r/crewai',
        'post_subject': 'How to use crewai to analyse and generate custom reddit post'  
    }
    try:
        RedditContentCreator().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        RedditContentCreator().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(): 
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'subreddit': '/r/crewai',
        'post_subject': 'How to use crewai to analyse and generate custom reddit post'   
    }
    try:
        RedditContentCreator().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
    
def run_http():
    serve(app, host="0.0.0.0", port=os.environ.get("PORT", 8080))

# Initialize the Flask app
app = Flask(__name__)

@app.route("/", methods=["POST"])
def data_handler():
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        inputs = {
            'subreddit': data.get('subreddit'),
            'post_subject': data.get('post_subject')
        }
        
        result = RedditContentCreator().crew().kickoff(inputs=inputs)
        
        task_id = data.get('task_id')
        if os.environ.get('USE_FIRESTORE') == 'True' and task_id:
            db.collection('Tasks').document(task_id).update({
                "postContent": result.raw,
                "status": "completed"
            })
        return result.raw, 200
        

    except Exception as e:
        return jsonify({"error": str(e)}), 500

  