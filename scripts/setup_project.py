import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from portfolio.models import Profile

User = get_user_model()

def setup():
    print("Running initial project setup...")

    # 1. Create Default Profile
    if not Profile.objects.exists():
        print("Creating default Profile...")
        Profile.objects.create(
            name="Nama Anda",
            hero_title="AI Engineer & Data Enthusiast",
            bio="Saya seorang AI Engineer yang bersemangat membangun solusi cerdas.",
            email="email@example.com"
        )
        print("✅ Default Profile created.")
    else:
        print("✅ Profile already exists.")

    # 2. Check/Create Superuser
    if not User.objects.filter(is_superuser=True).exists():
        print("\nBelum ada Superuser (Admin). Mari buat satu.")
        username = input("Username default (admin): ") or "admin"
        email = input("Email default (admin@example.com): ") or "admin@example.com"
        password = input("Password (minimal 8 karakter): ")
        
        if password:
            try:
                User.objects.create_superuser(username, email, password)
                print(f"✅ Superuser '{username}' created successfully.")
            except Exception as e:
                print(f"❌ Failed to create superuser: {e}")
        else:
            print("⚠️ Password kosong, superuser tidak dibuat.")
    else:
        print("✅ Superuser already exists.")

    print("\nSetup selesai! Jalankan server dengan 'python manage.py runserver'")

if __name__ == '__main__':
    setup()
