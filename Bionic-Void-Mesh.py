import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh

# =================================================================
#  ⚡ PROJECT RE-PHYSICS: MODULE "NAMIB-CORE" (v1.0.0)             
#  ⚡ Computational Bionic Design Engine for Fog Harvesting         
# =================================================================

# --- 1. ФИЗИЧЕСКИЕ КОНСТАНТЫ ---
RHO_WATER = 1000.0  # Плотность воды (кг/м3)
G = 9.81            # Ускорение свободного падения (м/с2)
SIGMA = 0.072       # Поверхностное натяжение (Н/м)
CONTACT_ANGLE = np.radians(110) # Угол контакта капли на гидрофобном склоне

class NamibeWaterSystem:
    def __init__(self, wind_speed=3.5, fog_density=0.0005):
        self.wind_speed = wind_speed
        self.fog_density = fog_density

    def _get_critical_drop_radius(self, R_bump):
        """Расчет радиуса срыва капли по балансу сил тяжести и сцепления"""
        numerator = 1.5 * R_bump * SIGMA * np.sin(CONTACT_ANGLE)
        denominator = RHO_WATER * G
        # Используем np.maximum вместо встроенного max, чтобы поддерживать массивы numpy
        return (np.maximum(numerator, 1e-9) / denominator) ** (1/3)

    def calculate_yield(self, R_bump, distance):
        # Заменяем обычный if на векторную проверку numpy.
        # Если условие нарушено, yield будет равен 0.0, иначе пойдет расчет.
        
        # 1. Поток тумана на один бугорок
        cross_area = np.pi * (R_bump ** 2)
        moisture_flux = cross_area * self.wind_speed * self.fog_density
        
        # 2. Масса капли перед падением
        r_crit = self._get_critical_drop_radius(R_bump)
        m_crit = (4/3) * np.pi * (r_crit ** 3) * RHO_WATER
        
        # 3. Частота сброса капель
        time_to_detach = m_crit / (moisture_flux + 1e-12)
        drops_per_sec = 1.0 / (time_to_detach + 1e-12)
        
        # 4. Плотность бугорков на м2
        bumps_per_m2 = 1.0 / (distance ** 2)
        
        # Итог в кг/ч
        raw_yield = drops_per_sec * m_crit * bumps_per_m2 * 3600
        
        # Финальный фильтр: если бугорки накладываются (distance <= 2 * R_bump), 
        # сбросить выработку в 0.0, иначе вернуть посчитанный raw_yield
        return np.where(distance <= 2 * R_bump, 0.0, raw_yield)


    def optimize(self):
        """Оптимизация параметров геометрии"""
        objective = lambda p: -self.calculate_yield(p[0], p[1])
        res = minimize(objective, [0.0005, 0.002], bounds=[(0.0001, 0.005), (0.0005, 0.020)], method='L-BFGS-B')
        return res.x if res.success else (0.0005, 0.002)

    def plot_efficiency_map(self, best_r, best_dist):
        """Построение 3D-карты эффективности геометрии"""
        r_space = np.linspace(0.0001, 0.004, 100)
        d_space = np.linspace(0.0005, 0.015, 100)
        R, D = np.meshgrid(r_space, d_space)
        
        # Считаем выработку для каждой точки сетки
        Z = np.zeros_like(R)
        for i in range(R.shape[0]):
            for j in range(R.shape[1]):
                Z[i, j] = self.calculate_yield(R[i, j], D[i, j])

        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Наносим поверхность
        surf = ax.plot_surface(R * 1000, D * 1000, Z, cmap='viridis', edgecolor='none', alpha=0.8)
        
        # Подсвечиваем красной точкой оптимальное решение
        best_yield = self.calculate_yield(best_r, best_dist)
        ax.scatter([best_r * 1000], [best_dist * 1000], [best_yield], color='red', s=100, label='Оптимум жука Намиб')
        
        ax.set_title('Анализ эффективности сбора воды (Генеративный дизайн)', fontsize=14)
        ax.set_xlabel('Радиус бугорка (мм)')
        ax.set_ylabel('Расстояние между ними (мм)')
        ax.set_zlabel('Сбор воды (кг / ч * м²)')
        fig.colorbar(surf, shrink=0.5, aspect=5, label='Выход воды (кг/ч)')
        plt.legend()
        plt.show()

    def generate_stl(self, R_bump, distance, grid_size=4):
        """Создание готовой 3D-панели и сохранение в STL файл"""
        print(f"\n[Генерация 3D-модели] Создание сетки {grid_size}x{grid_size} бугорков...")
        
        # Создаем плоское основание толщиной 1 мм
        base_width = grid_size * distance
        base_length = grid_size * distance
        base_thickness = 0.001
        
        # Генерируем вершины для бугорков-полусфер
        vertices = []
        faces = []
        v_idx = 0
        
        # 1. Строим плоскость подложки
        # Простая коробка основания
        box_verts = [
            [0, 0, 0], [base_width, 0, 0], [base_width, base_length, 0], [0, base_length, 0],
            [0, 0, base_thickness], [base_width, 0, base_thickness], [base_width, base_length, base_thickness], [0, base_length, base_thickness]
        ]
        vertices.extend(box_verts)
        v_idx += 8
        
        # Грани коробки основания
        box_faces = [
            [0, 2, 1], [0, 3, 2], [4, 5, 6], [4, 6, 7], # низ и верх
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], # бока
            [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7]
        ]
        faces.extend(box_faces)

        # 2. Выращиваем полусферы на поверхности подложки
        for i in range(grid_size):
            for j in range(grid_size):
                # Центр текущего бугорка
                cx = (i + 0.5) * distance
                cy = (j + 0.5) * distance
                cz = base_thickness
                
                # Создаем сетку меша для одной полусферы
                segments = 12
                rings = 6
                local_verts = []
                
                # Вершина купола
                local_verts.append([cx, cy, cz + R_bump])
                start_v = v_idx
                v_idx += 1
                
                for r in range(1, rings):
                    phi = np.pi / 2 * (r / rings)
                    z = cz + R_bump * np.cos(phi)
                    rad = R_bump * np.sin(phi)
                    for s in range(segments):
                        theta = 2 * np.pi * (s / segments)
                        x = cx + rad * np.cos(theta)
                        y = cy + rad * np.sin(theta)
                        local_verts.append([x, y, z])
                        v_idx += 1
                
                vertices.extend(local_verts)
                
                # Соединяем вершины полусферы в треугольные полигоны (Грани)
                # Верхушка купола
                for s in range(segments):
                    next_s = (s + 1) % segments
                    faces.append([start_v, start_v + 1 + s, start_v + 1 + next_s])
                
                # Кольца полусферы
                for r in range(rings - 2):
                    r_start = start_v + 1 + r * segments
                    next_r_start = r_start + segments
                    for s in range(segments):
                        next_s = (s + 1) % segments
                        faces.append([r_start + s, next_r_start + s, next_r_start + next_s])
                        faces.append([r_start + s, next_r_start + next_s, r_start + next_s])

        # Сборка меша через numpy-stl
        vertices = np.array(vertices)
        faces = np.array(faces)
        
        surface_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        for idx, face in enumerate(faces):
            for k in range(3):
                surface_mesh.vectors[idx][k] = vertices[face[k]]
                
        # Сохраняем файл на диск
        filename = "namib_surface_panel.stl"
        surface_mesh.save(filename)
        print(f"[Успех] Файл 3D-панели сохранен как: '{filename}'. Можешь открывать в 3D-редакторах!")

# --- СЦЕНАРИЙ ЗАПУСКА ---
if __name__ == "__main__":
    # Параметры среды: скорость ветра 3.5 м/с, плотность тумана 0.5 г/м³
    WIND = 3.5          
    FOG = 0.0005        
    
    # Инициализация системы
    system = NamibeWaterSystem(wind_speed=WIND, fog_density=FOG)
    
    # ПРИНУДИТЕЛЬНО ЗАДАЕМ ГРАНИЦЫ ПОД РЕАЛЬНУЮ ПЕЧАТЬ (bounds)
    # Ограничиваем радиус бугорка: от 1.5 мм до 5.0 мм
    # Ограничиваем расстояние между центрами: от 6.0 мм до 20.0 мм
    bounds = [(0.0015, 0.005), (0.006, 0.020)]
    initial_guess = [0.002, 0.008]
    
    # Запуск оптимизации с привязкой к целевой функции
    objective = lambda p: -system.calculate_yield(p[0], p[1]).item()
    
    # Запуск оптимизации    
    # res = minimize(objective, initial_guess, bounds=bounds, method='L-BFGS-B')
    # Заменяем метод на Nelder-Mead, он не боится обрывов функции в ноль
    res = minimize(objective, initial_guess, bounds=bounds, method='Nelder-Mead')
    if res.success:
        best_radius, best_distance = res.x
        best_yield = system.calculate_yield(best_radius, best_distance)
        
        # --- ФОРМАТИРОВАННЫЙ ВЫВОД ДЛЯ ИНЖЕНЕРОВ ---
        print("\n" + "="*60)
        print(" 🌀 PROJECT RE-PHYSICS: MODULE \"NAMIB-CORE\" (v1.0.0) ")
        print(" BIONIC DESIGN CALCULATOR FOR FIELD ENGINEERS")
        print("="*60)
        print(f" INPUT CONDITIONS:")
        print(f"  -> Simulated Wind Speed: {WIND} m/s")
        print(f"  -> Simulated Fog Density: {FOG * 1000} g/m³")
        print("-"*60)
        print(f" OPTIMAL GEOMETRY (READY FOR 3D PRINTING):")
        print(f"  -> Optimal Bump Radius:         {best_radius * 1000:.2f} mm")
        print(f"  -> Optimal Grid Step (Distance): {best_distance * 1000:.2f} mm")
        print("-"*60)
        print(f" EXPECTED HARVEST PERFORMANCE:")
        print(f"  -> Predicted Water Yield:        {best_yield:.4f} kg/h per 1 m²")
        print("="*60 + "\n")
        
        # Запуск визуализации и генерации STL меша
        system.generate_stl(best_radius, best_distance, grid_size=5)
        system.plot_efficiency_map(best_radius, best_distance)
        
    else:
        # --- ПРОКАЧАННЫЙ БЛОК ВЫВОДА ОШИБОК ДЛЯ ЛАБОРАНТОВ ---
        print("\n" + "!"*60)
        print(" 🚨 CRITICAL CRASH LOG: BIONIC OPTIMIZATION FAILED 🚨")
        print("!"*60)
        print(f"[-] SciPy Status Code:   {res.status}")
        print(f"[-] Error Description:   {res.message}")
        print(f"[-] Number of Iterations: {res.nit}")
        print(f"[-] Function Evaluations: {res.nfev}")
        print("-"*60)
        print(" CRASH POINT ANALYSIS (Where the solver gave up):")
        print(f"  -> Last attempted Radius:   {res.x[0]*1000:.4f} mm")
        print(f"  -> Last attempted Distance: {res.x[1]*1000:.4f} mm")
        print("-"*60)
        print("💡 FIX INSTRUCTIONS FOR FIELD VOLUNTEERS:")
        print(" 1. Check your 'initial_guess' values. They must be inside 'bounds'.")
        print(" 2. Ensure 'bounds' aren't too tight (e.g., radius min shouldn't equal max).")
        print(" 3. Verify physical inputs (WIND and FOG) are positive non-zero numbers.")
        print("!"*60 + "\n")
