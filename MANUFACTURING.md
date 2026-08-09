## 🧪 Chemical Post-Processing & Surface Coating Guide

To turn the generated `.stl` mesh into a functioning atmospheric water generator, the substrate must replicate the **biphilic surface chemistry** of the Namib Desert beetle. Raw 3D-printed plastic (PLA, PETG, or Resin) has a uniform wettability and **will not harvest water efficiently** without the following micro-layering process.

### ⏱️ Step-by-Step Manufacturing Protocol

[ 1. Raw 3D Mesh ]  ---> Clean & Sand (Smooth Surface)
|
[ 2. Hydrophobic ]  ---> Apply Fluoropolymer Base Layer (Entire Tile)
|
[ 3. Masking/Stamping ] ---> Shield the Valleys, Expose Only Peak Tips
|
[ 4. Hydrophilic ]  ---> Deposition of TiO2 or SiO2 Nanoparticles (Peaks Only)


#### Step 1: Substrate Preparation (Eliminating Print Artifacts)
* **Action:** Post-cure (if using SLA resin) or chemically smooth (if using FDM plastic like ABS/ASA via acetone vapor). 
* **Reason:** Micro-ridges from 3D printing layers act as geometric traps for water droplets, causing premature evaporation instead of detachment. The surface must be as smooth as possible before coating.

#### Step 2: Total Hydrophobic Base Coating (Valleys & Slopes)
* **Objective:** Achieve a static water contact angle ($\theta$) $> 110^\circ$ across the entire tile.
* **Materials to Use:** 
  * Superhydrophobic sprays containing **fluoropolymer / silica nanoparticles** (e.g., NeverWet, Ultra-Ever Dry, or lab-grade WX2100).
  * Alternatively, a thin micro-layer of **natural carnauba wax** or paraffin dissolved in hexane can be used for low-cost humanitarian deployment.
* **Application:** Spray or dip-coat the entire 3D-printed tile uniformly. Allow to cure completely according to the manufacturer's specification.

#### Step 3: Selective Peak Masking (The Stamping Method)
* **Objective:** Isolate only the extreme apexes (tips) of the calculated bumps, shielding the valleys from the next chemical step.
* **Method:** Use a flat, rigid silicone stamp or pad lightly coated with a temporary mask (such as water-soluble PVA glue or protective masking ink). Press it flat against the tile. Only the peaks will receive the mask.

#### Step 4: Hydrophilic Peak Activation
* **Objective:** Achieve a static water contact angle ($\theta$) $< 20^\circ$ on the bump apexes to force instant droplet nucleation.
* **Materials to Use:**
  * **Titanium Dioxide ($TiO_2$)** or **Silicon Dioxide ($SiO_2$)** nanoparticle suspensions.
  * Lab-grade hydrophilic polymer solutions (e.g., Polyvinyl alcohol or Polyethylene glycol coatings).
* **Application:** If using the mask from Step 3, spray the hydrophilic solution over the entire tile, then wash the tile with water. The mask will dissolve, leaving the hydrophilic coating *only* on the peaks. 
* *Alternative approach:* Skip Step 3 and use a high-precision micro-roller or precision brush to apply the $TiO_2$ slurry strictly to the top 5% height of the bumps.

### 🔬 Verification Metrics for Lab Technicians
Before deploying the panel into the fog harvesting field, verify the chemical boundaries using a goniometer:
* **Peak Apex Boundary:** Droplet must spread immediately ($\theta_{advancing} < 15^\circ$).
* **Valley/Slope Boundary:** Droplet must remain perfectly spherical and roll off at a tilt angle of $< 10^\circ$ ($\theta_{receding} > 110^\circ$).
