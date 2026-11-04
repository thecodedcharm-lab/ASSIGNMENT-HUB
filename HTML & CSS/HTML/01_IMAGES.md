1. Create an image tag that displays an image named flower.jpg which is in the same folder as your HTML file. Add proper alt text.

2. Display an image named logo.png that is stored inside a folder called images. Your HTML file is outside the images folder.
Also give the image a width of 200px.

3. An image named banner.jpg is inside a folder called assets/images. Your HTML file is in the root folder. Write the correct src path and add alt text.

4. Your HTML file is inside a folder called pages. The image photo.jpg is in the root folder. Write the correct path to display the image.

5. Display an image with:

src = images/nature.jpg
alt = "Beautiful nature view"
width = 300
height = 200
6. Add a title attribute to an image so that when the user hovers over it, the text “Click to view full size” appears.

7. Create an image that should load only when the user scrolls near it (lazy loading). Use an image from the images folder.

8. Create a hero image that should load immediately when the page opens (eager loading).

9. Write an image tag using loading="auto" and explain in one line what the browser will decide.

10. Create a responsive image using srcset with three versions:

small.jpg (400w)
medium.jpg (800w)
large.jpg (1200w)
Also add a normal src as fallback.

11. Create a complete image tag that includes all these attributes:

Image is inside images/ folder
alt text
width and height
loading="lazy"
title
srcset with two sizes
12. Create two images side by side:

First image loads immediately (eager) and is a logo from assets/logo.png
Second image loads lazily and is a product photo from images/products/shoe.jpg Both should have proper alt text and width of 250px.


 <div style="background-color: rgb(252, 196, 191);border-color: rgb(245, 255, 183); border-width: 2px; border-style: solid;">
  <h1>IMAGES</h1>
<H3>ANSWER 01</H3>
    <img src="flower.png" alt="Profile Image" width="200" height="200" class="center-image">
<H3>ANSWER 02 </H3>
    <img src="IMAGES/Myprofile.jpg" alt="Profile Image" width="200" height="200" class="center-image">
<H3>ANSWER 03</H3>
<img src="IMAGES/Myprofile.jpg" alt="Website banner">
<H3>ANSWER 04</H3>
<img src="../photo.jpg" alt="Photo">
<H3>ANSWER 05</H3>
<img src="images/nature.jpg" alt="Beautiful nature view" width="300" height="200">
<H3>ANSWER 06</H3>
<img src="images/photo.jpg" alt="Photo" title="Click to view full size">
<H3>ANSWER 07</H3>
<img src="images/nature.jpg" alt="Nature view" loading="lazy">
<H3>ANSWER 08</H3>
<img src="images/hero.jpg" alt="Hero image" loading="eager">
<H3>ANSWER 09</H3>
<img src="images/photo.jpg" alt="Photo" loading="auto">
<H3>ANSWER 10</H3>
<img
    src="large.jpg"
    srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
    alt="Responsive image">
<H3>ANSWER 11</H3>
<img
    src="images/photo.jpg"
    alt="Beautiful landscape"
    width="800"
    height="500"
    loading="lazy"
    title="View the image"
    srcset="images/photo-small.jpg 400w, images/photo-large.jpg 800w">
<H3>ANSWER 12</H3>
<img src="assets/logo.png" alt="Company logo" width="250" loading="eager">

<img src="images/products/shoe.jpg" alt="Product shoe" width="250" loading="lazy">
</div>

<div style="background-color: rgb(255, 232, 174);border-color: rgb(245, 255, 183); border-width: 2px; border-style: solid;">
