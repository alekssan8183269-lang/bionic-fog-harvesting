# Bionic Fog Harvesting: Generative Design Based on Namib Desert Beetle Physics

An open-source Python tool that revives forgotten equations of droplet nucleation and fluid dynamics to generate optimized 3D-printable surfaces for atmospheric water generation.

## 🌀 The Concept
In arid regions like Sub-Saharan Africa, fetching clean water is a daily crisis. This project bridges the gap between theoretical bionic physics and digital manufacturing. By translating the complex thermodynamic laws of the Namib Desert beetle's back into pure Python, this script calculates the mathematically perfect geometry of water-collecting bumps based on specific local weather conditions (wind speed and fog density).

## 🛠️ How It Works
1. **Thermodynamic Optimization:** The script uses `scipy.optimize` to process non-linear equations of droplet growth and surface tension energy balances.
2. **Interactive 3D Mapping:** Generates a real-time efficiency landscape visualization using `matplotlib`.
3. **Generative CAD Output:** Automatically compiles raw vertices and polygonal faces into a production-ready `.stl` mesh file without using heavy CAD software.

## 🚀 Quick Start

### Prerequisites
```bash
pip install numpy scipy matplotlib numpy-stl
```

### Running the Generator
Clone the repository and run the main script to calculate your optimal geometry, view the 3D performance map, and export the physical mesh file:
```bash
python namib_generator.py
```

## ⚠️ Engineering Note for Physical Testing
This code calculates the **ideal geometric form** for droplet detachment. To achieve high efficiency in real-world physical prototypes, 3D-printed tiles require appropriate material post-processing: the peaks of the generated bumps should be treated with hydrophilic coating, while the slopes and base valleys must remain highly hydrophobic (e.g., coated with specialized wax or hydrophobic spray), mimicking the beetle's actual biological structure.

### 🛖 Low-Cost Field Formulations (Гуманитарные "гаражные" рецепты)

*Warning: These formulations are designed for low-budget humanitarian deployment in field conditions where lab-grade reagents are unavailable. They cost almost zero.*

#### Formula A: Cheap Hydrophobic Coating (Защита впадин и склонов)
Instead of expensive fluoropolymers, we use simple wax-solvent chemistry available in any auto-shop or local market.
* **Hydrophobic Agent:** Regular **Carnauba car wax** (e.g., Turtle Wax) OR melted **Paraffin/Beeswax** candles.
* **Carrier Solvent:** Ordinary **White Spirit**, Mineral Spirits, or lighter fluid (Hexane alternative).
* **Proportions:** Dissolve **5-10 grams of wax/paraffin** into **100 mL of solvent**.
* **Preparation:** Warm the solvent slightly in a hot water bath (DO NOT use open fire!) and completely dissolve the wax. 
* **Application:** Spray or dip the entire tile. As the solvent evaporates, a micro-layer of hydrophobic wax remains, offering a strong water-repellent effect ($\theta > 95^\circ$).

#### Formula B: Cheap Hydrophilic Activation (Активация верхушек бугорков)
Instead of lab-grade $TiO_2$ nanoparticles, we use everyday building materials or mineral powders.
* **Hydrophilic Agent:** Common **Titanium Dioxide white pigment** (used in acrylic paints, food coloring, or homemade soap making, costs \$2 per kg) OR ordinary **White Talcum powder / Chalk dust**.
* **Carrier:** Cheap **Water-based Acrylic Matte Varnish / Lacquer** (Clear coat).
* **Proportions:** Mix **5 grams of pigment** into **50 mL of water-based clear varnish** until it forms a milky paste.
* **Application (Stamping):** Pour a thin layer of this mixture onto a flat surface. Take your wax-coated tile, and lightly press its face into the paint. The paint will stick *only* to the tips of the bumps. 
* **Result:** The matte acrylic resin locks the hydrophilic mineral powder onto the tips, creating a permanent water-attracting matrix without any nanotechnology.

### 🍯 100% Safe Eco-Formulations (Полностью пищевые безопасные составы)

*Crucial Note: These formulas use strictly non-toxic, food-grade materials. The harvested water is 100% safe for consumption and has no chemical odor.*

#### Formula A: Safe Bio-Hydrophobic Coating (Эко-защита впадин и склонов)
Instead of chemical solvents, we use pure thermal deposition of natural food-grade waxes.
* **Hydrophobic Agent:** Pure **Beeswax (Пчелиный воск)** OR natural **Carnauba wax (Воск карнауба)**.
* **Carrier Solvent:** NONE. We do not use any toxic solvents or thinners.
* **Application Process (Thermal Dip):**
  1. Melt the natural wax in a water bath (heat to ~70-80°C until it becomes a thin liquid).
  2. Briefly dip the entire 3D-printable panel into the liquid wax for 2 seconds, or apply a very thin layer using a natural bristle brush.
  3. Immediately blow hot air over the tile (using a heat gun or standard hair dryer). The hot air will melt away any excess thickness, leaving a microscopically thin, smooth, and highly hydrophobic bio-wax film across the valleys and slopes.

#### Formula B: Food-Grade Hydrophilic Activation (Безопасная активация верхушек)
To attract water strictly on the tips of the bumps without using micro-plastics or chemical varnishes.
* **Hydrophilic Mineral:** Food-grade **Titanium Dioxide ($TiO_2$, E171)** (the exact white powder used to color white M&Ms, chewing gums, and toothpaste, totally non-toxic and costs pennies) OR ordinary **Food-grade Cornstarch (Кукурузный крахмал)**.
* **Carrier Binder:** Organic **Gum Arabic (Гуммиарабик / Пищевая смола акации, E414)**. This is a natural, water-soluble tree sap powder used for centuries as a safe binder in food and watercolors.
* **Proportions:** Dissolve 2g of Gum Arabic in 20 mL of warm water, then mix in 5g of $TiO_2$ (or starch) until it forms a thick white paste.
* **Application (The Safe Stamping Method):**
  1. Spread a paper-thin layer of the white paste onto a flat glass plate.
  2. Take your wax-coated tile and press its face gently onto the plate. The organic paste will stick *only* to the apexes of the bumps.
  3. Let it dry completely. Once dry, the Gum Arabic forms a rock-hard, safe matrix that holds the water-attracting minerals on the peaks.
### 📊 Field Testing Protocol & Efficiency Hacking (Как тестировать и разгонять КПД)

*You don’t need an atmospheric lab to test this. You can run validation in 5 minutes using a simple water spray bottle and a kitchen scale.*

#### 🛠️ Standard Field Test Setup (Порядок проверки)
1. **The Fog Simulator:** Take a standard garden or cleaning spray bottle (nebulizer) filled with clean water. Adjust the nozzle to the finest possible mist setting to simulate natural fog.
2. **The Test Angle:** Mount your coated 3D-printed panel at a **45-degree angle** inside a collection container. 
3. **The Run:** Spray the mist uniformly from a distance of 30 cm for exactly **3 minutes**. Weight the collected water on a pocket scale.

---

#### 🚀 How to "Hack" and Maximize the Water Yield (КПД)

If your first test yields low water volume, do not panic. Use these three bionic parameters to optimize efficiency in your specific field conditions:

| Symptom / Problem | Root Cause | Engineering Solution (How to Fix) |
| :--- | :--- | :--- |
| **Water smears into a flat film** (No drops rolling down) | The wax layer is too thin or uneven. | **Re-wax:** Re-heat the plate with a hair dryer to let the beeswax flow more smoothly into the valleys. |
| **Droplets freeze on the peaks** (They grow but never fall) | The calculated bump radius is too small for current low wind. | **Run Python Again:** Increase the `WIND_SPEED` variable in the script by +1.5 m/s and re-generate a mesh with larger bumps. |
| **Droplets roll down too slowly** (Evaporating on their way) | The panel tilt angle is wrong or slopes are too rough. | **Steepen the Tilt:** Increase the physical panel deployment angle from 45° to 60° to let gravity win faster. |
| **The white paint washes off** | Gum Arabic mixture was too watery. | **Thicken the Paste:** Re-apply the peak stamping paste using less water and more food-grade starch/binder. |

---

### 💡 Why Communities Will Do This (The Gamification of Science)
By providing this simple checklist, you turn a complex engineering problem into a practical loop: **Run Python Code ➡️ Print ➡️ Wax ➡️ Spray ➡️ Measure.** 

When a field volunteer sees with their own eyes that changing the bump size in your code instantly adds +20% more water into their test cup, they become hooked. You give them the power to adapt the geometry to their specific village, climate, and printer.

## 📄 License
This project is open-source and available under the MIT License. Feel free to use it for humanitarian, educational, or research purposes.
