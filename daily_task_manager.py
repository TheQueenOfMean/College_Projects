import tkinter as tk
from tkinter import ttk
import sqlite3
from plyer import notification

class DailyTaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Task Manager")

        # Initialize SQLite database
        self.conn = sqlite3.connect('task_manager.db')
        self.create_tables()

        # Calendar Tab
        self.calendar_tab = ttk.Frame(self.root)
        self.calendar_tab.pack()
        self.initialize_calendar_tab()

        # Pill Schedule Tab
        self.pill_schedule_tab = ttk.Frame(self.root)
        self.pill_schedule_tab.pack()
        self.initialize_pill_schedule_tab()

    def create_tables(self):
        # Create tables if not exist
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    date TEXT,
                    time TEXT,
                    description TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS medications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    dosage TEXT,
                    frequency TEXT,
                    notes TEXT
                )
            ''')

    def initialize_calendar_tab(self):
        # Calendar UI components
        ttk.Label(self.calendar_tab, text="Event Title:").grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = ttk.Entry(self.calendar_tab)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.calendar_tab, text="Date:").grid(row=1, column=0, padx=10, pady=5)
        self.date_entry = ttk.Entry(self.calendar_tab)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.calendar_tab, text="Time:").grid(row=2, column=0, padx=10, pady=5)
        self.time_entry = ttk.Entry(self.calendar_tab)
        self.time_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.calendar_tab, text="Description:").grid(row=3, column=0, padx=10, pady=5)
        self.description_entry = ttk.Entry(self.calendar_tab)
        self.description_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(self.calendar_tab, text="Add Event", command=self.add_event_button).grid(row=4, column=0, columnspan=2, pady=10)

        # Display upcoming events
        ttk.Label(self.calendar_tab, text="Upcoming Events").grid(row=5, column=0, padx=10, pady=5, columnspan=2)
        self.upcoming_events_label = ttk.Label(self.calendar_tab, text="")
        self.upcoming_events_label.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

        self.display_upcoming_events()

    def initialize_pill_schedule_tab(self):
        # Pill Schedule UI components
        ttk.Label(self.pill_schedule_tab, text="Medication Name:").grid(row=0, column=0, padx=10, pady=5)
        self.med_name_entry = ttk.Entry(self.pill_schedule_tab)
        self.med_name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.pill_schedule_tab, text="Dosage:").grid(row=1, column=0, padx=10, pady=5)
        self.dosage_entry = ttk.Entry(self.pill_schedule_tab)
        self.dosage_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.pill_schedule_tab, text="Frequency:").grid(row=2, column=0, padx=10, pady=5)
        self.frequency_entry = ttk.Entry(self.pill_schedule_tab)
        self.frequency_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.pill_schedule_tab, text="Notes:").grid(row=3, column=0, padx=10, pady=5)
        self.notes_entry = ttk.Entry(self.pill_schedule_tab)
        self.notes_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(self.pill_schedule_tab, text="Add Medication", command=self.add_medication_button).grid(row=4, column=0, columnspan=2, pady=10)

        # Display upcoming medications
        ttk.Label(self.pill_schedule_tab, text="Upcoming Medications").grid(row=5, column=0, padx=10, pady=5, columnspan=2)
        self.upcoming_medications_label = ttk.Label(self.pill_schedule_tab, text="")
        self.upcoming_medications_label.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

        self.display_upcoming_medications()

    def add_event_button(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_entry.get()

        if title and date and time:
            self.add_event(title, date, time, description)
            self.display_upcoming_events()
            self.title_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

    def add_event(self, title, date, time, description):
        # Add event to the database
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO events (title, date, time, description)
                VALUES (?, ?, ?, ?)
            ''', (title, date, time, description))

    def display_upcoming_events(self):
        # Retrieve upcoming events from the database
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT title, date, time FROM events
                ORDER BY date, time
            ''')
            upcoming_events = cursor.fetchall()

        # Display upcoming events in the label
        if upcoming_events:
            events_text = "\n".join(f"{event[0]} - {event[1]} at {event[2]}" for event in upcoming_events)
            self.upcoming_events_label.config(text=events_text)
        else:
            self.upcoming_events_label.config(text="No upcoming events.")

    def add_medication_button(self):
        med_name = self.med_name_entry.get()
        dosage = self.dosage_entry.get()
        frequency = self.frequency_entry.get()
        notes = self.notes_entry.get()

        if med_name and dosage and frequency:
            self.add_medication(med_name, dosage, frequency, notes)
            self.display_upcoming_medications()
            self.med_name_entry.delete(0, tk.END)
            self.dosage_entry.delete(0, tk.END)
            self.frequency_entry.delete(0, tk.END)
            self.notes_entry.delete(0, tk.END)

    def add_medication(self, name, dosage, frequency, notes):
        # Add medication to the database
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO medications (name, dosage, frequency, notes)
                VALUES (?, ?, ?, ?)
            ''', (name, dosage, frequency, notes))

    def display_upcoming_medications(self):
    # Retrieve upcoming medications from the database
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT name, dosage, frequency FROM medications
                ORDER BY frequency
            ''')
            upcoming_medications = cursor.fetchall()

    # Display upcoming medications in the label
        if upcoming_medications:
            medications_text = "\n".join(f"{medication[0]} - {medication[1]} ({medication[2]})" for medication in upcoming_medications)
            self.upcoming_medications_label.config(text=medications_text)
        else:
            self.upcoming_medications_label.config(text="No upcoming medications.")



if __name__ == "__main__":
    root = tk.Tk()
    app = DailyTaskManager(root)
    root.mainloop()
