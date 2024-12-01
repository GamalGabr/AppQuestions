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
        "id": f"{random.randint(0, 100)}",
        "question": f"In a group of {total_population} people, {physics_only + physics_and_maths} like Physics, "
                    f"{maths_only + physics_and_maths} like Maths, and {physics_and_maths} like both. "
                    f"How many people like Physics only?",
        "options": [
            physics_only,
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 10)
        ],
        "correct": physics_only
    }
    random.shuffle(question["options"])  # Shuffle the options
    return question

def generate_absolute_vs_relative_change_question():
    """
    Generates a random question comparing absolute and relative percentage changes.
    Includes both increases and decreases to teach the importance of context.
    """
    initial_value = random.randint(1, 10)  # Random initial chance
    change = random.choice([-1, 1]) * random.randint(1, 5)  # Random change (positive or negative)
    new_value = max(1, initial_value + change)  # Ensure new value is at least 1

    absolute_change = new_value - initial_value
    relative_change = round((absolute_change / initial_value) * 100, 0)

    # Format the question to explain the difference
    question = {
        "id": f"{random.randint(0, 100)}",
        "question": f"An athlete's chances of qualifying for the Highland Games changed from {initial_value}% to "
                    f"{new_value}%. What is the absolute percentage change and the relative percentage change?",
        "options": [
            f"Absolute: {abs(absolute_change)}%, Relative: {abs(relative_change)}%",
            f"Absolute: {abs(absolute_change) + random.randint(1, 3)}%, Relative: {abs(relative_change) + random.randint(10, 20)}%",
            f"Absolute: {abs(absolute_change) - random.randint(1, 2)}%, Relative: {abs(relative_change) - random.randint(5, 10)}%",
            f"Absolute: {abs(absolute_change) + random.randint(2, 3)}%, Relative: {abs(relative_change) + random.randint(15, 30)}%"
        ],
        "correct": f"Absolute: {abs(absolute_change)}%, Relative: {abs(relative_change)}%"
    }
    random.shuffle(question["options"])  # Shuffle the options for randomness
    return question

def generate_percentage_question():
    """
    Generates a random percentage change question involving values between 1 and 10.
    """
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    percentage_change = round(((number2 - number1) / number1) * 100, 0)

    question = {
        "id": f"{random.randint(0, 100)}",
        "question": f"The initial value was {number1}, and the new value is {number2}. What is the percentage change?",
        "options": [
            percentage_change,
            percentage_change + random.randint(1, 5),
            percentage_change - random.randint(1, 5),
            percentage_change + random.randint(5, 10)
        ],
        "correct": percentage_change
    }
    random.shuffle(question["options"])  # Shuffle the options
    return question

def generate_price_change_question():
    """
    Generates a random percentage change question for price differences.
    """
    initial_price = random.randint(1, 10)
    new_price = random.randint(1, 10)
    percentage_change = round(((new_price - initial_price) / initial_price) * 100, 0)

    question = {
        "id": f"{random.randint(0, 100)}",
        "question": f"The initial price was {initial_price}, and the new price is {new_price}. "
                    f"What is the percentage change?",
        "options": [
            percentage_change,
            percentage_change + random.randint(1, 5),
            percentage_change - random.randint(1, 5),
            percentage_change + random.randint(5, 10)
        ],
        "correct": percentage_change
    }
    random.shuffle(question["options"])  # Shuffle the options
    return question

def update_questions_file():
    """
    Updates the questions.json file with 10 new questions.
    """
    questions = []

    # Add different types of questions
    for _ in range(4):
        questions.append(generate_venn_diagram_question())
    for _ in range(3):
        questions.append(generate_percentage_question())
    for _ in range(2):
        questions.append(generate_absolute_vs_relative_change_question())
    questions.append(generate_price_change_question())

    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)
    print("questions.json updated successfully with 10 questions.")

if __name__ == "__main__":
    update_questions_file()
