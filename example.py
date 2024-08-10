
from main import MiniAPI


miniapi = MiniAPI()

@miniapi.get("/users")
def get_users(req, res):
    res.send(400, 200)

@miniapi.post("/users")
def get_users(req, res):
    res.send(400, 200)