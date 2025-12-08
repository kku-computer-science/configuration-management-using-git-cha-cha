class Algorithms_sort:
    def quick_sort(self, input, reverse=False):
        """
        input: takes number array input
        reverse: takes Boolean 
        """
        if len(input) <= 1:
            return input 

        pivot = input[len(input) // 2]
        
        less = [x for x in input if x < pivot]
        equal = [x for x in input if x == pivot]
        greater = [x for x in input if x > pivot]

        if reverse == True:
            return self.quick_sort(greater, reverse=True) + equal  + self.quick_sort(less, reverse=True)
            
        return self.quick_sort(less) + equal  + self.quick_sort(greater)
    
    def bubble_sort(self, input, reverse=False):
        """
        input: takes number array input
        reverse: takes Boolean 
        """
        
        n = len(input)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if (input[j] > input[j+1] and not reverse) or (input[j] < input[j+1] and reverse):
                    input[j], input[j+1] = input[j+1], input[j]
        return input