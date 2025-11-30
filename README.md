# AI-task-manager
This capstone project focuses on designing and implementing an AI-powered Concierge Agent that helps users and teams manage tasks, schedules, and reminders efficiently.
Project Title: Intelligent Concierge Agent for Task and Workflow Management
# **1. Project Overview**

### This capstone project focuses on designing and implementing an AI-powered Concierge Agent that helps users and teams manage tasks, schedules, and reminders efficiently. The agent can autonomously create, update, prioritize, and notify about tasks while integrating with calendar systems, messaging platforms, and productivity tools.

#### The project demonstrates the practical application of autonomous agents in task management, multi-step reasoning, and user interaction to improve personal and organizational productivity.

# **2. Problem Statement**

### Managing multiple tasks, deadlines, and reminders manually is time-consuming and error-prone. Users often forget to update priorities, miss deadlines, or spend excessive time coordinating schedules.

#### The goal of this project is to develop an intelligent concierge agent that can:

- Manage tasks efficiently

- Prioritize and schedule tasks based on urgency and deadlines

- Notify users of upcoming deadlines

- Suggest task delegation or rescheduling

- Provide insights into productivity patterns

# **3. Project Objectives**

1. Design an autonomous Concierge Agent capable of task management.

2. Implement task creation, update, deletion, and prioritization functionality.

3. Integrate reminders and notifications for upcoming tasks.

4. Allow multi-step reasoning to suggest optimal task ordering.

5. Provide a user-friendly interface (CLI, web, or chat-based).

6. Demonstrate the agent in a real-life task scenario.

# **4. System Architecture**
## 4.1 Agent Components

Agent Name	Responsibilities

- Task Collector Agent	Gathers tasks from user input, emails, or external tools

- Scheduler Agent	Prioritizes and schedules tasks based on deadlines, urgency, and dependencies

- Notification Agent	Sends reminders via email, chat, or notifications

- Analysis Agent	Provides insights and suggestions for task optimization

- Coordinator Agent	Orchestrates workflow among all agents and resolves conflicts

## 4.2 Workflow

- User inputs task → Task Collector Agent records it.

- Scheduler Agent prioritizes tasks based on deadlines and urgency.

- Notification Agent sends reminders for pending tasks.

- Analysis Agent suggests optimization (e.g., rescheduling or delegation).

- Coordinator Agent ensures smooth interaction between all agents.

# **Architecture**

```

  +------------------+
  | TaskCollector    |
  +------------------+
          |
          v
  +------------------+
  |   Scheduler      |
  +------------------+
          |
          v
  +------------------+
  |  AnalysisAgent   |
  +------------------+
          |
          v
  +------------------+
  | NotificationAgent|
  +------------------+
          ^
          |
  +------------------+
  |   Coordinator    |
  +------------------+
      |          |
      v          v
 +---------+   +----------------+
 | Gemini  |   | Google Calendar|
 |  AI     |   +----------------+
 v
```

# **5. Tools & Technologies**

Programming Language: Python 3

- Agent Frameworks: LangChain, OpenAI API, or custom agent classes

- Task & Calendar Integration: Google Calendar API, Microsoft Graph API (optional)

- Notification Channels: Email (SMTP), Slack API, Telegram Bot API

- Libraries: pandas, datetime, rich (CLI), schedule

# **6. Implementation Plan**

Step 1: Task Input

1. CLI-based or chat-based input for tasks.

3. Optional import from email or calendar events.

Step 2: Scheduling & Prioritization

1. Assign priority based on deadline, urgency, and workload.

2. Multi-step reasoning: Suggest optimal task order.

Step 3: Notifications

- Notify users X hours before deadlines.

- Daily summary of pending tasks.

Step 4: Task Analysis

- Identify overdue or high-priority tasks.
  
- Provide suggestions for task delegation or rescheduling.

Step 5: Coordination

- Coordinator Agent ensures all agents operate without conflicts.

# **7. Sample Output (Task Summary)**

Task Dashboard:

1. Task Name	Priority	Deadline	Status	Suggested Action
   
2. Submit report	High	2025-12-02	Pending	Do today
   
3. Team meeting	Medium	2025-12-03	Scheduled	Attend
   
4. Code review	Low	2025-12-05	Pending	Reschedule if busy

### Notification Example:

Reminder: "Submit report" is due in 2 hours. Please prioritize this task.

# **8. Installation**

```bash
git clone https://github.com/rony926/ai-task-manager.git
cd ai-task-manager
```
### Create Python Virtual Environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### Install Required Libraries
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install slack_sdk
pip install openai  # Or Gemini SDK if officially available

```

### Setup API Keys

- Gemini API Key: Replace YOUR_GEMINI_API_KEY in the script.

- Slack Bot Token: Replace YOUR_SLACK_BOT_TOKEN in the script.

- Google Calendar: Place service_account.json in the project root.

### How to Run
```
python agent_gemini_integrated.py

```

# **9. Challenges Faced**

- Balancing task urgency vs user preference.

- Integrating multi-channel notifications reliably.

- Handling task conflicts and dependencies.

- Scaling the system for multiple users concurrently.

# **9. Future Enhancements**

- AI-powered task completion predictions.
  
- Integration with enterprise collaboration tools (Asana, Trello, Jira).
  
- Voice-based task input and interaction.
  
- Automatic delegation to team members based on workload.
  

# **10. Conclusion**

### The Concierge Agent successfully demonstrates autonomous task management for personal and professional productivity. By leveraging multi-agent architecture, intelligent scheduling, and notifications, the system reduces manual effort, prevents missed deadlines, and provides actionable productivity insights.
