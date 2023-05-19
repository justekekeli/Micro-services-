import os


api_key = os.getenv('OPENAI')

def test_connection():
    assert api_key!=None