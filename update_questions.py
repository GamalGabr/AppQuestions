import json
import random

def generate_questions():
    """Generates a new set of questions."""
    new_questions = [
        {
            "id": "0",
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "correct": "Paris"
        },
        {
            "id": "1",
            "question": "What is 5 + 7?",
            "options": ["10", "12", "15", "17"],
            "correct": "12"
        },
        {
            "id": "2",
            "question": "Who painted the ceiling of the Sistine Chapel?",
            "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
            "correct": "Michelangelo"
        },
        {
            "id": "3",
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus"],
            "correct": "Mitochondria"
        },
        {
            "id": "4",
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
            "correct": "Pacific Ocean"
        }
    ]
    return random.sample(new_questions, len(new_questions))  # Shuffle questions

def update_questions_file():
    """Updates the questions.json file with new questions."""
    questions = generate_questions()
    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)
    print("questions.json updated successfully.")

if __name__ == "__main__":
    update_questions_file()
