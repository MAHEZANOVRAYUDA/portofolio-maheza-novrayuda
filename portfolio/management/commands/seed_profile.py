from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project
from datetime import date

class Command(BaseCommand):
    help = 'Seeding initial data for Profile, Skills, and Projects'

    def handle(self, *args, **kwargs):
        # 1. Seeding Profile
        profile, created = Profile.objects.get_or_create(pk=1)
        profile.name = "Maheza Novrayuda"
        profile.hero_title = "AI & Data Engineering Enthusiast"
        profile.bio = ("Mahasiswa Teknik Informatika di Universitas Putra Indonesia YPTK Padang yang fokus "
                       "membangun solusi data end-to-end — mulai dari data pipeline, analisis statistik, "
                       "hingga model AI/Machine Learning siap produksi. Tertarik pada Generative AI (RAG), "
                       "NLP, dan arsitektur data yang scalable.")
        profile.about_long = ("Saya mulai serius menekuni AI dan Data Science sejak semester awal kuliah, belajar "
                              "lewat kombinasi kelas kampus, bootcamp (Dicoding Academy, CodePolitan), dan "
                              "eksperimen mandiri di GitHub. Fokus saya ada di tiga area yang saling terkait: "
                              "Data Engineering (pipeline & data cleaning), Data Science (analisis statistik & "
                              "machine learning klasik), dan AI Engineering (deep learning & Generative AI/RAG). "
                              "Saat ini saya sedang memperdalam sistem RAG (Retrieval-Augmented Generation) dan "
                              "arsitektur data yang efisien untuk kasus dunia nyata.")
        profile.location = "Padang, Sumatera Barat, Indonesia"
        profile.email = "mahezanovrayuda@gmail.com"
        profile.github_url = "https://github.com/MAHEZANOVRAYUDA"
        profile.linkedin_url = "https://www.linkedin.com/in/mahezanovrayuda"
        profile.save()
        
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded Profile: {profile.name}"))

        # 2. Seeding Skills
        skills_data = [
            {'name': 'Python', 'category': Skill.Category.LANGUAGES},
            {'name': 'SQL', 'category': Skill.Category.LANGUAGES},
            {'name': 'Django', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'Streamlit', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'Flask', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'Pandas', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'NumPy', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'Scikit-learn', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'TensorFlow', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'Keras', 'category': Skill.Category.FRAMEWORKS},
            {'name': 'XGBoost', 'category': Skill.Category.ML_AI},
            {'name': 'RAG Pipelines', 'category': Skill.Category.ML_AI},
            {'name': 'LLM Integration', 'category': Skill.Category.ML_AI},
            {'name': 'NLP', 'category': Skill.Category.ML_AI},
            {'name': 'Matplotlib', 'category': Skill.Category.ML_AI},
            {'name': 'Seaborn', 'category': Skill.Category.ML_AI},
            {'name': 'PostgreSQL', 'category': Skill.Category.CLOUD_DEVOPS},
            {'name': 'MySQL', 'category': Skill.Category.CLOUD_DEVOPS},
            {'name': 'Git & GitHub', 'category': Skill.Category.CLOUD_DEVOPS},
            {'name': 'Vercel', 'category': Skill.Category.CLOUD_DEVOPS},
        ]
        
        for sd in skills_data:
            skill, created = Skill.objects.get_or_create(name=sd['name'], defaults={'category': sd['category']})
            if not created:
                skill.category = sd['category']
                skill.save()
        self.stdout.write(self.style.SUCCESS("Successfully seeded Skills"))

        # 3. Seeding Projects
        projects_data = [
            {
                'title': 'RAG-BCA',
                'description': 'Sistem Retrieval-Augmented Generation (RAG) yang menggabungkan Large Language Model dengan vector embedding untuk pencarian semantik dan question-answering berbasis dokumen.',
                'github_link': 'https://github.com/MAHEZANOVRAYUDA/RAG-BCA',
                'featured': True,
                'created_at': date.today()
            },
            {
                'title': 'CNN Cat vs Dog Classifier',
                'description': 'Convolutional Neural Network untuk klasifikasi gambar kucing vs anjing, dengan optimisasi bobot model untuk mengurangi overfitting.',
                'github_link': 'https://github.com/MAHEZANOVRAYUDA/CNN_CatvDog',
                'featured': True,
                'created_at': date.today()
            },
            {
                'title': 'Real-time Sentiment Analysis',
                'description': 'Aplikasi NLP untuk mengklasifikasikan sentimen pengguna, dilengkapi antarmuka web interaktif.',
                'github_link': 'https://github.com/MAHEZANOVRAYUDA/SentimentAnalysis',
                'featured': False,
                'created_at': date.today()
            },
            {
                'title': 'Credit Risk Modeling',
                'description': 'Pipeline machine learning untuk memprediksi probabilitas gagal bayar pinjaman, membantu keputusan kredit berbasis data.',
                'github_link': 'https://github.com/MAHEZANOVRAYUDA/Credit_Risk_Analysis',
                'featured': True,
                'created_at': date.today()
            },
            {
                'title': 'Home Pricing Regression (Streamlit)',
                'description': 'Proyek data science end-to-end memprediksi harga properti menggunakan regresi multivariat, dengan dashboard Streamlit interaktif.',
                'github_link': 'https://github.com/MAHEZANOVRAYUDA/Regression_HomePricingStreamlit',
                'featured': False,
                'created_at': date.today()
            },
            {
                'title': 'AI/ML Multi-Case Portfolio',
                'description': 'Kumpulan studi kasus AI/ML dunia nyata: exploratory data analysis, feature engineering, dan benchmarking model.',
                'github_link': 'https://github.com/MAHEZANOVRAYUDA/AI-ML_DL-Project-Portofolio',
                'featured': False,
                'created_at': date.today()
            }
        ]

        for pd in projects_data:
            project, created = Project.objects.get_or_create(
                title=pd['title'], 
                defaults={
                    'description': pd['description'],
                    'github_link': pd['github_link'],
                    'featured': pd['featured'],
                    'created_at': pd['created_at']
                }
            )
            if not created:
                project.description = pd['description']
                project.github_link = pd['github_link']
                project.featured = pd['featured']
                project.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded Projects"))
        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
