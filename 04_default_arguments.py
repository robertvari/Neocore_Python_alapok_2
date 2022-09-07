#                   required posittional params     default parameters
def register_user(username, password, address=None, email=None, phone=None):
    print(f"Hello {username}")
    print(f"Your password is: {password}")

    if address:
        print(f"Address:{address}")

    if email:
        print(f"Email: {email}")

    if phone:
        print(f"Phone: {phone}")


register_user(
    username="robert", 
    password="testpas123", 
    address="Budapest",
    phone="06 20 123 4567",
    email="robert@gmail.com"
)