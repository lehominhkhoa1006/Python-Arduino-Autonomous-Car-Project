# 🚗 Python-Arduino Autonomous Car Project  

A mini **autonomous lane-keeping car** built with **Python + Arduino**, combining computer vision, control algorithms, and hardware integration.  

## 📌 Features  
- Lane detection using **OpenCV (Python)**  
- Vehicle control with **Arduino UNO + L293D Motor Shield**  
- PID-based steering control for smooth navigation  
- Real-time serial communication between Python & Arduino  
- Custom-built chassis with Logitech C920e webcam  

## 🛠️ Hardware  
- Arduino UNO + L293D Shield  
- 4 DC motors + wheels  
- Acrylic chassis + Lego Technic camera frame  
- Logitech C920e webcam  
- Lithium battery pack

## 💻 Software  
- **Python (OpenCV, NumPy, Serial)** → Lane detection + decision making  
- **Arduino IDE (AFMotor library)** → Motor control  

## 🚀 How It Works  
1. Webcam captures road lanes → processed with OpenCV  
2. Python detects lanes, applies control logic (PID)  
3. Commands (Left / Right / Forward / Stop) sent via Serial  
4. Arduino receives signals → controls motors accordingly  

## 📊 Results  
- Successfully detects lanes and follows a marked path  
- Stable movement with smooth turning mechanism  
- Tested on a lab-scale track using tape lanes  

## 🔮 Future Improvements  
- Add **Lidar / Ultrasonic / GPS** for advanced navigation  
- Optimize algorithms with **machine learning**  
- Integrate **solar power** for sustainability  

---

👉 Developed by **Group 4 – HCMUTE (2024)**  
Guiding lecturer: **PhD. Lê Thanh Phúc**
Leader: **Lê Hồ Minh Khoa** 




