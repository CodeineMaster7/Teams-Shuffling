import tkinter as tk
from tkinter import Canvas, Button, Label, Listbox
from itertools import combinations
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

def balance_teams(players):
    best_combination = None
    smallest_avg_diff = float('inf')
    num_players = len(players)
    
    num_team1 = num_players // 2
    num_team2 = num_players - num_team1

    for team1 in combinations(players, num_team1):
        team2 = [player for player in players if player not in team1]
        
        avg_team1 = sum(player['mmr'] for player in team1) / num_team1
        avg_team2 = sum(player['mmr'] for player in team2) / num_team2
        
        avg_diff = abs(avg_team1 - avg_team2)

        if avg_diff < smallest_avg_diff:
            smallest_avg_diff = avg_diff
            best_combination = (team1, team2)
    
    return best_combination

def update_result_label():
    avg_team1 = sum(player['mmr'] for player in team1) / len(team1)
    avg_team2 = sum(player['mmr'] for player in team2) / len(team2)

    result_text = f"Team 1 (Average Rating: {avg_team1:.2f}):\n"
    result_text += "\n".join([f"{p['name']} (MMR: {p['mmr']})" for p in team1])
    
    result_text += f"\n\nTeam 2 (Average Rating: {avg_team2:.2f}):\n"
    result_text += "\n".join([f"{p['name']} (MMR: {p['mmr']})" for p in team2])

    result_label.config(text=result_text)

def calculate_balance():
    global team1, team2
    players = []
    for i in range(len(entry_names)):
        try:
            name = entry_names[i].get()
            mmr = int(entry_mmrs[i].get())
            players.append({'name': name, 'mmr': mmr})
        except:
            pass
    print(players)

    if len(players) < 2:
        result_label.config(text="Need at least 2 players to balance teams.")
        return

    team1, team2 = map(list, balance_teams(players))
    
    update_teams()
    show_mmr_distribution(team1, team2)  # Отображаем диаграмму после балансировки

def move_to_team1():
    if team2_listbox.curselection():
        index = team2_listbox.curselection()[0]
        player = team2.pop(index)
        team1.append(player)
        update_teams()

def move_to_team2():
    if team1_listbox.curselection():
        index = team1_listbox.curselection()[0]
        player = team1.pop(index)
        team2.append(player)
        update_teams()

def update_teams():
    team1_listbox.delete(0, tk.END)
    team2_listbox.delete(0, tk.END)
    
    for player in team1:
        team1_listbox.insert(tk.END, f"{player['name']} (MMR: {player['mmr']})")
    
    for player in team2:
        team2_listbox.insert(tk.END, f"{player['name']} (MMR: {player['mmr']})")
    
    update_result_label()

def show_mmr_distribution(team1, team2):
    team1_mmr = [player['mmr'] for player in team1]
    team2_mmr = [player['mmr'] for player in team2]
    
    fig, ax = plt.subplots()
    ax.hist([team1_mmr, team2_mmr], bins=5, label=['Team 1', 'Team 2'], color=['blue', 'red'], alpha=0.7)
    ax.set_title('MMR Distribution Between Teams')
    ax.set_xlabel('MMR')
    ax.set_ylabel('Number of Players')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=4, rowspan=15, padx=20, pady=10)

def update_player_fields():
    num_players = int(num_players_entry.get())
    
    for entry in entry_names + entry_mmrs:
        entry.grid_forget()
    
    entry_names.clear()
    entry_mmrs.clear()

    for i in range(num_players):
        tk.Label(root, text=f"Player {i + 1}:", bg=bg_color, fg=fg_color).grid(row=i+1, column=0, padx=10, pady=5, sticky=tk.W)
        name_entry = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color)
        name_entry.grid(row=i+1, column=1, padx=10, pady=5)
        entry_names.append(name_entry)
        
        tk.Label(root, text=f"MMR:", bg=bg_color, fg=fg_color).grid(row=i+1, column=2, padx=10, pady=5, sticky=tk.W)
        mmr_entry = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color)
        mmr_entry.grid(row=i+1, column=3, padx=10, pady=5)
        entry_mmrs.append(mmr_entry)

root = tk.Tk()
root.title("Balance Teams by CodeineMaster7")

bg_color = "#2b2b2b"
fg_color = "#e0e0e0"
button_color = "#4a90e2"
entry_bg_color = "#1f1f1f"
entry_fg_color = "#ffffff"
balance_button_color = "#f92c3f"

root.configure(bg=bg_color)

entry_names = []
entry_mmrs = []

tk.Label(root, text="Number of Players (1-10):", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=(10, 5))
num_players_entry = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color)
num_players_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

update_button = Button(root, text="Update Players", command=update_player_fields, bg=button_color, fg=fg_color)
update_button.grid(row=0, column=2, padx=10, pady=5)

balance_button = Button(root, text="Balance Teams", command=calculate_balance, bg=balance_button_color, fg=fg_color)
balance_button.grid(row=11, column=0, columnspan=4, pady=10)

team1_listbox = Listbox(root, bg=entry_bg_color, fg=entry_fg_color)
team1_listbox.grid(row=12, column=0, padx=10, pady=5)

team2_listbox = Listbox(root, bg=entry_bg_color, fg=entry_fg_color)
team2_listbox.grid(row=12, column=2, padx=10, pady=5)

move_to_team2_button = Button(root, text="→", command=move_to_team2, bg=button_color, fg=fg_color)
move_to_team2_button.grid(row=12, column=1, padx=5, pady=5)

move_to_team1_button = Button(root, text="←", command=move_to_team1, bg=button_color, fg=fg_color)
move_to_team1_button.grid(row=13, column=1, padx=5, pady=5)

result_label = Label(root, text="", justify=tk.LEFT, bg=bg_color, fg=fg_color, font=("Arial", 12))
result_label.grid(row=14, column=0, columnspan=4, padx=10, pady=10)

root.mainloop() 