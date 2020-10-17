import random

def select():
    books=['Wings of Fire','Attitude is Everything','Wasted in Engineering','The Theory of Everything','The Miracles of Your Mind',
           'Zero to One','Believe in Yourself','The Secret','Think and Grow Rich','Why I Assassinated Gandhi']
    movies=['The Shawshank Redemption','The Godfather','The Dark Knight','Inception','Pursuit of Happiness',
            'Rang De Basanti','Gangs of Wasseypur','Zindagi Na Milegi Dobara','Lage Raho Munna Bhai','A Wednesday']
    songs=['Like A Rolling Stone','Bohemian Rhapsody','Stairway To Heaven','Bridge Over Troubled Water,''Every Breath You Take',
           'When Doves Cry','Mera Dil Bhi Kitna Pagal Hai','Jab Koi Baat Bigad Jaaye','Agar Tum Saath Ho','Akele Hain To Kya Gam Hai']
    shows=['Band of Brothers','House of cards','Persons of Interest','The Walking Dead','Curb Your Enthusiasm',
           'Arrested Development','Two and a Half Men','How I Met Your Mother','Stranger Things','Six Feet under']
    print(''' 
       Press 1 -> Books
       Press 2 -> Movies
       press 3 -> Songs
       Press 4 -> Shows
       Select category : ''', end=' ')
    i = int(input())
    if i > 4 or i < 1:
        return None
    x=random.randint(0,10)
    if i==1:
        return books[x]
    elif i==2:
        return movies[x]
    elif i==3:
        return songs[x]
    else:
        return shows[x]

def dic(name):
    name=name.upper()
    word_dict={}
    for i in range(len(name)):
        if name[i] in word_dict:
            word_dict[name[i]].append(i)
        else:
            word_dict[name[i]]=[i]
    return(word_dict)

def hide(name):
    hidden=['_' for i in range(len(name))]
    return hidden

def guess(word_dict,hidden,ch):
    if ch in word_dict:
        for i in word_dict[ch]:
            hidden[i]=ch
        return hidden
    return None

def print_hidden(hidden):
    for i in hidden:
        print(f"{i}",end=' ')

def check(hidden):
    if '_' in hidden:
        return True
    return False

def winner():
    print(" - - - - - - Y O U - W O N - - - - - -")
    print('The Word was ',end=' ')
    print_hidden(hidden)

def loser():
    print(" - - - - - - Y O U - L O S T - - - - - -")
    print('The Word was ',end=' ')
    print_hidden(name.upper())

if __name__=='__main__':
    Flag=True
    while Flag:
        name=select()
        if name:
            no_of_guesses=7
            word_dict=dic(name)
            hidden=hide(name)
            hidden = guess(word_dict, hidden, ' ')
            while no_of_guesses>0:
                if check(hidden):
                    print('Present Status => ',end=' ')
                    print_hidden(hidden)
                    print(f'You have {no_of_guesses} Wrong Guess left. Enter a Alphabet : ',end=' ')
                    ch=input()
                    ch=ch.upper()
                    if len(ch)==1 or ch in hidden:
                        new_hidden = guess(word_dict, hidden, ch)
                        if new_hidden:
                            hidden = new_hidden
                        else:
                            no_of_guesses -= 1
                else:
                    winner()
                    break
            if no_of_guesses==0:
                loser()
        else:
            print ('Try Again')
        print('\nPress Y to Play Again, anything else to quit : ',end=' ')
        chp=input()
        chp=chp.upper()
        if chp!='Y':
            Flag=False