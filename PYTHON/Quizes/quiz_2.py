def borrow_book(book_type, member_type, days_borrowed, has_library_card):
    fee = 0
    

    if member_type == "guest" and book_type in ["reference", "rare"]:
        return f" Borrowing denied: Guests cannot borrow {book_type} books."
    if book_type == "rare" and member_type != "faculty":
        return f" Borrowing denied: Only faculty can borrow rare books."
    

    if book_type == "regular":
        free_days = 5
        if days_borrowed > free_days:
            if member_type == "student":
                fee += (days_borrowed - free_days) * 1
            elif member_type == "faculty":
                fee += (days_borrowed - free_days) * 0.5
            elif member_type == "guest":
                fee += (days_borrowed - free_days) * 2
    
    elif book_type == "reference":
        free_days = 2
        if days_borrowed > free_days:
            fee += (days_borrowed - free_days) * 2
    
    elif book_type == "rare":
        free_days = 0
        if days_borrowed > free_days:
            fee += (days_borrowed - free_days) * 5
    

    if not has_library_card:
        fee += 10
    
    return f" Borrow successful: Total fee = ${fee:.2f}"



print(borrow_book("regular", "student", 7, True))   
print(borrow_book("regular", "faculty", 10, False)) 
print(borrow_book("regular", "guest", 8, True))   
print(borrow_book("reference", "faculty", 5, True))
print(borrow_book("reference", "guest", 3, True)) 
print(borrow_book("rare", "faculty", 4, False))    
print(borrow_book("rare", "student", 2, True))     
