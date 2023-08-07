from pymongo import MongoClient

con = MongoClient('mongodb+srv://Shreshika:Bunny234@cluster0.lzku1n5.mongodb.net/')
db=con["student"]  #db name sutdent
collection=db["studentdata"]   #collection name studentdata
