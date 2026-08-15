"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        # เก็บค่าตัวของตัวเลขและค่าของตัวเลขนั้นๆ
        roman_number = [["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"],
                        [1,4,5,9,10,40,50,90,100,400,500,900,1000]]
        result = ""
        if number <= 0:
            return "number can not less than 0"
        # ให้เริ่ม loop จากตัวสุดท้ายของ list เพื่อเอาตัวเลขที่มากที่สุดก่อน ถ้าน้อยกว่าให้เอาตัวเลขที่น้อยลงมาไปเทียบจนกว่าจะเจอค่าที่น้อยกว่า
        # number และเอาตัวเลขนั้นไปบวกกับ result และลบค่าของตัวเลขนั้นออกจาก number
        for i in range(len(roman_number[0]) - 1, -1, -1):
            while number >= roman_number[1][i]:
                result = result + roman_number[0][i]
                number = number - roman_number[1][i]
        return result
obj = Solution()
result = obj.number_to_roman(101)
print(result)
