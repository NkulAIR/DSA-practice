"""
Daily LeetCode Challenge Tracker
Provides daily random questions from your offline question bank
"""

import json
import random
from datetime import datetime
from pathlib import Path


class DailyLeetCodeChallenge:
    def __init__(self, questions_file="leetcode_questions.json", progress_file="leetcode_progress.json"):
        self.questions_file = questions_file
        self.progress_file = progress_file
        self.questions = self._load_questions()
        self.progress = self._load_progress()
    
    def _load_questions(self):
        """Load questions from JSON file"""
        with open(self.questions_file, 'r') as f:
            data = json.load(f)
        return data['questions']
    
    def _load_progress(self):
        """Load progress from JSON file"""
        if Path(self.progress_file).exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {
            "completed": [],
            "attempted": [],
            "last_daily_date": None,
            "last_daily_question": None
        }
    
    def _save_progress(self):
        """Save progress to JSON file"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def get_daily_challenge(self):
        """Get today's challenge (same question all day)"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Return cached question if already retrieved today
        if self.progress['last_daily_date'] == today:
            question_id = self.progress['last_daily_question']
            return self._get_question_by_id(question_id)
        
        # Get available questions (not completed)
        completed_ids = set(self.progress['completed'])
        available = [q for q in self.questions if q['id'] not in completed_ids]
        
        if not available:
            return {"message": "All questions completed! Resetting progress..."}
        
        # Select random question
        question = random.choice(available)
        
        # Update progress
        self.progress['last_daily_date'] = today
        self.progress['last_daily_question'] = question['id']
        self._save_progress()
        
        return question
    
    def _get_question_by_id(self, question_id):
        """Get question by ID"""
        for q in self.questions:
            if q['id'] == question_id:
                return q
        return None
    
    def mark_completed(self, question_id):
        """Mark a question as completed"""
        if question_id not in self.progress['completed']:
            self.progress['completed'].append(question_id)
            self._save_progress()
            print(f"✓ Question {question_id} marked as completed!")
            return True
        print(f"Question {question_id} already completed.")
        return False
    
    def mark_attempted(self, question_id):
        """Mark a question as attempted"""
        if question_id not in self.progress['attempted']:
            self.progress['attempted'].append(question_id)
            self._save_progress()
            print(f"→ Question {question_id} marked as attempted!")
            return True
        print(f"Question {question_id} already attempted.")
        return False
    
    def get_stats(self):
        """Get practice statistics"""
        total = len(self.questions)
        completed = len(self.progress['completed'])
        attempted = len(self.progress['attempted'])
        
        stats = {
            "total_questions": total,
            "completed": completed,
            "attempted": attempted,
            "remaining": total - completed,
            "completion_percentage": round((completed / total) * 100, 2)
        }
        return stats
    
    def display_daily_challenge(self):
        """Display today's challenge in a nice format"""
        question = self.get_daily_challenge()
        
        if "message" in question:
            print(f"\n{question['message']}")
            return
        
        print("\n" + "=" * 70)
        # print(f"{'TODAY\'S LEETCODE CHALLENGE'}")
        print("=" * 70)
        print(f"\nQuestion #{question['id']}: {question['title']}")
        print(f"Difficulty: {question['difficulty']}")
        print(f"Topics: {', '.join(question['topics'])}")
        print(f"Link: {question['url']}")
        print("\n" + "=" * 70)
    
    def display_stats(self):
        """Display progress statistics"""
        stats = self.get_stats()
        print("\n" + "=" * 70)
        print(f"{'YOUR PROGRESS':^70}")
        print("=" * 70)
        print(f"Total Questions:        {stats['total_questions']}")
        print(f"Completed:              {stats['completed']}")
        print(f"Attempted:              {stats['attempted']}")
        print(f"Remaining:              {stats['remaining']}")
        print(f"Completion:             {stats['completion_percentage']}%")
        print("=" * 70 + "\n")
    
    def display_random_by_difficulty(self, difficulty):
        """Get random question by difficulty level"""
        filtered = [q for q in self.questions if q['difficulty'] == difficulty]
        
        if not filtered:
            print(f"No questions found with difficulty: {difficulty}")
            return None
        
        question = random.choice(filtered)
        print(f"\n{difficulty.upper()} Question:")
        print(f"Question #{question['id']}: {question['title']}")
        print(f"Topics: {', '.join(question['topics'])}")
        print(f"Link: {question['url']}\n")
        return question
    
    def search_by_topic(self, topic):
        """Search questions by topic"""
        filtered = [q for q in self.questions if any(t.lower() == topic.lower() for t in q['topics'])]
        
        if not filtered:
            print(f"No questions found with topic: {topic}")
            return []
        
        print(f"\n{len(filtered)} questions found for topic: {topic}")
        print("-" * 70)
        for q in filtered:
            status = "✓" if q['id'] in self.progress['completed'] else "→" if q['id'] in self.progress['attempted'] else " "
            print(f"{status} #{q['id']}: {q['title']} ({q['difficulty']})")
        print("-" * 70 + "\n")
        return filtered


def main():
    """Interactive menu"""
    tracker = DailyLeetCodeChallenge()
    
    while True:
        print("\n" + "=" * 70)
        print("LEETCODE DAILY CHALLENGE TRACKER")
        print("=" * 70)
        print("1. Get Today's Challenge")
        print("2. View Progress Stats")
        print("3. Mark Question as Completed")
        print("4. Mark Question as Attempted")
        print("5. Random Question by Difficulty")
        print("6. Search by Topic")
        print("7. Exit")
        print("-" * 70)
        
        choice = input("Select option (1-7): ").strip()
        
        if choice == '1':
            tracker.display_daily_challenge()
        
        elif choice == '2':
            tracker.display_stats()
        
        elif choice == '3':
            try:
                q_id = int(input("Enter question ID: "))
                tracker.mark_completed(q_id)
            except ValueError:
                print("Invalid ID!")
        
        elif choice == '4':
            try:
                q_id = int(input("Enter question ID: "))
                tracker.mark_attempted(q_id)
            except ValueError:
                print("Invalid ID!")
        
        elif choice == '5':
            print("\nDifficulty levels: Easy, Medium, Hard")
            difficulty = input("Enter difficulty: ").strip()
            tracker.display_random_by_difficulty(difficulty)
        
        elif choice == '6':
            topic = input("Enter topic (e.g., Array, DFS, Dynamic Programming): ").strip()
            tracker.search_by_topic(topic)
        
        elif choice == '7':
            print("\nHappy coding! 🚀")
            break
        
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
