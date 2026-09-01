import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Profile, Skill, Project

def migrate_media_to_cloudinary():
    print("Migrating Profile images...")
    for profile in Profile.objects.all():
        if profile.avatar and not str(profile.avatar.name).startswith('image/upload/'):
            local_path = os.path.join('media', str(profile.avatar.name))
            if os.path.exists(local_path):
                print(f"Uploading {local_path}...")
                with open(local_path, 'rb') as f:
                    profile.avatar.save(os.path.basename(local_path), File(f), save=True)
            else:
                print(f"Skipping {local_path} (not found locally)")

    print("Migrating Skill icons...")
    for skill in Skill.objects.all():
        if skill.icon and not str(skill.icon.name).startswith('image/upload/'):
            local_path = os.path.join('media', str(skill.icon.name))
            if os.path.exists(local_path):
                print(f"Uploading {local_path}...")
                with open(local_path, 'rb') as f:
                    skill.icon.save(os.path.basename(local_path), File(f), save=True)
            else:
                print(f"Skipping {local_path} (not found locally)")

    print("Migrating Project images...")
    for project in Project.objects.all():
        if project.image and not str(project.image.name).startswith('image/upload/'):
            local_path = os.path.join('media', str(project.image.name))
            if os.path.exists(local_path):
                print(f"Uploading {local_path}...")
                with open(local_path, 'rb') as f:
                    project.image.save(os.path.basename(local_path), File(f), save=True)
            else:
                print(f"Skipping {local_path} (not found locally)")

if __name__ == '__main__':
    migrate_media_to_cloudinary()
    print("Migration complete!")
