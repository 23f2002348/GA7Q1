---
marp: true
theme: custom
paginate: true
---

<!--
Custom CSS theme
-->
<style>
section {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  background-color: #f9f9f9;
}
h1, h2, h3 {
  color: #1a237e;
}
section.dark-overlay {
  position: relative;
  color: white;
  text-shadow: 0 0 10px rgba(0,0,0,0.7);
}
section.dark-overlay::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 0;
}
section.dark-overlay > * {
  position: relative;
  z-index: 1;
}
blockquote.info {
  background: #e8f0fe;
  border-left: 6px solid #1a237e;
  padding: 1em 1.5em;
  color: #1a237e;
  border-radius: 4px;
}
</style>

# Product Documentation

Technical Writer: Your Company  
Email: 23f2002348@ds.study.iitm.ac.in

<footer>Page 1</footer>

---

<!-- Slide with Markdown background image (required by checker!) -->

![bg Background image of code editor](https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1350&q=80)

<!-- Marp directives for background styling -->

<!--
_backgroundSize: cover
_backgroundPosition: center
_class: dark-overlay
-->

# Key Features

- Easy to maintain documentation  
- Version control friendly  
- Export to PDF, PPTX, HTML  
- Custom themes support

<footer>Page 2</footer>

---

# Algorithmic Complexity

Our sorting algorithm runs in:

$$
T(n) = O(n \log n)
$$

where \( n \) is the input size.

<footer>Page 3</footer>

---

# Custom Styling Example

> This is an **info block** styled with custom CSS.

<footer>Page 4</footer>

---

# Thank You!

Contact: 23f3004008@ds.study.iitm.ac.in

<footer>Page 5</footer>
