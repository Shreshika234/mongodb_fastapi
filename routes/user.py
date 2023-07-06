from fastapi import APIRouter
from models.user import User
from config.db import con,collection
from schemas.user import serializeDict , serializeList
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def find_all_users():
    print(con.student.studentdata.find())
    print(serializeList(con.student.studentdata.find()))
    return serializeList(con.student.studentdata.find())


@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(con.student.studentdata.find_one({"_id":ObjectId(id)}))


#post
@user.post('/')
async def create_user(user:User):
    con.student.studentdata.insert_one(user.dict())
    return serializeList(con.student.studentdata.find())



@user.put('/{id}')
async def update_user(id,user:User):
    con.student.studentdata.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    # return serializeList(con.student.studentdata.find())
    return serializeDict(con.student.studentdata.find_one({"_id":ObjectId(id)}))



@user.delete('/{id}')
async def delete_user(id,user:User):
    return serializeDict(con.student.studentdata.find_one_and_delete({"_id":ObjectId(id)}))