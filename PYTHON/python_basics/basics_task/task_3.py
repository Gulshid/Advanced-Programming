# MAke the Program which take all data type and display in one line 
integer_num=int(input("Enter the Integer Number:"))
float_num=float(input("Enter the Decimal  Number:"))
String_value=str(input("Enter the String value:"))
Boolean_value= bool(input("Enter the Boolean Value"))

set_value=set(input('Enter the set value:'))
list_value=list(input('Enter the list value:'))
tuple_value=tuple(input('Enter the tuple value:'))
dict_value=eval(input('Enter the dict value:'))

print(f"Integer Number is : {integer_num}, Float Number is : {float_num} , String Value is : {String_value} , Boolean Value is :{Boolean_value}, List Number is :{list_value} , Tuple Number is :{tuple_value}, Set Number is :{set_value} , Dict value is :{dict_value}")