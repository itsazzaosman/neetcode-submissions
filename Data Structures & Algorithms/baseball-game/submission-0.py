class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # ops = ["1", "2", "+", "C", "5", "D"]
        store = []

        for operation in operations:
            if operation == "+":
                store.append(store[-1] + store[-2])
            elif operation == "C":
                store.pop()  
            elif operation == "D":
                store.append(store[-1] * 2)  
            else:
                store.append(int(operation))  
        total_score = sum(store)
        return total_score
