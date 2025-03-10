num = int(input("Enter a number: "))  # รับค่าตัวเลขจากผู้ใช้
num2 = 1  # เริ่มต้นตัวคูณที่ 1

while num2 <= 12:  # ทำซ้ำตั้งแต่ 1 ถึง 12
    num3 = num * num2  # คำนวณค่าผลคูณ
    print(f"{num} x {num2} = {num3}")  # แสดงผลลัพธ์
    num2 += 1