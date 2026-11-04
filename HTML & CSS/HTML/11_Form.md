
<title>HTML Forms - Questions 1 to 42</title>
h1 {
text-align: center;
}
h2 {
margin-top: 35px;
border-bottom: 2px solid #333;
padding-bottom: 5px;
}
section {
background-color: white;
padding: 20px;
margin-bottom: 25px;
border-radius: 8px;
}
form {
margin-top: 15px;
}
label {
display: block;
margin-top: 10px;
margin-bottom: 5px;
font-weight: bold;
}
input,
select,
textarea {
padding: 8px;
margin-bottom: 10px;
max-width: 100%;
}
button {
padding: 8px 15px;
margin: 5px;
cursor: pointer;
}
fieldset {
margin-bottom: 15px;
padding: 15px;
}
legend {
font-weight: bold;
}
.box {
padding: 10px;
border: 1px solid #ccc;
margin-top: 10px;
}
</style>
</head>
<body>
<h1>HTML Forms - Complete Assignment</h1>
<section>
<h2>Question 1 - Basic Form Structure</h2>
<form action="/submit.php" method="post" autocomplete="on">
<label for="q1-name">Name:</label>
<input type="text" id="q1-name" name="name">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 2 - Form with GET Method</h2>
<form action="/search.php" method="get">
<label for="q2-search">Search:</label>
<input type="search" id="q2-search" name="search">
<button type="submit">Search</button>
</form>
</section>
<section>
<h2>Question 3 - Form without Browser Validation</h2>
<form action="/register.php" method="post" novalidate>
<label for="q3-name">Name:</label>
<input type="text" id="q3-name" name="name" required>
<label for="q3-email">Email:</label>
<input type="email" id="q3-email" name="email" required>
<button type="submit">Submit Without Validation</button>
</form>
</section>
<section>
<h2>Question 4 - Default enctype</h2>
<form action="/submit.php" method="post" enctype="application/x-www-form-urlencoded">
<label for="q4-name">Name:</label>
<input type="text" id="q4-name" name="name">
<label for="q4-email">Email:</label>
<input type="email" id="q4-email" name="email">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 5 - File Upload</h2>
<form action="/upload.php" method="post" enctype="multipart/form-data">
<label for="q5-file">Choose File:</label>
<input type="file" id="q5-file" name="file">
<button type="submit">Upload File</button>
</form>
</section>
<section>
<h2>Question 6 - text/plain Encoding</h2>
<form action="/plain.php" method="post" enctype="text/plain">
<label for="q6-name">Name:</label>
<input type="text" id="q6-name" name="name">
<label for="q6-message">Message:</label>
<input type="text" id="q6-message" name="message">
<button type="submit">Submit</button>
</form>
<p>Note: text/plain encoding is rarely used in real-world projects.</p>
</section>
<section>
<h2>Question 7 - Form Name and Target</h2>
<form action="/response.php" method="post" name="userForm" target="_blank">
<label for="q7-name">Username:</label>
<input type="text" id="q7-name" name="username">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 8 - Proper Label</h2>
<form action="/submit.php" method="post">
<label for="email">Email Address:</label>
<input type="email" id="email" name="email">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 9 - Radio Button Group</h2>
<form action="/submit.php" method="post">
<p>Gender:</p>
<input type="radio" id="q9-male" name="gender" value="male" checked>
<label for="q9-male">Male</label>
<input type="radio" id="q9-female" name="gender" value="female">
<label for="q9-female">Female</label>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 10 - Multiple Checkboxes</h2>
<form action="/submit.php" method="post">
<p>Hobbies:</p>
<input type="checkbox" id="q10-coding" name="hobbies" value="coding" checked>
<label for="q10-coding">Coding</label>
<input type="checkbox" id="q10-reading" name="hobbies" value="reading">
<label for="q10-reading">Reading</label>
<input type="checkbox" id="q10-sports" name="hobbies" value="sports">
<label for="q10-sports">Sports</label>
<input type="checkbox" id="q10-music" name="hobbies" value="music">
<label for="q10-music">Music</label>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 11 - Drop-down List</h2>
<form action="/submit.php" method="post">
<label for="q11-car">Choose a Car:</label>
<select name="cars" id="q11-car">
<option value="toyota">Toyota</option>
<option value="honda">Honda</option>
<option value="ford">Ford</option>
</select>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 12 - Multi-select Drop-down</h2>
<form action="/submit.php" method="post">
<label for="q12-courses">Select Courses:</label>
<select id="q12-courses" name="courses" multiple size="3">
<option value="html">HTML</option>
<option value="css">CSS</option>
<option value="javascript">JavaScript</option>
<option value="python">Python</option>
</select>
<br>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 13 - optgroup</h2>
<form action="/submit.php" method="post">
<label for="q13-fruit">Choose Fruit:</label>
<select id="q13-fruit" name="fruit">
<optgroup label="Tropical Fruits">
<option value="mango">Mango</option>
<option value="banana">Banana</option>
</optgroup>
<optgroup label="Other Fruits">
<option value="apple">Apple</option>
<option value="orange">Orange</option>
</optgroup>
</select>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 14 - Multi-line Textarea</h2>
<form action="/submit.php" method="post">
<label for="q14-message">Your Comments:</label>
<textarea id="q14-message" name="message" rows="4" cols="50" placeholder="Enter your comments here"></textarea>
<br>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 15 - Button Types</h2>
<form action="/submit.php" method="post">
<button type="submit">Submit</button>
<button type="reset">Reset</button>
<button type="button">Normal Button</button>
</form>
</section>
<section>
<h2>Question 16 - Fieldset and Legend</h2>
<form action="/submit.php" method="post">
<fieldset>
<legend>Personal Information</legend>
<label for="q16-name">Name:</label>
<input type="text" id="q16-name" name="name">
<label for="q16-email">Email:</label>
<input type="email" id="q16-email" name="email">
</fieldset>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 17 - Disabled Fieldset</h2>
<form action="/submit.php" method="post">
<fieldset disabled>
<legend>Account Information</legend>
<label for="q17-username">Username:</label>
<input type="text" id="q17-username" name="username">
<label for="q17-password">Password:</label>
<input type="password" id="q17-password" name="password">
</fieldset>
</form>
</section>
<section>
<h2>Question 18 - Datalist</h2>
<form action="/submit.php" method="post">
<label for="q18-browser">Choose Browser:</label>
<input list="browsers" id="q18-browser" name="browser">
<datalist id="browsers">
<option value="Google Chrome">
<option value="Mozilla Firefox">
<option value="Microsoft Edge">
<option value="Safari">
</datalist>
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 19 - Password Constraints</h2>
<form action="/submit.php" method="post">
<label for="q19-password">Password:</label>
<input type="password" id="q19-password" name="password" required minlength="8">
<button type="submit">Create Password</button>
</form>
</section>
<section>
<h2>Question 20 - Multiple Email Values</h2>
<form action="/submit.php" method="post">
<label for="q20-email">Email Addresses:</label>
<input type="email" id="q20-email" name="emails" multiple placeholder="email1@example.com, email2@example.com">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 21 - Date Picker</h2>
<form action="/submit.php" method="post">
<label for="q21-date">Choose a Date in 2023:</label>
<input type="date" id="q21-date" name="date" min="2023-01-01" max="2023-12-31">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 22 - Number Input</h2>
<form action="/submit.php" method="post">
<label for="q22-quantity">Quantity:</label>
<input type="number" id="q22-quantity" name="quantity" min="1" max="10" step="1">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 23 - Range Slider</h2>
<form action="/submit.php" method="post">
<label for="q23-volume">Volume:</label>
<input type="range" id="q23-volume" name="volume" min="0" max="100" value="50">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 24 - File Restrictions</h2>
<form action="/upload.php" method="post" enctype="multipart/form-data">
<label for="q24-file">Upload PDF or DOCX:</label>
<input type="file" id="q24-file" name="document" accept=".pdf,.docx" required>
<button type="submit">Upload</button>
</form>
</section>
<section>
<h2>Question 25 - Hidden Input</h2>
<form action="/submit.php" method="post">
<input type="hidden" name="session_token" value="ABC123XYZ">
<label for="q25-name">Name:</label>
<input type="text" id="q25-name" name="name">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 26 - Color Picker</h2>
<form action="/submit.php" method="post">
<label for="q26-color">Favorite Color:</label>
<input type="color" id="q26-color" name="color" value="#ff0000">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 27 - Telephone Pattern</h2>
<form action="/submit.php" method="post">
<label for="q27-phone">Phone Number:</label>
<input type="tel" id="q27-phone" name="phone" pattern="[0-9]{10}" placeholder="Enter 10 digit phone number">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 28 - URL Input</h2>
<form action="/submit.php" method="post">
<label for="q28-url">Website URL:</label>
<input type="url" id="q28-url" name="website" required placeholder="https://example.com">
<button type="submit">Submit</button>
</form>
</section>
<section>
<h2>Question 29 - Search with Autofocus</h2>
<form action="/search.php" method="get">
<label for="q29-search">Search:</label>
<input type="search" id="q29-search" name="q" autofocus placeholder="Search here...">
<button type="submit">Search</button>
</form>
</section>
<section>
<h2>Question 30 - Input Outside Form</h2>
<form id="q30-form" action="/submit.php" method="post">
<button type="submit">Submit</button>
</form>
<label for="q30-name">Name Outside Form:</label>
<input type="text" id="q30-name" name="name" form="q30-form">
</section>
<section>
<h2>Question 31 - formaction Override</h2>
<form action="/default.php" method="post">
<label for="q31-name">Name:</label>
<input type="text" id="q31-name" name="name">
<br>
<button type="submit">Submit to Default</button>
<button type="submit" formaction="/special.php">Submit to Different URL</button>
</form>
</section>
<section>
<h2>Question 32 - formmethod Override</h2>
<form action="/submit.php" method="post">
<label for="q32-name">Name:</label>
<input type="text" id="q32-name" name="name">
<br>
<button type="submit">Submit with POST</button>
<button type="submit" formmethod="get">Submit with GET</button>
</form>
</section>
<section>
<h2>Question 33 - formnovalidate</h2>
<form action="/register.php" method="post">
<label for="q33-name">Name:</label>
<input type="text" id="q33-name" name="name" required>
<label for="q33-email">Email:</label>
<input type="email" id="q33-email" name="email" required>
<label for="q33-password">Password:</label>
<input type="password" id="q33-password" name="password" required>
<br>
<button type="submit">Register</button>
<button type="submit" formnovalidate>Save as Draft</button>
</form>
</section>
<section>
<h2>Question 34 - formtarget</h2>
<form action="/submit.php" method="post" target="_self">
<label for="q34-name">Name:</label>
<input type="text" id="q34-name" name="name">
<br>
<button type="submit">Submit Normally</button>
<button type="submit" formtarget="_blank">Preview in New Tab</button>
</form>
</section>
<section>
<h2>Question 35 - Complete Login Form</h2>
<form action="/login.php" method="post">
<label for="q35-username">Username:</label>
<input type="text" id="q35-username" name="username" required>
<label for="q35-password">Password:</label>
<input type="password" id="q35-password" name="password" required minlength="8">
<br>
<button type="submit">Login</button>
</form>
</section>
<section>
<h2>Question 36 - Registration Form with Fieldsets</h2>
<form action="/register.php" method="post">
<fieldset>
<legend>Personal Information</legend>
<label for="q36-name">Full Name:</label>
<input type="text" id="q36-name" name="name" required>
<label for="q36-email">Email:</label>
<input type="email" id="q36-email" name="email" required>
</fieldset>
<fieldset>
<legend>Preferences</legend>
<input type="checkbox" id="q36-newsletter" name="newsletter" value="yes">
<label for="q36-newsletter">Subscribe to Newsletter</label>
</fieldset>
<button type="submit">Register</button>
</form>
</section>
<section>
<h2>Question 37 - Contact Us Form</h2>
<form action="/contact.php" method="post">
<label for="q37-name">Name:</label>
<input type="text" id="q37-name" name="name" required>
<label for="q37-email">Email:</label>
<input type="email" id="q37-email" name="email" required>
<label for="q37-message">Message:</label>
<textarea id="q37-message" name="message" rows="6" cols="50" required></textarea>
<br>
<button type="submit">Send Message</button>
</form>
</section>
<section>
<h2>Question 38 - Survey / Feedback Form</h2>
<form action="/feedback.php" method="post">
<label for="q38-satisfaction">Satisfaction (1-10):</label>
<input type="range" id="q38-satisfaction" name="satisfaction" min="1" max="10" value="5">
<p>Would you recommend us?</p>
<input type="radio" id="q38-yes" name="recommend" value="yes">
<label for="q38-yes">Yes</label>
<input type="radio" id="q38-no" name="recommend" value="no">
<label for="q38-no">No</label>
<label for="q38-comments">Comments:</label>
<textarea id="q38-comments" name="comments" rows="5" cols="50" placeholder="Enter your feedback"></textarea>
<br>
<button type="submit">Submit Feedback</button>
</form>
</section>
<section>
<h2>Question 39 - Complete File Upload Form</h2>
<form action="/upload.php" method="post" enctype="multipart/form-data">
<label for="q39-resume">Resume:</label>
<input type="file" id="q39-resume" name="resume" accept=".pdf,.docx" required>
<label for="q39-photo">Profile Photo:</label>
<input type="file" id="q39-photo" name="photo" accept="image/*">
<br>
<button type="submit">Upload Files</button>
</form>
</section>
<section>
<h2>Question 40 - Search Form Using GET</h2>
<form action="/search.php" method="get">
<label for="q40-search">Search:</label>
<input type="search" id="q40-search" name="q" autofocus placeholder="Search the website...">
<button type="submit">Search</button>
</form>
</section>
<section>
<h2>Question 41 - Advanced Job Application Form</h2>
<form action="/apply.php" method="post" enctype="multipart/form-data">
<fieldset>
<legend>Personal Details</legend>
<label for="q41-name">Full Name:</label>
<input type="text" id="q41-name" name="name" required>
<label for="q41-email">Email:</label>
<input type="email" id="q41-email" name="email" required>
<label for="q41-phone">Phone:</label>
<input type="tel" id="q41-phone" name="phone" pattern="[0-9]{10}" placeholder="10 digit number" required>
</fieldset>
<fieldset>
<legend>Experience</legend>
<label for="q41-experience">Work Experience:</label>
<textarea id="q41-experience" name="experience" rows="6" cols="50" placeholder="Describe your experience"></textarea>
</fieldset>
<label for="q41-resume">Resume:</label>
<input type="file" id="q41-resume" name="resume" accept=".pdf" required>
<p>Employment Type:</p>
<input type="radio" id="q41-fulltime" name="employment_type" value="full-time">
<label for="q41-fulltime">Full-time</label>
<input type="radio" id="q41-parttime" name="employment_type" value="part-time">
<label for="q41-parttime">Part-time</label>
<input type="radio" id="q41-internship" name="employment_type" value="internship">
<label for="q41-internship">Internship</label>
<p>
<input type="checkbox" id="q41-terms" name="terms" value="accepted" required>
<label for="q41-terms">I agree to the Terms and Conditions.</label>
</p>
<button type="submit">Submit Application</button>
<button type="submit" formnovalidate>Save Draft</button>
</form>
</section>
<section>
<h2>Question 42 - All Major Form Override Attributes</h2>
<form action="/default.php" method="post" target="_self">
<label for="q42-name">Name:</label>
<input type="text" id="q42-name" name="name" required>
<label for="q42-email">Email:</label>
<input type="email" id="q42-email" name="email" required>
<br><br>
<button type="submit">1. Default Submit</button>
<button type="submit" formaction="/other.php">2. Override Action</button>
<button type="submit" formmethod="get">3. Override Method</button>
<button type="submit" formnovalidate>4. Skip Validation</button>
<button type="submit" formtarget="_blank">5. Open in New Tab</button>
</form>
</section>
<footer>
<hr>
<p style="text-align: center;">
HTML Forms Assignment - Questions 1 to 42
</p>
