Team Balance Application

This Python application helps to balance teams based on players' MMR (Matchmaking Rating). It allows you to input the names and MMR values of players, and automatically creates two balanced teams with the smallest possible difference in average MMR.

Features:
Team Balancing: The application uses the combinations function to generate all possible combinations of players and calculates the balance by minimizing the difference in the average MMR between two teams.

Graphical Interface: Built using Tkinter, the app features a user-friendly GUI where you can input player names and MMRs. The teams are displayed in a list, and you can manually move players between teams.

Visualization: After balancing the teams, the app displays a histogram of MMR distribution between the two teams using Matplotlib, giving a visual representation of the balance.

Dynamic Player Management: Users can adjust the number of players, and the list fields are dynamically updated based on the input.

Real-Time Updates: The teams and their MMRs are updated in real-time as players are moved between teams.

How it Works:
Enter the number of players and their respective names and MMR values.

Click the "Balance Teams" button, and the app will find the best balance by minimizing the MMR difference.

The teams are displayed in two lists, and you can move players between them manually.

The average MMR for each team is displayed along with a histogram showing the MMR distribution.

Requirements:
Tkinter (for GUI)

Matplotlib (for displaying MMR distribution histogram)

Pillow (for working with images)

Dependencies:
matplotlib>=3.0.0

Pillow>=8.0.0

This project is ideal for balancing teams in games or other competitive scenarios based on rating systems.
