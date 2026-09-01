import os

file_path = r'e:\MAHEZA NOVRAYUDA\portofolio-maheza-novrayuda\templates\home.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_block = """                        {% if c.credential_id %}
                        <div class="text-[11px] text-slate-500">ID: {{ c.credential_id }}</div>
                        {% endif %}
                        {% if c.credential_url %}
                        <a href="{{ c.credential_url }}" target="_blank"
                            class="mt-1 text-[11px] text-sky-400 hover:text-sky-300 transition-colors">Lihat kredensial
                            &rarr;</a>
                        {% endif %}"""

replacement_block = """                        {% if c.credential_id %}
                        <div class="text-[11px] text-slate-500">ID: {{ c.credential_id }}</div>
                        {% endif %}
                        {% if c.file %}
                        {% if c.is_pdf %}
                        <a href="{{ c.file.url }}" target="_blank"
                            class="mt-1 flex items-center gap-1 text-[11px] text-emerald-400 hover:text-emerald-300 transition-colors">
                            <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                            </svg>
                            View PDF
                        </a>
                        {% else %}
                        <a href="{{ c.file.url }}" target="_blank"
                            class="mt-1 flex items-center gap-1 text-[11px] text-sky-400 hover:text-sky-300 transition-colors">
                            <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                            </svg>
                            View &rarr;
                        </a>
                        {% endif %}
                        {% elif c.credential_url %}
                        <a href="{{ c.credential_url }}" target="_blank"
                            class="mt-1 text-[11px] text-sky-400 hover:text-sky-300 transition-colors">Lihat kredensial
                            &rarr;</a>
                        {% endif %}"""

if target_block in content:
    new_content = content.replace(target_block, replacement_block)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated home.html")
else:
    print("Target block not found in home.html")
    # Clean up whitespace issues for matching
    import re
    # normalize spaces
    def normalize(s):
        return re.sub(r'\s+', ' ', s).strip()
    
    if normalize(target_block) in normalize(content):
        print("Found with whitespace mismatch, trying regex replace...")
        # Since logic is complex, better to not risk regex blind replace without manual verification.
        # But for now, let's output failure.
        print("Please check content manually.")
