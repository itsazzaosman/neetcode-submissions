class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_minus_number = -1

        for i in range(len(arr) - 1, -1, -1):
            number_picked_up = arr[i]
            # print(numbers)
            arr[i] = last_minus_number

            if number_picked_up > last_minus_number:
                last_minus_number =  number_picked_up
        return arr

        