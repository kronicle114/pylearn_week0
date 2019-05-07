# def subtractor(a, b): 
#    """I subtract b from a and return the result"""  
#    print("I'm a function. My name is {}".format(subtractor.__name__))
#    print("I'm about to subtract {} and {}\n\n".format(a,b))
#    return a - b  # i output a value by using the return statement


# if __name__ == '__main__':
#    subtractor(3, 2)

# def print_function():
#    """I'm also a function, but I don't take any parameters"""
#    print("I'm {}, and I'm printing now".format(print_function.__name__))

# if __name__ == '__main__':
#    print_function()

# def function3(a=1, b=1): 
#   """I'm a function that calls other functions """
#   print("I'm {} and I'm about to call subtractor function".format(function3.__name__))
#   total = subtractor(a,b)
#   print("I'm {} and I'm about to call print_function".format(function3.__name__))
#   print_function()
#   print("I'm {} and I'm about return total".format(function3.__name__))
#   return total

# if __name__ == '__main__':
#   total = function3()
#   print("total is {}".format(total))

""" =======  side effects ======= """
def side_effect_test(value):
  # Do something to modify the value, assuming that value is a list
  value[1] = "orange" 
  print("Inside the fn, the value becomes {}".format(value))

def number_side_effect(value):
  value[0] = 2
  print("Inside number_side_effect, the value becomes {}".format(value))

def tuple_side_effect(value):
  value[2] = (15,)
  print("Inside tuple_side_effect, the value becomes {}".format(value))

def bool_side_effect(value):
  value = True
  print("Inside bool_side_effect, the value becomes {}".format(value))

if __name__ == "__main__":
  #Create the value
  value = ["red", "green", "blue"]
  
  print("Outside the fn, the value starts as {}".format(value))

  side_effect_test(value)

  print("outside the fn, the value is now {}".format(value))

  print("calling {}".format(number_side_effect.__name__))
  
  number_side_effect(value)

  print("outside the fn, the value is now {}".format(value))

  print("calling {}".format(tuple_side_effect.__name__))
  
  tuple_side_effect(value)

  print("outside the fn, the value is now {}".format(value))

  print("calling {}".format(bool_side_effect.__name__))
  
  bool_side_effect(value)

  print("outside the fn, the value is now {}".format(value))
