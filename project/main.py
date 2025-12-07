from Algorithms import Algorithms_sort

def main():
    try:
        user_input = input("Array Number input (example: 5 3 1 4): ")
        algorithm_input = input("Choose Algorithm (Quick or Bubble): ").lower()
        reverse = input("Reverse sort? (Yes or No): ").lower()

        reverse = True if reverse == "yes" or reverse == "y" else False
            
        arr = [int(x) for x in user_input.split()]

        x = Algorithms_sort()

        if algorithm_input == "quick" or algorithm_input == "q":
            result = x.quick_sort(arr, reverse=reverse)
        elif algorithm_input == "bubble" or algorithm_input == "b":
            result = x.bubble_sort(arr, reverse=reverse)
        else:
            print("Invalid algorithm! Choose Quick or Bubble.")
            return

        print("Sorted:", result)

    except:
        print("Invalid Input")


if __name__ == "__main__":
    main()
