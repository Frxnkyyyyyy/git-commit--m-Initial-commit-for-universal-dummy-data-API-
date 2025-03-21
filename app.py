from flask import Flask, jsonify

app = Flask(__name__)

# 🌍 Universal Dummy Data API
data = {
    "eclothes": [
        {"id": 1, "name": "T-Shirt", "price": 499},
        {"id": 2, "name": "Hoodie", "price": 999},
        {"id": 3, "name": "Jeans", "price": 1200},
        {"id": 4, "name": "Jacket", "price": 1999},
        {"id": 5, "name": "Sweatshirt", "price": 799},
        {"id": 6, "name": "Kurta", "price": 650},
        {"id": 7, "name": "Blazer", "price": 2200},
        {"id": 8, "name": "Shorts", "price": 400},
        {"id": 9, "name": "Shirt", "price": 750},
        {"id": 10, "name": "Track Pants", "price": 699}
    ],
    "ebooks": [
        {"id": 1, "title": "Python 101", "author": "Franky", "price": 299},
        {"id": 2, "title": "Flask for Beginners", "author": "OpenAI", "price": 399},
        {"id": 3, "title": "Learn React", "author": "Meta", "price": 349},
        {"id": 4, "title": "Data Science Crash Course", "author": "Franky", "price": 499},
        {"id": 5, "title": "The AI Handbook", "author": "Franky", "price": 599},
        {"id": 6, "title": "Machine Learning in Practice", "author": "Google", "price": 549},
        {"id": 7, "title": "Django Deep Dive", "author": "Django Team", "price": 429},
        {"id": 8, "title": "Frontend Recipes", "author": "Franky", "price": 279},
        {"id": 9, "title": "Next.js Guide", "author": "Vercel", "price": 399},
        {"id": 10, "title": "SQL Mastery", "author": "DataCamp", "price": 299}
    ],
    "mobiles": [
        {"id": 1, "model": "iPhone 14", "price": 79999},
        {"id": 2, "model": "Samsung S23", "price": 69999},
        {"id": 3, "model": "OnePlus 11", "price": 57999},
        {"id": 4, "model": "Xiaomi 13 Pro", "price": 52999},
        {"id": 5, "model": "Realme GT Neo 3", "price": 36999},
        {"id": 6, "model": "Pixel 7a", "price": 45999},
        {"id": 7, "model": "Vivo V27", "price": 30999},
        {"id": 8, "model": "Moto Edge 30", "price": 27999},
        {"id": 9, "model": "iQOO Z7", "price": 18999},
        {"id": 10, "model": "Asus ROG Phone 6", "price": 71999}
    ],
    "resumes": [
        {"id": 1, "name": "Franky", "position": "AI Engineer", "experience": "2 years"},
        {"id": 2, "name": "Riya", "position": "Frontend Dev", "experience": "1.5 years"},
        {"id": 3, "name": "Rahul", "position": "Backend Dev", "experience": "3 years"},
        {"id": 4, "name": "Sana", "position": "Data Scientist", "experience": "4 years"},
        {"id": 5, "name": "Karthik", "position": "ML Engineer", "experience": "2.5 years"},
        {"id": 6, "name": "Sneha", "position": "UI/UX Designer", "experience": "2 years"},
        {"id": 7, "name": "Aditya", "position": "DevOps Engineer", "experience": "3.5 years"},
        {"id": 8, "name": "Meera", "position": "Product Manager", "experience": "5 years"}
    ],

    "furniture": [
        {"id": 1, "item": "Sofa", "material": "Leather", "price": 15000},
        {"id": 2, "item": "Dining Table", "material": "Wood", "price": 12000},
        {"id": 3, "item": "Bed", "material": "Sheesham", "price": 20000},
        {"id": 4, "item": "Office Chair", "material": "Mesh", "price": 3500},
        {"id": 5, "item": "TV Stand", "material": "MDF", "price": 5000},
        {"id": 6, "item": "Bookshelf", "material": "Engineered Wood", "price": 4000},
        {"id": 7, "item": "Coffee Table", "material": "Glass", "price": 3000},
        {"id": 8, "item": "Recliner", "material": "Leatherette", "price": 18000}
    ],

    "fooddelivery": [
        {"id": 1, "dish": "Paneer Butter Masala", "restaurant": "Tandoori Nights", "price": 250},
        {"id": 2, "dish": "Burger", "restaurant": "Snack Shack", "price": 150},
        {"id": 3, "dish": "Pizza", "restaurant": "Domino's", "price": 300},
        {"id": 4, "dish": "Sushi", "restaurant": "Tokyo Treats", "price": 500},
        {"id": 5, "dish": "Chicken Biryani", "restaurant": "Biryani Blues", "price": 230},
        {"id": 6, "dish": "Dosa", "restaurant": "South Express", "price": 120},
        {"id": 7, "dish": "Fried Rice", "restaurant": "China Town", "price": 200},
        {"id": 8, "dish": "Pasta", "restaurant": "Italiano", "price": 350}
    ],

    "cars": [
        {"id": 1, "model": "BMW X5", "year": 2024, "price": 7500000},
        {"id": 2, "model": "Hyundai i20", "year": 2023, "price": 800000},
        {"id": 3, "model": "Tesla Model 3", "year": 2024, "price": 6000000},
        {"id": 4, "model": "Maruti Swift", "year": 2022, "price": 650000},
        {"id": 5, "model": "Audi A6", "year": 2023, "price": 5800000},
        {"id": 6, "model": "Kia Seltos", "year": 2023, "price": 1500000},
        {"id": 7, "model": "MG Hector", "year": 2024, "price": 1700000},
        {"id": 8, "model": "Mahindra Thar", "year": 2023, "price": 1800000}
    ],

    "fitness": [
        {"id": 1, "plan": "Weight Loss", "duration": "3 Months", "price": 2500},
        {"id": 2, "plan": "Muscle Gain", "duration": "6 Months", "price": 5000},
        {"id": 3, "plan": "Beginner Gym", "duration": "1 Month", "price": 1000},
        {"id": 4, "plan": "HIIT Plan", "duration": "2 Months", "price": 2200},
        {"id": 5, "plan": "CrossFit", "duration": "3 Months", "price": 3500},
        {"id": 6, "plan": "Cardio Boost", "duration": "1.5 Months", "price": 1800},
        {"id": 7, "plan": "Home Workout", "duration": "3 Months", "price": 1500},
        {"id": 8, "plan": "Yoga Plan", "duration": "2 Months", "price": 2000},
        {"id": 9, "plan": "Zumba", "duration": "1 Month", "price": 1200}
    ],

    "music": [
        {"id": 1, "title": "Blinding Lights", "artist": "The Weeknd", "price": 129},
        {"id": 2, "title": "Shape of You", "artist": "Ed Sheeran", "price": 149},
        {"id": 3, "title": "Believer", "artist": "Imagine Dragons", "price": 139},
        {"id": 4, "title": "Let Me Love You", "artist": "Justin Bieber", "price": 109},
        {"id": 5, "title": "Bad Guy", "artist": "Billie Eilish", "price": 129},
        {"id": 6, "title": "Perfect", "artist": "Ed Sheeran", "price": 149},
        {"id": 7, "title": "Senorita", "artist": "Shawn Mendes", "price": 139},
        {"id": 8, "title": "Rockstar", "artist": "Post Malone", "price": 119}
    ],

    "jobs": [
        {"id": 1, "title": "Backend Developer", "company": "Google", "salary": "12 LPA"},
        {"id": 2, "title": "AI Intern", "company": "OpenAI", "salary": "20K/month"},
        {"id": 3, "title": "Data Analyst", "company": "Amazon", "salary": "10 LPA"},
        {"id": 4, "title": "Frontend Dev", "company": "Meta", "salary": "11 LPA"},
        {"id": 5, "title": "Product Manager", "company": "Microsoft", "salary": "18 LPA"},
        {"id": 6, "title": "UI Designer", "company": "Zomato", "salary": "8 LPA"},
        {"id": 7, "title": "QA Tester", "company": "Flipkart", "salary": "7 LPA"},
        {"id": 8, "title": "Cloud Engineer", "company": "AWS", "salary": "14 LPA"}
    ],

    "flights": [
        {"id": 1, "from": "Mumbai", "to": "Delhi", "price": 4500},
        {"id": 2, "from": "Chennai", "to": "Bangalore", "price": 3000},
        {"id": 3, "from": "Hyderabad", "to": "Kolkata", "price": 5000},
        {"id": 4, "from": "Delhi", "to": "Goa", "price": 3200},
        {"id": 5, "from": "Pune", "to": "Jaipur", "price": 4100},
        {"id": 6, "from": "Mumbai", "to": "Dubai", "price": 15000},
        {"id": 7, "from": "Kolkata", "to": "Bali", "price": 22000},
        {"id": 8, "from": "Delhi", "to": "London", "price": 45000}
    ],

    "doctors": [
        {"id": 1, "name": "Dr. Mehta", "specialist": "Cardiologist", "available": "Mon-Fri"},
        {"id": 2, "name": "Dr. Arya", "specialist": "Dermatologist", "available": "Tue-Sat"},
        {"id": 3, "name": "Dr. Ramesh", "specialist": "ENT", "available": "Wed-Fri"},
        {"id": 4, "name": "Dr. Khanna", "specialist": "Pediatrician", "available": "Mon-Sat"},
        {"id": 5, "name": "Dr. Kapoor", "specialist": "Orthopedic", "available": "Tue-Thu"},
        {"id": 6, "name": "Dr. Shetty", "specialist": "Neurologist", "available": "Mon-Wed"},
        {"id": 7, "name": "Dr. Nair", "specialist": "Psychiatrist", "available": "Mon-Fri"},
        {"id": 8, "name": "Dr. Joshi", "specialist": "Gynecologist", "available": "Wed-Sat"}
    ],

    "realestate": [
        {"id": 1, "property": "2BHK Apartment", "location": "Pune", "price": 6500000},
        {"id": 2, "property": "Villa", "location": "Bangalore", "price": 12000000},
        {"id": 3, "property": "Studio Flat", "location": "Mumbai", "price": 9000000},
        {"id": 4, "property": "Penthouse", "location": "Delhi", "price": 25000000},
        {"id": 5, "property": "Farmhouse", "location": "Goa", "price": 30000000},
        {"id": 6, "property": "1BHK Apartment", "location": "Chennai", "price": 5000000},
        {"id": 7, "property": "3BHK Apartment", "location": "Noida", "price": 8000000},
        {"id": 8, "property": "Commercial Space", "location": "Hyderabad", "price": 20000000}
    ]
}

@app.route('/api/<category>', methods=['GET'])
def get_data(category):
    if category in data:
        return jsonify(data[category])
    return jsonify({"error": "Category not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
