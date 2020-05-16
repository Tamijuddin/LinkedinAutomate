def get_var_value(filename="varstore.py"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

your_counter = get_var_value()

list = [
    'Tough times don’t last. Tough people do.',
    'Keep going. Everything you need will come to you at the perfect time.',
    'You have to be at your strongest when you’re feeling at your weakest.',
    'Never give up. Great things take time. Be patient.',
    'It does not matter how slowly you go as long as you do not stop.',
    'Courage is one step ahead of fear.',
    'Whatever is worrying you right now, forget about it. Take a deep breath, stay positive and know that things will get better',
    'If you feel like giving up, just look back on how far you are already.',
    'Look in the mirror. That’s your competition.',
    'Focus on your goal. Don’t look in any direction but ahead.',
    'Everything you’ve ever wanted is on the other side of fear.',
    'Pain is temporary. Quitting lasts forever.',
    'The pain you feel today will be the strength you feel tomorrow.',
    'We must embrace pain and burn it as fuel for our journey.',
    'A problem is a chance for you to do your best.',
    'Hard times don’t create heroes. It is during the hard times when the ‘hero’ within us is revealed.',
    'Remember it’s just a bad day, not a bad life.',
    'It’s not about perfect. It’s about effort.',
    'Believe you can and you’re halfway there',
    'Challenges are what make life interesting. Overcoming them is what makes them meaningful.',
    'You are so much more than what you are going through.',
    'Passion first and everything will fall into place.',
    'You don’t gain anything from stressing. Remember that.',
    'Difficult roads always lead to beautiful destinations.',
    'Staying positive does not mean that things will turn out okay. Rather it is knowing that you will be okay no matter how things turn out.',
    'Success is what happens after you have survived all of your disappointments.',
    'Goals may give focus, but dreams give power.',
    'Don’t wish it were easier. Wish you were better.'
    ]

text = list[your_counter-1]

    

