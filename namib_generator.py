import numpy as np
from scipy.optimize import minimize

# =================================================================
#  ⚡ PROJECT RE-PHYSICS: MODULE "NAMIB-CORE" (v1.0.0)             
#  ⚡ Computational Bionic Design Engine for Fog Harvesting         
# =================================================================

# --- 1. ФИЗИЧЕСКИЕ КОНСТАНТЫ ---
RHO_WATER = 1000.0  # Плотность воды (кг/м3)
G = 9.81            # Ускорение свободного падения (м/с2)
SIGMA = 0.072       # Поверхностное натяжение воды (Н/м)
CONTACT_ANGLE = np.radians(110) # Угол контакта на гидрофобном склоне (в радианах)

class NamibeOptimizer:
    def __init__(self, wind_speed, fog_density):
        """
        wind_speed: скорость ветра (м/с)
        fog_density: плотность тумана / водного пара (кг/м3)
        """
        self.wind_speed = wind_speed
        self.fog_density = fog_density

    def calculate_critical_drop_radius(self, R_bump):
        """
        Вычисляет критический радиус капли, при котором она 
        срывается с бугорка под действием силы тяжести.
        """
        # Упрощенный баланс сил: Сила тяжести капли >= Силе сцепления на границе бугорка
        # (4/3) * pi * r_drop^3 * rho * g = 2 * pi * R_bump * sigma * sin(theta)
        numerator = 1.5 * R_bump * SIGMA * np.sin(CONTACT_ANGLE)
        denominator = RHO_WATER * G
        
        # Защита от отрицательных значений
        if numerator <= 0:
            return 0.001
            
        r_critical = (numerator / denominator) ** (1/3)
        return r_critical

    def water_collection_rate(self, params):
        """
        Целевая функция, которую мы хотим МАКСИМИЗИРОВАТЬ.
        params[0]: R_bump - радиус бугорка (в метрах)
        params[1]: Distance - расстояние между центрами бугорков (в метрах)
        """
        R_bump, distance = params
        
        # Ограничение геометрии: расстояние между центрами не может быть меньше двух радиусов
        if distance <= 2 * R_bump:
            return 1e6 # Возвращаем огромный штраф, так как оптимизатор минимизирует функцию
            
        # 1. Считаем поток влаги, сталкивающийся с одним бугорком (пропорционально площади сечения)
        cross_section_area = np.pi * (R_bump ** 2)
        moisture_flux = cross_section_area * self.wind_speed * self.fog_density # кг/с на один бугорок
        
        # 2. Считаем критическую массу капли перед срывом
        r_crit = self.calculate_critical_drop_radius(R_bump)
        m_crit = (4/3) * np.pi * (r_crit ** 3) * RHO_WATER
        
        # Время, необходимое для роста одной капли до срыва
        time_to_detach = m_crit / (moisture_flux + 1e-12)
        
        # Частота срывов капель (капель в секунду с одного бугорка)
        drops_per_second = 1.0 / (time_to_detach + 1e-12)
        
        # 3. Считаем количество бугорков на 1 квадратном метре поверхности
        # Предполагаем квадратную сетку размещения бугорков
        bumps_per_m2 = 1.0 / (distance ** 2)
        
        # Итоговая масса собранной воды с 1 кв. метра в секунду (кг / (м2 * с))
        total_water_mass = drops_per_second * m_crit * bumps_per_m2
        
        # scipy умеет только минимизировать, поэтому возвращаем отрицательное значение,
        # чтобы найти максимум сбора воды
        return -total_water_mass

    def optimize_surface(self):
        """
        Запуск процесса генеративного дизайна геометрии
        """
        # Начальная догадка: радиус бугорка 0.5 мм, расстояние 2 мм
        initial_guess = [0.0005, 0.002]
        
        # Границы для поиска (Bounds):
        # Радиус от 0.1 мм до 5 мм
        # Расстояние от 0.5 мм до 20 мм
        bounds = [(0.0001, 0.005), (0.0005, 0.020)]
        # Заменяем метод на Nelder-Mead, он не боится обрывов функции в ноль
        result = minimize(self.water_collection_rate, initial_guess, bounds=bounds, method='Nelder-Mead')
        
        return result

# --- 2. ПРИМЕР ИСПОЛЬЗОВАНИЯ ---
if __name__ == "__main__":
    # Параметры среды (например, типичное утро в пустыне Намиб или африканской саванне)
    WIND = 3.5          # Скорость ветра 3.5 м/с
    FOG = 0.0005        # Плотность влажного тумана (0.5 г на кубический метр)
    
    optimizer = NamibeOptimizer(wind_speed=WIND, fog_density=FOG)
    optimization_result = optimizer.optimize_surface()
    
    if optimization_result.success:
        best_r, best_dist = optimization_result.x
        # Переводим в миллиметры для удобства инженера
        print("=== ОПТИМАЛЬНАЯ ГЕОМЕТРИЯ ПОВЕРХНОСТИ РАССЧИТАНА ===")
        print(f"Оптимальный радиус бугорка: {best_r * 1000:.2f} мм")
        print(f"Оптимальное расстояние между бугорками: {best_dist * 1000:.2f} мм")
        print(f"Прогнозируемый сбор воды: {-optimization_result.fun * 3600:.2f} кг/ч с одного кв. метра!")
    else:
        print("Ошибка оптимизации:", optimization_result.message)
