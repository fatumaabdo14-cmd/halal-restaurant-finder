"""
╔════════════════════════════════════════════════════════════╗
║         HALAL RESTAURANT FINDER - CLI APPLICATION          ║
║                   Portfolio Project                        ║
║                  By: Fatuma | Cloud Engineer               ║
╚════════════════════════════════════════════════════════════╝

PYTHON FUNDAMENTALS DEMONSTRATED:
✅ Variables - Storing user input, search queries, results
✅ Strings - Restaurant names, user prompts, formatted output
✅ Lists - Collection of all restaurants
✅ Dictionaries - Each restaurant's data (name, cuisine, rating, location, price)
✅ Functions - search_by_name(), filter_by_cuisine(), display_restaurants(), etc.
✅ Loops (for) - Iterating through restaurants to search/filter
✅ Loops (while) - Main game loop keeps running until user exits
✅ Control Structures (if/elif/else) - Menu selection & validation
✅ Comments - Documented every section and function
✅ File Imports - Import restaurants data from separate file

HOW TO RUN:
    python3 finder.py

FEATURES:
    1. Search restaurants by name
    2. Filter by cuisine type
    3. View all restaurants
    4. Sort by rating (highest first)
    5. Exit

USAGE EXAMPLE:
    Search: "baba" → Shows "Baba Kebab"
    Filter: "Italian" → Shows all Italian restaurants
    Sort: Shows highest rated restaurants first
"""

from resturants import restaurants


def display_menu():
    print("\n" + "=" * 50)
    print("🍽️ RESTAURANT FINDER 🍽️")
    print("=" * 50)
    print("1. Search by restaurant name")
    print("2. Filter by cuisine")
    print("3. View all restaurants")
    print("4. Sort by rating")
    print("5. Exit")
    print("=" * 50)


def search_by_name(search_term):
    return [restaurant for restaurant in restaurants
            if search_term.lower() in restaurant["name"].lower()]


def filter_by_cuisine(cuisine_type):
    return [restaurant for restaurant in restaurants
            if restaurant["cuisine"].lower() == cuisine_type.lower()]


def display_restaurants(restaurant_list):
    if not restaurant_list:
        print("\n❌ No restaurants found!")
        return

    print(f"\n✅ Found {len(restaurant_list)} restaurant(s):")
    for restaurant in restaurant_list:
        print(f"  📍 {restaurant['name']}")
        print(f"     Cuisine: {restaurant['cuisine']}")
        print(f"     Rating: ⭐ {restaurant['rating']}")
        print(f"     Location: {restaurant['location']}")
        print(f"     Price: {restaurant['price_range']}\n")


def sort_by_rating():
    return sorted(restaurants, key=lambda restaurant: restaurant["rating"], reverse=True)


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_restaurants(search_by_name(input("Enter restaurant name to search: ")))
        elif choice == "2":
            display_restaurants(filter_by_cuisine(input("Enter cuisine: ")))
        elif choice == "3":
            display_restaurants(restaurants)
        elif choice == "4":
            display_restaurants(sort_by_rating())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
                           
        
