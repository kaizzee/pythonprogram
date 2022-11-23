list1=[60,77,56,43,86,76,20]
def odd_even(list1):
    odd,even=0,0
    for i in list1:
        if i%2==0:
            even=even+1

        else:
            odd=odd+1

    print("even number is=",even)
    print("odd number is=",odd)
odd_even(list1)
