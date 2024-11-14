<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - Online CV</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; }
        h1, h2 { color: #333; }
        .bio, .contact, .skills, .education, .experience { margin-bottom: 20px; }
        ul { list-style-type: square; }
        img { max-width: 150px; border-radius: 50%; }
        .form-container { margin-top: 30px; }
        label { display: block; margin: 8px 0 4px; }
        input[type="text"], input[type="email"], textarea { width: 100%; padding: 8px; margin-bottom: 10px; }
        input[type="submit"] { background-color: #007BFF; color: white; padding: 10px 15px; border: none; cursor: pointer; }
    </style>
</head>
<body>

    <header>
        <h1>Your Name</h1>
        <p class="bio">I am a passionate [Your Profession/Field] with experience in [Relevant Fields]. My interests include [Your Interests], and I am motivated by [What Drives You]. My ultimate goal is to [Your Career Goals].</p>
    </header>

    <section class="contact">
        <h2>Contact Information</h2>
        <p><strong>Name:</strong> Your Name</p>
        <p><strong>Phone:</strong> (123) 456-7890</p>
        <p><strong>Email:</strong> yourname@example.com</p>
        <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a></p>
    </section>

    <section class="profile-image">
        <h2>Profile Picture</h2>
        <img src="path/to/your-image.jpg" alt="Your Profile Picture">
    </section>

    <section class="skills">
        <h2>Skills & Competencies</h2>
        <ul>
            <li>Skill 1: Proficiency Level</li>
            <li>Skill 2: Proficiency Level</li>
            <li>Skill 3: Proficiency Level</li>
        </ul>
    </section>

    <section class="education">
        <h2>Education</h2>
        <p><strong>Degree:</strong> Bachelor/Master of [Your Degree]</p>
        <p><strong>Institution:</strong> Your University, Year</p>
        <p><strong>Relevant Coursework:</strong> Course 1, Course 2, Course 3</p>
    </section>

    <section class="experience">
        <h2>Work Experience</h2>
        <p><strong>Job Title</strong> at <strong>Company Name</strong> (Year Started - Year Ended)</p>
        <ul>
            <li>Responsibility or achievement 1</li>
            <li>Responsibility or achievement 2</li>
            <li>Responsibility or achievement 3</li>
        </ul>
    </section>

    <!-- Search Form (GET) -->
    <section class="form-container">
        <h2>Search My CV</h2>
        <form method="GET" action="search-results.html">
            <label for="search">Search keywords:</label>
            <input type="text" id="search" name="search" placeholder="Enter keywords">
            <input type="submit" value="Search">
        </form>
    </section>

    <!-- Contact Form (POST) -->
    <section class="form-container">
        <h2>Contact Me</h2>
        <form method="POST" action="submit-feedback.html">
            <label for="visitor-name">Name:</label>
            <input type="text" id="visitor-name" name="visitor-name" required>
            
            <label for="visitor-email">Email:</label>
            <input type="email" id="visitor-email" name="visitor-email" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>
            
            <input type="submit" value="Send Message">
        </form>
    </section>

</body>
</html>
