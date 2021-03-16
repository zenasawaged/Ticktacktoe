

monthConversions = dict(Jan="January", Feb="February", Mar="March", Apr="April", May="May")
print(monthConversions.get("luv", "Not a Valid Key"))
i= 1
while i <=11:
    print (i)
    i= i+1

print ("Done with loop")


friends=["jim", "Karen", "Kevin"]
for index in range(5):
    if index==0:
        print ("friends iteration")
else:
    print("Not first")

def raise_to_power(base_num, pow_num):
    result=1
    for index in range (pow_num):
        result= result * base_num
    return result
print (raise_to_power(3,2))
