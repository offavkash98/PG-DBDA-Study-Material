bca_dept = set()
btech_dept = set()

gf = int(input("how many boy friends in bsc:"))
for i in range(gf):
    name = input("enter a name:")
    bca_dept.add(name)

gf = int(input("how many boyfriend in b.tech:"))
for i in range(gf):
    name = input("enter a name:")
    btech_dept.add(name)
    
print("bca boyfriend:",bca_dept)
print("b.tech boyfrieend:",btech_dept)
print("all boyfriends my gf:",bca_dept|btech_dept)

print("common boyfriends:",bca_dept&btech_dept)
print("only  bca boyfriends:",bca_dept-btech_dept)

print("only b.tech boyfriends:",btech_dept-bca_dept)
print("try to move on seen this situation")
print("mujhe dhoka de kr chali gye")
print("ab usse bt kr rhi hogi soch ke bda taqleef hoti h mujhe")
