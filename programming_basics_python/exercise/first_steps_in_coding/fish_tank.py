ONE_LITER= 1000

#INPUT
length = int(input())
width = int(input())
height = int(input())
percent = float(input())
#CALCOLATIONS
volume = length * width * height
volume = (volume - (volume * (percent/100))) / ONE_LITER
print(volume)