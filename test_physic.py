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
   assert No_time().velocity_init(5,2,4) == 3
   assert No_time().acceleration(5,4,4.5) == 1
   assert No_time().distance(5,-2,3) == 3.5

def test_no_final_velocity():\
   # assert True is False
   assert No_final_velocity().distance(3, 5, 7) == 143.5
   assert No_final_velocity().velocity_init(5, 3, 5) == -6.5
   assert No_final_velocity().acceleration(5, 3, 5) == -0.16
   assert No_final_velocity().time(5, 4, -2) == (1.0, 4.0)  
   assert No_final_velocity().time(5, 2.5, -5) == 1
   assert No_final_velocity().time(5, 6, -5) == "No possible solution without using complex numbers!"

def test_no_initial_velocity():
   # assert True is False
   assert No_initial_velocity().distance(10, 6, 3) == 3
   assert No_initial_velocity().velocity_final(10, 6, 3) == 30.5
   assert No_initial_velocity().acceleration(10, 5, 3) == 3.76
   assert No_initial_velocity().time(10, 4, 8) == (4, 1)
   assert No_initial_velocity().time(10, 2, 25) == 5
   assert No_initial_velocity().time(10, 3, 25) == "No possible solution without using complex numbers!"