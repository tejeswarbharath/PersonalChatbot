import os
import requests
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get port from .env or default to 5050
# huggingFace = os.getenv('HUGGING_FACE')

class Chat:
    def __init__(self):
        pass

    def bot(self,prompt):
        API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
        headers = {
            "Authorization": "Bearer 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"
        }

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": "minimaxai/minimax-m1-80k"
        })

        rs = response["choices"][0]["message"]["content"]

        idx = rs.index("</think>")+8

        rs = rs[idx:]

        return rs