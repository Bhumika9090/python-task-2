#  EVEN OR ODD

# def even_or_odd(num):
#     # num = int(input("enter a number"))
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# even_or_odd(9)      



# # swappint two number

# def swap_two_num(num1,num2):
#     temp = num1
#     num1 = num2
#     num2 = temp
#     print(num1,num2)
# swap_two_num(5,7)
  
# to find number index of list
def index_number(list,num):
    for index , value in enumerate(list):
        if value == num:
            print(f"number found at index{index}")
            break
    else:
       print("number not found")
index_number([3,6,8,2,6],8)


 