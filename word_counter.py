text = """
Suddenly, something has happened to me
As I was having my cup of tea
Suddenly, I was feeling depressed
I was utterly and totally stressed
Do you know you made me cry? (Woah-oh)
Do you know you made me die?
And the thing that gets to me (thing that gets to me)
Is you'll never really see (never really see)
And the thing that freaks me out (thing that freaks me out)
Is I'll always be in doubt (always be in)
It is the lovely thing that we have
It is the lovely thing that we
It is the lovely thing
The animal, the animal instinct
So take my hands and come with me
We will change reality
So take my hands and we will pray
They won't take you away
They will never make me cry, no-oh
They will never make me die
And the thing that gets to me (thing that gets to me)
Is you'll never really see (never really see)
And the thing that freaks me out (thing that freaks me out)
Is I'll always be in doubt (always be in)
The animal, the animal
The animal instinct in me
It's the animal, the animal
The animal instinct in me
It's the animal, it's the animal
It's the animal instinct in me
It's the animal, it's the animal
It's the animal instinct in me
The animal, the animal
The animal instinct in me
It's the animal, it's the animal
It's the animal instinct in me
"""

print(text.split())

word_count = {}

for word in text.lower().split():
    
    if word in word_count:
        word_count[word] += 1
    else:
     word_count[word] = 1


print(word_count)
