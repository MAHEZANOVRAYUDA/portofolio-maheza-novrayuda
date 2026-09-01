from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'style': 'display:none;'}),
        label="Leave empty"
    )

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message', 'website')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg bg-slate-900/60 border border-slate-700 text-slate-100 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500',
                'placeholder': 'Nama lengkap',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg bg-slate-900/60 border border-slate-700 text-slate-100 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500',
                'placeholder': 'Alamat email',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg bg-slate-900/60 border border-slate-700 text-slate-100 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500',
                'placeholder': 'Subjek (opsional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg bg-slate-900/60 border border-slate-700 text-slate-100 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500',
                'rows': 5,
                'placeholder': 'Ceritakan singkat kebutuhan, project, atau pertanyaan Anda...',
            }),
        }

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website:
            raise forms.ValidationError("Spam terdeteksi!")
        return website

