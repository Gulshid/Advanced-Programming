def list_operation():
    # 1
    numbers =[1,2,3,4,5,6,7,89]
    for i in numbers:
        print(i)
        
    # 2 
    fruit = ["Apple", "banana", "peach"]
    for i in range(len(fruit)):
        print(f"index{i} :{fruit[i]}")
        
    # 3
    score = [1,2,3,4,5]
    for i in range(len(score)):
        score[i] += 3
    print(score) 
        
    # 4
    color = ["Red", "blue", "green", "Yellow"]
    index = 0
    while index < len(color):
        print(index+1)
        index = index + 1

    
list_operation()

