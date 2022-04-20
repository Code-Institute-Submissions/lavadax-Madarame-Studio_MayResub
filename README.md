<!-- PROJECT LOGO -->
<br />
<p align="center">
    <a href="https://lavadax-madarame-studio.herokuapp.com">
        <img src="documentation/logo.png" alt="Logo" width="310" height="40">
    </a>
</p>

<p align="center">
    <h2 align="center">MADARAME STUDIO</h2>
    <br />
    <p align="center">
        This is the 4th milestone project for code institute and is mostly focused on bringing together HTML, CSS, Javascript and Python through the use of the django framework.  
        This project is meant to simulate an e-commerce shop focusing on art, enabling users to purchase art, sign up for an account, and complete purchases using Stripe.
        <br />
        ·
        <a href="https://github.com/lavadax/Madarame-Studio/issues">Report Bug</a>
        ·
        <a href="https://github.com/lavadax/Madarame-Studio/issues">Request Feature</a>
    </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
    <summary><strong>Table of Contents</strong></summary>
    <ol>
        <li>
            <a href="#about-the-project">About The Project</a>
            <ul>
                <li><a href="#built-with">Built With</a></li>
            </ul>
        </li>
        <li>
            <a href="#deployment">Deployment</a>
            <ul>
                <li><a href="#heroku">Heroku</a></li>
            </ul>
        </li>
        <li>
            <a href="#usage">Usage</a>
            <ul>
                <li><a href="#user-stories">User Stories</a></li>
                <li><a href="#design">Design</a></li>
                <li><a href="#wireframes">Wireframes</a></li>
                <li><a href="#er-diagram">ER Diagram</a></li>
            </ul>
        </li>
        <li>
            <a href="#roadmap">Roadmap</a>
            <ul>
                <li><a href="#future-plans">Future Plans</a></li>
                <li><a href="#open-issues">Open Issues</a></li>
                <li><a href="#past-issues">Past issues</a></li>
            </ul>
        </li>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
    </ol>
</details>


<!-- ABOUT THE PROJECT-->
## About The Project  

Below you can see a few screenshots of the finished project.  
  
Home Page:  
![Home Page](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/showcase/home.png)  
  
Product List:  
![Product List](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/showcase/products.png)  
  
Product Detail:  
![Product Details](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/showcase/Product_detail.png)  
  
Login:  
![Login](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/showcase/login.png)  
  
Profile:  
![Profile](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/showcase/profile.png)  
  
Order History:  
![Order History](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/showcase/order_history.png)  

### Built With

#### Languages
* HTML5
* CSS
* Javascript
* Python

#### Databases
* SQLite - local database used during development.
* Postgres - database used post-deployment.
* AWS S3 - Database used to host static files and product images.

#### Frameworks & external sites
* [GitHub](https://github.com) - Used for version control.
* [Gitpod](https://www.gitpod.io/) / [Gitpod Chrome extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) - Used to develop the site and push the project to Github.
* [Whimsical](https://whimsical.com/) - Used to set up the wireframes at the start of the dev cycle.
* [favicon.io](https://favicon.io/favicon-converter/) - Used to generate the favicon files.
* [fontawesome](https://fontawesome.com) - Used to add icons across the site.
* [bootstrap](https://getbootstrap.com) - Used to simplify styling.
* [W3 HTML validator](https://validator.w3.org/nu/) - Used to validate HTML code.
* [W3 CSS validator](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code.
* [JSHint](https://jshint.com) - Used to validate JS code.
* [pycodestyle](https://pypi.org/project/pycodestyle/) - Used to validate python code.


<!-- DEPLOYMENT -->
## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Install the required dependencies in your repository, and save them in requirements.txt by typing "pip3 freeze --local > requirements.txt".
2. Create a Procfile by typing "echo web: python app.py > Procfile" so Heroku knows what file to run.
3. Log into heroku and create a new app.
4. Give your app a unique name and select the applicaple region.
5. Go to the "Deploy" tab, and select your preferred deployment method. For this project, I used automatic deployment from github.
6. After selecting automatic deployment, enter the name of your github repository, select it from the menu when it is found, and click connect.
7. Navigate to the "Settings" tab, click "Reveal Config Vars", and apply the same variables as in your env.py file, or your IDE environment variables.
8. Now return to the "Deploy tab, scroll down, and enable automatic deployment.


<!-- USAGE EXAMPLES -->
## Usage

### User Stories

#### First Time Visitors

* As a new user, I want to easily understand the purpose of the site.
* As a new user, I want to be able to easily navigate the site and access the content it provides.
* As a new user, I want to easily find where to sign up for an account.
* As a new user, I want to find product reviews.

#### Returning Visitors

* As a returning user, I want to easily log into my account.
* As a returning user, I want to be able to locate my order history and check the status of my pending orders.
* As a returning user, I want to leave reviews for products that I purchased before.

### Design

#### Colour Scheme

* The main colours used are #f9b87b and #7bbcf9, pastel orange and pastel blue.  
* Pastel orange is meant to illicit feelings of excitement, energy and confidence for the site visitor, while pastel blue is meant to show trust and competence.

#### Typography

* For headers the main font will be Abril Fatface, with Rockwell and serif as fallbacks in case the font isn't being imported correctly for some reason.  
* For regular text on the site, the main font will be Dosis, with Helvetica and sans-serif as fallbacks.  
* Using serif fonts as headers makes it easier to read the serif fonts, as they'll be forced into uppercase which makes them easier to read, while also adding to the playfulness and creativity of the site.  
* Using sans-serif on the rest of the page is to balance the playfulness with a cleaner feel as well as increasing the readability of the site.

### Wireframes

All wireframes are in a single file and can be found [here](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/wireframes/wireframes.pdf).

### ER Diagram

The ER Diagram for the project describes the relationship between the used models and can be found [here](https://github.com/lavadax/Madarame-Studio/blob/main/documentation/er-diagrams/er-diagram.pdf)


<!-- ROADMAP -->
## Roadmap

### Future Plans

* Allow users to leave reviews on products which will dynamically affect the product ratings.
* Allow users to sign up as an artist.
* Allow artists to upload art and sell it on the page after being reviewed by the site owners.

### Open Issues

See the [open issues](https://github.com/lavadax/Madarame-Studio/issues) for a list of proposed features (and known issues).

### Past Issues

See the [closed issues](https://github.com/lavadax/Madarame-Studio/issues?q=is%3Aissue+is%3Aclosed) for a list of the past issues.

Notable past issues:  

* When creating fixtures, a typo in one of the artist models caused it to remain empty, raising an error from Django.  
Unfortunately this typo went unnoticed for around an hour where no progress was being made on the project.
* When creating the artist app and swapping the artist name and url fields from the product model,  
mutliple site refreshes as old references kept being pointed out.


<!-- TESTING -->
## Testing

Testing information can be found in it's own [TESTING.md](https://github.com/lavadax/Madarame-Studio/blob/main/TESTING.md) file.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License
Distributed under the MIT License. See [`LICENSE`](https://github.com/lavadax/Madarame-Studio/blob/main/LICENSE.txt) for more information.


<!-- CONTACT -->
## Contact

Lavadax - [Twitter](https://twitter.com/LavadaxTwitch) - [facebook](https://www.facebook.com/kevin.schepers.5)
Project Link: [Madarame Studio](https://lavadax-madarame-studio.herokuapp.com)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [github.com/othneildrew](https://github.com/othneildrew/Best-README-Template): for providing the readme template.
* [github.com/Code-Institute-Solutions](https://github.com/Code-Institute-Solutions/SampleREADME): for filling in gaps in the readme template.
* [github.com - boutique ado miniproject](https://github.com/Code-Institute-Solutions/boutique_ado_v1): for providing a solid base for this project.
* [djangoproject.com](https://docs.djangoproject.com/en/3.2/): for providing documentation on the django framework.
* [pixabay.com](https://pixabay.com): for providing all the images and artists featured on the page.
* [github.com/nar3nd3r](https://github.com/nar3nd3r): for providing support as my project mentor.