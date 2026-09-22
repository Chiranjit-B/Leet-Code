class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr = []
        for i in range(1,n+1) :
            if n < 3 :
                arr.append(str(i))
            elif i%3 == 0 and i%5!= 0:
                arr.append('Fizz')
            elif i%5 == 0 and i%3 != 0:
                arr.append('Buzz')
            elif i%3 == 0 and i%5 == 0:
                arr.append('FizzBuzz')
            else :
                arr.append(str(i))
            
        return arr