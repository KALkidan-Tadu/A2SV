class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = []
        operands = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operands:
                opr1 = operation.pop()
                opr2 = operation.pop()
                if token == "+": 
                    operation.append(opr1 + opr2)
                elif token == "-":
                    operation.append(opr2 - opr1)
                elif token == "*":
                    operation.append(opr1 * opr2)
                else:
                    operation.append(int(opr2 / opr1))
            else:
                operation.append(int(token))
        return operation[0]

