import os
import sys
from pathlib import Path
import django

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datetime import date
from portfolio.models import Project, Profile, Skill, Achievement, Education, Certificate

def sync():
    print("=== SYNCHRONIZING PROFILE WITH LINKEDIN & GITHUB ===")
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(name="Maheza Novrayuda")
    
    profile.name = "Maheza Novrayuda"
    profile.hero_title = "AI & Data Engineering Enthusiast"
    profile.location = "Padang, Sumatera Barat, Indonesia"
    profile.github_url = "https://github.com/MAHEZANOVRAYUDA"
    profile.linkedin_url = "https://www.linkedin.com/in/mahezanovrayuda"
    profile.bio = (
        "Mahasiswa Teknik Informatika di Universitas Putra Indonesia YPTK Padang dan mantan Data Scientist "
        "Virtual Intern di ID/X Partners. Berfokus membangun solusi data end-to-end — mulai dari arsitektur "
        "Data Pipeline (ETL, Airflow, SQL), pemodelan Machine Learning (Credit Risk Scoring, XGBoost), arsitektur "
        "Computer Vision (YOLOv8), hingga integrasi Generative AI berbasis RAG."
    )
    profile.about_long = (
        "Perjalanan saya di dunia teknologi berakar pada ketertarikan kuat terhadap bagaimana data mentah dapat "
        "ditransformasikan menjadi kecerdasan komputasi yang memberikan dampak nyata. Sebagai mahasiswa Teknik Informatika "
        "di Universitas Putra Indonesia YPTK Padang, saya memadukan fondasi ilmu komputer akademis dengan praktik industri "
        "yang intensif.\n\n"
        "Pengalaman berharga saya jalani sebagai Data Scientist Virtual Intern di ID/X Partners, di mana saya bertanggung "
        "jawab melakukan pemodelan risiko kredit (Credit Risk Assessment & Scorecard). Dalam proyek tersebut, saya menerapkan "
        "data cleaning menyeluruh, feature engineering berbasis Weight of Evidence (WoE) & Information Value (IV), serta "
        "melatih model prediktif (Logistic Regression, Random Forest, LightGBM) dengan evaluasi metrik AUC-ROC teroptimasi.\n\n"
        "Bagi saya, model AI terbaik bertumpu pada arsitektur data yang kokoh. Oleh karena itu, saya menguasai seluruh spektrum: "
        "Data Engineering (Airflow, PostgreSQL, Docker), Machine Learning & Deep Learning (Scikit-Learn, TensorFlow, YOLOv8), "
        "hingga Generative AI & Retrieval-Augmented Generation (RAG). Setiap proyek saya rancang dengan standar rekayasa bersih, "
        "reproducible, dan siap pakai di lingkungan produksi."
    )
    profile.save()
    print("Profile updated successfully.")

    print("\n=== SYNCHRONIZING ACHIEVEMENTS ===")
    achievements_data = [
        {
            "title": "Data Scientist Virtual Internship",
            "organization": "ID/X Partners x Rakamin Academy",
            "kind": Achievement.Kind.PROJECT,
            "date": date(2026, 5, 15),
            "highlight": "Credit Risk Scoring & AUC-ROC Optimization",
            "description": "Menyelesaikan tugas akhir pemodelan risiko kredit end-to-end pada dataset keuangan historis 2007-2014, feature engineering WoE/IV, dan deployment dashboard Streamlit interaktif.",
            "link": "https://github.com/MAHEZANOVRAYUDA/credit-risk-analysis",
            "is_featured": True,
            "ordering": 1
        },
        {
            "title": "Peserta KSN-K Bidang Astronomi",
            "organization": "Puspresnas / Kemendikbudristek",
            "kind": Achievement.Kind.COMPETITION,
            "date": date(2022, 6, 1),
            "highlight": "Kompetisi Sains Nasional",
            "description": "Terpilih sebagai perwakilan sekolah dalam kompetisi sains tingkat kabupaten, menyelesaikan analisis kalkulasi astrofisika dan mekanika orbit.",
            "link": "",
            "is_featured": True,
            "ordering": 2
        },
        {
            "title": "15+ Repositori Proyek AI & Data di GitHub",
            "organization": "GitHub Open Source (@MAHEZANOVRAYUDA)",
            "kind": Achievement.Kind.PROJECT,
            "date": date(2026, 9, 6),
            "highlight": "15+ Repositori Terverifikasi",
            "description": "Mengembangkan 15+ sistem rekayasa perangkat lunak terapan meliputi Computer Vision, Data Engineering, Generative AI (RAG), NLP, hingga Mobile Engineering.",
            "link": "https://github.com/MAHEZANOVRAYUDA",
            "is_featured": True,
            "ordering": 3
        }
    ]

    for item in achievements_data:
        ach, created = Achievement.objects.update_or_create(
            title=item["title"],
            defaults=item
        )
        print(f"- Achievement: {ach.title} (created: {created})")

    print("\n=== SYNCHRONIZING 15 REAL GITHUB PROJECTS ===")
    # Map skill names to Skill objects
    skill_map = {}
    for s in Skill.objects.all():
        skill_map[s.name.lower()] = s

    def get_skills(names):
        res = []
        for n in names:
            n_lower = n.lower()
            if n_lower in skill_map:
                res.append(skill_map[n_lower])
            else:
                for k, v in skill_map.items():
                    if n_lower in k:
                        res.append(v)
                        break
        return res

    projects_data = [
        {
            "title": "Computer Vision Sitinjau Lauik: Intelligent Traffic Monitoring",
            "slug": "computer-vision-sitinjau-lauik",
            "description": "Sistem pemantauan lalu lintas pintar berbasis Computer Vision yang dirancang khusus untuk mendeteksi, menghitung, dan menganalisis volume serta kepadatan kendaraan di jalur ekstrem Sitinjau Lauik secara real-time. Dilengkapi arsitektur inferensi YOLOv8 dengan throughput tinggi, Docker containerization, dan dashboard analitik komprehensif.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/Computer-Vision-Sitinjau-Lauik",
            "demo_link": "",
            "created_at": date(2026, 8, 30),
            "metrics": "Real-time 30+ FPS YOLOv8",
            "featured": True,
            "skill_names": ["Python", "TensorFlow", "Docker", "Jupyter notebook"]
        },
        {
            "title": "Olist E-Commerce End-to-End Data Pipeline & Analytics",
            "slug": "olist-e-commerce-data-engineering-project",
            "description": "Pipeline Data Engineering komprehensif untuk dataset Olist Brazilian E-Commerce. Memproses lebih dari 100k+ records transaksi dari 9 file CSV relasional mentah menjadi star schema data warehouse di PostgreSQL dengan orkestrasian otomatis Apache Airflow dan dashboard visualisasi performa bisnis.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/Olist-E-Commerce-Data-Engineering-Project",
            "demo_link": "",
            "created_at": date(2026, 8, 4),
            "metrics": "100k+ Records (9 Tables ETL)",
            "featured": True,
            "skill_names": ["Python", "SQL", "PostgreSQL", "Pandas", "Docker"]
        },
        {
            "title": "RAG Enterprise Banking Assistant (Bank Central Asia)",
            "slug": "rag-enterprise-banking-assistant-bca",
            "description": "Sistem chatbot Retrieval-Augmented Generation (RAG) cerdas untuk Bank Central Asia yang terhubung langsung ke dokumen regulasi dan produk perbankan. Menggunakan semantic embedding, TiDB vector DB, dan LLM Ollama untuk menyajikan jawaban kontekstual tanpa risiko halusinasi.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/RAG-BCA",
            "demo_link": "",
            "created_at": date(2026, 6, 20),
            "metrics": "Semantic Context Retrieval (Zero Hallucination)",
            "featured": True,
            "skill_names": ["Python", "RAG Pipelines", "LLM Integration", "NLP", "Streamlit"]
        },
        {
            "title": "Credit Risk Assessment & Scorecard (ID/X Partners)",
            "slug": "credit-risk-assessment-scorecard-idx",
            "description": "Proyek akhir Virtual Internship Data Scientist di ID/X Partners. Membangun model machine learning evaluasi risiko kredit pada data historis pinjaman (2007–2014). Menerapkan pembersihan data, penanganan data imbalance, feature engineering WoE & IV, serta komparasi model regresi logistik dan ensemble tree untuk memprediksi probabilitas default.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/credit-risk-analysis",
            "demo_link": "",
            "created_at": date(2026, 5, 15),
            "metrics": "Optimized AUC-ROC Scorecard",
            "featured": True,
            "skill_names": ["Python", "Scikit-learn", "XGBoost", "Streamlit", "Pandas"]
        },
        {
            "title": "Indonesian Customer Sentiment Analysis Web App",
            "slug": "indonesian-customer-sentiment-analysis-web-app",
            "description": "Platform analisis sentimen berbasis web untuk ulasan pelanggan berbahasa Indonesia. Mengadopsi arsitektur decoupled microservices dengan backend Flask/Python, antarmuka pengguna responsif React, basis data PostgreSQL, serta preprocessing teks NLP (stemming & tokenizing) untuk klasifikasi polaritas ulasan otomatis.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/sentiment-analysis-website",
            "demo_link": "",
            "created_at": date(2026, 6, 2),
            "metrics": "Multi-Class Sentiment Classification",
            "featured": True,
            "skill_names": ["Python", "Flask", "NLP", "PostgreSQL", "Docker"]
        },
        {
            "title": "House Price Prediction & Real Estate Analytics App",
            "slug": "house-price-prediction-real-estate-analytics",
            "description": "Aplikasi prediksi harga properti interaktif yang dideploy ke Streamlit Cloud. Dilatih menggunakan regresi teroptimasi pada seluruh kolom numerik dan fitur struktural hunian, memungkinkan pengguna melakukan estimasi harga pasar secara instan berdasarkan parameter kustom.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/Regression_HomePricingStreamlit",
            "demo_link": "",
            "created_at": date(2026, 5, 10),
            "metrics": "R² Score 0.88 Regression",
            "featured": True,
            "skill_names": ["Python", "Scikit-learn", "Streamlit", "Pandas", "Matplotlib"]
        },
        {
            "title": "Deep Learning CNN Image Classification",
            "slug": "deep-learning-cnn-image-classification",
            "description": "Model Computer Vision klasifikasi gambar biner menggunakan arsitektur Convolutional Neural Network (CNN) dengan TensorFlow dan Keras. Mengimplementasikan konvolusi multi-layer, max-pooling, augmentasi citra untuk mencegah overfitting, dan regularisasi dropout.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/CNN-for-prediction-cat-ot-dog",
            "demo_link": "",
            "created_at": date(2026, 4, 20),
            "metrics": "87%+ Test Accuracy on Validation",
            "featured": False,
            "skill_names": ["Python", "TensorFlow", "Keras", "Jupyter notebook"]
        },
        {
            "title": "AkadBot: Academic Knowledge Retrieval Assistant",
            "slug": "akadbot-academic-knowledge-retrieval-assistant",
            "description": "Chatbot informasi akademik cerdas untuk mahasiswa Universitas Putra Indonesia YPTK Padang. Menggunakan pendekatan retrieval semantic similarity pada basis pengetahuan kampus untuk menyajikan jawaban instan terkait kurikulum, administrasi, dan kalender perkuliahan.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/akadBot-",
            "demo_link": "",
            "created_at": date(2026, 6, 18),
            "metrics": "Instant Academic FAQ & Query",
            "featured": False,
            "skill_names": ["Python", "Streamlit", "NLP"]
        },
        {
            "title": "End-to-End Machine Learning Lifecycle Suite",
            "slug": "end-to-end-machine-learning-lifecycle-suite",
            "description": "Kumpulan modul implementasi machine learning lengkap dari hulu ke hilir: klasifikasi kelangsungan hidup Titanic, hyperparameter tuning pada California Housing Dataset, segmentasi klaster pelanggan (K-Means/DBSCAN), serta teknik penanganan bias, overfitting, dan underfitting.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/End-to-end-machine-learning",
            "demo_link": "",
            "created_at": date(2026, 4, 10),
            "metrics": "Comprehensive ML Pipelines",
            "featured": False,
            "skill_names": ["Python", "Scikit-learn", "Pandas", "NumPy", "Seaborn"]
        },
        {
            "title": "Multi-Domain AI, ML & Deep Learning Case Studies",
            "slug": "multi-domain-ai-ml-deep-learning-case-studies",
            "description": "Portofolio kompilasi 7 studi kasus terapan: Analisis Sentimen Vaksin Covid-19, Prediksi Harga Cryptocurrency, Augmentasi Data dengan Deep Neural Network (DNN), Deteksi Spam Email dengan NLP, Prediksi Penjualan Masa Depan, Prediksi Harga Emas, serta Sistem Rekomendasi Hotel.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/AI-ML_DL-Project-Portofolio",
            "demo_link": "",
            "created_at": date(2026, 5, 25),
            "metrics": "7 Specialized ML/DL Case Studies",
            "featured": False,
            "skill_names": ["Python", "TensorFlow", "Scikit-learn", "NLP", "Jupyter notebook"]
        },
        {
            "title": "Student Performance Predictive Modeling (Dibimbing.id)",
            "slug": "student-performance-predictive-modeling-dibimbing",
            "description": "Proyek benchmarking algoritma machine learning pada kursus intensif Data Science Framework di Dibimbing.id. Melakukan komparasi performa algoritma klasifikasi dan regresi untuk memprediksi nilai serta performa siswa berdasarkan fitur demografis dan aktivitas belajar.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/DSF-dibimbing",
            "demo_link": "",
            "created_at": date(2026, 4, 15),
            "metrics": "Algorithm Benchmarking & Comparison",
            "featured": False,
            "skill_names": ["Python", "Scikit-learn", "Pandas", "Jupyter notebook"]
        },
        {
            "title": "Relational Data Wrangling & Transactional Analytics",
            "slug": "relational-data-wrangling-transactional-analytics",
            "description": "Pembersihan, transformasi, dan audit data relasional berskala besar meliputi tabel pelanggan (customers), pesanan (orders), produk (products), dan transaksi penjualan (sales). Menghasilkan dataset bersih siap analitik serta visualisasi distribusi transaksi.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/data_wragling",
            "demo_link": "",
            "created_at": date(2026, 3, 25),
            "metrics": "Multi-Table Relational Cleaning",
            "featured": False,
            "skill_names": ["Python", "Pandas", "Matplotlib", "Seaborn", "Jupyter notebook"]
        },
        {
            "title": "MahesElectronics: Cross-Platform E-Commerce Mobile App",
            "slug": "maheselectronics-cross-platform-ecommerce-mobile-app",
            "description": "Aplikasi mobile e-commerce katalog elektronik yang dibangun dengan Flutter & Dart. Menampilkan antarmuka pengguna modern responsif, navigasi modular, katalog produk dinamis, dan pengelolaan keranjang belanja belanja digital.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/mahesElectronics-flutter",
            "demo_link": "",
            "created_at": date(2026, 5, 28),
            "metrics": "Modular Flutter State Management",
            "featured": False,
            "skill_names": ["Flutter", "Javascript", "VS Code"]
        },
        {
            "title": "Web-Based Attendance & Administration Management System",
            "slug": "web-based-attendance-administration-system",
            "description": "Aplikasi manajemen absensi dan pencatatan presensi digital berbasis web untuk monitoring kehadiran harian secara terpusat, rekapitulasi data kehadiran otomatis, dan pelaporan administrasi.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/absensi-web",
            "demo_link": "",
            "created_at": date(2026, 6, 11),
            "metrics": "Digital Attendance & Shift Tracking",
            "featured": False,
            "skill_names": ["SQL", "MySQL", "php"]
        },
        {
            "title": "Modern AI & Data Engineering Portfolio Web App",
            "slug": "modern-ai-data-engineering-portfolio-web-app",
            "description": "Situs web portofolio profesional berarsitektur modern dengan standar Craftsman UI dan Zero AI-Slop. Dibangun dengan Django 5, PostgreSQL Neon, Tailwind CSS, CDN Cloudinary untuk resolusi retina ultra-tajam, serta arsitektur serverless edge deployment di Vercel.",
            "github_link": "https://github.com/MAHEZANOVRAYUDA/portofolio-maheza-novrayuda",
            "demo_link": "https://portofolio-maheza-novrayuda.vercel.app",
            "created_at": date(2026, 9, 6),
            "metrics": "Production Edge Serverless Architecture",
            "featured": False,
            "skill_names": ["Python", "Django", "PostgreSQL", "Vercel", "Git & GitHub"]
        }
    ]

    # Clean existing projects or update them by slug/github_link
    print(f"Total current projects: {Project.objects.count()}")
    # We will update or create based on slug
    synced_count = 0
    for pdata in projects_data:
        skill_names = pdata.pop("skill_names")
        slug = pdata["slug"]
        proj, created = Project.objects.update_or_create(
            slug=slug,
            defaults=pdata
        )
        # associate skills
        skills_to_add = get_skills(skill_names)
        proj.skills.set(skills_to_add)
        synced_count += 1
        print(f"- [{proj.id}] {proj.title} (created: {created}, skills: {len(skills_to_add)})")

    # If there are older duplicate projects that don't match our 15 canonical slugs, clean them
    canonical_slugs = [p["slug"] for p in projects_data]
    old_extras = Project.objects.exclude(slug__in=canonical_slugs)
    if old_extras.exists():
        print(f"Removing {old_extras.count()} obsolete/duplicate project records...")
        old_extras.delete()

    print(f"\nSuccessfully synchronized {Project.objects.count()} projects in database!")

if __name__ == '__main__':
    sync()
