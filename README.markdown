To link to a Google Map:
========================

Creating a link in this manner is important because it makes it easy for people on the computer and on mobile phones to get directions quickly. In particular, clicking this link on an iPhone will launch the Google Maps app.

1. Search for the school in question on Google Maps.
2. Find the school and select "more info,"
3. From the school's info page, click the "directions" link.
4. A map should appear with a place to enter an address on the left side. Click the "link" link above the top-right of the map.
5. Copy and paste the link onto the website's homepage.

To create a reminder e-mail:
============================

1. Update the HP Science webpage.
2. Copy the webpage into a new e-mail.
3. Change the font to something nice like Helvetica.
4. If you can, adjust the size of the table to fit the new font. This can be done in GMail on in TextEdit on a Mac, but it requires patience and a steady hand to select the edges of the table. It can also be done by editing the HTML, if you're into that.
5. Make the subject of the e-mail something descriptive, so people will open it.
6. Address the e-mail to yourself, CC Mr. Chuang, and BCC everybody else.

E-mail template:
================

    <p>UIL Science Team,</p>

    <p><strong>Saturday, March 5</strong> is our next meet. The bus leaves at <strong>7:45 A.M.</strong></p>

    <h2>Address</h2>
    <a href="http://maps.google.com/maps/place?cid=1494598335925802517">
    3411 Peters Colony<br>
    Flower Mound, TX 75022</a>

    <h2>Schedule</h2>
    <table>
    <tr><td>8:55</td>
    <td>Number Sense</td></tr>
    <tr><td>9:10</td>
    <td>Calculator</td></tr>
    <tr><td>9:45</td>
    <td>Mathematics</td></tr>
    <tr><td>10:35</td>
    <td>Science</td></tr>
    </table>

    <p>Until Then,<br>
    Trey</p>

To update the Results tab:
==========================

1. Download `results.py` from the server
2. From the terminal, `cd` into the folder where you downloaded `results.py` and run the command `python3 results.py`
3. If the script runs successfully, upload the `results` folder back to the server

Troubleshooting `results.py`:
=============================

1. If you don't have Python 3, install it using [this guide](http://diveintopython3.org/installing-python.html).
2. If you don't know how to run `results.py`, ask someone or use Google.
3. If the script produces old data, be sure all of the parameters are up to date. Open the script in a text editor and verify that `year`, `districts`, etc. are all set to the correct values.
4. If heaven forbid a regular expression breaks, use the interactive Python shell or a regex tool to manually adjust and test the regular expressions until they work. Be sure that you are modeling the regular expressions off of the source of the HTML data pages, rather than just what they look like in the browser.