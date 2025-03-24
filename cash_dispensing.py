amount=int(input("Enter the amount in multiple of 500"))
count_five=0
count_two=0
while(amount!=0):
  if amount%2000==0:
   amount=amount-2000
   count_two=count_two+1
  elif amount%500==0:
   amount=amount-500
   count_five+=count_five+1
  else:
   print("Amount unavailable")

print(f"You have got {count_five} notes of 500 and {count_two} notes of 2000")