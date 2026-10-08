'''REARRANGE EVEN LENGTH TUPLE BY PLACING MIDDLE ELEMENTS AT ENDS

Write a function add_middle_elems_to_ends_in_even_length_tuple that takes a tuple of even length and performs the following operations:

1. Extract the two middle elements.
2. Place the first middle element at the beginning and the second middle element at the end.
3. Return the newly rearranged tuple.

NOTE:
This is a function type question. You don't have to take input or print the output. Just complete the required function definition.

EXAMPLES:

add_middle_elems_to_ends_in_even_length_tuple((10, 20, 30, 40))
→ (20, 10, 40, 30)

add_middle_elems_to_ends_in_even_length_tuple(("Lenovo", "Dell", "HP", "Asus"))
→ ("Dell", "Lenovo", "Asus", "HP")'''


#ANSWER
def add_middle_elems_to_ends_in_even_length_tuple(t):
    mid = len(t)//2
    return (t[mid-1],) + (t[:mid-1]) + (t[mid+1:]) + (t[mid],)

print(add_middle_elems_to_ends_in_even_length_tuple((10, 20, 30, 40)))
