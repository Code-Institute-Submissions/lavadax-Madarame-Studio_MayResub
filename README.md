<!-- PROJECT LOGO -->
<br />
<!-- TODO update href and src to GitHub & Logo link -->
<p align="center">
    <a href="#">
        <img src="#" alt="Logo" width="200" height="200">
    </a>
</p>

<!-- TODO add title, description & links -->
<p align="center">
    <h2 align="center">PROJECT TITLE</h2>
    <br />
    <p align="center">
        This is a description
        <br />
        <a href="#"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="#">View Demo</a>
        ·
        <a href="#">Report Bug</a>
        ·
        <a href="#">Request Feature</a>
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
        <li>
            <a href="#testing">Testing</a>
            <ul>
                <li><a href="#validation">Validation</a></li>
                <li><a href="#testing-user-stories">Testing User Stories</a></li>
                <li><a href="#functional-testing">Functional Testing</a></li>
                <li><a href="#accessibility-testing">Accessibility Testing</a></li>
            </ul>
        </li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
    </ol>
</details>


<!-- ABOUT THE PROJECT-->
## About The Project  

Below you can see a few screenshots of the finished project.  
  
<!-- TODO Add screenshots of the live site -->

### Built With

<!-- TODO Add/remove software/pages used -->
* [Gitpod](https://www.gitpod.io/) / [Gitpod Chrome extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) - Used to develop the site and push the project to Github.
* [GitHub](https://github.com) - Used for version control.
* [Whimsical](https://whimsical.com/) - Used to set up the wireframes at the start of the dev cycle. 
* [favicon.io](https://favicon.io/favicon-converter/) - Used to generate the favicon files.  


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

All wireframes are in a single file and can be found [here](https://github.com/lavadax/Madarame-Studio/blob/master/documentation/wireframes/wireframes.pdf).

### ER Diagram

The ER Diagram for the project describes the relationship between the used models and can be found [here](https://github.com/lavadax/Madarame-Studio/blob/master/documentation/er-diagrams/er-diagram.pdf)


<!-- ROADMAP -->
## Roadmap

<!-- TODO Add roadmap -->

### Future Plans

<!-- TODO Add plans -->

### Open Issues
<!-- TODO Add link -->
See the [open issues](https://github.com/lavadax/Madarame-Studio/issues) for a list of proposed features (and known issues).

### Past Issues
<!-- TODO Add link -->
See the [closed issues](https://github.com/lavadax/Madarame-Studio/issues?q=is%3Aissue+is%3Aclosed) for a list of the past issues.

Notable past issues:  
<!-- TODO Add major bugs encountered during dev process -->


<!-- TESTING -->
## Testing

### Validation
<!-- TODO Add code validation -->


### Testing User Stories
<!-- TODO Add user stories testing -->
#### First Time Visitor goals  
  

#### Returning Visitor Goals


### Functional Testing
<!-- TODO Add functional testing -->

### Accessibility Testing
<!-- TODO Add accessibility testing -->


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
<!-- TODO Add link -->
Distributed under the MIT License. See [`LICENSE`](https://github.com/lavadax/Madarame-Studio/blob/master/LICENSE.txt) for more information.


<!-- CONTACT -->
## Contact

Lavadax - [Twitter](https://twitter.com/LavadaxTwitch) - [facebook](https://www.facebook.com/kevin.schepers.5)
<!-- TODO Add link -->
Project Link: [#](#)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
<!-- TODO Add acknowledgements -->
* [github.com/othneildrew](https://github.com/othneildrew/Best-README-Template): for providing the readme template.
* [github.com/Code-Institute-Solutions](https://github.com/Code-Institute-Solutions/SampleREADME): for filling in gaps in the readme template.
