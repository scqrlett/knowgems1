import tkinter as tk
# Create a global variable to store the reference to the third page
third_page = None
def open_second_page():
   second_page = tk.Toplevel(root)
   second_page.title("FlashGo - Year 9 Flash Cards")
   second_page.geometry("2100x1200")
   english_button = tk.Button(second_page, text="English", bg="lightcoral", font=("Arial", 50))
   english_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
   math_button = tk.Button(second_page, text="Mathematics", bg="lightblue", font=("Arial", 50))
   math_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
   science_button = tk.Button(second_page, text="Science", bg="lightgreen", font=("Arial", 50))
   science_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
   english_button.config(command=open_third_page)
   second_page.grid_rowconfigure(0, weight=1)
   second_page.grid_rowconfigure(1, weight=1)
   second_page.grid_rowconfigure(2, weight=1)
def open_third_page():
   global third_page  # Declare the third_page variable as global
   third_page = tk.Toplevel(root)
   third_page.title("English - FlashGo")
   third_page.geometry("2100x1100")
   events_button = tk.Button(third_page, text="Events", bg="#FFFFE0", font=("Arial", 50))
   events_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
   events_button.config(command=open_fourth_page)
   topics_website_button = tk.Button(third_page, text="Topics & Website", bg="#FFFFE0", font=("Arial", 50))
   topics_website_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
   topics_website_button.config(command=open_fifth_page)
   staff_button = tk.Button(third_page, text="Staff", bg="#FFFFE0", font=("Arial", 50))
   staff_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
   staff_button.config(command=open_sixth_page)
   back_button = tk.Button(third_page, text="Back", font=("Arial", 20), command=third_page.destroy)
   back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
def open_fourth_page():
   fourth_page = tk.Toplevel(root)
   fourth_page.title("Events - FlashGo")
   fourth_page.geometry("2100x1200")
   fourth_page.configure(bg="lightcoral")
   fourth_page.attributes('-alpha', 1)
   events_info = """EVENTS:
   - World book day
   - Oxford Story Writing Competition
   - Poetry writing competition
   - Poetry recitation competition
   - Read aloud day
   - Letter writing competition
   - Summer Reading challenge"""
   events_label = tk.Label(fourth_page, text=events_info, font=("Arial", 50), justify=tk.LEFT)
   events_label.pack(pady=10, padx=10)
   back_button = tk.Button(fourth_page, text="Back", font=("Arial", 20), command=fourth_page.destroy)
   back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
def open_fifth_page():
   fifth_page = tk.Toplevel(root)
   fifth_page.title("Topics & Websites - FlashGo")
   fifth_page.geometry("2100x1200")
   fifth_page.configure(bg="lightcoral")
   fifth_page.attributes('-alpha', 1)
   websites_info = """WEBSITES:
   • Kerboodle
   • Achieve300
   • Activelearn
   • Myon
   • Pearson
   • Scribo"""
   curriculum_info = """CURRICULUM STANDARD:
   • Summarising
   • Structuring a text
   • Choosing the right words
   • Building a paragraph of advice
   • Comparing texts
   • Building a response"""
   websites_label = tk.Label(fifth_page, text=websites_info, font=("Arial", 50), justify=tk.LEFT)
   websites_label.pack(pady=10, padx=10, side=tk.LEFT)
   curriculum_label = tk.Label(fifth_page, text=curriculum_info, font=("Arial", 50), justify=tk.LEFT)
   curriculum_label.pack(pady=10, padx=10, side=tk.RIGHT)
   back_button = tk.Button(fifth_page, text="Back", font=("Arial", 30), command=fifth_page.destroy)
   back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
def open_sixth_page():
   sixth_page = tk.Toplevel(root)
   sixth_page.title("Staff - FlashGo")
   sixth_page.geometry("2100x1200")
   sixth_page.configure(bg="lightcoral")
   sixth_page.attributes('-alpha', 1)
   staff_info = """STAFF:
   Ms. Sonia (Head of English)
   Ms. Udya
   EMAILS FOR STAFF:
   sonia.c_wsa@gemsedu.com
   udya.s_wsa@gemsedu.com"""
   staff_label = tk.Label(sixth_page, text=staff_info, font=("Arial", 50), justify=tk.LEFT)
   staff_label.pack(pady=10, padx=10)
   back_button = tk.Button(sixth_page, text="Back", font=("Arial", 20), command=sixth_page.destroy)
   back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
root = tk.Tk()
root.title("FlashGo")
root.geometry("2100x1200")
root.configure(bg="#E6E6FA")
title_label = tk.Label(root, text="KnowGems", font=("Arial", 200))
title_label.pack(pady=50)
flashcards_button = tk.Button(root, text="Secodary information", font=("Arial", 90), command=open_second_page)
flashcards_button.pack(pady=50)
root.mainloop()




