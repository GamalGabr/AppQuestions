import json
import random
import os
import subprocess

TARGET_REPO_URL = "https://github.com/GamalGabr/Target-Questions-Repo.git"
LOCAL_TARGET_REPO_PATH = "Target-Questions-Repo"  # Path to clone the target repo
BRANCH_NAME = "main"  # Target branch name

def generate_venn_diagram_question():
    # (Question generation logic remains the same)
    total_population = 10
    physics_and_maths = random.randint(1, total_population - 1)
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
    random.shuffle(question["options"])
    return question

def generate_absolute_vs_relative_change_question():
    # (Question generation logic remains the same)
    initial_value = random.randint(1, 10)
    change = random.choice([-1, 1]) * random.randint(1, 5)
    new_value = max(1, initial_value + change)
    absolute_change = new_value - initial_value
    relative_change = round((absolute_change / initial_value) * 100, 0)

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
    random.shuffle(question["options"])
    return question

def generate_percentage_question():
    # (Question generation logic remains the same)
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
    random.shuffle(question["options"])
    return question

def generate_price_change_question():
    # (Question generation logic remains the same)
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
    random.shuffle(question["options"])
    return question

def update_questions_file():
    # Step 1: Generate Questions
    questions = []

    for _ in range(4):
        questions.append(generate_venn_diagram_question())
    for _ in range(3):
        questions.append(generate_percentage_question())
    for _ in range(2):
        questions.append(generate_absolute_vs_relative_change_question())
    questions.append(generate_price_change_question())

    # Step 2: Clone Target Repository if Not Already Cloned
    if not os.path.exists(LOCAL_TARGET_REPO_PATH):
        print(f"Cloning target repository: {TARGET_REPO_URL}")
        subprocess.run(["git", "clone", TARGET_REPO_URL, LOCAL_TARGET_REPO_PATH], check=True)

    # Step 3: Write Questions File to Target Repository
    questions_file_path = os.path.join(LOCAL_TARGET_REPO_PATH, "questions.json")
    with open(questions_file_path, "w") as file:
        json.dump(questions, file, indent=4)
    print(f"questions.json updated successfully in {LOCAL_TARGET_REPO_PATH}")

    # Step 4: Commit and Push Changes to Target Repository
    os.chdir(LOCAL_TARGET_REPO_PATH)  # Change to target repo directory
    subprocess.run(["git", "add", "questions.json"], check=True)
    subprocess.run(["git", "commit", "-m", "Update questions.json with new questions"], check=True)
    subprocess.run(["git", "push", "origin", BRANCH_NAME], check=True)
    print("Changes pushed to target repository.")

if __name__ == "__main__":
    update_questions_file()
