nums = []

while True:
    user_input = input("Anna luku (tyhjä lopettaa): ")
    if user_input == "":
        break
    nums.append(float(user_input))

if len(nums) > 0:
    print("Pienin:", min(nums))
    print("Suurin:", max(nums))
else:
    print("Et lukua.")