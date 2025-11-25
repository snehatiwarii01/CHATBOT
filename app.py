from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize Flask with specific static folder settings
# static_url_path='' allows accessing static files at root if needed, 
# but we will serve index.html explicitly.
app = Flask(__name__, static_folder='static')

# --- Model Loading ---
# We removed the local 'model/' directory logic. 
# This will now download/cache the model in the default system cache (~/.cache/huggingface).
MODEL_NAME = "facebook/blenderbot-400M-distill"

print(f"Loading model: {MODEL_NAME}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route("/")
def home():
    # Serve index.html directly from the static folder
    return app.send_static_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"reply": "Please send a valid message."}), 400

        # Tokenize and generate
        inputs = tokenizer(user_input, return_tensors="pt")
        outputs = model.generate(**inputs)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({"reply": response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Sorry, an error occurred."}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)