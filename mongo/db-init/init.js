
db.createUser({
    user: "user",
    pwd: "secretPassword",
    roles: [ { role: "readWrite", db: "restdb" } ]
})

db.stars.insert(
    [
        {
            name: "1",
            distance: "1"
        },
        {
            name: "2",
            distance: "2"
        },
        {
            name: "4",
            distance: "4"
        },
        {
            name: "8",
            distance: "8"
        },
        {
            name: "16",
            distance: "16"
        },
        {
            name: "32",
            distance: "32"
        },
        {
            name: "64",
            distance: "64"
        }
    ]
)
