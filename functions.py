def c_sound_f(T, k, R):
  c_square = T * k * R

  if c_square < 0:
    print("Speed of sound must be a positive value!")
    return 0

  return (c_square)**(0.5)
