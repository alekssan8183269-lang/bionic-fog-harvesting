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

## 📄 License
This project is open-source and available under the MIT License. Feel free to use it for humanitarian, educational, or research purposes.
