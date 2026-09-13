## Lab 1 — Part C AI Checkpoint
- **Date:** 2026-08-31
- **Tool Used:** ChatGPT
- **Prompt Given:** "Write a Python program that stores a person's name and age as variables and prints a sentence combining them."
- **Output Received:**
```python
name = "Aseel"
age = 20

print(f"My name is {name} and I am {age} years old.")

## Lab 2 — AI Checkpoint

### AI tool
ChatGPT

### Prompt
"Write a Python class called Student with attributes name, age, and gpa, plus getter and setter methods for each attribute."

### How I used the AI response
I used the AI-generated Student class for the Part C comparison. The AI solution uses getter and setter methods and stores the attributes with leading underscores, such as `_name`, `_age`, and `_gpa`. I compared this approach with the Student class used in my lab.

### What I learned
Python generally allows direct access to attributes, so getter and setter methods are not always necessary. If controlled access to an attribute is needed, Python's `property` feature can be used.

# AI Log — Lab 2

## Step 1: Prompt Given
> "Write a Python function that removes duplicate values from a list."

## Step 2: Assistant's Response
```python
def remove_duplicates(my_list):
    return list(set(my_list))