from physic import *

def test_base_velocity_equation():
   assert Base_velocity_equation().velocity(5.0,5.0) == 1.0
   assert Base_velocity_equation().distance(5.0,5.0) == 25.0
   assert Base_velocity_equation().time(5.0,5.0) == 1.0

def test_no_distance():
   assert No_distance().velocity_final(5,6,1) == 11