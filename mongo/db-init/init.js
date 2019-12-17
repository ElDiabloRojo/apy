
db.createUser({
    user: "user",
    pwd: "secretPassword",
    roles: [ { role: "readWrite", db: "apy" } ]
})

db.stars.insert(
    [
        {
            label: "one",
            duration: "10",
            value: "1"
        },
        {
            label: "one",
            duration: "12",
            value: "2"
        },
        {
            label: "two",
            duration: "15",
            value: "4"
        },
        {
            label: "three",
            duration: "13",
            value: "8"
        },
        {
            label: "four",
            duration: "12",
            value: "16"
        },
        {
            label: "5",
            duration: "8",
            value: "32"
        },
        {
            label: "six",
            duration: "7",
            value: "64"
        }
    ]
)
