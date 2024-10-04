import streamlit as st
css='''
<style>
    * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

.footer-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    padding: 0 10px;
}

.footer-section {
    margin-bottom: 20px;
}

.footer-section h3 {
    margin-bottom: 15px;
}

.footer-section p, .footer-section ul, .footer-section a {
    font-size: 14px;
    color: #bbb;
    text-decoration: none;
}

.footer-section ul {
    list-style-type: none;
    padding: 0;
}

.footer-section ul li {
    margin-bottom: 10px;
}

.footer-section a:hover {
    color: #fff;
}

.social-links a {
    display: inline-block;
    margin-right: 10px;
    color: #bbb;
}

.social-links a:hover {
    color: #fff;
}

.footer-bottom {
    background-color: #222;
    padding: 10px 0;
    font-size: 12px;
    color: #bbb;
}

@media (max-width: 768px) {
    .footer-container {
        flex-direction: column;
        align-items: center;
    }

    .footer-section {
        width: 80%;
        text-align: center;
    }
}
'''

ht='''
<footer>
        <div class="footer-container">
            <div class="footer-section about">
                <h3>About Us</h3>
                <p>We are a team of passionate developers building great web solutions. Our goal is to deliver high-quality projects with the best user experience.</p>
            </div>
            <div class="footer-section links">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section social">
                <h3>Follow Us</h3>
                <div class="social-links">
                    <a href="#">Facebook</a>
                    <a href="#">Twitter</a>
                    <a href="#">Instagram</a>
                    <a href="#">LinkedIn</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2024 | Designed by WebDev Team
        </div>
    </footer>
'''
