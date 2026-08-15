"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number > 10000000 or number < 0 :
            return "ไม่สามารถรับค่าเกินสิบล้าน หรือน้อยกว่า 0 ได้"
        result = ""
        # แปลงจาก int ไปเป็น str 
        stringnumber = str(number)
        # list เก็บคำของตัวเลขเพื่อใช่ใน loop 
        num_str = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่","ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        # list เก็บหลักแต่ละหลักเพื่อใช่ใน loop 
        unit = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        # เก็บตัวเลขที่ได้จาก number 
        num_of_result = []
        # หาจำนวนหลัก และ เก็บตัวเลขไว้ตามตำแหน่งของเลข
        for i in range(len(stringnumber)):
            num_of_result.append(int(stringnumber[i]))
        print(num_of_result)
        count_result = len(num_of_result) - 1
        # เริ่ม loop จากหลักที่มากที่สุด
        for i in range(len(num_of_result) - 1, -1, -1):
            # -1 เพื่อเอาตำแหน่ง และ - i เพื่อเอาตำแหน่งของ loop 
            current_num = num_of_result[len(num_of_result) - 1 - i]
            # ถ้าเจอ 0 ให้ปล่อยผ่านไปเลยโดยไม่ต้องเพื่มทั้งเลขและหลัก
            if current_num == 0:
                # -1เพื่อเอาตำแหน่งที่ 0 เพราะตัว count_result จะมีแค่จำนวนสมาชิคไม่ใช่ ตำแหน่ง
                count_result = count_result - 1
                continue
            # หลักสิบถ้าเจอ 2 ให้ใส่เป็น ยี่สิบ  และ ถ้าเจอ 1 ให้ใส่เป็น สิบ
            if i == 1:
                if current_num == 1:
                    result += "สิบ"
                elif current_num == 2:
                    result += "ยี่สิบ"
                else:
                    result += num_str[current_num] + "สิบ"
            # หลักหน่วย
            elif i == 0:
                # ถ้ามีมากกว่าหลักหน่วยแล้วเจอ1ให้แก้เป็น เอ็ด
                if current_num == 1 and len(num_of_result) > 1:
                    result += "เอ็ด"
                else:
                    result += num_str[current_num]
            else:
                result += num_str[current_num] + unit[i]
            count_result -= 1
        return result
obj = Solution()
result1 = obj.number_to_thai(101)
result2 = obj.number_to_thai(-1)
print(result1)
print(result2)