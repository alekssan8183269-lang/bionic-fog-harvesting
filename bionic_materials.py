import numpy as np

class TropicalBionicFluid:
    """
    Тропический модуль для расчета критических состояний капли на бионической поверхности.
    Использует Max-Plus логику для определения доминирующего физического процесса.
    """
    def __init__(self, surface_tension=0.0728, tilt_angle=45):
        self.sigma = surface_tension  # Поверхностное натяжение воды (Н/м)
        self.theta = np.radians(tilt_angle) # Угол наклона панели

    def calculate_forces(self, droplet_radius, wind_speed, air_density=1.225):
        """
        Сравнивает три силы, действующие на каплю на выступе:
        1. Сила гравитации (тянет вниз)
        2. Сила аэродинамического давления ветра (прижимает/сдвигает)
        3. Сила капиллярного удержания (удерживает каплю на гидрофильном пике)
        """
        volume = (4/3) * np.pi * (droplet_radius**3)
        mass = volume * 1000  # Плотность воды 1000 кг/м³
        
        # 1. Гравитационный сдвиг
        F_gravity = mass * 9.81 * np.sin(self.theta)
        
        # 2. Сила ветра (аэродинамическое сопротивление)
        A_front = np.pi * (droplet_radius**2)
        F_wind = 0.5 * air_density * (wind_speed**2) * A_front * 0.47 # Cd сферы = 0.47
        
        # 3. Капиллярное удержание (Сила сцепления)
        F_capillary = 2 * np.pi * droplet_radius * self.sigma
        
        return F_gravity, F_wind, F_capillary

    def predict_droplet_behavior(self, droplet_radius, wind_speed):
        """
        Тропический оператор (Max-Plus). 
        Определяет, какой процесс побеждает прямо сейчас в данной точке геометрии панциря жука.
        """
        F_g, F_w, F_c = self.calculate_forces(droplet_radius, wind_speed)
        
        # Нам нужно понять, перевешивают ли отрывающие силы (гравитация + ветер) удерживающую капиллярную силу
        detachment_potential = (F_g + F_w) - F_c
        
        # Тропическое ветвление:
        # Если потенциал > 0 -> Капля срывается в желоб (Успех)
        # Если потенциал <= 0 -> Капля сидит на месте и испаряется (Стагнация)
        if detachment_potential > 0:
            return "DETACHMENT"  # Вода стекает в резервуар
        else:
            return "HOLD"        # Капля слишком мала или ветер слаб
