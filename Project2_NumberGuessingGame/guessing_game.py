import random
best=None
while True:
    lvl=input("Difficulty (easy/medium/hard): ").lower()
    m={'easy':10,'medium':50,'hard':100}.get(lvl,10)
    n=random.randint(1,m); att=0
    while True:
        g=int(input(f"Guess (1-{m}): ")); att+=1
        if g<n: print("Higher")
        elif g>n: print("Lower")
        else:
            print("Correct!",att,"attempts")
            if best is None or att<best: best=att
            print("Best:",best); break
    if input("Play again? (y/n): ").lower()!='y': break
