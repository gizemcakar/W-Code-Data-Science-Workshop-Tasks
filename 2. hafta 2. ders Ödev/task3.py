# 3 - transform this example to enumarate method

meyveler = ["elma", "armut", "muz", "çilek", "kivi"]

#example:
print("---------by for loop------------")
for index in range(len(meyveler)):
    print("{}. indexte bulunan meyve: {}".format(index,meyveler[index]))

print("-------by enumarate method------")
# transform to enumerate method

for index, value in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, value))