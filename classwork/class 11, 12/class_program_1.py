_money = int(input("enter value: "))
_2000_notes = _money//2000
print("Rs 2000 notes: ",_2000_notes)
_500_notes = (_money%2000)//500
print("Rs 500 notes: ",_500_notes)
_200_notes = (_money%500)//200
print("Rs 200 notes: ",_200_notes)
if _500_notes == 1 or 3:
    print("Rs 100 notes: ",((_money - 500)%200)//100)
elif _500_notes == 2:
    print("Rs 100 notes: ",(_money%200)//100)
_50_notes = (_money%100)//50
print("Rs 50 notes: ",_50_notes)
_20_notes = (_money%50)//20
print("Rs 20 notes: ",_20_notes)
if _50_notes == 1:
    print("Rs 10 notes: ",((_money - 50)%20)//10)
elif _50_notes == 0:
    print("Rs 10 notes: ",(_money%20)//10)
_coins = _money%10
print("coins: ",_coins)
