shop = {
    "apple": 20,
    "laptop": 800,
    "pen": 10,
    "phone": 600,
    "notebook": 80
}
more_than_50={}
for key,value in shop.items():#for i in shop.values()
   if(value>50):
      more_than_50[key]=value

for key , value  in more_than_50.items():
  print(f"{key} : {value}")