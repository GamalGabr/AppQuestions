import json
import random

def generate_venn_diagram_question():
    """
    Generates a random Venn diagram question about the relationships between people liking physics and maths.
    """
    total_population = 10
    physics_and_maths = random.randint(1, total_population - 1)  # People liking both
    physics_only = random.randint(0, total_population - physics_and_maths)
    maths_only = total_population - physics_and_maths - physics_only
    
    question = {
        "id": "0",
        "question": f"In a group of {total_population} people, {physics_only + physics_and_maths} like Physics, "
                    f"{maths_only + physics_and_maths} like Maths, and {physics_and_maths} like both. "
                    f"How many people like Physics only?",
        "options": [
            physics_only,
            physics_only + random.randint(1, 2),
            physics_only - random.randint(1, 2),
            physics_only + random.randint(2, 3)
        ],
        "correct": physics_only
    }
    random.shuffle(question["options"])  # Shuffle the options
    return question

def generate_percentage_question():
    """
    Generates a random percentage-related question involving numbers between 0.5 and 10.
    """
    number1 = round(random.uniform(0.5, 10), 1)
    number2 = round(random.uniform(0.5, 10), 1)
    percentage_change = round(((number2 - number1) / number1) * 100, 1)
    question = {
        "id": "1",
        "question": f"The initial value was {number1} and the new value is {number2}. What is the percentage change?",
        "options": [
            round(percentage_change, 1),
            round(percentage_change + random.uniform(1, 5), 1),
            round(percentage_change - random.uniform(1, 5), 1),
            round(percentage_change + random.uniform(5, 10), 1)
        ],
        "correct": round(percentage_change, 1)
    }
    random.shuffle(question["options"])  # Shuffle the options
    return question

def generate_price_change_question():
    """
    Generates a random percentage change question for price differences.
    """
    initial_price = random.randint(1, 10)
    new_price = random.randint(1, 20)
    percentage_change = round(((new_price - initial_price) / initial_price) * 100, 1)
    question = {
        "id": "2",
        "question": f"The initial price was {initial_price}, and the new price is {new_price}. "
                    f"What is the percentage change?",
        "options": [
            round(percentage_change, 1),
            round(percentage_change + random.uniform(1, 5), 1),
            round(percentage_change - random.uniform(1, 5), 1),
            round(percentage_change + random.uniform(5, 10), 1)
        ],
        "correct": round(percentage_change, 1)
    }
    random.shuffle(question["options"])  # Shuffle the options
    return question

def update_questions_file():
    """
    Updates the questions.json file with two new questions daily.
    """
    questions = [
        generate_venn_diagram_question(),
        generate_percentage_question(),
        generate_price_change_question()
    ]
    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)
    print("questions.json updated successfully.")

if __name__ == "__main__":
    update_questions_file()
