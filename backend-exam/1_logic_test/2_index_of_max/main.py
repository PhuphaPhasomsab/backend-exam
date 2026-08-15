"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:

        if not numbers:
            return "list can not blank"
        # index เอาไว้เทียบค่ามากที่สุด
        Max_index = 0
        # เริ่มจาก 0 ไป ถึงตัวสุดท้ายของ numbers  ค่า index ไม่ใช่ค่า value แต่เป็นตำแหน่ง 
        for index in range(len(numbers)):
            # เอาตำแหน่ง index , Max_index  ไปเทียบค่า value  
            if numbers[Max_index] < numbers[index]:
                Max_index  = index
        return Max_index
obj = Solution()
result = obj.find_max_index([1,2,1,3,5,6,4])
print(result)