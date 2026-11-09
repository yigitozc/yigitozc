<p align="center">
  <img src="assets/banner.svg" alt="Yiğit Özçelik — Computer Engineering @ Ankara University" width="100%">
</p>

<p align="center">
  <a href="https://yigitozc.github.io"><img src="https://img.shields.io/badge/Portfolio-yigitozc.github.io-2ee6c5?style=for-the-badge&logo=githubpages&logoColor=white&labelColor=0f1b33" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/yi%C4%9Fit-%C3%B6z%C3%A7elik-386645382"><img src="https://img.shields.io/badge/LinkedIn-Yiğit_Özçelik-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0f1b33" alt="LinkedIn"></a>
  <a href="mailto:yigitozcelik88@gmail.com"><img src="https://img.shields.io/badge/Email-yigitozcelik88@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0f1b33" alt="Email"></a>
</p>

<p align="center">
  🇬🇧 English · <a href="#-türkçe">🇹🇷 Türkçe</a>
</p>

## 👋 About me

I am a second-year **Computer Engineering** student at **Ankara University**, working on **autonomous ground vehicles** and the software that lets perception, localization and planning run together on a real platform. What interests me most is the engineering that makes these systems dependable: clear interfaces between modules, repeatable tests and simulations that reflect the field. I also build web applications and take an active part in student communities at my university.

```python
class Yigit:
    location  = "Ankara, Türkiye"
    studying  = "Computer Engineering @ Ankara University"
    focus     = ["autonomous ground vehicles", "robot simulation", "web applications"]
    languages = {"Turkish": "native", "English": "limited working", "Japanese": "elementary"}
```

**What I build with**

| | |
|---|---|
| **Python** | ROS 2 nodes and simulation tooling: a seed-generated Gazebo test field, Gazebo vehicle models generated from Blender meshes, tools around a CARLA and ROS 2 bridge |
| **ROS 2** | Autonomous bus-stop manoeuvre and the system architecture of the Robotaxi stack |
| **TypeScript · React** | Frontend of the MTA tracking system, a PWA with TanStack, Zod, Tailwind CSS and Keycloak |
| **JavaScript · Canvas** | Library-free lidar, occupancy grid and A* simulation on my website; MTA inventory app |
| **Blender** | 3D model of the unmanned ground vehicle, carried into Gazebo |

## 🎓 Education

| | |
|---|---|
| <img src="https://img.shields.io/badge/2025_→_now-0f1b33?style=flat-square" alt="2025 to now"> | **Ankara University**: B.Sc. Computer Engineering · GPA 3.23 |

## 💼 Experience

**National Technology Workshop (MTA)**<br>
*Workshop tracking system · Frontend development*

I work on the frontend of the workshop's tracking system, a React and TypeScript progressive web app where students request materials and workshop staff manage approvals and hand-overs.

## 🏁 Competitions

**TEKNOFEST 2026 Robotaxi Passenger Autonomous Vehicle Competition**<br>
*Ready-made vehicle category · Team AUtomotion-R · Finalist*

An end-to-end autonomy stack for the BEE1 passenger vehicle, built for static and dynamic traffic scenarios on a closed track. The source code is private.

| | |
|---|---|
| **My role** | Started on the autonomous bus-stop manoeuvre (stop sign detection, entering the bay, IMU-confirmed full stop, rejoining the lane), later grew to cover the architecture of the whole system |
| **Perception** | Lane detection with a CLRerNet model fine-tuned on track data, traffic sign and light detection with YOLO, Velodyne lidar processing per zone around the vehicle |
| **Localization** | Map-frame pose from an Xsens MTi GNSS/INS unit, supported by wheel odometry |
| **Planning** | A* routing between map zones, Lanelet2 centre-line following, behaviour tree for overtaking and parking |
| **Control** | Lane following and overtaking controller, the only node writing to the vehicle's CAN bus |
| **Deployment** | ROS 2 Foxy in a single GPU Docker image, with a simulation bridge and per-day scenario tests |

## 🚀 Projects

**Active projects · 2026** (source code not public)

| Project | Work | Stack |
|---|---|---|
| **Unmanned Ground Vehicle (İKA)** | Team captain. Modelled the vehicle in Blender for our Gazebo simulation of the competition course | ROS 2, Gazebo, Blender, Python |
| **Advanced Autonomous Systems** | Simulation and route planning, including a seed-generated Gazebo and RViz test field | ROS 2, Gazebo, RViz, Python, Hybrid A* |
| **Swarm UAV** | Active 2026 project | |
| **Polar Research** | Team captain, TÜBİTAK polar research | |
| **Robotaxi: Original Vehicle** | Real-time simulation in CARLA, connected through a ROS 2 bridge | CARLA, ROS 2, Python, Blender |

**Open source**

<table>
<tr>
<td width="50%" valign="top">

### 🧰 [MTA Workshop Inventory](https://github.com/yigitozc/mta-atolye-takip)
Inventory and request system for the National Technology Workshop. Students request parts, and coordinators approve and hand them out. 

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</td>
<td width="50%" valign="top">

### 🗺️ [Portfolio site](https://github.com/yigitozc/yigitozc.github.io)
My personal site at [yigitozc.github.io](https://yigitozc.github.io). Its simulation implements frontier-based exploration: lidar ray casting, an occupancy grid, A* replanning and path tracking, with no libraries.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</td>
</tr>
</table>

**Other projects** (source code not public)

- **Edge AI Perception Pod**: HackAntarktika project, an edge AI perception module for polar field conditions
- **MTA Tracking Platform**: team project with a separate frontend, API gateway and Java backend, where I work on the frontend

## 🛠️ Tech stack

| | |
|---|---|
| **Languages** | <img src="https://skillicons.dev/icons?i=python,cpp,java,js,html,css" alt="Python, C++, Java, JavaScript, HTML, CSS"> |
| **Robotics & simulation** | <img src="https://skillicons.dev/icons?i=ros,opencv,blender" alt="ROS, OpenCV, Blender"> ![Gazebo](https://img.shields.io/badge/Gazebo-F58113?style=flat-square) ![CARLA](https://img.shields.io/badge/CARLA-0f1b33?style=flat-square) ![RViz](https://img.shields.io/badge/RViz-0f1b33?style=flat-square) ![YOLO](https://img.shields.io/badge/YOLO-111F68?style=flat-square) |
| **Tools** | <img src="https://skillicons.dev/icons?i=linux,ubuntu,docker,git,github,vscode,maven" alt="Linux, Ubuntu, Docker, Git, GitHub, VS Code, Maven"> |

## 🌍 Languages

| Language | Level |
|---|---|
| 🇹🇷 Turkish | Native |
| 🇬🇧 English | Limited working proficiency |
| 🇯🇵 Japanese | Elementary proficiency |

## 📜 Certifications

- **Programming with Python**: MATHCOM · Ankara University · *Nov 2025*

## 🤝 Active communities

- **CORE Student Community**, Ankara University · Board Member · *2025 – present*

## 📡 Activity

<p align="center">
  <img src="assets/activity.svg" alt="Contribution radar: one ring per weekday, one spoke per week" width="100%">
</p>

---

## 🇹🇷 Türkçe

<details>
<summary><b>Türkçe özet için tıkla</b></summary>

<br>

Ankara Üniversitesi Bilgisayar Mühendisliği ikinci sınıf öğrencisiyim. Otonom kara araçları ve algı, konumlama ve planlama katmanlarının gerçek bir araç üzerinde birlikte çalışmasını sağlayan yazılımlar üzerine çalışıyorum. Bu sistemlerde beni en çok, onları güvenilir kılan mühendislik ilgilendiriyor: modüller arasında net arayüzler, tekrarlanabilir testler ve sahayı doğru yansıtan simülasyonlar. Bunun yanında web uygulamaları geliştiriyor, üniversitemdeki öğrenci topluluklarında aktif olarak yer alıyorum.

**Eğitim:** Ankara Üniversitesi, Bilgisayar Mühendisliği (2025 → devam ediyor) · Ortalama 3.23

**Neyle ne yaptım**
- **Python**: ROS 2 düğümleri ve simülasyon araçları (Gazebo test sahası, Blender'dan Gazebo model üretimi, CARLA ve ROS 2 köprüsü araçları)
- **ROS 2**: Robotaksi yazılımında otonom durak manevrası ve sistem mimarisi
- **TypeScript · React**: MTA takip sisteminin frontend'i
- **JavaScript · Canvas**: kişisel sitemdeki kütüphanesiz LiDAR ve A* simülasyonu, MTA malzeme takip uygulaması
- **Blender**: insansız kara aracının 3D modeli

**Deneyim**
- **Milli Teknoloji Atölyesi (MTA)**: atölye takip sisteminin frontend tarafında çalışıyorum (React, TypeScript)

**Katıldığım yarışmalar**
- **TEKNOFEST 2026 Robotaksi Binek Otonom Araç Yarışması** (hazır araç kategorisi, AUtomotion-R, finalist): BEE1 binek aracı için uçtan uca otonom sürüş yazılımı. CLRerNet ile şerit algılama, YOLO ile trafik işareti ve ışık tespiti, Velodyne LiDAR ile engel algılama, Xsens MTi GNSS/INS ile konumlama, Lanelet2 ve davranış ağacı ile planlama; ROS 2 Foxy ve Docker. İşe otonom durak manevrasıyla başladım, sonrasında sistemin tüm mimarisine hâkim oldum. Kaynak kodu paylaşılmıyor.

**Aktif projeler · 2026** (kaynak kodu paylaşılmıyor)
- **İnsansız Kara Aracı (İKA)**: takım kaptanı; aracı Blender üzerinde modelledim, parkurun Gazebo simülasyonunda kullanıyoruz (ROS 2, Gazebo, Blender, Python)
- **İleri Otonom Sistemler**: simülasyon ve rota planlama (ROS 2, Gazebo, RViz, Python, Hybrid A*)
- **Sürü İHA**
- **Kutup Araştırmaları**: takım kaptanı, TÜBİTAK kutup araştırmaları
- **Robotaksi Özgün**: CARLA üzerinde gerçek zamanlı simülasyon (CARLA, ROS 2, Python, Blender)

**Açık kaynak projeler**
- **[MTA Atölye Malzeme Takip Sistemi](https://github.com/yigitozc/mta-atolye-takip)**: öğrencilerin malzeme talep ettiği, koordinatörlerin onaylayıp teslim ettiği web uygulaması
- **[Portfolyo sitesi](https://yigitozc.github.io)**: sınır tabanlı keşif simülasyonu içeren kişisel sitem: LiDAR ışın izleme, doluluk ızgarası, A* ile yeniden planlama

**Diğer projeler** (kaynak kodu paylaşılmıyor)
- **Edge AI Otonom Algı Podu**: HackAntarktika projesi; kutup saha koşulları için uç yapay zekâ tabanlı algı modülü
- **MTA Takip Platformu**: ayrı frontend, API gateway ve Java backend içeren takım projesi; frontend tarafında çalışıyorum

**Diller:** Türkçe (ana dil) · İngilizce (sınırlı mesleki yeterlilik) · Japonca (başlangıç)

**Sertifikalar:** MATHCOM Python ile Programlama Eğitimi, Ankara Üniversitesi (Kasım 2025)

**Aktif olarak görev aldığım topluluklar**
- **CORE Öğrenci Topluluğu**, Ankara Üniversitesi: Yönetim Kurulu Üyesi (2025 – devam ediyor)

📫 Bana [LinkedIn](https://www.linkedin.com/in/yi%C4%9Fit-%C3%B6z%C3%A7elik-386645382) veya [e-posta](mailto:yigitozcelik88@gmail.com) ile ulaşabilirsin.

</details>
