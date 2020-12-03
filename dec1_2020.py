# Dec 1 Puzzle #

def open_and_read_file(file_path):
   
    f = open(file_path, 'r')
    f = f.read()
   
    return f

def sort_nums(input_str):
    
    inputs = input_str.strip().split()
    sorted_inputs = []

    for num in inputs:
        new_num = int(num)
        sorted_inputs.append(new_num)

    sorted_inputs = sorted(sorted_inputs)
    #print(sorted_inputs)
    return sorted_inputs

def find_2020(sorted_inputs):
    # eliminate nums that are too big

    reduced_nums = []

    for num in sorted_inputs:
        compare = 2020 - sorted_inputs[0]
        if num < compare:
            reduced_nums.append(num)

    print("LENGTHS: ", len(sorted_inputs), len(reduced_nums))
    print(reduced_nums)
    #print(reduced_nums)

    # slice_index = len(sorted_inputs) / 2
    # slice_index = int(slice_index)

    # little_nums = sorted_inputs[0:slice_index]
    # big_nums = sorted_inputs[slice_index:]

    # tail_counter = slice_index - 1
    

    # for little_num in little_nums:
    #     # print(little_num, little_nums[tail_counter - 1])
    #     if (little_num + little_nums[tail_counter] == 2020):
    #         print("FOUND 2020 with nums: ", num, sorted_inputs[tail_counter])
    #         print("HERE'S THE FINAL PRODUCT: ", num*sorted_inputs[tail_counter])
    #     else:
    #         tail_counter -= 1
    #         print(little_num + little_nums[tail_counter])

def find_sum_to_2020_better(nums):
    counterparts = set()

    for num in nums:
        if 2020-num in nums:
            
            return num, 2020-num #num:  788 2020-num:  1232


            
    
        # for big_num in big_nums:
        #     print("sum is: ", little_num + big_num)
        #     if (little_num + big_num == 2020):
        #         print("FOUND 2020 with nums: ", num, sorted_inputs[tail_counter])
        #         print("HERE'S THE FINAL PRODUCT: ", num*sorted_inputs[tail_counter])
      
    


def find_three_sum_to_2020(nums):
    for num in nums:
        for num2 in nums:
            for num3 in nums:
                if num + num2 + num3 == 2020:
                    print(num, num2, num3)
                    return (num, num2, num3) 






file_path = "1_input.txt"
input_str = open_and_read_file(file_path)
sorted_inputs = sort_nums(input_str)
find_2020(sorted_inputs)
find_sum_to_2020_better(sorted_inputs)
find_three_sum_to_2020(sorted_inputs)
