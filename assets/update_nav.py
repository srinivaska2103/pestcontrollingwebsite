import os
import re

nav_template = """<nav id="navbar" class="fixed w-full z-50 bg-white/90 dark:bg-darkbg/90 backdrop-blur-md border-b border-gray-200 dark:border-gray-800 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <div class="flex-shrink-0 flex items-center gap-3">
                    <a href="index.html" class="flex items-center gap-3">
                        <img src="assets/logo/logo.svg" alt="ShieldGuard Logo" class="h-10 w-10">
                        <span class="font-bold text-2xl text-gray-900 dark:text-white tracking-tight font-poppins">ShieldGuard</span>
                    </a>
                </div>

                <!-- Desktop Menu -->
                <div class="hidden lg:flex items-center gap-3 xl:gap-6">
                    <a href="index.html" class="nav-link {HOME_CLASS} transition">Home</a>
                    <a href="home2.html" class="nav-link {HOME2_CLASS} transition">Home 2</a>
                    <a href="aboutus.html" class="nav-link {ABOUT_CLASS} transition">About</a>
                    <a href="services.html" class="nav-link {SERVICES_CLASS} transition">Services</a>
                    <a href="gallery.html" class="nav-link {GALLERY_CLASS} transition">Gallery</a>
                    <a href="pricing.html" class="nav-link {PRICING_CLASS} transition">Pricing</a>
                    <a href="contact.html" class="nav-link {CONTACT_CLASS} transition">Contact</a>
                </div>
                <div class="hidden lg:flex items-center gap-2 xl:gap-4">
                    <button class="theme-toggle text-gray-500 hover:text-primary p-2 transition" title="Toggle Dark/Light Mode">
                        <i class="fas fa-moon dark:hidden text-xl"></i>
                        <i class="fas fa-sun hidden dark:block text-yellow-400 text-xl"></i>
                    </button>
                    <button class="dir-toggle text-gray-500 hover:text-primary p-2 flex items-center justify-center" title="Toggle Language">
                        <span class="font-bold text-sm">LTR</span>
                    </button>
                    <a href="login.html" class="btn-primary text-sm w-28 py-3 text-center">Login</a>
                    <a href="booknow.html" class="btn-primary text-sm w-28 py-3 text-center">Book</a>
                </div>
                <div class="lg:hidden flex items-center gap-4">
                    <button id="mobileMenuBtn" class="text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white p-2"><i class="fas fa-bars text-2xl"></i></button>
                </div>
            </div>
        </div>
        <div id="mobileMenu" class="hidden lg:hidden bg-white dark:bg-darkbg border-t border-gray-200 dark:border-gray-800 absolute w-full shadow-lg">
            <div class="px-4 py-6 space-y-1">
                <a href="index.html" class="block px-3 py-2 {HOME_MOB_CLASS}">Home</a>
                <a href="home2.html" class="block px-3 py-2 {HOME2_MOB_CLASS}">Home 2</a>
                <a href="aboutus.html" class="block px-3 py-2 {ABOUT_MOB_CLASS}">About</a>
                <a href="services.html" class="block px-3 py-2 {SERVICES_MOB_CLASS}">Services</a>
                <a href="gallery.html" class="block px-3 py-2 {GALLERY_MOB_CLASS}">Gallery</a>
                <a href="pricing.html" class="block px-3 py-2 {PRICING_MOB_CLASS}">Pricing</a>
                <a href="contact.html" class="block px-3 py-2 {CONTACT_MOB_CLASS}">Contact</a>
                <div class="pt-4 mt-2 border-t border-gray-200 dark:border-gray-700 flex flex-col gap-2">
                    <div class="flex justify-center gap-4 mb-2">
                        <button class="theme-toggle text-gray-500 hover:text-primary p-2 transition bg-gray-100 dark:bg-gray-800 rounded-lg w-full flex justify-center">
                            <i class="fas fa-moon dark:hidden text-xl"></i>
                            <i class="fas fa-sun hidden dark:block text-yellow-400 text-xl"></i>
                        </button>
                        <button class="dir-toggle text-gray-500 hover:text-primary p-2 transition bg-gray-100 dark:bg-gray-800 rounded-lg w-full flex justify-center items-center">
                            <span class="font-bold text-sm">LTR</span>
                        </button>
                    </div>
                    <a href="login.html" class="block w-full text-center px-3 py-3 bg-primary text-white rounded-lg font-semibold hover:opacity-90 transition">Login</a>
                    <a href="booknow.html" class="block w-full text-center px-3 py-3 bg-primary text-white rounded-lg font-semibold hover:opacity-90 transition">Book</a>
                </div>
            </div>
        </div>
    </nav>"""

active_desk = "text-primary font-semibold"
inactive_desk = "text-gray-600 dark:text-gray-300 hover:text-primary font-medium"
active_mob = "text-primary font-medium"
inactive_mob = "text-gray-700 dark:text-gray-300"

html_files = ["index.html", "home2.html", "aboutus.html", "services.html", "gallery.html", "pricing.html", "contact.html"]

for f in html_files:
    if not os.path.exists(f):
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Generate the nav content for this file
    nav_content = nav_template
    
    # Map for the current page
    nav_content = nav_content.replace("{HOME_CLASS}", active_desk if f == 'index.html' else inactive_desk)
    nav_content = nav_content.replace("{HOME_MOB_CLASS}", active_mob if f == 'index.html' else inactive_mob)
    
    nav_content = nav_content.replace("{HOME2_CLASS}", active_desk if f == 'home2.html' else inactive_desk)
    nav_content = nav_content.replace("{HOME2_MOB_CLASS}", active_mob if f == 'home2.html' else inactive_mob)
    
    nav_content = nav_content.replace("{ABOUT_CLASS}", active_desk if f == 'aboutus.html' else inactive_desk)
    nav_content = nav_content.replace("{ABOUT_MOB_CLASS}", active_mob if f == 'aboutus.html' else inactive_mob)
    
    nav_content = nav_content.replace("{SERVICES_CLASS}", active_desk if f == 'services.html' else inactive_desk)
    nav_content = nav_content.replace("{SERVICES_MOB_CLASS}", active_mob if f == 'services.html' else inactive_mob)
    
    nav_content = nav_content.replace("{GALLERY_CLASS}", active_desk if f == 'gallery.html' else inactive_desk)
    nav_content = nav_content.replace("{GALLERY_MOB_CLASS}", active_mob if f == 'gallery.html' else inactive_mob)
    
    nav_content = nav_content.replace("{PRICING_CLASS}", active_desk if f == 'pricing.html' else inactive_desk)
    nav_content = nav_content.replace("{PRICING_MOB_CLASS}", active_mob if f == 'pricing.html' else inactive_mob)
    
    nav_content = nav_content.replace("{CONTACT_CLASS}", active_desk if f == 'contact.html' else inactive_desk)
    nav_content = nav_content.replace("{CONTACT_MOB_CLASS}", active_mob if f == 'contact.html' else inactive_mob)
    
    pattern = re.compile(r'<nav id="navbar".*?</nav>', re.DOTALL)
    new_content, count = pattern.subn(nav_content, content)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated nav in {f}")
