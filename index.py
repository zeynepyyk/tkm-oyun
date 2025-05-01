import tkinter as tk
from tkinter import messagebox
import random

# Ana pencere
window = tk.Tk()
window.title("Taş Kağıt Makas")
window.geometry("500x600")
window.configure(bg="#f8c8dc")  # pudra pembe

# Global değişkenler
player_score = 0
computer_score = 0
rounds_left = 0

# Oyun başlangıç ekranı
def start_game():
    global rounds_left, player_score, computer_score

    name = name_entry.get()
    try:
        rounds_left = int(rounds_entry.get())
    except ValueError:
        messagebox.showwarning("Hata", "Tur sayısı geçerli bir sayı olmalıdır!")
        return

    if not name or rounds_left <= 0:
        messagebox.showwarning("Hata", "Lütfen adınızı ve tur sayısını girin!")
        return

    player_score = 0
    computer_score = 0
    update_scores()
    game_frame.pack(pady=20)

# Seçim işlemi
def play(player_choice):
    global player_score, computer_score, rounds_left

    choices = ['taş', 'kağıt', 'makas']
    computer_choice = random.choice(choices)

    player_choice_label.config(text=player_choice)
    computer_choice_label.config(text=computer_choice)

    if player_choice == computer_choice:
        pass  # Beraberlik
    elif (player_choice == 'taş' and computer_choice == 'makas') or \
         (player_choice == 'kağıt' and computer_choice == 'taş') or \
         (player_choice == 'makas' and computer_choice == 'kağıt'):
        player_score += 1
    else:
        computer_score += 1

    rounds_left -= 1
    update_scores()

    if rounds_left == 0:
        result = f"Oyun Bitti!\nSkor: Oyuncu {player_score} - Bilgisayar {computer_score}"
        messagebox.showinfo("Sonuç", result)
        game_frame.pack_forget()

# Skorları güncelle
def update_scores():
    player_score_label.config(text=str(player_score))
    computer_score_label.config(text=str(computer_score))
    rounds_label.config(text=str(rounds_left))

# Başlangıç ekranı
title = tk.Label(window, text="Taş Kağıt Makas", font=("Comic Sans MS", 24), bg="#f8c8dc")
title.pack(pady=20)

name_entry = tk.Entry(window, font=("Arial", 14))
name_entry.pack(pady=5)
name_entry.insert(0, "Adınız")

rounds_entry = tk.Entry(window, font=("Arial", 14))
rounds_entry.pack(pady=5)
rounds_entry.insert(0, "Tur Sayısı")

start_button = tk.Button(window, text="Oyna", command=start_game, bg="red", fg="black", font=("Arial", 14))
start_button.pack(pady=10)

# Oyun ekranı
game_frame = tk.Frame(window, bg="#f8c8dc")

button_frame = tk.Frame(game_frame, bg="#f8c8dc")
button_frame.pack(pady=10)

for choice in ['taş', 'kağıt', 'makas']:
    btn = tk.Button(button_frame, text=choice.capitalize(), font=("Arial", 14),
                    bg="red", fg="black", width=10, command=lambda c=choice: play(c))
    btn.pack(side="left", padx=5)

result_frame = tk.Frame(game_frame, bg="#f8c8dc")
result_frame.pack(pady=10)

tk.Label(result_frame, text="Sen Seçtin:", font=("Arial", 12), bg="#f8c8dc").grid(row=0, column=0)
player_choice_label = tk.Label(result_frame, text="-", font=("Arial", 12), bg="#f8c8dc")
player_choice_label.grid(row=0, column=1)

tk.Label(result_frame, text="Bilgisayar Seçti:", font=("Arial", 12), bg="#f8c8dc").grid(row=1, column=0)
computer_choice_label = tk.Label(result_frame, text="-", font=("Arial", 12), bg="#f8c8dc")
computer_choice_label.grid(row=1, column=1)

score_frame = tk.Frame(game_frame, bg="white", bd=2, relief="solid")
score_frame.pack(pady=20)

tk.Label(score_frame, text="Oyuncu", font=("Arial", 12), width=10).grid(row=0, column=0)
tk.Label(score_frame, text="Bilgisayar", font=("Arial", 12), width=10).grid(row=0, column=1)
tk.Label(score_frame, text="Kalan Tur", font=("Arial", 12), width=10).grid(row=0, column=2)

player_score_label = tk.Label(score_frame, text="0", font=("Arial", 12))
player_score_label.grid(row=1, column=0)
computer_score_label = tk.Label(score_frame, text="0", font=("Arial", 12))
computer_score_label.grid(row=1, column=1)
rounds_label = tk.Label(score_frame, text="0", font=("Arial", 12))
rounds_label.grid(row=1, column=2)

# Ana döngü
window.mainloop()
