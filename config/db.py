from pymongo import MongoClient

con = MongoClient('mongodb+srv://Shreshika:Bunny234@cluster0.lzku1n5.mongodb.net/')
db=con["student"]
collection=db["studentdata"]