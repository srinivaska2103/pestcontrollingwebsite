document.addEventListener('DOMContentLoaded', () => {
    // ---- Theme Toggle (Dark/Light Mode) ----
    const themeToggleBtns = document.querySelectorAll('.theme-toggle');
    
    // Check local storage for theme preference
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        document.documentElement.classList.add('dark');
    } else if (currentTheme === 'light') {
        document.documentElement.classList.remove('dark');
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.classList.add('dark'); // Fallback to OS preference
    }

    // Toggle theme on button click
    themeToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            document.documentElement.classList.toggle('dark');
            if (document.documentElement.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    });

    // ---- Direction Toggle (LTR/RTL) ----
    const dirToggleBtns = document.querySelectorAll('.dir-toggle');
    const currentDir = localStorage.getItem('dir');
    
    if (currentDir === 'rtl') {
        document.documentElement.setAttribute('dir', 'rtl');
    } else {
        document.documentElement.setAttribute('dir', 'ltr'); // Default
    }

    dirToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (document.documentElement.getAttribute('dir') === 'ltr') {
                document.documentElement.setAttribute('dir', 'rtl');
                localStorage.setItem('dir', 'rtl');
            } else {
                document.documentElement.setAttribute('dir', 'ltr');
                localStorage.setItem('dir', 'ltr');
            }
        });
    });

    // ---- Mobile Menu Toggle ----
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // ---- Sticky Navbar ----
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // ---- Scroll to Top Button ----
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    if (scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });

        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ---- Active Navigation Link ----
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    // Desktop Nav Links
    const desktopNavLinks = document.querySelectorAll('.nav-link');
    desktopNavLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        if (linkHref === currentPath) {
            link.classList.add('text-primary', 'font-semibold');
            link.classList.remove('text-gray-600', 'dark:text-gray-300');
        } else {
            link.classList.remove('text-primary', 'font-semibold');
            link.classList.add('text-gray-600', 'dark:text-gray-300');
        }
    });

    // Mobile Nav Links
    const mobileNavLinks = document.querySelectorAll('#mobileMenu a:not([class*="btn-"])');
    mobileNavLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        // Check if the link is a standard navigation link (has a valid href and is not just '#')
        if (linkHref && !linkHref.startsWith('#')) {
            if (linkHref === currentPath) {
                link.classList.add('text-primary');
                link.classList.remove('text-gray-700', 'dark:text-gray-300');
            } else {
                link.classList.remove('text-primary');
                link.classList.add('text-gray-700', 'dark:text-gray-300');
            }
        }
    });

    // ---- Password Show/Hide Toggle ----
    const togglePasswordBtns = document.querySelectorAll('.toggle-password');
    togglePasswordBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            const targetId = this.getAttribute('data-target');
            const input = document.getElementById(targetId);
            const icon = this.querySelector('i');
            
            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });
});
