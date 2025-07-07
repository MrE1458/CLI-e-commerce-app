import bcrypt

def hash_password(original_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(original_password.encode(), salt)
    return hashed_password.decode() #--- decode to store in json database

def compare_password(entered_password, correct_password):
    return bcrypt.checkpw(entered_password.encode(), correct_password.encode())