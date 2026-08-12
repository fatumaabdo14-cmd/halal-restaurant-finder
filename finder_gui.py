# Restaurant Finder - GUI Version
import tkinter as tk
from tkinter import ttk, messagebox
from resturants import restaurants

# This is where we'll build the GUI

# --- Helper functions ---
def search_restaurants():
	query = search_entry.get().strip().lower()
	results_text.delete("1.0", tk.END)
	if not query:
		results_text.insert(tk.END, "Please enter a search term.\n")
		return
	found = [r for r in restaurants if query in (r.get('name','').lower() if isinstance(r, dict) else str(r).lower())]
	if not found:
		results_text.insert(tk.END, "No restaurants found.\n")
		return
	for r in found:
		name = r.get('name', str(r)) if isinstance(r, dict) else str(r)
		cuisine = r.get('cuisine','N/A') if isinstance(r, dict) else 'N/A'
		rating = r.get('rating','N/A') if isinstance(r, dict) else 'N/A'
		results_text.insert(tk.END, f"{name} | Cuisine: {cuisine} | Rating: {rating}\n")

def filter_restaurants():
	cuisine_q = filter_entry.get().strip().lower()
	results_text.delete("1.0", tk.END)
	if not cuisine_q:
		results_text.insert(tk.END, "Please enter a cuisine to filter.\n")
		return
	found = [r for r in restaurants if cuisine_q in (r.get('cuisine','').lower() if isinstance(r, dict) else '')]
	if not found:
		results_text.insert(tk.END, "No restaurants match that cuisine.\n")
		return
	for r in found:
		name = r.get('name', str(r)) if isinstance(r, dict) else str(r)
		rating = r.get('rating','N/A') if isinstance(r, dict) else 'N/A'
		results_text.insert(tk.END, f"{name} | Cuisine: {cuisine_q} | Rating: {rating}\n")

def view_all():
	results_text.delete("1.0", tk.END)
	if not restaurants:
		results_text.insert(tk.END, "No restaurants available.\n")
		return
	for r in restaurants:
		name = r.get('name', str(r)) if isinstance(r, dict) else str(r)
		cuisine = r.get('cuisine','N/A') if isinstance(r, dict) else 'N/A'
		rating = r.get('rating','N/A') if isinstance(r, dict) else 'N/A'
		results_text.insert(tk.END, f"{name} | Cuisine: {cuisine} | Rating: {rating}\n")

def sort_restaurants():
	results_text.delete("1.0", tk.END)
	try:
		sorted_list = sorted(restaurants, key=lambda r: float(r.get('rating', 0)) if isinstance(r, dict) else 0, reverse=True)
	except Exception:
		results_text.insert(tk.END, "Could not sort restaurants.\n")
		return
	for r in sorted_list:
		name = r.get('name', str(r)) if isinstance(r, dict) else str(r)
		cuisine = r.get('cuisine','N/A') if isinstance(r, dict) else 'N/A'
		rating = r.get('rating','N/A') if isinstance(r, dict) else 'N/A'
		results_text.insert(tk.END, f"{name} | Cuisine: {cuisine} | Rating: {rating}\n")

def clear_results():
	results_text.delete("1.0", tk.END)
	search_entry.delete(0, tk.END)
	filter_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("🍽️ Restaurant Finder")
root.geometry("600x700")

# Title Label
title = tk.Label(root, text="🍽️ RESTAURANT FINDER 🍽️", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Search Section
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search Restaurant:", font=("Arial", 10)).pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame, width=20)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="🔍 Search", command=lambda: search_restaurants()).pack(side=tk.LEFT)

# Filter Section
filter_frame = tk.Frame(root)
filter_frame.pack(pady=10)

tk.Label(filter_frame, text="Filter by Cuisine:", font=("Arial", 10)).pack(side=tk.LEFT)
filter_entry = tk.Entry(filter_frame, width=20)
filter_entry.pack(side=tk.LEFT, padx=5)
tk.Button(filter_frame, text="🍜 Filter", command=lambda: filter_restaurants()).pack(side=tk.LEFT)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="📋 View All", command=lambda: view_all()).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="⭐ Sort by Rating", command=lambda: sort_restaurants()).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="❌ Clear", command=lambda: clear_results()).pack(side=tk.LEFT, padx=5)

# Results Display (Text Area)
results_text = tk.Text(root, height=15, width=70)
results_text.pack(pady=10)

scrollbar = tk.Scrollbar(results_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_text.config(yscrollcommand=scrollbar.set)

# --- Helper Functions ---

def search_restaurants():
    query = search_entry.get().strip().lower()
    results_text.delete("1.0", tk.END)
    
    if not query:
        results_text.insert(tk.END, "Please enter a search term!")
        return
    
    found = [r for r in restaurants if query in r["name"].lower()]
    
    if not found:
        results_text.insert(tk.END, "❌ No restaurants found.")
        return
    
    results_text.insert(tk.END, f"✅ Found {len(found)} restaurant(s):\n\n")
    for r in found:
        results_text.insert(tk.END, f"📍 {r['name']}\nCuisine: {r['cuisine']}\nRating: ⭐ {r['rating']}\nLocation: {r['location']}\nPrice: {r['price_range']}\n\n")

def filter_restaurants():
    cuisine = filter_entry.get().strip().lower()
    results_text.delete("1.0", tk.END)
    
    if not cuisine:
        results_text.insert(tk.END, "Please enter a cuisine type!")
        return
    
    found = [r for r in restaurants if r["cuisine"].lower() == cuisine]
    
    if not found:
        results_text.insert(tk.END, "❌ No restaurants found with that cuisine.")
        return
    
    results_text.insert(tk.END, f"✅ Found {len(found)} restaurant(s):\n\n")
    for r in found:
        results_text.insert(tk.END, f"📍 {r['name']}\nCuisine: {r['cuisine']}\nRating: ⭐ {r['rating']}\nLocation: {r['location']}\nPrice: {r['price_range']}\n\n")

def view_all():
    results_text.delete("1.0", tk.END)
    results_text.insert(tk.END, f"📋 ALL RESTAURANTS ({len(restaurants)}):\n\n")
    for r in restaurants:
        results_text.insert(tk.END, f"📍 {r['name']}\nCuisine: {r['cuisine']}\nRating: ⭐ {r['rating']}\nLocation: {r['location']}\nPrice: {r['price_range']}\n\n")

def sort_restaurants():
    sorted_list = sorted(restaurants, key=lambda r: r["rating"], reverse=True)
    results_text.delete("1.0", tk.END)
    results_text.insert(tk.END, "⭐ SORTED BY RATING (Highest First):\n\n")
    for r in sorted_list:
        results_text.insert(tk.END, f"📍 {r['name']}\nCuisine: {r['cuisine']}\nRating: ⭐ {r['rating']}\nLocation: {r['location']}\nPrice: {r['price_range']}\n\n")

def clear_results():
    results_text.delete("1.0", tk.END)
    search_entry.delete(0, tk.END)
    filter_entry.delete(0, tk.END)

# Start the app
root.mainloop()