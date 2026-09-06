import os
import sys
from pathlib import Path
from datetime import date
import django

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Experience, Achievement, Profile, Education, Skill

def run():
    print("=== 1. ELIMINASI AI-SLOP & DATA SMA ===")
    deleted_count, _ = Achievement.objects.filter(title__icontains="astronomi").delete()
    print(f"Dihapus {deleted_count} entri halusinasi KSN Astronomi dari Achievement.")

    # Pastikan Education hanya S1 Teknik Informatika UPI YPTK Padang
    Education.objects.filter(institution__icontains="SMA").delete()
    Education.objects.filter(degree__icontains="SMA").delete()
    edu = Education.objects.first()
    if not edu:
        edu = Education.objects.create(
            institution="Universitas Putra Indonesia YPTK Padang",
            degree="S1 Teknik Informatika",
            start_date=date(2023, 9, 26),
            end_date=date(2027, 8, 31),
            description="Fokus studi pada Rekayasa Perangkat Lunak, Kecerdasan Buatan (AI/ML), Computer Vision, dan Rekayasa Data.",
            ordering=1
        )
    else:
        edu.institution = "Universitas Putra Indonesia YPTK Padang"
        edu.degree = "S1 Teknik Informatika"
        edu.start_date = date(2023, 9, 26)
        edu.end_date = date(2027, 8, 31)
        edu.description = "Fokus studi pada Rekayasa Perangkat Lunak, Kecerdasan Buatan (AI/ML), Computer Vision, dan Rekayasa Data."
        edu.save()
    print("Pendidikan formal dipastikan murni jenjang universitas.")

    print("\n=== 2. MEMPERBARUI PROFIL RESMI MAHEZA NOVRAYUDA ===")
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(name="Maheza Novrayuda")
    
    profile.name = "Maheza Novrayuda"
    profile.hero_title = "Research Assistant & AI / Data Engineer"
    profile.location = "Padang, Sumatera Barat, Indonesia"
    profile.github_url = "https://github.com/MAHEZANOVRAYUDA"
    profile.linkedin_url = "https://www.linkedin.com/in/mahezanovrayuda"
    profile.bio = (
        "Research Assistant di LPPM Universitas Putra Indonesia YPTK Padang dengan fokus pada Software Engineering, "
        "AI/ML, Computer Vision, dan IoT. Berpengalaman dalam penguatan keamanan infrastruktur data center (Diskominfo Padang), "
        "pemodelan Credit Risk Scoring skala 466k+ record (ID/X Partners), serta akselerasi talenta AI di Digistar Club dan Indigo Telkom."
    )
    profile.about_long = (
        "Saya adalah seorang pembelajar berkelanjutan dan praktisi rekayasa perangkat lunak serta AI/Data yang berbasis di Padang, Sumatera Barat. "
        "Saat ini, saya mengemban amanah sebagai Research Assistant di Lembaga Penelitian dan Pengabdian Masyarakat (LPPM) UPI YPTK Padang, "
        "di mana saya memimpin riset terapan dan implementasi sistem di bidang Software Engineering, Artificial Intelligence / Machine Learning (AI/ML), "
        "Computer Vision, serta integrasi sensor Internet of Things (IoT).\n\n"
        "Sebelumnya, saya telah menyelesaikan program magang intensif di Pusat Komputasi & Data Center Dinas Komunikasi dan Informatika (Diskominfo Padang), "
        "melakukan analisis forensik terhadap 450.000+ log autentikasi SSH dan 213.000+ web traffic Nginx untuk mitigasi botnet dan cyber threat. "
        "Pada ranah data science industri, saya mengembangkan Credit Scoring Engine skala 466k+ catatan pinjaman sebagai Project-Based Virtual Intern di ID/X Partners x Rakamin Academy, "
        "meraih akurasi 97.86% dan AUC 97.35% dengan model Gradient Boosting.\n\n"
        "Komitmen saya adalah membangun solusi cerdas dengan prinsip Data-First Architecture, metrik evaluasi yang dapat dipertanggungjawabkan, "
        "serta kode yang modular, aman, dan siap pakai di lingkungan produksi."
    )
    profile.save()
    print("Profil resmi berhasil diperbarui dengan peran Research Assistant LPPM UPI YPTK Padang.")

    print("\n=== 3. MEMUAT 8 PENGALAMAN KERJA DARI LINKEDIN RESMI ===")
    experiences_data = [
        {
            "title": "Research Assistant",
            "organization": "LPPM Universitas Putra Indonesia YPTK Padang",
            "employment_type": Experience.EmploymentType.RESEARCH,
            "location": "Padang, Sumatera Barat, Indonesia",
            "location_type": Experience.LocationType.ON_SITE,
            "start_date": date(2026, 6, 1),
            "end_date": None,
            "is_current": True,
            "description": "Bertanggung jawab dalam riset dan implementasi sistem terapan di lingkungan Lembaga Penelitian dan Pengabdian Masyarakat (LPPM) UPI YPTK Padang.",
            "highlights": (
                "Melaksanakan rekayasa perangkat lunak (Software Engineering) dan arsitektur sistem berbasis Artificial Intelligence & Machine Learning (AI/ML).\n"
                "Merancang dan menguji model Computer Vision cerdas serta integrasi sensor Internet of Things (IoT) untuk riset komputasi terapan.\n"
                "Menyusun dokumentasi teknis dan evaluasi performa model komputasi untuk publikasi penelitian dan pengabdian masyarakat."
            ),
            "technologies_summary": "Software Engineering, AI/ML, Computer Vision, IoT, Python",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 1,
        },
        {
            "title": "Data Center Internship",
            "organization": "Dinas Komunikasi dan Informatika (Diskominfo Padang)",
            "employment_type": Experience.EmploymentType.INTERNSHIP,
            "location": "Padang, Sumatera Barat, Indonesia",
            "location_type": Experience.LocationType.ON_SITE,
            "start_date": date(2026, 4, 1),
            "end_date": date(2026, 6, 30),
            "is_current": False,
            "description": "Menjalankan operasi keamanan data center dan penguatan infrastruktur digital (infrastructure hardening) untuk layanan publik pemerintah kota.",
            "highlights": (
                "Melakukan analisis forensik komprehensif pada 450.000+ log autentikasi SSH untuk mendeteksi dan memetakan serangan brute-force, dictionary attack, dan botnet terkoordinasi dari 872+ threat actor unik.\n"
                "Menganalisis 213.000+ web request server Nginx untuk mengidentifikasi pola pemindaian kerentanan (vulnerability scanning), termasuk WordPress probing, SQL Injection (SQLi), directory traversal, dan credential harvesting.\n"
                "Merumuskan rekomendasi mitigasi keamanan terapan: penerapan Fail2Ban, SSH key-based authentication, non-standard port configuration, dan IP whitelisting.\n"
                "Menyelesaikan full-stack security audit pada aplikasi web analisis sentimen dengan mengevaluasi 75 kontrol keamanan sistem autentikasi dan otorisasi."
            ),
            "technologies_summary": "Linux, Nginx, SSH Hardening, Fail2Ban, Log Forensics, Cyber Security, Bash",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 2,
        },
        {
            "title": "Project-Based Virtual Intern: Data Scientist",
            "organization": "ID/X Partners x Rakamin Academy",
            "employment_type": Experience.EmploymentType.APPRENTICESHIP,
            "location": "Indonesia",
            "location_type": Experience.LocationType.REMOTE,
            "start_date": date(2026, 2, 1),
            "end_date": date(2026, 3, 31),
            "is_current": False,
            "description": "Mengembangkan Credit Scoring Engine performa tinggi berbasis Machine Learning untuk mengidentifikasi debitur berisiko tinggi dan meminimalkan potensi kredit macet (loan default) perusahaan multifinance.",
            "highlights": (
                "Memproses dan membersihkan dataset skala besar berisi 466.285 riwayat pinjaman dengan 75 fitur, menangani rasio missing value tinggi (>40%) serta data imbalance.\n"
                "Mengevaluasi berbagai algoritma klasifikasi (Logistic Regression, Random Forest, XGBoost), dengan Gradient Boosting sebagai model terbaik yang meraih Akurasi 97.86% dan AUC 97.35%.\n"
                "Membangun dan men-deploy web application interaktif end-to-end menggunakan Streamlit untuk simulasi penilaian risiko kredit secara real-time.\n"
                "Merumuskan strategi bisnis berbasis data, termasuk perancangan Early Warning System (EWS) dan segmentasi risk-grade debitur."
            ),
            "technologies_summary": "Python, Scikit-Learn, XGBoost, Gradient Boosting, Streamlit, WoE / IV, Pandas",
            "link": "https://github.com/MAHEZANOVRAYUDA/credit-risk-analysis",
            "is_featured": True,
            "ordering": 3,
        },
        {
            "title": "AI Ecosystem & Infrastructure",
            "organization": "Digistar Club by Telkom Indonesia",
            "employment_type": Experience.EmploymentType.PROGRAM,
            "location": "Indonesia",
            "location_type": Experience.LocationType.HYBRID,
            "start_date": date(2026, 5, 1),
            "end_date": None,
            "is_current": True,
            "description": "Bagian dari komunitas akselerasi talenta digital nasional Telkom Indonesia dalam pilar AI Ecosystem & Infrastructure.",
            "highlights": (
                "Aktif dalam program DigiConnect, DigiCourse, dan DigiLearn untuk meningkatkan kompetensi teknis arsitektur AI dan infrastruktur digital.\n"
                "Berkolaborasi dengan mentor industri dalam pengembangan aplikasi cloud-native dan arsitektur pipeline AI/ML."
            ),
            "technologies_summary": "Cloud-Native, AI/ML Pipeline Architecture, Cloud Computing, Python",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 4,
        },
        {
            "title": "National AI Talent Development",
            "organization": "Indigo Telkom",
            "employment_type": Experience.EmploymentType.PROGRAM,
            "location": "Jakarta Selatan, DKI Jakarta, Indonesia",
            "location_type": Experience.LocationType.HYBRID,
            "start_date": date(2025, 11, 1),
            "end_date": date(2025, 11, 30),
            "is_current": False,
            "description": "Mengikuti program akselerasi talenta kecerdasan buatan nasional oleh Indigo Telkom berfokus pada Generative AI dan infrastruktur komputasi AI skala besar.",
            "highlights": (
                "Menyelesaikan kurikulum spesialisasi dan meraih sertifikasi Alibaba Cloud untuk Generative AI, Model Studio Fundamentals, dan Alibaba Cloud Native for AI (PAI).\n"
                "Mempelajari GPU-accelerated computing, AI ethics, dan implementasi bertanggung jawab solusi AI skala enterprise."
            ),
            "technologies_summary": "Generative AI, Alibaba Cloud PAI, Model Studio, GPU Computing, AI Ethics",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 5,
        },
        {
            "title": "Dewan Pengawas Organisasi & Divisi Pemrograman",
            "organization": "UKM IT Cybernetix",
            "employment_type": Experience.EmploymentType.ORGANIZATION,
            "location": "Padang, Sumatera Barat, Indonesia",
            "location_type": Experience.LocationType.ON_SITE,
            "start_date": date(2024, 4, 1),
            "end_date": None,
            "is_current": True,
            "description": "Berperan sebagai Dewan Pengawas Organisasi (DPO) (Jul 2026 – Sekarang) dan sebelumnya anggota Divisi Pemrograman Backend (Apr 2024 – Jun 2026).",
            "highlights": (
                "Menjalankan fungsi supervisi organisasi serta kepatuhan program kerja di UKM IT Cybernetix.\n"
                "Berkontribusi dalam pengembangan sistem backend, pembinaan pemrograman bagi anggota baru, dan kepanitiaan teknis kegiatan IT kampus."
            ),
            "technologies_summary": "Backend Engineering, Python, Leadership, System Design",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 6,
        },
        {
            "title": "Data Engineer Bootcamp",
            "organization": "Dsarea (digitalskillsarea)",
            "employment_type": Experience.EmploymentType.BOOTCAMP,
            "location": "Indonesia",
            "location_type": Experience.LocationType.REMOTE,
            "start_date": date(2026, 6, 1),
            "end_date": date(2026, 7, 31),
            "is_current": False,
            "description": "Pelatihan intensif spesialisasi Data Engineering yang berfokus pada pembangunan data pipeline streaming & batch skala industri.",
            "highlights": (
                "Praktik implementasi orkestrasian data, ingestion real-time menggunakan Apache Kafka, dan containerization layanan berbasis Docker.\n"
                "Menyelesaikan tugas akhir arsitektur pipeline data dan integrasi penyimpanan data warehouse."
            ),
            "technologies_summary": "Docker, Apache Kafka, ETL Pipelines, SQL, Data Warehouse",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 7,
        },
        {
            "title": "Data Science & Machine Learning Student",
            "organization": "Dicoding Academy",
            "employment_type": Experience.EmploymentType.INTERNSHIP,
            "location": "Bandung, Jawa Barat, Indonesia",
            "location_type": Experience.LocationType.REMOTE,
            "start_date": date(2024, 9, 1),
            "end_date": date(2024, 12, 31),
            "is_current": False,
            "description": "Program magang dan pelatihan intensif kurikulum Data Science dan Machine Learning bersertifikasi industri.",
            "highlights": (
                "Mempelajari siklus hidup lengkap data science: pengumpulan data, EDA, feature engineering, pemodelan prediktif, hingga evaluasi metrik akurasi.\n"
                "Mengembangkan proyek analisis data dan model klasifikasi menggunakan Python, Pandas, Scikit-Learn, dan visualisasi data."
            ),
            "technologies_summary": "Python, Data Science, Machine Learning, Pandas, Scikit-Learn",
            "link": "https://www.linkedin.com/in/mahezanovrayuda",
            "is_featured": True,
            "ordering": 8,
        },
    ]

    for item in experiences_data:
        exp, created = Experience.objects.update_or_create(
            title=item["title"],
            organization=item["organization"],
            defaults=item
        )
        print(f"- Experience: {exp.title} at {exp.organization} (created: {created})")

    # Pastikan Achievement bersih dari astronomi
    Achievement.objects.filter(title__icontains="astronomi").delete()
    
    print("\n=== SEMUA DATA PENGALAMAN BERHASIL DISINKRONKAN DENGAN RESMI ===")

if __name__ == "__main__":
    run()
