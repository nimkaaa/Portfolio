user_name = "STRANGER"
robot_name = "ROBOT"
user_age = 0

user_name = input(f"- [{robot_name}] Hi, stranger... What's your name?\n- [{user_name}] ").upper()

print(f"- [{robot_name}] It's nice to meet you, {user_name}")

question = input(f"- [INNER VOICE] *ask about its name (just say - \"And what's your name?\")*\n- [{user_name}] ")

# Asking until the correct question is asked
while question != "And what's your name?":
   question = input(f"- [INNER VOICE] *just say - \"And what's your name?\")*\n- [{user_name}] ")

# Robot's introduction
robot_name = "ADA"
print(f"- [{robot_name}] My name is Ada. I'm a robot")

# Age question
user_age = int(input(f"- [{robot_name}] {user_name}, how old are you?\n- [{user_name}] "))
if user_age < 25:
   print(f"- [{robot_name}] Oh, i'm a little older than you. I'm 25 years old")
elif user_age == 25:
   print(f"- [{robot_name}] Wow, we are the same age!")
else:
   print(f"- [{robot_name}] Oh, you're older than me!")

# Second question
question2 = input(f"- [{robot_name}] Do you wanna know who am I?\n(yes/no)\n- [{user_name}] ")
if question2 == "yes":
   print(f"- [{robot_name}] I'm a robot created by a great programmer named Mykyta")
else:
   print(f"- [{robot_name}] Oh, okay...")

# End of the chat
print(f"- [{robot_name}] Well, {user_name}, I gotta go, see you later!")