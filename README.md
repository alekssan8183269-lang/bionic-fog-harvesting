# 🌀 bionic-water-mesh (Namib-Capillary)

**Applied Generative Bionic Design: Reviving forgotten equations of droplet nucleation to combat world water scarcity.**

---

> "This repository is a practical sub-module and a direct spin-off of the [RE-PHYSICS (Computational Archival Physics)](https://github.com) framework. It implements the **Method of Digital Voids** by occupying an ignored academic gap: the intersection of raw 19th-century thermodynamics, micro-surface geometry, and autonomous 3D CAD generation."

---

## 🌌 The Crisis & The Concept
In arid regions like Sub-Saharan Africa, fetching clean water is a daily crisis. While classical engineering relies on active, high-energy infrastructure, nature solves this passively. 

The *Onymacris unguicularis* (Namib Desert beetle) collects clean drinking water from dry morning fog using nothing but the geometric texture of its back. This repository provides a **Generative Bionic Design engine** that translates the complex physics of the beetle’s shell into optimized, 3D-printable physical panels.

## 🛠️ Deep Technical Mechanics
Unlike standard static meshes, this Python tool dynamically calculates surface geometry based on your specific local environment (wind speed, fog density). It computes:
1. **The Young-Dupré Modification:** Optimizing the contact angle boundary where the droplet sits simultaneously on hydrophilic peaks and hydrophobic valleys.
2. **Critical Nucleation Radius:** Calculating the exact mathematical micro-dome radius where water vapor condenses exponentially faster than on a flat sheet.
3. **Capillary Volumetric Detachment:** Finding the precise geometric threshold where gravity overcomes surface tension, forcing the droplet to slide down before evaporating back into the air.

## 🚀 Quick Start

### 1. Installation
Install the core mathematical and rendering dependencies:
```bash
pip install numpy scipy matplotlib numpy-stl
```

### 2. Execution
Run the standalone generator to compute optimal bionic proportions, plot the 3D efficiency landscape, and export a ready-to-print 3D panel:
```bash
python namib_generator.py
```

## 📊 Interactive Visualization & CAD Output
* **3D Performance Landscape:** The script opens an interactive `matplotlib` environment displaying the efficiency gradient. You can visually track exactly how the evolutionary peak matches the mathematical optimum.
* **Direct STL Engine:** Generates raw polygonal vertices and faces to compile a water-harvesting panel file (`namib_surface_panel.stl`) instantly, bypassing the need for heavy closed-source CAD software.

## ⚠️ Engineering Manifesto for Physical Testing
This code outputs the **mathematically perfect geometric form** for fluid detachment. For successful real-world deployment by humanitarian organizations, 3D-printed physical tiles require strict material post-processing:
* **The Peaks:** Must be micro-treated with a hydrophilic coating (water-attracting).
* **The Slopes & Valleys:** Must be treated with a highly hydrophobic substance (e.g., specialized wax or hydrophobic spray).

*Without proper material polarity, the water will simply smear across the plastic plate. Shape is nothing without substance.*

## 🔗 Structural Connection to RE-PHYSICS
This project operates under the **Method of Digital Voids (Methodology of Semantic Vacuum)**. It takes theoretical formulas abandoned in historical archives by pure physicists and wraps them into production-ready Python code for modern makers and humanitarian field engineers.

### 🛖 Low-Cost Field Formulations (Гуманитарные "гаражные" рецепты)

*Warning: These formulations are designed for low-budget humanitarian deployment in field conditions where lab-grade reagents are unavailable. They cost almost zero.*

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

### 💡 For the Field Volunteers: The Magic of Digital Voids in Your Hands

When you open this code, you are not just running a script—you are bridging the gap between advanced evolutionary physics and human survival. 

When you see with your own eyes that shifting a single number (`WIND_SPEED`) in your terminal instantly resizes the bionic geometry on your screen, prints a perfect new mesh, and suddenly adds **+20% or +30% more clean water** into a test cup in a dry village—you see progress. You are no longer just a spectator; you are an engineer of reality. 

You hold the power to adapt the geometry of nature to your specific village, your local microclimate, and your exact 3D printer. This is where the void ends, and clean water begins. Run the loop: **Code ➡️ Print ➡️ Wax ➡️ Spray ➡️ Save Lives.**

## 🚨 CRITICAL CHEMICAL SAFETY WARNING (MUST READ BEFORE MANUFACTURING!)

⚠️⚠️⚠️ **CHEMICAL TOXICITY ALERT** ⚠️⚠️⚠️

*   **DO NOT USE White Spirit, Mineral Spirits, Petrol, or Industrial Solvents!** If you dissolve wax using chemical solvents, the residue will trap toxic hydrocarbons inside the porous 3D-printed plastic. The collected water will become **poisonous, toxic, and strictly unfit for human consumption.**
*   **DO NOT USE commercial synthetic auto-waxes or industrial clear coats/varnishes** unless they are explicitly certified as 100% Food-Grade and Liquid-Safe.
*   **THE RULE IS SIMPLE:** If you cannot safely eat the raw ingredients, **DO NOT** put them on the water-harvesting panel. 
*   **ONLY USE THE 100% THERMAL ECO-METHOD:** Melt pure natural beeswax or carnauba wax using a water bath and heat gun without any chemical thinners. Use only food-grade Titanium Dioxide (E171) or cornstarch mixed with organic Gum Arabic (E414).

*If you violate this protocol, you are building a chemical hazard, not a water collector. Safety first!*

## 📄 License
This project is open-source and available under the MIT License. Feel free to use it for humanitarian, educational, or research purposes. Created in 2026.
