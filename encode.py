def main():
    target = input("What is the string you want to encode?:\n").lower()
    sauce = {
        "a": " .-",
        "b": " -...",
        "c":"",
        "d":"",
        "e":"",
        "f":"",
        "g":"",
        "h":"",
        "i":"",
        "j":"",
        "k":"",
        "l":"",
        "m":"",
        
        
    }
    new =''
    for i in target:
        new = new + sauce[i]
    print(new)
        