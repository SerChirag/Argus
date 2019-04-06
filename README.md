# Argus

## Abstract

Vision is out most dominant sense and account for a majority of our sensory information.
But a lot of people suffer from undiagnosed optical disorders, especially myopia (Nearsightedness). It is expected that by 2050, 50% of the world's population, a total of nearly 5 billion, will suffer from myopia.

Thus, eye healthcare is of utmost importance in developing countries like India. We have sought to develop a web-application to facilitate the process of eye-checkup. 
**This app targets those people who have connection to the internet but cannot visit eye clinics due to affordability, remoteness etc.**

This project was made for TopCoder Hackathon organized in April 2019.

## Installation

 1. `git clone https://github.com/prabhakarpd7284/GiantPanda`
 2. `cd GiantPanda/`
 3. `pip install requirements.txt`

To test on localhost, run `python app.py`

## Details



**Distance Measurement**

The first and foremost conditions for any test is a controlled environment. For our eye-checkups, we need to have a fixed distance from the screen.
In order to do that, we use the web-cam of the device and a simple piece of paper of universal dimension.
All the user has to do is hold that paper in front of a clear background, and move to the required distance.
**In this way, user does not have to externally measure the distance.**

To improve the Computer Vision algorithm, we added wieghted sum average of the distances to get stable values.

![Alt Text](https://media.giphy.com/media/U3rkHdWab0vqsC3UPr/giphy.gif)


**Vision Acuity using Speech Processing**

We have used the **The Snellen test**, using letters are different sizes. 
The user stands a fixed distance away from the screen (1 meter) and using **his/her voice communicates** with the computer of what letter he/she can see. The size of the letter keep decreasing with very succesful answer.
When the user is no longer, **he/she can say "STOP"** and the results for that particular eye are calculated.

**Colour Vision**

We have used the **Ishihara Color Test**.
Images 1 – 10 each contain a number, plates 18 – 24 contain one or two wiggly lines. To pass each test you must identify the correct number.

**Results**

After the completion of the test, the user will be presented with the following results. 

 1. Outcome of each test for each eye.
 2. Location of nearest Ophthalmologist/eye-clinic.
 3. General tips for better eye-care.

## License
This project is under Apache License. Check out : [License](https://github.com/prabhakarpd7284/GiantPanda/blob/master/LICENSE)

## Authors

 - [Chirag Vashist](https://github.com/SerChirag)
 - [Prabhakar PD](https://github.com/prabhakarpd7284)
 - [Akhilesh Devrari](http://github.com/akhileshdevrari/) 

