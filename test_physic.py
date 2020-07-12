from physic import *

def test_base_velocity_equation():
   # assert True is False
   assert Base_velocity_equation().velocity(5.0,5.0) == 1.0
   assert Base_velocity_equation().distance(5.0,5.0) == 25.0
   assert Base_velocity_equation().time(5.0,5.0) == 1.0

def test_no_distance():
   # assert True is False
   assert No_distance().velocity_final(5,6,1) == 11
   assert No_distance().velocity_init(7,6,1) == 1   
   assert No_distance().acceleration(6,5,1) == 1
   assert No_distance().time(82,65,1) == 17

def test_no_acceleration():
   # assert True is False
   assert No_acceleration().distance(5,5,2) == 10
   assert No_acceleration().time(5,5,10) == 2
   assert No_acceleration().velocity_init(5,4,2) == -4
   assert No_acceleration().velocity_final(5,4,2) == -4

def test_no_time():
   # assert True is False
   assert No_time().velocity_final(5,-2,4) == 3