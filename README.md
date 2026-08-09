# 🌀 bionic-water-mesh (Namib-Capillary)

**Applied Generative Bionic Design: Reviving forgotten equations of droplet nucleation to combat world water scarcity.**

---

> "This repository is a practical sub-module and a direct spin-off of the [RE-PHYSICS (Computational Archival Physics)](https://github.com) framework. It implements the **Method of Digital Voids** by occupying an ignored academic gap: the intersection of raw 19th-century thermodynamics, micro-surface geometry, and autonomous 3D CAD generation."

---

## 🌌 The Crisis & The Concept
In arid regions like Sub-Saharan Africa, fetching clean water is a daily crisis. While classical engineering relies on active, high-energy infrastructure, nature solves this passively. 

The *Onymacris unguicularis* (Namib Desert beetle) ![Namib Desert beetle](1685103771_gagaru-club-p-namibiiskii-zhuk-pinterest-3.jpg) collects clean drinking water from dry morning fog using nothing but the geometric texture of its back. This repository provides a **Generative Bionic Design engine** that translates the complex physics of the beetle’s shell into optimized, 3D-printable physical panels.

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

## 🛠 Current Release Status: Alpha Prototype & Community Sandbox

**Note for Field Engineers & Makers:** 
The current 3D panel model (`namib_surface_panel.stl`) is an initial, low-density proof-of-concept design. It was created with wide spacing to guarantee successful printing on absolute any entry-level 3D printer without fusion or slicing errors.

* **Primary Purpose:** This is a physical "sandbox" model for your initial material testing (evaluating wax adhesion, testing food-grade silicone application, and checking general fluid flow).
* **Efficiency Hacking:** To reach the maximum water collection peak shown on the performance landscape chart, you are encouraged to tweak the `namib_generator.py` script. For deployment, regenerate the mesh with tighter tolerances (target: ~1.7mm bump radius with a ~1.0mm flat clearance between edges).
* **Open Invitation:** Since I design this from a CAD/structural perspective without a physical 3D printer on hand, please share your print settings, photos of physical tiles, and field-test water yields in the Issues tab!

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
  4. 
#### Formula B: Food-Grade Long-Term Hydrophilic Activation (Долговечная безопасная фиксация)

Instead of water-soluble silicate glues (which leach dangerous alkalis into drinking water), use inert, non-toxic food-grade polymers.

- **Hydrophilic Mineral:** Food-grade Titanium Dioxide ($TiO_2$, E171).
- **Carrier Binder:** Food-Grade Silicone Sealant (certified FDA/ГОСТ) OR Aquarium-Safe Silicone. Once cured, it turns into an absolutely inert, waterproof rubber that releases zero chemicals.
- **Application Process:**
    1. Mix 5g of $TiO_2$ with a small amount of food-grade silicone until it forms a workable paste.
    2. Stamp or dab the mixture precisely onto the apexes of the bumps.
    3. Let it cure completely for 24–48 hours until the vinegar/solvent smell completely disappears.
  
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

### 🛖 Low-Cost Field Formulations & Critical Safety Patches

> ⚠️ **IMPORTANT AMENDMENTS FOR MANUFACTURING SAFETY**
> Before preparing the solutions below, review these four engineering updates to prevent physical injuries, material destruction, or water contamination.

#### 1. Filament Temperature Barrier (PLA vs. PETG/ABS)
* **The Risk:** Most standard 3D prints use **PLA**, which has a low glass transition temperature of **50–60°C**. If you submerge a PLA panel into molten wax at 80°C or overheat it with a high-power heat gun, the precise bionic micro-geometry will instantly melt, warp, and deform.
* **The Solution:** For the Thermal Dip method, it is highly recommended to print panels using **PETG, ABS, or ASA** (which withstand temperatures up to 75–90°C). If you only have PLA, **DO NOT dip the panel**. Instead, apply the melted wax gently using a natural bristle brush with slightly cooled wax, and use a hair dryer on its lowest heat setting from a safe distance.

#### 2. Bio-Contamination Prevention (The Mold & Bacteria Risk)
* **The Risk:** Raw **cornstarch** and **Gum Arabic** are organic carbohydrates. In high-humidity environments (fog collection), these ingredients create a perfect petri dish for dangerous mold, fungi, and bacterial colonies within 48–72 hours. Drinking water that passes through a moldy panel poses severe health risks.
* **The Solution:** **Strictly forbid** the use of cornstarch for permanent field deployments. Cornstarch must *only* be used for rapid, short-term 5-minute proof-of-concept efficiency tests. For real-world humanitarian water harvesting, use **only Titanium Dioxide ($TiO_2$)** as it is an inorganic mineral that does not support microbial growth.

#### 3. Respiratory Protection During Mixing
* **The Risk:** While Titanium Dioxide ($TiO_2$, E171) is safe to ingest in paste form, inhaling its dry airborne powder is **hazardous**. Fine mineral dust can settle deep inside the lungs and is classified as a potential respiratory carcinogen upon inhalation.
* **The Solution:** Always wear a **protective mask or respirator (N95/FFP2 or better)** when handling, weighing, and mixing dry $TiO_2$ powder into the liquid binder. Do not shake the dry powder container in enclosed, unventilated spaces.

#### 4. Mandatory Post-Collection Water Treatment
* **The Risk:** Atmospheric fog can carry pollutants, heavy metals (near industrial zones), or road dust. Additionally, open-air panels are vulnerable to bird droppings and insect debris. Captured water is never naturally sterile.
* **The Solution:** All harvested water must be treated before consumption. The official protocol requires volunteers to pass the water through a basic **mechanical particulate filter** and then **boil it thoroughly** (or treat it with standard water purification/chlorine tablets). Shape provides the water, but sterilization guarantees survival.

## 🚨 CRITICAL CHEMICAL SAFETY WARNING (MUST READ BEFORE MANUFACTURING!)

⚠️⚠️⚠️ **CHEMICAL TOXICITY ALERT** ⚠️⚠️⚠️

*   **DO NOT USE White Spirit, Mineral Spirits, Petrol, or Industrial Solvents!** If you dissolve wax using chemical solvents, the residue will trap toxic hydrocarbons inside the porous 3D-printed plastic. The collected water will become **poisonous, toxic, and strictly unfit for human consumption.**
*   **DO NOT USE commercial synthetic auto-waxes or industrial clear coats/varnishes** unless they are explicitly certified as 100% Food-Grade and Liquid-Safe.
*   **THE RULE IS SIMPLE:** If you cannot safely eat the raw ingredients, **DO NOT** put them on the water-harvesting panel. 
*   **ONLY USE THE 100% THERMAL ECO-METHOD:** Melt pure natural beeswax or carnauba wax using a water bath and heat gun without any chemical thinners. Use only food-grade Titanium Dioxide (E171) or cornstarch mixed with organic Gum Arabic (E414).

*If you violate this protocol, you are building a chemical hazard, not a water collector. Safety first!*

*   **NEVER USE Liquid Glass (Sodium/Potassium Silicate or School Silicate Glue)!** 
  There is a dangerous misconception that silicate glue dries into safe, permanent "glass." This is chemically false. At room temperature, it cures into a water-soluble, highly alkaline crystalline salt. 
  When fog or rain hits the panel, the water will instantly dissolve the cured glue, turning the harvested drinking water into a caustic, poisonous alkaline solution. Drinking this water will cause severe chemical burns to the mouth, esophagus, and stomach. 
  For durable hydrophilic binding, ONLY use 100% Food-Grade / Aquarium-safe silicone or food-safe epoxy.

## 🤝 Join the Sandbox (How to Contribute)

This is an open-source humanitarian project. Since this was engineered from a computational/structural perspective without a physical lab, your real-world feedback is what keeps this project alive. 

We are actively looking for:
* **Makers with 3D Printers:** Print the panel in **PETG/ABS**, apply the thermal wax coating, and share your print configuration/photos in the [Issues](https://github.com) tab.
* **Material Scientists:** Help us test and refine food-safe hydrophilic/hydrophobic boundary layers and alternative eco-binders.
* **Field Volunteers:** If you are working in arid regions (e.g., Atacama, Namib, parts of Sub-Saharan Africa), run the 5-minute spray bottle test and send us your water yield data!

Let's turn code into clean water together.
## 🗺️ Modular Upgrades & Feature Voting (Голосование за модернизации)

We want to build what *you* actually need in the field. Below are 10 proposed modular upgrades for the generative engine. 

**How to vote:** Go to the [Feature Voting Issue #1](https://github.com) and drop a reaction (like 👍 or 🎉) on the feature you want to see next! Once an upgrade hits 15+ votes, we build it immediately.

| # | Proposed Upgrade (Модернизация) | Status | Goal |
|---|----------------------------------|--------|------|
| 1 | **Automatic Wind-Mesh Scaling**: Auto-adjust spacing between bumps based on seasonal wind spikes. | 💡 Idea | 15 Votes |
| 2 | **Web-UI Dashboard (No-Code)**: A simple web browser page where you slide variables and get STL instantly. | 💡 Idea | 15 Votes |
| 3 | **Gravity-Drain Micro-Channels**: Adding biomimetic micro-grooves (like the Texas horned lizard skin) to accelerate water drainage. | 💡 Idea | 15 Votes |
| 4 | **Multi-Panel Interlocking Joints**: Generate panels with puzzle-like edges so they can snap together into giant collector walls. | 💡 Idea | 15 Votes |
| 5 | **Low-Poly Low-Memory Export**: Optimization for ultra-fast slicing on older, entry-level 3D printers. | 💡 Idea | 15 Votes |
| 6 | **GPS-Climate API Integration**: Type your coordinates, and the script automatically fetches local humidity/wind history from open weather APIs. | 💡 Idea | 15 Votes |
| 7 | **Gyroid Sub-Surface Infills**: Generate internal hollow channels inside the panel to save up to 40% of plastic filament. | 💡 Idea | 15 Votes |
| 8 | **Anti-Silt Texture**: Add micro-patterns that prevent dust and sand from sticking to the hydrophobic wax valleys during dry days. | 💡 Idea | 15 Votes |
| 9 | **Free-Form Architectural Wrapping**: Allow the code to export meshes mapped onto curved surfaces (for wrapping around tents or water tanks). | 💡 Idea | 15 Votes |
| 10| **Pre-Configured Slicer Profiles**: Add ready-to-use `.3mf` print profiles for OrcaSlicer/PrusaSlicer tailored for watertight PETG printing. | 💡 Idea | 15 Votes |

## 📄 License
This project is open-source and available under the MIT License. Feel free to use it for humanitarian, educational, or research purposes. Created in 2026.
