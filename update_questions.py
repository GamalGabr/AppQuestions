import json
import random
import os
import subprocess

# Updated to use `TARGET_REPO_TOKEN` instead of `GITHUB_TOKEN` for authentication
TARGET_REPO_URL = f"https://x-access-token:{os.getenv('TARGET_REPO_TOKEN')}@github.com/GamalGabr/Target-Questions-Repo.git"
LOCAL_TARGET_REPO_PATH = "Target-Questions-Repo"
BRANCH_NAME = "main"

# Existing Venn diagram question generator
def generate_venn_diagram_question():
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

# Generate absolute vs relative change question
def generate_absolute_vs_relative_change_question():
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

# Generate a question about percentage change
def generate_percentage_question():
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

# Generate a new type of question about machine efficiency
def generate_machine_efficiency_question():
    # Generate random initial values
    num_machines = random.randint(2, 10)  # Number of machines
    time_per_set = random.randint(1, 10)  # Time in minutes for one set of output
    crackers_per_set = random.randint(5, 20)  # Crackers made in one set

    # Scale up the problem
    scaled_machines = num_machines * 10
    scaled_crackers = crackers_per_set * random.randint(2, 5)  # Random scaling factor for crackers

    # Calculate the correct time based on scaled crackers and machines
    time_for_scaled_crackers = (time_per_set * scaled_crackers) / (scaled_machines * crackers_per_set / num_machines)

    # Format the question text
    question_text = (
        f"If it takes {num_machines} machines {time_per_set} minutes to make {crackers_per_set} crackers, "
        f"how long would it take {scaled_machines} machines to make {scaled_crackers} crackers?"
    )

    # Create plausible options
    correct_time = round(time_for_scaled_crackers, 2)
    question = {
        "id": f"{random.randint(0, 100)}",
        "question": question_text,
        "options": [
            f"{correct_time} minutes",
            f"{correct_time + random.uniform(0.5, 2.5):.2f} minutes",
            f"{correct_time - random.uniform(0.5, 1.5):.2f} minutes",
            f"{correct_time + random.uniform(2.5, 5):.2f} minutes",
            f"{correct_time * random.randint(2, 3):.2f} minutes"
        ],
        "correct": f"{correct_time} minutes"
    }

    # Shuffle the options
    random.shuffle(question["options"])
    return question

# Function to update the questions.json file
def update_questions_file():
    questions = []

    # Generate a wider range of questions
    for _ in range(4):
        questions.append(generate_venn_diagram_question())
    for _ in range(3):
        questions.append(generate_percentage_question())
    for _ in range(2):
        questions.append(generate_absolute_vs_relative_change_question())
    for _ in range(2):
        questions.append(generate_machine_efficiency_question())

    # Clone the target repository
    if not os.path.exists(LOCAL_TARGET_REPO_PATH):
        subprocess.run(["git", "clone", TARGET_REPO_URL, LOCAL_TARGET_REPO_PATH], check=True)

    # Write questions.json
    questions_file_path = os.path.join(LOCAL_TARGET_REPO_PATH, "questions.json")
    with open(questions_file_path, "w") as file:
        json.dump(questions, file, indent=4)

    # Commit and push changes
    os.chdir(LOCAL_TARGET_REPO_PATH)
    subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
    subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "add", "questions.json"], check=True)
    subprocess.run(["git", "commit", "-m", "Update questions.json with new questions"], check=True)
    subprocess.run(["git", "push", "origin", BRANCH_NAME], check=True)

if __name__ == "__main__":
    update_questions_file()
