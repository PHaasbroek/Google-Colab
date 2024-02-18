def c_sound(T, k, R):
  # T is temperature [K]
  # k is heat capacity ratio [-]. Usually 1.4 for air
  # R is the specific gas constant. Usually = 287 # [J/kg/K] for air
  
  c_square = T * k * R 

  if c_square < 0: # test to see if positive
    print("Speed of sound must be a positive value!")
    return 0

  return (c_square)**(0.5)

def density (p, R, T):
  # T is temperature [K]
  # p is pressure [Pa]. 
  # R is the specific gas constant. Usually = 287.0 # [J/kg/K] for air
  
  return p / R / T
