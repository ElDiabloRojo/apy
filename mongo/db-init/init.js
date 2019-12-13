
db.createUser({
    user: "user",
    pwd: "secretPassword",
    roles: [ { role: "readWrite", db: "restdb" } ]
})

db.stars.insert({
    name: "abc",
    distance: "abc"
})
