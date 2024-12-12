import json
import random
import os
import subprocess

TARGET_REPO_URL = f"https://x-access-token:{os.getenv('GITHUB_TOKEN')}@github.com/GamalGabr/Target-Questions-Repo.git"
LOCAL_TARGET_REPO_PATH = "Target-Questions-Repo"
BRANCH_NAME = "main"

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

def update_questions_file():
    questions = []

    # Generate questions
    for _ in range(4):
        questions.append(generate_venn_diagram_question())

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
