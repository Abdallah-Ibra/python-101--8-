# ---------------------------
# -- Practical Slice Email --
# ---------------------------

name = input('What\'s Your Name ? ').strip().capitalize()
email = input('What\'s Your Email ? ').strip()

username = email[:email.index("@")]
website = email[email.index("@") + 1:]

print(f"\nHello {name} Your Email Is {email}")
print(f"Your Username Is {username} \nYour Website Is {website}")