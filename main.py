from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Load flashcards from a JSON file
def load_flashcards(topic):
    path = os.path.join(app.root_path, 'templates', 'topics', f'{topic}.json')
    with open(path, 'r') as file:
        return json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    topics = ['network_basics', 'layer3_technologies', 'vpn_technologies', 'infrastructure_security', 'infrastructure_services']
    topic = request.args.get('topic', 'network_basics')  # Default topic
    flashcards = load_flashcards(topic)
    card_index = int(request.args.get('card', 0))  # Default to first card

    return render_template('index.html', card=flashcards[card_index], topic=topic, card_index=card_index, total_cards=len(flashcards), topics=topics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

