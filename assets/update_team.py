import re

with open('d:/Srinivas/pestcontrolwebsite/aboutus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update grid cols
content = content.replace(
    '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">',
    '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">'
)

# 2. Make images bigger (replace h-72 with h-96 in the team section)
# We can just replace all instances in the team section, or all instances of `<div class="relative h-72 overflow-hidden">`
content = content.replace('<div class="relative h-72 overflow-hidden">', '<div class="relative h-96 overflow-hidden">')

# 3. Remove team member 5 and 6
# Replace everything from Team Member 5 to the end of the section
pattern = re.compile(r'<!-- Team Member 5 -->.*?</div>\s*</div>\s*</div>\s*</section>\s*<!-- 7\. Safety & Quality Standards -->', re.DOTALL)
replacement = '''</div>
            </div>
        </section>

        <!-- 7. Safety & Quality Standards -->'''
content = pattern.sub(replacement, content)

with open('d:/Srinivas/pestcontrolwebsite/aboutus.html', 'w', encoding='utf-8') as f:
    f.write(content)
