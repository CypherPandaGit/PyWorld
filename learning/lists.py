# ip_address = input("Please input an IP address: ")
# print(ip_address.count("."))


parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

print("This parrot is ...")
print("What you want to add? ")
parrot_list.append(input())
for state in parrot_list:
    print("This parrot is " + state)
