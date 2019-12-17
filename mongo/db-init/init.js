
db.createUser({
    user: "user",
    pwd: "secretPassword",
    roles: [ { role: "readWrite", db: "apy" } ]
})

db.stars.insert(
    [
        {
            label: "one",
            value: "1"
        },
        {
            label: "two",
            value: "2"
        },
        {
            label: "four",
            value: "4"
        },
        {
            label: "eight",
            value: "8"
        },
        {
            label: "sixteen",
            value: "16"
        },
        {
            label: "thirty two",
            value: "32"
        },
        {
            label: "sixty four",
            value: "64"
        }
    ]
)
