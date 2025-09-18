import subprocess
import os

# ----------------------------
# CONFIGURATION
# ----------------------------
REPO_PATH = os.getcwd()  # SERAI repo folder
FILE_TO_PUSH = "extensions/Aura.xlsx"  # Your .xlsl file
COMMIT_MESSAGE = "Update Aura.xlsx with new STEM modules and teleport logs"

# ----------------------------
# STEP 1: Add file to git
# ----------------------------
subprocess.run(["git", "add", FILE_TO_PUSH], cwd=REPO_PATH)

# ----------------------------
# STEP 2: Commit changes
# ----------------------------
subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], cwd=REPO_PATH)

# ----------------------------
# STEP 3: Push to GitHub
# ----------------------------
subprocess.run(["git", "push", "origin", "main"], cwd=REPO_PATH)

print(f"✅ {FILE_TO_PUSH} has been committed and pushed to GitHub.")
