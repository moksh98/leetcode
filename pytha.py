class pytha:
    def triplets(self, array):
        ans = []
        for i in range(len(array)-3):
            num1 = array[i]
            num2 = array[i+1]
            num3 = array[i+2]
            if self.isTriplet(num1, num2, num3):
                ans.append(1)
            else:
                ans.append(0)
    def isTriplet(self, num1, num2, num3):
        if num1*num1 + num2*num2 == num3*num3:
            return True
        elif num1*num1 + num3*num3 == num2*num2:
            return True
        elif num3*num3 + num2*num2 == num1*num1:
            return True
        else:
            return False