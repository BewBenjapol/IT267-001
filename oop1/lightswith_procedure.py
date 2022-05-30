#lightswith_procedure.py
#สร้างฟังก์ชั่นเปิด/ปิดไฟ

def turnon():
    global switch_status
    switch_status = True #สถานะเป็นเปิดไฟ
    

#สร้างฟังก์ชั่นเปิดไฟ
def turnoff():
    global switch_status
    switch_status = False

switch_status = False
print(f"Status ={switch_status}") #False
turnon()
print(f"Status ={switch_status}") #True
turnoff()
print(f"Status ={switch_status}") #False
