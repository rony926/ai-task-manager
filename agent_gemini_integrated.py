# concierge_agent_gemini_integrated.py
# Intelligent Concierge Agent with Gemini, Google Calendar, and Slack Notifications

import datetime
import os
from collections import deque
from google.ai import gemini  # Placeholder: replace with real Gemini client import
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# -----------------------------
# CONFIGURATION
# -----------------------------
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
SLACK_TOKEN = "YOUR_SLACK_BOT_TOKEN"
SLACK_CHANNEL = "#general"

GOOGLE_CREDENTIALS_FILE = "service_account.json"
SCOPES = ['https://www.googleapis.com/auth/calendar']

# -----------------------------
# LLM CLIENT SETUP
# -----------------------------
client = gemini.GeminiClient(api_key=GEMINI_API_KEY)

def query_gemini(prompt):
    response = client.complete(prompt=prompt, max_output_tokens=200)
    return response.text.strip()

# -----------------------------
# Slack Client
# -----------------------------
slack_client = WebClient(token=SLACK_TOKEN)

def send_slack_message(message):
    try:
        slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        print(f"[Slack] Sent notification: {message}")
    except SlackApiError as e:
        print(f"[Slack Error] {e.response['error']}")

# -----------------------------
# Google Calendar Client
# -----------------------------
creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
calendar_service = build('calendar', 'v3', credentials=creds)
CALENDAR_ID = 'primary'

def add_event_to_calendar(task_name, deadline):
    event = {
        'summary': task_name,
        'start': {'dateTime': deadline.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': (deadline + datetime.timedelta(hours=1)).isoformat(), 'timeZone': 'UTC'},
    }
    event = calendar_service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"[Calendar] Event created: {event.get('htmlLink')}")

# -----------------------------
# Task Classes
# -----------------------------
class Task:
    def __init__(self, name, deadline, priority="Medium"):
        self.name = name
        self.deadline = deadline
        self.priority = priority
        self.status = "Pending"

    def __repr__(self):
        return f"{self.name} | Priority: {self.priority} | Deadline: {self.deadline} | Status: {self.status}"

# -----------------------------
# Agent Classes
# -----------------------------
class TaskCollectorAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline, priority="Medium"):
        task = Task(name, deadline, priority)
        self.tasks.append(task)
        print(f"[Collector] Added task: {task.name}")
        add_event_to_calendar(name, deadline)  # Calendar integration
        return task

    def get_tasks(self):
        return self.tasks

class SchedulerAgent:
    def prioritize_tasks(self, tasks):
        for task in tasks:
            prompt = f"Task: {task.name}\nDeadline: {task.deadline}\nCurrent Priority: {task.priority}\n" \
                     f"Suggest new priority: High, Medium, or Low based on urgency and importance."
            suggested_priority = query_gemini(prompt)
            if suggested_priority in ["High", "Medium", "Low"]:
                task.priority = suggested_priority
        tasks.sort(key=lambda t: ({"High":1, "Medium":2, "Low":3}[t.priority], t.deadline))
        print("[Scheduler] Tasks prioritized with Gemini")
        return tasks

class NotificationAgent:
    def notify(self, task):
        message = f"Reminder: '{task.name}' is due at {task.deadline} (Priority: {task.priority})"
        print(f"[Notification] {message}")
        send_slack_message(message)

class AnalysisAgent:
    def analyze_tasks(self, tasks):
        task_summary = "\n".join([f"{t.name} | Priority: {t.priority} | Status: {t.status}" for t in tasks])
        prompt = f"Analyze these tasks and suggest which need urgent attention:\n{task_summary}"
        analysis = query_gemini(prompt)
        print("[Analysis] Generated task analysis via Gemini")
        return analysis

class CoordinatorAgent:
    def __init__(self):
        self.collector = TaskCollectorAgent()
        self.scheduler = SchedulerAgent()
        self.notifier = NotificationAgent()
        self.analyzer = AnalysisAgent()
        self.task_queue = deque()

    def add_task(self, name, deadline_str, priority="Medium"):
        deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        task = self.collector.add_task(name, deadline, priority)
        self.task_queue.append(task)

    def run(self):
        tasks = list(self.task_queue)
        tasks = self.scheduler.prioritize_tasks(tasks)

        now = datetime.datetime.now()
        for task in tasks:
            if task.status == "Pending" and (task.deadline - now).total_seconds() <= 86400:
                self.notifier.notify(task)

        report = self.analyzer.analyze_tasks(tasks)
        print("\n--- Executive Task Summary ---")
        print(report)
        return report

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    coordinator = CoordinatorAgent()
    coordinator.add_task("Submit Report", "2025-12-02 17:00", "High")
    coordinator.add_task("Team Meeting", "2025-12-03 10:00", "Medium")
    coordinator.add_task("Code Review", "2025-12-05 15:00", "Low")
    coordinator.add_task("Prepare Presentation", "2025-12-04 09:00", "High")

    coordinator.run()

