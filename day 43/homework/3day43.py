def sum_of_list(num_list):
    total=0
    for num in num_list:
        total+=num
    return total

def average_of_list(num_list):
    if len(num_list)==0:
     return 0  
    total=sum_of_list(num_list)
    average=total/len(num_list)
    return average
