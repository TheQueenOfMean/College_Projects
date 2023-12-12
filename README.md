#My Project: Daily Task Manager

for senior citizens

## Overview

Daily Task Manager is a simple task management application designed to help senior citizens keep track of medications, doctors' appointments, and other important events. The application provides a user-friendly interface for managing events and medications efficiently.

## Key Features

1. **Calendar:**
   - Add, view, and edit events on a basic calendar.
   - Each event includes a title, date, time, and an optional description.
   - Display upcoming events on the main screen.

2. **Pill Schedule:**
   - Add medications to a daily pill schedule.
   - Each medication includes a name, dosage, frequency, and optional notes.
   - Notifications for pill reminders based on the specified schedule.
   - Display upcoming medication doses on the main screen.

3. **User Interface:**
   - Simple graphical interface for the calendar and pill schedule.
   - Tabs or sections for Calendar and Pill Schedule.
   - Intuitive forms for adding and editing events and medications.
   - Visual cues for upcoming events and medications on the main screen.

4. **Data Storage:**
   - Save user data to ensure persistence between sessions.
   - Uses SQLite for simple local database storage.

5. **Testing:**
   - Basic testing to ensure core functionalities work as expected.
   - Test scenarios include adding events, medications, and receiving reminders.

6. **Documentation:**
   - Clear documentation for users on how to use the calendar and pill schedule.
   - Document any configuration needed for the project.

## Installation

1. Clone the repository:

   bash 
   git clone https://github.com/TheQueenOfMean/College_Projects.git
   
   
Install dependencies:

bash
pip install -r requirements.txt
Run the application:

bash
python daily_task_manager.py


Dependencies:
- tkinter (GUI)
- SQLite (Data storage)
- plyer (Notifications)

##Challenges and Solutions##


    1. Implementing Calendar Functionality:

        Challenge: Creating a functional calendar system might be new and require careful planning.
        Solution: Break down the calendar feature into smaller tasks. Start by designing a simple event structure, then work on displaying events on a calendar. Utilize online resources and documentation for guidance.

    2. Managing Pill Schedule:

        Challenge: Designing and implementing a pill schedule with notifications may pose a challenge.
        Solution: Begin with a basic structure for medication entries. Explore libraries or modules that can help with notifications in Python. Test the schedule functionality thoroughly to ensure timely reminders.

    3. Creating a Simple User Interface:

        Challenge: Designing an easy-to-use interface might be challenging without prior experience.
        Solution: Keep the interface clean and minimal. Utilize simple forms for adding and editing events and medications. Seek inspiration from user-friendly applications and consider peer feedback if possible.

    4. Data Storage:

        Challenge: Saving user data between sessions can be a new concept to grasp.
        Solution: Explore simple local databases like SQLite or file storage methods. Break down the process of saving and retrieving data step by step. Use online tutorials or documentation for guidance.

    5. Testing Functionality:

        Challenge: Ensuring that the core features work without issues may require thorough testing.
        Solution: Develop a testing plan that covers adding events, medications, and receiving reminders. Utilize simple debugging techniques and online forums for guidance if issues arise.

    6. Documentation:

        Challenge: Creating clear documentation may be challenging without a specific structure in mind.
        Solution: Outline the usage steps for the personal assistant. Clearly explain how to add events, medications, and navigate the interface.

Madeleine Gonzalez

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

