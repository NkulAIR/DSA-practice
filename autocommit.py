import subprocess
import time
import os
import sys

# --- CONFIGURATION ---
# How often to check/prompt (in minutes)
CHECK_INTERVAL_MINUTES = 10 

def git_has_changes():
    """Checks if there are modified or untracked files."""
    try:
        # 'git status --porcelain' gives a clean output for parsing
        result = subprocess.run(
            ["git", "status", "--porcelain"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        print("Error: Not a valid git repository or git is not installed.")
        return False

def commit_changes():
    """Prompts for message and commits."""
    print("\n" + "="*40)
    print(f"Changes detected at {time.strftime('%H:%M')}")
    print("="*40)
    
    # Show a brief summary of files
    subprocess.run(["git", "status", "-s"])
    print("-" * 40)
    
    try:
        msg = input("Enter commit message (Press Enter to skip): ").strip()
        
        if msg:
            print("Staging files...")
            subprocess.run(["git", "add", "."])
            
            print("Committing...")
            subprocess.run(["git", "commit", "-m", msg])
            print("Success! Changes committed.")
        else:
            print("Skipping commit for this cycle.")
            
    except KeyboardInterrupt:
        print("\nInput cancelled.")
        return

def main():
    if not os.path.exists(".git"):
        print("Error: Run this script from the root of a Git repository.")
        sys.exit(1)

    print(f"Auto-commit script started.")
    print(f"Interval: {CHECK_INTERVAL_MINUTES} minutes.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            # Wait for the interval
            time.sleep(CHECK_INTERVAL_MINUTES * 60)
            
            if git_has_changes():
                commit_changes()
            else:
                print(f"[{time.strftime('%H:%M')}] No changes detected.")

    except KeyboardInterrupt:
        print("\n\nScript stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()