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