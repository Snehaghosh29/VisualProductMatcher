from pymongo import MongoClient
import json

#  MongoDB Atlas connection string
uri = "mongodb+srv://snehaghosh2903_db_user:SN2903%40%239osh@visual-matcher-cluster.jzawms2.mongodb.net/?retryWrites=true&w=majority&appName=visual-matcher-cluster"


#  Connect to the cluster
client = MongoClient(uri)
db = client["visual_matcher"]         # Database name
collection = db["products"]           # Collection name

# Load  product JSON data

data = json.loads("""
[
  {
    "name": "Classic White T-shirt",
    "category": "T-shirt",
    "brand": "H&M",
    "color": "White",
    "gender": "Unisex",
    "price": 799,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt1.jpg",
    "metadata": {
      "material": "Cotton",
      "sleeve": "Short",
      "fit": "Regular",
      "pattern": "Solid"
    }
  },
  {
    "name": "Graphic Oversized Tee",
    "category": "T-shirt",
    "brand": "Zara",
    "color": "Black",
    "gender": "Unisex",
    "price": 1299,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt2.jpg",
    "metadata": {
      "material": "Polyester",
      "sleeve": "Short",
      "fit": "Oversized",
      "pattern": "Printed"
    }
  },
  {
    "name": "Striped Cotton Tee",
    "category": "T-shirt",
    "brand": "Levi's",
    "color": "Blue",
    "gender": "Men",
    "price": 999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt3.jpeg",
    "metadata": {
      "material": "Cotton",
      "sleeve": "Half",
      "fit": "Slim",
      "pattern": "Striped"
    }
  },
  {
    "name": "Plain Red Crew Neck",
    "category": "T-shirt",
    "brand": "Uniqlo",
    "color": "Red",
    "gender": "Men",
    "price": 899,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt4.jpg",
    "metadata": {
      "material": "Cotton",
      "sleeve": "Short",
      "fit": "Regular",
      "pattern": "Solid"
    }
  },
  {
    "name": "Women's Floral Tee",
    "category": "T-shirt",
    "brand": "H&M",
    "color": "Pink",
    "gender": "Women",
    "price": 1199,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt5.jpeg",
    "metadata": {
      "material": "Viscose",
      "sleeve": "Short",
      "fit": "Regular",
      "pattern": "Floral"
    }
  },
  {
    "name": "V-neck Casual Tee",
    "category": "T-shirt",
    "brand": "Zara",
    "color": "Beige",
    "gender": "Women",
    "price": 1099,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt6.jpeg",
    "metadata": {
      "material": "Linen",
      "sleeve": "Short",
      "fit": "Slim",
      "pattern": "Plain"
    }
  },
  {
    "name": "Athletic Grey Tee",
    "category": "T-shirt",
    "brand": "Nike",
    "color": "Grey",
    "gender": "Unisex",
    "price": 1299,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt7.jpeg",
    "metadata": {
      "material": "Polyester",
      "sleeve": "Half",
      "fit": "Slim",
      "pattern": "Solid"
    }
  },
  {
    "name": "Graphic Anime Tee",
    "category": "T-shirt",
    "brand": "Uniqlo",
    "color": "White",
    "gender": "Unisex",
    "price": 1399,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt8.jpeg",
    "metadata": {
      "material": "Cotton",
      "sleeve": "Short",
      "fit": "Regular",
      "pattern": "Graphic"
    }
  },
  {
    "name": "Striped Polo Tee",
    "category": "T-shirt",
    "brand": "Tommy Hilfiger",
    "color": "Navy",
    "gender": "Men",
    "price": 1999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt9.jpeg",
    "metadata": {
      "material": "Cotton",
      "sleeve": "Half",
      "fit": "Regular",
      "pattern": "Striped"
    }
  },
  {
    "name": "Pastel Crop Top",
    "category": "T-shirt",
    "brand": "Zara",
    "color": "Peach",
    "gender": "Women",
    "price": 999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/tshirt10.jpeg",
      "metadata": {
        "material": "Cotton",
        "sleeve": "Short",
        "fit": "Crop",
        "pattern": "Plain"
      }
  },
  {
    "name": "Air Runner Sneaker",
    "category": "Shoes",
    "brand": "Nike",
    "color": "White",
    "gender": "Unisex",
    "price": 4999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe1.jpeg",
    "metadata": {
      "material": "Mesh",
      "type": "Sneaker",
      "sole": "Rubber"
    }
  },
  {
    "name": "Classic Black Loafer",
    "category": "Shoes",
    "brand": "Bata",
    "color": "Black",
    "gender": "Men",
    "price": 2499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe2.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Loafer",
      "sole": "PU"
    }
  },
  {
    "name": "Retro High Sneaker",
    "category": "Shoes",
    "brand": "Adidas",
    "color": "Red",
    "gender": "Unisex",
    "price": 5499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe3.jpeg",
    "metadata": {
      "material": "Synthetic",
      "type": "Sneaker",
      "sole": "Rubber"
    }
  },
  {
    "name": "Women's Running Shoe",
    "category": "Shoes",
    "brand": "Puma",
    "color": "Pink",
    "gender": "Women",
    "price": 3599,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe4.jpeg",
    "metadata": {
      "material": "Mesh",
      "type": "Sports",
      "sole": "EVA"
    }
  },
  {
    "name": "Brown Formal Shoe",
    "category": "Shoes",
    "brand": "Hush Puppies",
    "color": "Brown",
    "gender": "Men",
    "price": 3999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe5.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Formal",
      "sole": "PU"
    }
  },
  {
    "name": "Canvas Everyday Sneaker",
    "category": "Shoes",
    "brand": "Vans",
    "color": "Blue",
    "gender": "Unisex",
    "price": 2999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe6.jpeg",
    "metadata": {
      "material": "Canvas",
      "type": "Casual",
      "sole": "Rubber"
    }
  },
  {
    "name": "White Slip-on",
    "category": "Shoes",
    "brand": "Skechers",
    "color": "White",
    "gender": "Women",
    "price": 3799,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe7.jpeg",
    "metadata": {
      "material": "Fabric",
      "type": "Slip-on",
      "sole": "Foam"
    }
  },
  {
    "name": "Men's Trail Runner",
    "category": "Shoes",
    "brand": "Decathlon",
    "color": "Grey",
    "gender": "Men",
    "price": 4299,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe8.jpeg",
    "metadata": {
      "material": "Mesh",
      "type": "Running",
      "sole": "Rubber"
    }
  },
  {
    "name": "High Heel Sandal",
    "category": "Shoes",
    "brand": "Catwalk",
    "color": "Beige",
    "gender": "Women",
    "price": 2599,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe9.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Heels",
      "sole": "Synthetic"
    }
  },
  {
    "name": "Black Sports Trainer",
    "category": "Shoes",
    "brand": "Reebok",
    "color": "Black",
    "gender": "Unisex",
    "price": 3499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/shoe10.jpeg",
    "metadata": {
      "material": "Mesh",
      "type": "Trainer",
      "sole": "Rubber"
    }
  },
  {
    "name": "Leather Crossbody Bag",
    "category": "Bag",
    "brand": "Zara",
    "color": "Brown",
    "gender": "Women",
    "price": 2299,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag1.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Crossbody",
      "size": "Medium"
    }
  },
  {
    "name": "Canvas Backpack",
    "category": "Bag",
    "brand": "Wildcraft",
    "color": "Blue",
    "gender": "Unisex",
    "price": 1799,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag2.jpeg",
    "metadata": {
      "material": "Canvas",
      "type": "Backpack",
      "size": "Large"
    }
  },
  {
    "name": "Office Laptop Bag",
    "category": "Bag",
    "brand": "Samsonite",
    "color": "Black",
    "gender": "Men",
    "price": 3199,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag3.jpeg",
    "metadata": {
      "material": "Polyester",
      "type": "Laptop",
      "size": "Medium"
    }
  },
  {
    "name": "Mini Shoulder Bag",
    "category": "Bag",
    "brand": "H&M",
    "color": "Pink",
    "gender": "Women",
    "price": 1599,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag4.jpeg",
    "metadata": {
      "material": "PU",
      "type": "Shoulder",
      "size": "Small"
    }
  },
  {
    "name": "Travel Duffel Bag",
    "category": "Bag",
    "brand": "Skybags",
    "color": "Grey",
    "gender": "Unisex",
    "price": 2899,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag5.jpeg",
    "metadata": {
      "material": "Nylon",
      "type": "Duffel",
      "size": "Large"
    }
  },
  {
    "name": "Sling Pouch",
    "category": "Bag",
    "brand": "Decathlon",
    "color": "Black",
    "gender": "Unisex",
    "price": 899,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag6.jpeg",
    "metadata": {
      "material": "Polyester",
      "type": "Sling",
      "size": "Small"
    }
  },
  {
    "name": "Women's Tote Bag",
    "category": "Bag",
    "brand": "Zara",
    "color": "Beige",
    "gender": "Women",
    "price": 2699,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag7.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Tote",
      "size": "Large"
    }
  },
  {
    "name": "Sporty Gym Bag",
    "category": "Bag",
    "brand": "Puma",
    "color": "Red",
    "gender": "Unisex",
    "price": 2199,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag8.jpeg",
    "metadata": {
      "material": "Polyester",
      "type": "Gym",
      "size": "Medium"
    }
  },
  {
    "name": "Leather Backpack",
    "category": "Bag",
    "brand": "Tommy Hilfiger",
    "color": "Brown",
    "gender": "Unisex",
    "price": 3599,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag9.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Backpack",
      "size": "Large"
    }
  },
  {
    "name": "Women's Party Clutch",
    "category": "Bag",
    "brand": "H&M",
    "color": "Gold",
    "gender": "Women",
    "price": 1999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/bag10.jpeg",
    "metadata": {
      "material": "Sequins",
      "type": "Clutch",
      "size": "Small"
    }
  },
  {
    "name": "Classic Leather Watch",
    "category": "Watch",
    "brand": "Fossil",
    "color": "Brown",
    "gender": "Men",
    "price": 7999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/watch1.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Analog",
      "waterResistant": "Yes"
    }
  },
  {
    "name": "Rose Gold Bracelet Watch",
    "category": "Watch",
    "brand": "Michael Kors",
    "color": "Rose Gold",
    "gender": "Women",
    "price": 11999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/watch2.jpeg",
    "metadata": {
      "material": "Metal",
      "type": "Analog",
      "waterResistant": "Yes"
    }
  },
  {
    "name": "Sport Digital Watch",
    "category": "Watch",
    "brand": "Casio",
    "color": "Black",
    "gender": "Unisex",
    "price": 4999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/watch3.jpeg",
    "metadata": {
      "material": "Resin",
      "type": "Digital",
      "waterResistant": "Yes"
    }
  },
  {
    "name": "Silver Chain Watch",
    "category": "Watch",
    "brand": "Titan",
    "color": "Silver",
    "gender": "Men",
    "price": 6499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/watch4.jpeg",
    "metadata": {
      "material": "Stainless Steel",
      "type": "Analog",
      "waterResistant": "Yes"
    }
  },
  {
    "name": "Minimal White Dial Watch",
    "category": "Watch",
    "brand": "Daniel Wellington",
    "color": "White",
    "gender": "Unisex",
    "price": 9999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/watch5.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Analog",
      "waterResistant": "No"
    }
  },
  {
    "name": "Smart Fitness Band",
    "category": "Watch",
    "brand": "Fitbit",
    "color": "Blue",
    "gender": "Unisex",
    "price": 10999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/watch6.jpeg",
    "metadata": {
      "material": "Silicone",
      "type": "Smart",
      "waterResistant": "Yes"
    }
  },
  {
    "name": "Aviator Classic",
    "category": "Sunglasses",
    "brand": "Ray-Ban",
    "color": "Gold",
    "gender": "Unisex",
    "price": 6999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/sunglass1.jpeg",
    "metadata": {
      "frame": "Metal",
      "lens": "Green",
      "uvProtection": "100%"
    }
  },
  {
    "name": "Round Oversized Shades",
    "category": "Sunglasses",
    "brand": "Gucci",
    "color": "Black",
    "gender": "Women",
    "price": 12999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/sunglass2.jpeg",
    "metadata": {
      "frame": "Acetate",
      "lens": "Black",
      "uvProtection": "100%"
    }
  },
  {
    "name": "Sport Wrap Sunglasses",
    "category": "Sunglasses",
    "brand": "Oakley",
    "color": "Grey",
    "gender": "Men",
    "price": 9999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/sunglass3.jpeg",
    "metadata": {
      "frame": "Plastic",
      "lens": "Mirror",
      "uvProtection": "100%"
    }
  },
  {
    "name": "Retro Cat Eye",
    "category": "Sunglasses",
    "brand": "Prada",
    "color": "Pink",
    "gender": "Women",
    "price": 15999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/sunglass4.jpeg",
    "metadata": {
      "frame": "Acetate",
      "lens": "Gradient",
      "uvProtection": "100%"
    }
  },
  {
    "name": "Square Wayfarer",
    "category": "Sunglasses",
    "brand": "Ray-Ban",
    "color": "Brown",
    "gender": "Men",
    "price": 7499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/sunglass5.jpeg",
    "metadata": {
      "frame": "Plastic",
      "lens": "Brown",
      "uvProtection": "100%"
    }
  },
  {
    "name": "Transparent Frame Glasses",
    "category": "Sunglasses",
    "brand": "H&M",
    "color": "Transparent",
    "gender": "Unisex",
    "price": 1999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/sunglass6.jpeg",
    "metadata": {
      "frame": "Plastic",
      "lens": "Clear UV",
      "uvProtection": "100%"
    }
  },
  {
    "name": "Basic Black Hoodie",
    "category": "Hoodie",
    "brand": "H&M",
    "color": "Black",
    "gender": "Unisex",
    "price": 1999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/hoodie1.jpeg",
    "metadata": {
      "material": "Cotton",
      "fit": "Regular",
      "pattern": "Solid"
    }
  },
  {
    "name": "Zipper Grey Hoodie",
    "category": "Hoodie",
    "brand": "Nike",
    "color": "Grey",
    "gender": "Men",
    "price": 2999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/hoodie2.jpeg",
    "metadata": {
      "material": "Fleece",
      "fit": "Regular",
      "pattern": "Solid"
    }
  },
  {
    "name": "Cropped Pink Hoodie",
    "category": "Hoodie",
    "brand": "Zara",
    "color": "Pink",
    "gender": "Women",
    "price": 2499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/hoodie3.jpeg",
      "metadata": {
        "material": "Cotton",
        "fit": "Crop",
        "pattern": "Plain"
      }
  },
  {
    "name": "Oversized White Hoodie",
    "category": "Hoodie",
    "brand": "Adidas",
    "color": "White",
    "gender": "Unisex",
    "price": 3299,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/hoodie4.jpeg",
    "metadata": {
      "material": "Cotton Blend",
      "fit": "Oversized",
      "pattern": "Solid"
    }
  },
  {
    "name": "Graphic Print Hoodie",
    "category": "Hoodie",
    "brand": "Uniqlo",
    "color": "Blue",
    "gender": "Men",
    "price": 2799,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/hoodie5.jpeg",
    "metadata": {
      "material": "Cotton",
      "fit": "Regular",
      "pattern": "Graphic"
    }
  },
  {
    "name": "Athleisure Hoodie",
    "category": "Hoodie",
    "brand": "Puma",
    "color": "Red",
    "gender": "Women",
    "price": 2999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/hoodie6.jpeg",
    "metadata": {
      "material": "Polyester",
      "fit": "Slim",
      "pattern": "Logo"
    }
  },
  {
    "name": "Classic Blue Denim",
    "category": "Jeans",
    "brand": "Levi's",
    "color": "Blue",
    "gender": "Men",
    "price": 3499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jeans1.jpeg",
    "metadata": {
      "material": "Denim",
      "fit": "Regular",
      "wash": "Mid"
    }
  },
  {
    "name": "High Waist Skinny",
    "category": "Jeans",
    "brand": "Zara",
    "color": "Black",
    "gender": "Women",
    "price": 2999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jeans2.jpeg",
    "metadata": {
      "material": "Stretch Denim",
      "fit": "Skinny",
      "wash": "Dark"
    }
  },
  {
    "name": "Ripped Light Wash Jeans",
    "category": "Jeans",
    "brand": "H&M",
    "color": "Light Blue",
    "gender": "Unisex",
    "price": 2799,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jeans3.jpeg",
    "metadata": {
      "material": "Denim",
      "fit": "Slim",
      "wash": "Light"
    }
  },
  {
    "name": "Mom Fit Jeans",
    "category": "Jeans",
    "brand": "Zara",
    "color": "Blue",
    "gender": "Women",
    "price": 3199,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jeans4.jpeg",
    "metadata": {
      "material": "Denim",
      "fit": "Mom",
      "wash": "Medium"
    }
  },
  {
    "name": "Tapered Fit Jeans",
    "category": "Jeans",
    "brand": "Jack & Jones",
    "color": "Grey",
    "gender": "Men",
    "price": 3299,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jeans5.jpeg",
    "metadata": {
      "material": "Denim",
      "fit": "Tapered",
      "wash": "Grey"
    }
  },
  {
    "name": "Wide Leg Jeans",
    "category": "Jeans",
    "brand": "H&M",
    "color": "Blue",
    "gender": "Women",
    "price": 2899,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jeans6.jpeg",
    "metadata": {
      "material": "Denim",
      "fit": "Wide",
      "wash": "Light"
    }
  },
  {
    "name": "Black Leather Jacket",
    "category": "Jacket",
    "brand": "Zara",
    "color": "Black",
    "gender": "Men",
    "price": 6999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jacket1.jpeg",
    "metadata": {
      "material": "Leather",
      "type": "Biker",
      "closure": "Zipper"
    }
  },
  {
    "name": "Denim Trucker Jacket",
    "category": "Jacket",
    "brand": "Levi's",
    "color": "Blue",
    "gender": "Unisex",
    "price": 5999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jacket2.jpeg",
    "metadata": {
      "material": "Denim",
      "type": "Trucker",
      "closure": "Button"
    }
  },
  {
    "name": "Puffer Jacket",
    "category": "Jacket",
    "brand": "Uniqlo",
    "color": "Grey",
    "gender": "Unisex",
    "price": 6499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jacket3.jpeg",
    "metadata": {
      "material": "Polyester",
      "type": "Puffer",
      "closure": "Zipper"
    }
  },
  {
    "name": "Beige Trench Coat",
    "category": "Jacket",
    "brand": "H&M",
    "color": "Beige",
    "gender": "Women",
    "price": 7999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jacket4.jpeg",
    "metadata": {
      "material": "Cotton Blend",
      "type": "Trench",
      "closure": "Belted"
    }
  },
  {
    "name": "Bomber Jacket",
    "category": "Jacket",
    "brand": "Nike",
    "color": "Green",
    "gender": "Men",
    "price": 5499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jacket5.jpeg",
    "metadata": {
      "material": "Nylon",
      "type": "Bomber",
      "closure": "Zipper"
    }
  },
  {
    "name": "Faux Fur Jacket",
    "category": "Jacket",
    "brand": "Zara",
    "color": "White",
    "gender": "Women",
    "price": 8999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/jacket6.jpeg",
    "metadata": {
      "material": "Faux Fur",
      "type": "Winter",
      "closure": "Hook"
    }
  },
  {
    "name": "Floral Summer Dress",
    "category": "Dress",
    "brand": "H&M",
    "color": "Yellow",
    "gender": "Women",
    "price": 3499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/dress1.jpeg",
    "metadata": {
      "material": "Cotton",
      "length": "Midi",
      "pattern": "Floral"
    }
  },
  {
    "name": "Black Bodycon Dress",
    "category": "Dress",
    "brand": "Zara",
    "color": "Black",
    "gender": "Women",
    "price": 3999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/dress2.jpeg",
    "metadata": {
      "material": "Polyester",
      "length": "Mini",
      "pattern": "Solid"
    }
  },
  {
    "name": "White Maxi Dress",
    "category": "Dress",
    "brand": "Uniqlo",
    "color": "White",
    "gender": "Women",
    "price": 4499,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/dress3.jpeg",
    "metadata": {
      "material": "Cotton",
      "length": "Maxi",
      "pattern": "Plain"
    }
  },
  {
    "name": "Red Evening Gown",
    "category": "Dress",
    "brand": "Mango",
    "color": "Red",
    "gender": "Women",
    "price": 7999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/dress4.jpeg",
    "metadata": {
      "material": "Silk Blend",
      "length": "Floor",
      "pattern": "Solid"
    }
  },
  {
    "name": "Denim Shirt Dress",
    "category": "Dress",
    "brand": "Levi's",
    "color": "Blue",
    "gender": "Women",
    "price": 4599,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/dress5.jpeg",
    "metadata": {
      "material": "Denim",
      "length": "Knee",
      "pattern": "Solid"
    }
  },
  {
    "name": "Printed Wrap Dress",
    "category": "Dress",
    "brand": "Zara",
    "color": "Green",
    "gender": "Women",
    "price": 4999,
    "imageUrl": "https://raw.githubusercontent.com/Snehaghosh29/sneha-visual-matcher/main/dress6.jpeg",
    "metadata": {
      "material": "Viscose",
      "length": "Midi",
      "pattern": "Printed"
    }
  }
]

""")

# 🧠 Insert all products
result = collection.insert_many(data)
print(f"✅ Inserted {len(result.inserted_ids)} products successfully!")

# 🧾 Verify inserted count
print("Total documents now:", collection.count_documents({}))
