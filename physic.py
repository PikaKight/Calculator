import typing, math

class Base_velocity_equation:
    def velocity(self, d:float, t:float) -> float:
        self._velocity = d / t
        return self._velocity

    def distance(self, v:float, t:float) -> float:
        self._distance = v * t
        return self._distance

    def time(self, v:float, d:float) -> float:
        self._time = d/v
        return self._time

class No_distance:
    def velocity_final(self, vinit:float, a:float, t:float) -> float:
        self._velocity_final = vinit + a*t
        return self._velocity_final
    
    def velocity_init(self, vfin:float, a:float, t:float) -> float:
        self._velocity_init = vfin - a*t
        return self._velocity_init

    def acceleration(self, vfin:float, vinit:float, t:float) -> float:
        self._acceleration = (vfin - vinit) / t
        return self._acceleration

    def time(self, vfin:float, vinit:float, a:float) -> float:
        self._time = (vfin - vinit) / a
        return self._time

class No_acceleration:
    def distance(self, vfin:float, vinit:float, t:float) -> float:
        self._distance = 0.5*(vfin + vinit)*t
        return self._distance

    def time(self, vfin:float, vinit:float, d:float) -> float:
        self._time = 2*d/(vfin + vinit)
        return self._time

    def velocity_init(self, vfin:float, t:float, d:float) -> float:
        self._velocity_init = (2*d/t) - vfin
        return self._velocity_init
    
    def velocity_final(self, vinit:float, t:float, d:float) -> float:
        self._velocity_final = (2*d/t) - vinit
        return self._velocity_final

class No_time:
    def velocity_final(self, vinit:float, a:float, d:float) -> float:
        self._velocity_final = math.sqrt(vinit**2 + 2*a*d)
        return self._velocity_final
    
    def velocity_init(self, vfin:float, a:float, d:float) -> float:
        self._velocity_init = math.sqrt((vfin**2) - (2*a*d))
        return self._velocity_init
    
    def acceleration(self, vfin:float, vinit:float, d:float) -> float:
        self._acceleration = ((vfin**2) - (vinit**2)) / (2*d)
        return self._acceleration
    
    def distance(self, vfin:float, vinit:float, a:float) -> float:
        self._distance = ((vfin**2) - (vinit**2)) / (2*a)
        return self._distance

class No_final_velocity:
    def distance(self, vinit:float, a:float, t:float) -> float:
        self._distance = vinit*t + 0.5*a*(t**2)
        return self._distance
    
    def velocity_init(self, d:float, a:float, t:float) -> float:
        self._velocity_init = (d - 0.5*a*(t**2)) / t
        return self._velocity_init
    
    def acceleration(self, vinit:float, d:float, t:float) -> float:
        self._acceleration = (d - vinit) / (0.5*(t**2))
        return self._acceleration
    
    def time(self, vinit:float, d:float, a:float) -> float:
        if vinit**2 + 2 *d*a > 0:
            self._time_1 = (-vinit + math.sqrt(vinit**2 + 2*d*a)) / (a)
            self._time_2 = (-vinit - math.sqrt(vinit**2 + 2*d*a)) / (a)
            return self._time_1, self._time_2
        elif vinit**2 + 2*d*a == 0:
            self._time = -vinit/ (a)
            return self._time
        else:
            return "No possible solution without using complex numbers!"
