#Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
#All ages will be different.
def oldest(dict):
    a=max(dict[i] for i in dict)
    for k,v in dict.items():
        if a==v:
            return k


print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}) )
#➞ "Emma"

print(oldest({
  "Max": 9,
  "Josh": 13,
  "Sam": 48,
  "Anne": 33
}))
#➞ "Sam"