```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semantic HTML - Questions 1 to 10</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        h2 {
            margin-top: 30px;
            border-bottom: 2px solid #333;
            padding-bottom: 5px;
        }

        section {
            background-color: white;
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 8px;
        }

        nav a {
            margin-right: 15px;
        }

        figure {
            margin: 15px 0;
        }

        img {
            max-width: 300px;
        }

        aside {
            background-color: #f0f0f0;
            padding: 15px;
            margin-top: 15px;
        }

        footer {
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>

<body>

    <h1>Semantic HTML - Complete Assignment</h1>


    <!-- ===================================================== -->
    <!-- QUESTION 1 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 1 - Basic Semantic Page Structure</h2>

        <!-- ANSWER 01 -->

        <header>
            <h1>SkillForge Academy</h1>
            <p>Welcome to our learning platform.</p>
        </header>

        <main>
            <article>
                <h2>Learn Web Development</h2>
                <p>Build your skills with practical web development courses and projects.</p>
            </article>
        </main>

        <aside>
            <p>Related Information: Explore our programming courses.</p>
        </aside>

        <footer>
            <p>Copyright &copy; 2026 SkillForge Academy</p>
        </footer>
    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 2 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 2 - Semantic News Item</h2>

        <!-- ANSWER 02 -->

        <article>

            <header>
                <h2>New Technology Workshop Announced</h2>
            </header>

            <p>
                Published on
                <time datetime="2026-08-31">August 31, 2026</time>.
                The workshop will introduce students to
                <mark>Artificial Intelligence</mark>
                and modern development tools.
            </p>

            <footer>
                <p>Source: SkillForge News</p>
            </footer>

        </article>
    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 3 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 3 - Blog Style Page</h2>

        <!-- ANSWER 03 -->

        <header>
            <h1>My Tech Blog</h1>

            <nav>
                <a href="#">Home</a>
                <a href="#">Articles</a>
                <a href="#">Contact</a>
            </nav>
        </header>

        <main>

            <article>
                <h2>Learning HTML</h2>
                <p>HTML provides the structure and meaning of web pages.</p>
            </article>

            <article>
                <h2>Starting with CSS</h2>
                <p>CSS helps us style websites and create attractive layouts.</p>
            </article>

            <aside>
                <h3>Related Links</h3>
                <ul>
                    <li><a href="#">HTML Basics</a></li>
                    <li><a href="#">CSS Basics</a></li>
                    <li><a href="#">JavaScript Basics</a></li>
                </ul>
            </aside>

        </main>

        <footer>
            <p>Copyright &copy; 2026 My Tech Blog</p>
        </footer>
    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 4 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 4 - FAQ with Details</h2>

        <!-- ANSWER 04 -->

        <h2>Frequently Asked Questions</h2>

        <details>
            <summary>What is HTML?</summary>
            <p>HTML is the standard language used to structure web pages.</p>
        </details>

        <details>
            <summary>What is CSS?</summary>
            <p>CSS is used to style and design HTML elements.</p>
        </details>

        <details>
            <summary>What is JavaScript?</summary>
            <p>JavaScript is used to add behavior and interactivity to websites.</p>
        </details>

    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 5 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 5 - Product Page Fragment</h2>

        <!-- ANSWER 05 -->

        <main>

            <article>

                <h2>Smart Study Lamp</h2>

                <p>
                    The Smart Study Lamp provides adjustable lighting
                    for comfortable studying and reading.
                </p>

                <figure>
                    <img src="https://via.placeholder.com/300" alt="Smart Study Lamp">
                    <figcaption>Smart Study Lamp for students</figcaption>
                </figure>

                <details>
                    <summary>Technical Specifications</summary>
                    <p>Power: 12W</p>
                    <p>Brightness: Adjustable</p>
                    <p>Color Temperature: 3000K - 6500K</p>
                </details>

            </article>

            <aside>
                <h3>Seller Information</h3>
                <p>Seller: TechStore</p>
                <p>Contact: seller@example.com</p>
            </aside>

        </main>
    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 6 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 6 - Article with Time and Highlighting</h2>

        <!-- ANSWER 06 -->

        <article>

            <header>
                <h2>The Future of Web Development</h2>
            </header>

            <p>
                Published on
                <time datetime="2026-08-31">August 31, 2026</time>.
            </p>

            <p>
                Reading time:
                <time datetime="PT5M">5 minutes</time>.
            </p>

            <p>
                Modern websites focus on
                <mark>accessibility and user experience</mark>
                to provide better experiences for everyone.
            </p>

            <aside>
                <h3>Related Information</h3>
                <p>Learn more about HTML, CSS, JavaScript, and responsive design.</p>
            </aside>

            <footer>
                <p>Written by: Alex Johnson</p>
            </footer>

        </article>
    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 7 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 7 - Navigation in Three Places</h2>

        <!-- ANSWER 07 -->

        <header>
            <h1>Tech Academy</h1>

            <nav>
                <a href="#">Home</a>
                <a href="#">Courses</a>
                <a href="#">About</a>
            </nav>
        </header>

        <main>
            <h2>Welcome to Tech Academy</h2>
            <p>Learn programming, web development, and modern technology skills.</p>
        </main>

        <aside>

            <nav>
                <a href="#">HTML</a>
                <a href="#">CSS</a>
                <a href="#">Python</a>
            </nav>

        </aside>

        <footer>

            <nav>
                <a href="#">Privacy Policy</a>
                <a href="#">Terms and Conditions</a>
            </nav>

        </footer>

    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 8 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 8 - Review Section</h2>

        <!-- ANSWER 08 -->

        <article>

            <header>
                <h2>Student Review</h2>
            </header>

            <figure>
                <img src="https://via.placeholder.com/300" alt="Student using a laptop">
                <figcaption>Student learning web development</figcaption>
            </figure>

            <p>
                Published on
                <time datetime="2026-08-31">August 31, 2026</time>.
            </p>

            <details>
                <summary>Read Full Review</summary>
                <p>
                    This course helped me understand HTML, CSS, and
                    JavaScript through practical examples and projects.
                </p>
            </details>

            <footer>
                <p>Reviewed by: Student</p>
            </footer>

        </article>
    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 9 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 9 - Complete Semantic Homepage</h2>

        <!-- ANSWER 09 -->

        <header>
            <h1>TechWorld</h1>

            <nav>
                <a href="#">Home</a>
                <a href="#">Courses</a>
                <a href="#">Blog</a>
            </nav>
        </header>

        <main>

            <section>

                <article>

                    <header>
                        <h2>Learn Web Development</h2>
                    </header>

                    <p>
                        Start learning <mark>HTML</mark> and build your first website.
                        Published on
                        <time datetime="2026-08-31">August 31, 2026</time>.
                    </p>

                    <figure>
                        <img src="https://via.placeholder.com/300" alt="Web development illustration">
                        <figcaption>Learning modern web development</figcaption>
                    </figure>

                    <details>
                        <summary>Learn More</summary>
                        <p>Explore HTML, CSS, JavaScript, and responsive web design.</p>
                    </details>

                    <footer>
                        <p>Article by TechWorld Team</p>
                    </footer>

                </article>

            </section>


            <section>

                <article>

                    <header>
                        <h2>Why Learn Programming?</h2>
                    </header>

                    <p>
                        Programming helps you solve problems and create useful
                        applications and websites.
                    </p>

                    <footer>
                        <p>Article by TechWorld Team</p>
                    </footer>

                </article>

            </section>


            <aside>
                <h3>Related Content</h3>
                <p>Explore our latest technology tutorials.</p>
            </aside>

        </main>

        <footer>
            <p>Copyright &copy; 2026 TechWorld</p>
        </footer>

    </section>


    <!-- ===================================================== -->
    <!-- QUESTION 10 -->
    <!-- ===================================================== -->

    <section>
        <h2>Question 10 - News Magazine Layout</h2>

        <!-- ANSWER 10 -->

        <header>
            <h1>Daily Tech Magazine</h1>
        </header>

        <main>

            <section>

                <article>

                    <header>
                        <h2>AI Technology Continues to Grow</h2>
                    </header>

                    <p>
                        Published on
                        <time datetime="2026-08-31">August 31, 2026</time>.
                    </p>

                    <p>
                        New developments in
                        <mark>Artificial Intelligence</mark>
                        are changing how people work and learn.
                    </p>

                    <footer>
                        <p>Author: Tech News Team</p>
                    </footer>

                </article>

            </section>


            <section>

                <article>

                    <header>
                        <h2>New Web Development Tools Released</h2>
                    </header>

                    <p>
                        Published on
                        <time datetime="2026-08-30">August 30, 2026</time>.
                    </p>

                    <p>
                        Developers are using
                        <mark>modern development tools</mark>
                        to create faster and more accessible websites.
                    </p>

                    <footer>
                        <p>Author: Web News Team</p>
                    </footer>

                </article>

            </section>


            <aside>
                <h2>Editor's Picks</h2>
                <p>Top Technology Trends of 2026</p>
                <p>Best Web Development Practices</p>
                <p>Introduction to Artificial Intelligence</p>
            </aside>

        </main>

        <footer>
            <p>Copyright &copy; 2026 Daily Tech Magazine</p>
        </footer>

    </section>


    <footer>
        <hr>
        <p style="text-align: center;">
            Semantic HTML Assignment - Questions 1 to 10
        </p>
    </footer>

</body>
</html>
```
