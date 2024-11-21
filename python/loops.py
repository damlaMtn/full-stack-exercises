for i in range(-4,5):
    print(i)


Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in Genres:
    print(genre)


squares=['red', 'yellow', 'green', 'purple', 'blue']
for i in squares:
    print(i)


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
score = PlayListRatings[0]
while i<len(PlayListRatings) and score >= 6:
    print(score)
    i = i+1
    score = PlayListRatings[i]


squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while i<len(squares) and squares[i] == "orange":
    new_squares.append(squares[i])
    i=i+1
print(new_squares)