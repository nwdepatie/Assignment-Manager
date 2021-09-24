This app uses a table that exists within an already established SQL database. safeguardexample.py is imported into the scripts that interface with the table and holds all the credentials to the SQL database.

First, the user must initialize the table for use by running database_interface.assignmentdatabase.initialize_table, then homework_app.py can be run to launch the app.

The app consists of a button to retrieve all the assignments in the database which mergesorts the assignments by proximity to deadline and priority and displays them in a list format. The assignments can be entered into the 3 line edit boxes, and can then be logged into the database by clicking the button.

This app is very, very early in development and will be outfitted with more later on

TODO:
1) Log assignments into Google Calendar using API
2) Attach custom skins to QT widgets
3) Make TODO column separate from assignments for ongoing projects
