# File Name: day9_rohit_assignment.py

# =========================
# Question 1
# =========================

student = {
    "name": "Rohit",
    "age": 21,
    "course": "CSE",
    "city": "Kolkata",
    "gpa": 8.5
}

print(student["name"])
print(student.get("name"))

print(student["age"])
print(student.get("age"))

print(student["course"])
print(student.get("course"))

print(student["city"])
print(student.get("city"))

print(student["gpa"])
print(student.get("gpa"))

student["email"] = "rohit@gmail.com"
student["phone"] = "9876543210"

print(student)

student["gpa"] = 9.0

del student["city"]

print(student)

print("name" in student)
print("address" in student)

print("Length =", len(student))


# =========================
# Question 2
# =========================

inventory = {
    "apple": 50,
    "banana": 30,
    "mango": 0,
    "cherry": 15,
    "grape": 0
}

print(inventory.keys())
print(inventory.values())

for item, qty in inventory.items():
    print(f"{item}: {qty} units")

print(inventory.get("papaya", "Not available"))

removed = inventory.pop("mango")
print("Removed:", removed)

inventory.update({
    "orange": 25,
    "kiwi": 12,
    "pineapple": 8
})

inventory.setdefault("watermelon", 25)

print(inventory)

print("\nOut of Stock:")

for item, qty in inventory.items():
    if qty == 0:
        print(item)


# =========================
# Question 3
# =========================

phonebook = {
    "Rohit": {
        "phone": "1111",
        "email": "rohit@gmail.com",
        "city": "Kolkata"
    },
    "Amit": {
        "phone": "2222",
        "email": "amit@gmail.com",
        "city": "Delhi"
    },
    "Rahul": {
        "phone": "3333",
        "email": "rahul@gmail.com",
        "city": "Mumbai"
    },
    "Saurav": {
        "phone": "4444",
        "email": "saurav@gmail.com",
        "city": "Kolkata"
    }
}

def search_contact(name):

    if name in phonebook:
        print(phonebook[name])

    else:
        print("Contact not found")

def add_contact(name, phone, email, city):

    phonebook[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }

def delete_contact(name):

    if name in phonebook:
        del phonebook[name]

def contacts_in_city(city):

    result = []

    for name, details in phonebook.items():

        if details["city"].lower() == city.lower():
            result.append(name)

    return result

def display_all():

    for name, details in phonebook.items():
        print(name, details)

search_contact("Rohit")
search_contact("Amit")
search_contact("XYZ")

add_contact("Priya", "5555", "priya@gmail.com", "Delhi")
add_contact("Ankit", "6666", "ankit@gmail.com", "Mumbai")
add_contact("Riya", "7777", "riya@gmail.com", "Pune")

delete_contact("Ankit")

print(contacts_in_city("Kolkata"))
print(contacts_in_city("Delhi"))

display_all()


# =========================
# Question 4
# =========================

text = """
Python is a high level programming language.
Python is easy to learn and easy to use.
Python is used for web development data science and automation.
"""

text = text.lower()

for ch in ".,!?":
    text = text.replace(ch, "")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

sorted_words = sorted(
    freq.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 5 Words")

for word, count in sorted_words[:5]:
    print(word, count)

print("\nAppear Once")

for word, count in freq.items():

    if count == 1:
        print(word)

filtered = {
    word: count
    for word, count in freq.items()
    if count >= 2
}

print(filtered)


# =========================
# Question 5
# =========================

A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}

print("Union:", A | B)
print("Intersection:", A & B)
print("A-B:", A - B)
print("B-A:", B - A)
print("Symmetric:", A ^ B)

print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(B))

A.add(14)

B.discard(3)

print(A)
print(B)

nums = [5,1,3,5,2,1,4,3,5,2,6]

print(set(nums))

fs = frozenset(A)

print(fs)

# fs.add(20)  # Error


# =========================
# Question 6
# =========================

paragraph1 = """
Python is easy to learn.
Python is powerful.
Python is used in web development.
"""

paragraph2 = """
Python is popular.
Data science uses Python.
Automation uses Python.
"""

def tokenize(text):

    text = text.lower()

    for ch in ".,!?":
        text = text.replace(ch, "")

    return set(text.split())

set1 = tokenize(paragraph1)
set2 = tokenize(paragraph2)

print("Intersection:", set1 & set2)

print("Only P1:", set1 - set2)

print("Only P2:", set2 - set1)

print("Union:", set1 | set2)

print("Symmetric:", set1 ^ set2)

def common_letters(word1, word2):

    return set(word1) & set(word2)

print(common_letters("python", "typhoon"))

combined = (paragraph1 + paragraph2).lower()

words = combined.split()

freq = {}

for word in words:

    word = word.strip(".,!?")

    freq[word] = freq.get(word, 0) + 1

top = sorted(
    freq.items(),
    key=lambda x: x[1],
    reverse=True
)

print(top[:5])


# =========================
# Question 7
# =========================

print("a) Tuple - fixed days")
print("b) Set - unique IPs")
print("c) Dictionary - code mapping")
print("d) List - ordered scores")
print("e) Tuple - employee record")


# =========================
# Challenge 1
# =========================

students = [

{
"name":"A",
"roll":1,
"subjects":{"Math":80,"Science":70,"English":75}
},

{
"name":"B",
"roll":2,
"subjects":{"Math":90,"Science":95,"English":85}
},

{
"name":"C",
"roll":3,
"subjects":{"Math":45,"Science":50,"English":60}
}

]

def get_average(student):

    marks = student["subjects"].values()

    return sum(marks) / len(marks)

print("\nAverages")

for student in students:

    avg = get_average(student)

    print(student["name"], avg)

print("\nPassed Students")

for student in students:

    if all(mark >= 40 for mark in student["subjects"].values()):
        print(student["name"])

low_subjects = set()

for student in students:

    for subject, mark in student["subjects"].items():

        if mark < 50:
            low_subjects.add(subject)

print("Subjects below 50:", low_subjects)

subject_scores = {}

for student in students:

    for subject, mark in student["subjects"].items():

        subject_scores.setdefault(subject, []).append(mark)

print(subject_scores)

print("\nSubject Averages")

for subject, marks in subject_scores.items():

    print(subject, sum(marks)/len(marks))

topper = max(
    students,
    key=get_average
)

print("Topper:", topper["name"])

ranked = sorted(
    students,
    key=get_average,
    reverse=True
)

print("\nRanking")

for i, student in enumerate(ranked, start=1):

    print(i, student["name"], get_average(student))

common_subjects = set(
    students[0]["subjects"].keys()
)

for student in students[1:]:

    common_subjects &= set(
        student["subjects"].keys()
    )

print("Common Subjects:", common_subjects)