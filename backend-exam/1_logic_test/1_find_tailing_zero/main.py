"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        # ถ้าน้อยกว่าหรือเท่ากับ 0 ให้ ส่งข้อความเตือน
        if number <= 0:
            return "number cant be negative or zero"
        else:
            # หาค่า factorial ของ number 
            result_fact = 1 
            while number > 0:
                result_fact = result_fact * number
                number = number -1 
            # แปลงเป็น String เพื่อหา 0 ตัวท้าย
        find0 = str(result_fact)
        count = 0
        # ให้เริ่มloop ที่ตัวสุดท้าย ที่ - 1 เพราะ ตัว range(len(find0) มันบอกจำนวนสมาชิคทั้งหมดโดยที่ไม่นับ 0  
        for i in range(len(find0) -1 ,-1,-1):
            # ถ้าเจอ 0 ให้ นับเพื่ม 
            if (find0[i]) == "0":
                count = count + 1 
            # ถ้าไม่เจอให้ออกจาก loop เลย 
            else:
                break
        return count
obj = Solution()
result1 = obj.find_tailing_zeroes(7)
result2 = obj.find_tailing_zeroes(-10)
print(result1)
print(result2)