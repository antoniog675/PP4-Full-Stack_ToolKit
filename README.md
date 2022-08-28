<h1>Cocktails</h1>

<h3>About the website</h3>
<hr>
<p>This is a website where users can explore different types of cocktails, in this website if users register then can create their own cocktail, upload it to share, and if they change their mind they can edit or even delete their posts.</p>
<p>Users can also interact with other users in the comment sections to be able to share their ideas f and just add more interactivity throughout the website.</p>

![Am I responsive image](/media/amiresponsive_cocktailzapp.jpg)

[Live Site](https://cocktailzapp.herokuapp.com/) 

<h3>Target Audience</h3>
<p>This website is designed for people that love their Cocktails, in this website they can view different types of Cocktails that have been uploaded, see the ingredients, how to make it and reviews from other website users. People that sign up can also share their passion for their favourite Cocktails, they can themselves upload and share their go to drinks on nights out!</p>
<p>18 and over


<h1>User Stories</h1>

<ul>
    <li>As a admin/user I can view my liked posts on a different page so that I can see which are my favourites drinks</li>
    <li>As a admin/user I can manage my post so that if I made a mistake and can change it and update it</li>
    <li>As a user I can view a post so that I can see the content of the drinks, likes and comment section</li>
    <li>As a user I can comment on a post so that I can be involved in the conversation</li>
    <li>As a user I can like and unlike a post so that interact with the content</li>
    <li>As a user I can save a draft so that I can finish adding my drink to the site</li>
    <li>As a user I can view paginated list of posts so that I can have a list of all the items and view them easily</li>
    <li>As a user I can create an account so that I can add drinks, like and comment on other people posts</li>
    <li>As a user I can see how may likes/dislikes there are for a drink so that I can see which is more popular or which is the least</li>
    <li>As the admin I can approve of user comments so that only positive comments are uploaded into the site, this approval will just be for posts that do not belong to the user</li>
    <li>As a admin I can approve which drinks are added into the website so that there is interactivity between myself and users and so that I can make sure there are not any duplicates or just mixed drinks</li>
    <li>As a user I can add my own drink if it isn't there already so that people will be able to explore more cocktails</li>
</ul>

<h2>Structure</h2>

<details>
<summary>Home Page</summary>
<br>

![Home Page](/media/main_page_visitor.jpg)

<ul>
    <h3>NavBar -</h3>
    <ul>
        <li>As a first time visitor the nav bar is going to let users navigate to the 'Explore' page, 'Register' and a 'Login' page if they already have an account</li>
        <li>On the hero image and its text, and lower on the home page there are going to be two buttons which will let users register</li>
    </ul>
    <h3>Title</h3>
    <ul>
        <li>Title is LARGE and stands out, users instantly get an idea what the website is about</li>
    </ul>
    <h3>Content</h3>
    <ul>
        <li>The content in this page explains to users breifly what this site is about, and tries to incentivise users to sign up</li>
    </ul>
    <ul>
        <li></li>
    </ul>
    <ul>
        <li></li>
    </ul>
    <ul>
        <li></li>
    </ul>
</ul>
</details>
<hr>
<details>
<summary>Explore Page</summary>
<br>

![Explore Page](/media/explore_page.jpg)
<ul>
    <li>When users click on the 'Explore' link on the nav bar it will redirect them to explore page which will contain a list of drinks they can view</li>
    <li>The posts will contain the name of the drink, the main spirit that is used, who and when it was made and the number of likes it contains</li>
    <li>The more likes the more popular the drinks, this can help users decided which drinks to view because of its popularity</li>
    <li>Which ever image was uploaded by admin/user will be on the post, if there is no image then a placeholder image will be substituted.
    </li>

![Placeholder image](/media/bug_4.jpg)
</ul>
</details>
<hr>

<details>
<summary>Register Page</summary>
<br>

![Register Page](/media/register_page.jpg)
<ul>
    <li>When a user wants to register the will be taken to this register page, it will ask them to create a username, password and email(but that is not needed)</li>
    <li>This is need for the authentication so that users will be able to like, comment, add posts, edit and delete posts</li>
</ul>
</details>
<hr>

<details>
<summary>Login Page</summary>
<br>

![Login Page](/media/logging_in.jpg)
<ul>
    <li>Similar to the register page, but on this page we only require the users username and password</li>
    <li>Users can also be redirected to the register page from the login page</li>
</ul>
</details>
<hr>

<details>
<summary>Add Drinks Page</summary>
<br>

![Add Drinks Page](/media/adding_drink_form.jpg)
<ul>
    <li>The drink form will require a Title, Spirit, Ingredients, Instructions, an Image if possible and Publish open for the post to be uploaded</li>
    <li>If users fail to fill all required fields it will not let them post anything</li>
    <li>Publish button only works, drafts will cause the website to break as no URL or views was set for it</li>
    <li>After users succesfully post a drink it will redirect them to the explore page where they can view their drink!</li>
</ul>
</details>
<hr>

<details>
<summary>Favourites Page</summary>
<br>

![Favourites Page](/media/favourites.jpg)
<ul>
    <li>This page will be new for users if have JUST signed up, in order to have content here users will need to explore and like posts in order for posts to be stored here</li>
    <li>As you can see on the hearts it will only save the post when users have liked the drink post</li>
</ul>
</details>
<hr>

<details>
<summary>Logout Page</summary>
<br>

![Logout Page](/media/sign_out.jpg)
<ul>
    <li>After users have had their fun they can click on the 'Sign out' on the navbar and be redirected to the sign out page where it will ask them again and if they confirm, it will successfully sign them out.
    </li>
</ul>
</details>
<hr>

<details>
<summary>Admin Page</summary>
<br>

<ul>
    <li>Login in page for admin</li>

![Admin login page](/media/admin_login.jpg)
    <li>Administration panel</li>
![Administration page where you can check on posts and comments](/media/admin_administration_page.jpg)
    <li>Post panel, where admin can see all posts on webpage</li>

![View all posts in admin panel](/media/admin_view_posts.jpg)
    <li>Admin selects 'Add Post' and they then get redirected to the add post page where they need to fill in all the fields like in the user form to create a post</li>
![Adding post form](/media/admin_add_post.jpg)
    <li>View comments on admin panel</li>

![View all comments possted on website to be approved](/media/admin_comment_view.jpg)
    <li>Comments need to be approved by admin in order to be on the website</li>

![Overview of all requested comments](/media/admin_add_comments.jpg)

</ul>

</details>

<h2>Responsiveness</h2>

<hr>

<h2>Mobile Screen</h2>

<h3>Home</h3>

![Home](/media/mobile_view.jpg)

<h3>Explore</h3>

![Explore](/media/mobile_view_explore.jpg)

<h3>Register</h3>

![Register](/media/mobile_view_register.jpg)

<h3>Sign in</h3>

![Sign in](/media/mobiel_view_sign_in.jpg)

<h3>Logged in Nav</h3>

![Logged in Navbar](/media/mobile_view_navbar_loggedin.jpg)

<h3>Add drink</h3>

![Add drink](/media/mobile_view_add_drink.jpg)

<h3>Favourite</h3>

![Favourite](/media/mobile_view_favourite.jpg)

<h3>Sign out</h3>

![Sign out](/media/mobile_view_sign_out.jpg)


<h2>Features</h2>

<ul><h3>Home Page Feature</h3>
    <li>When a user creates and account and is logged on the register buttons and nav bar are update
    </li>
    <li>Register buttons will dissapear and on the nav bar the will get options to add drinks, check out their favourite drinks and be able to sign out</li>

![Home page updated when logged in](/media/main_page_logged_feature.jpg)

![Logged in nav bar](/media/logged_navbar_feature.jpg)
</ul>

<ul><h3>Creating posts</h3>
    <li>When users have created an account and are logged on the can start adding drinks onto the website</li>
    <li>On the post form users will need to fill all fields on order to be able to post</li>

![Fields with content](/media/form_complete_fields.jpg)
![Add drinks page](/media/adding_drink_form.jpg)
<li>After users have added the drinks it will update and appear on the explore page</li>

![Batanga drink on page](/media/successful_post_user.jpg)
</ul>

<ul><h3>Edit and delete</h3>
    <li>When users are logged on they will be able to edit ONLY posts that THEY have created
    </li>
    <li>When the click on a post to see the post detail and 'Edit' will appear at the bottom</li>
    <li>When they select the edit button the will be taken to the edit page where they can change their post and select update</li>
    <li>If a user selects the delete button they will be taken to the delete page where they will need to CONFIRM that they want to delete their post</li>

![Edit button when logged on](/media/author_view_edit.jpg)
![Edit post view](/media/edit_post_update_delete.jpg)
![Delete](/media/delete_post_page.jpg)

<p>The Batanga drinks has been removed from the 'Explore' page</p>

![Delete works](/media/delete_works.jpg)
</ul>

<ul><h3>Like and Comment</h3>
    <li>Users that have created an account will be able to like and comment on all posts</li>
    <li>To like a post the user just needs to click on the heart and the heart will turn black, and this post will then be stored in the favourties section of the users page</li>
    <li>A comment form will also be there under the post so users can leave a comment, when uses post a comment a message will appear saying that they comment needs to be approved by the admin</li>

![Users can like and a comment form](/media/like_and_comment_logged_in.jpg)
![Comment waiting to be approved, post also liked](/media/user_commented_waiting_approval.jpg)
![Commented approved](/media/comment_approved_posted.jpg)
</ul>



<h2>Wireframes</h2>
Desktop Wireframes

![Desktop Home Page](/media/wireframe_home_desktop.jpg)
<br>

![Desktop Post detail page](/media/wireframe_post_desktop.jpg)
<br>

![Desktop Sign in/out](/media/wireframe_sign_desktop.jpg)
<br>

![Desktop Favourites page](/media/wireframe_favourites_desktop.jpg)
<br>

![Desktop Register Page](/media/wireframe_register_desktop.jpg)

Mobile Wireframes

![Mobile Home Page](/media/wireframe_home_mobile.jpg)
<br>

![Mobile Post detail Page](/media/wireframe_post_mobile.jpg)
<br>

![Mobile Sign in/out Page](/media/wireframe_signinout_mobile.jpg)
<br>

![Mobile Favourites page](/media/wireframe_favourites_mobile.jpg)
<br>

![Mobile register page](/media/wireframe_register_mobile.jpg)

<h1>Data Model</h1>

![Entity Relationship Diagram for Project](media/ERD_for_PP4.jpeg)

<p>The User Model - Django default User Model. We will use user (PK), Email and Password.</p>
<p>The Drinks Model - This will be our main model and we are going to use this to create posts, get post id, autor id to be able to select, edit and delete the correct posts.
The post model contains the title, spirit, slug, author, feature_image, updated_on, created_on, ingredients, instructions, status and likes</p>
<p>The Post Model - The post model is derived from the drinks model, when we create our forms we will be using the post model for this</p>
<p>The Comment Model - The comment model will contain the post, name, email, body, created_on, approved</p>
<p>The Categories Model - we were suppose to use this in order to retrieve the spirit id to return a certain group of drinks but ran out of time and was not able to implement this, will be a future idea</p>
Favourites Model - Contains post.id, user, likes, image

<h3>Relationships</h3>
<p>User and Post model is a one to many relationship</p>
<p>User and favourties model is a one to many relationship between eachother</p>
<p>post andcomments model is a one to many relationships</p>
<p>Like model had a many to many field</p>

<h2>Colours</h2>

<h2>Typegraphy</h2>
<ul>
    <li>Fonts used for this website:
    <ul>
    <li>Montserrat</li>
    <li>Aboreto is going to be used for title and smaller heading, Helvetica as secondary font</li>
    <li>Montserrat for details and other descriptions, Arial as secondary font</li>
    <li>Roboto Slab - Spirit Names - Rum, Vodka, Gin, Sans Serif as secondary font</li>
    </ul>
    </li>
</ul>

<h2>Colors</h2>
<p>So the type of style I was going for was a premium looking website, so I kept it sharp and simple, black and white.</p>
<p>I used red for some of the buttons when hovered over and on the social links</p>
<p>For the post detail eveything was white and overwhelming so I decided to wrap the instructions div in a rgb(247, 242, 242) </p>

![Description box color rgb(247, 242, 242)](/media/description_box_color.jpg)

<h2>Font Awesome Icons</h2>
<p>Only used a few icons in this project, did not want to overwhelm users with icons all over the page, and it kept it simpe to retrieve when appending its values</p>
<p>A Martini glass icon is used on the websites title</p>

![Martini glass next to the websites title](/media/font_awesome_icon_2.jpg)
<p>The next icons are the like and comment icons, the heart fills up when a valid user likes it, next to the icons there will just be there the number of likes and comments on the post</p>

![Like and comment icons](/media/font_awesome_icon_1.jpg)

<h2>Future Features/Ideas</h2>
<ul>
<li>Let users be able to have a drafts section, so that if they have an unfinished post they can finis making it later</li>
<li>Add virgin drinks, so that our target audience can expand so that everyone can gain benefits from this page</li>
<li>Add a category filter that filters out through spirit name, if a user wants to view drinks ONLY made by rum they can filter out the drinks and only drinks made with rum will appear on the site</li>
<li>Favicon, wish I got find the piece to the puzzle but ran of out time and I was not able to implement this feature</li>
</ul>


<h2>Languages</h2>
<ul>
    <p>Python</p>
    <p>HTML</p>
    <p>CSS</p>
    <p>Javascript</p>
</ul>

<h2>Technologies</h2>
<ul>
    <p>Django</p>
    <p>Github</p>
    <p>Gitpod</p>
    <p>Heroku</p>
    <p>Stack Overflow</p>
    <p>Balsamiq</p>
    <p>Pep8</p>
    <p>Cloudinary</p>
    <p>PostgrelSQL</p>
    <p>Bootstrap</p>
</ul>

<h2>Testing, bugs and fixed</h2>
<ul>
    <li>Testing
    <ul>
    <li>Pep8 screenshots code</li>
<p>Admin code</p>

![Pep8 report for blog admin page](/media/pep8_admin.jpg)
<p>Admin URLs code</p>

![Pep8 report for for blog urls](/media/pep8_admin_urls.jpg)
<p>Apps code</p>

![Pep8 report for blog apps](/media/pep8_apps.jpg)
<p>Forms code</p>

![Pep8 report for blog forms](/media/pep8_forms.jpg)
<p>manage.py code</p>

![Pep8 report for blog manage.py](/media/pep8_manage.py.jpg)
<p>Models code</p>

![Pep8 report for blog models](/media/pep8_models.jpg)
<p>Settings code - Warnings are because of the lines being too long, if I tried to indent this lines then it cause the website to break, so I am aware of these warnings and have left them so that the website does not break</p>

![Pep8 report for settings](/media/pep8_settings.jpg)
<p>Test code</p>

![Pep8 report for tests](/media/pep8_tests.jpg)
<p>URLs code</p>

![Pep8 report for blog url](/media/pep8_urls.jpg)
<p>Views code</p>

![Pep8 report for blog views](/media/pep8_views.jpg)
    </ul>
    </li>
</ul>

<p>HTML validator - Only ONE warning which was because I wrapped the title of the website in a h1 tag, this was not recommended but when I tried wrapping this in anything else the title was too small and did not stand out, so I kept it as it is. Apart from that, no warnings or errors</p>

![Validator for HTML](/media/html_validator.jpg)

<p>CSS validator - One error and 6 warnings</p>

![CSS validator Error](/media/css_validator_1.jpg)
![CSS validator warnings](/media/css_validator_2.jpg)

<p>CSS validator passing after problems solved</p>
 
![CSS validator passing](/media/css_validator_pass.jpg)
<h3>Manuel testing</h3>
<p>Manuel testing was done for this project, most of them are on the feature but I will explain here what I tested</p>
<p>On the home page there is the nav bar and register buttons on the content of the page, I have gone through each link to make sure they are wired up. You can see this with all the screenshots I got above</p>
<p>A feature I want to show that I tested is the user authentication, when the user is new or is not logged in options to register will appear, but when users have logged on then they will get the extra pages 'Add drinks' and 'Favourites' and instead of 'Login' they will have 'Logout'</p>
<p>A message will appear confirming users that they have logged in successfully</p>

![Main page for logged off user/ new user](/media/main_page_visitor.jpg)
![Main page for registered user](/media/main_page_logged.jpg)

<h3>Explore page</h3>
<p>Tested the explore page, to see that posts will appear for users to view, posts do not have any broken images and if they do the placeholder image will appear.</p>
<p>From here users are able to select a post and view the posts detail, ingredients and instructions on how to prep the drink</p>
<p>Likes and comments at the bottom, registered users can like and leave comments, unregistered users cannot</p>

![](/media/explore_page.jpg)
![](/media/post_detail.jpg)

<p>A user that is viewing their own post will have an 'Edit' button appear for them which will redirect them to an edit page where they can update or delete their posts</p>


![Edit button on post](/media/author_view_edit.jpg)
![Edit page, containes update and delete button](/media/edit_post_update_delete.jpg)

<h3>Registering, Logging in and out</h3>
<p>When logging in users will need to put the username and password they registered with</p>
<p>To show this works a message will appear informing the users that they have successfully logged on</p>

![Log in form](/media/logging_in.jpg)
![Successful login with message](/media/main_page_logged.jpg)

<p>Same when users log out, will be taken to the signout form to confirm the want to log out, and a message will appear when this i successful, features to like, comment, add drinks and view favourties will get revoked</p>

![Sign out form](/media/sign_out.jpg)
![Sign out successful](/media/signout_message.jpg)

<p>Registering user works as I created the user1 user from the register form</p>

![Register form](/media/user_register.jpg)

<h3>Solved Bugs</h3>
<p>The first bug I noticed was with the hero image, on my small screen it looked fine, but when I was going through it with my mentor the image stopped half way. After playing with the css and not using the bootstrap class img-fluid the problem was solved</p>

![Hero Image takes up half the page](/media/bug_2.jpg)
![Hero Image fills up screen](/media/bu_2_solved.jpg)

<p>Bug 2 - In this bug the images that I added pushed all the way down, causing the footer to float front of all the elements, this is not appealing to users. I styled the footer to always be at the bottom of the screen and be pushed down by the body</p>

![Image stretching all the way to the bottom, making the footer appear as if it floating](/media/bug_3.jpg)
![Footer pushed all the way down](/media/bug_3_solved.jpg)

![Code that solved footer float bug](/media/bug_3_code_solved.jpg)
<p>Bug is solved, users image will now be posted rather than the placeholder image</p>

![Placeholder image](/media/bug_4.jpg)
![Placeholder image solved](/media/placeholder_image.jpg)

<p>The last bug that I found was the footer wrapping around the div, and leaving a blank space at the bottom. Styled it so footer is at the bottom now</p>

![Footer leaving blank space beneath it](/media/bug_5.jpg)
![Footer at bottom of page now as it should be](/media/bug_5_solved.jpg)
![](/media/bug_5_solution.jpg)


<h3>Unsolved Bugs</h3> <p>- Bug appeared when I was trying to edit from the admin page and it was asking me for an email, the email is not required, I used some@email.com as a placeholder and it passed</p>

![Admin edit post REQUIRES email](/media/bug_6_unsolved.jpg)

<p>In this bug I cannot find out what the problem, the font is not consistent for each post, on some posts it is the Montserrat font family but for other posts it is just the Helvetica font</p>

![Font using font family Montserrat](/media/bug_2_unsolved.jpg)
![Post with Helvetica font](/media/bug_2_unsolved_font.jpg)

<h3>Issue</h3>
<p>An incomplete issue I currently have is the draft option, when users select draft it will send it to the admin, where the admin can publish it or just leave it. A feature I would like to add is have a drafts page where the drafts will be posted to this page, where users can view their drafts, and continue editing it or delete the post </p>

![Admin receiving drafts](/media/draft_issue.jpg)

<h2>Deployment</h2>

<p>To deploy the project to heroku we first have to set 'DEBUG = False' rather than 'True'</p>

<p>And we have to add 'X_FRAME_OPTIONS = "SAMEORIGIN'" Under the debug</p>
<ul>
    <li>We will than go to the Herokuapp and go to settings and select 'Reveal Config Vars'</li>
    <li>Remove 'DISABLE_COLLECTSTATIC' from the config vars</li>
    <li>Go on 'Delpoy', scroll down and select 'Deploy Branch'</li>
</ul>

<h2>Credits</h2>
<ul>
    <li>Credits to code institutes I think therefore I blog videos, was a perfect walkthrough video to be able to get the base implemented and understanding of the project</li>
    <li>To my mentor Narender for helping me and giving me amazing advice, when creating the delete view I was not able to link up the URLs, he gave me the solution and allowed me to complete the project</li>
    <li>Stackover flow for all the advice on models, forms</li>
    <li>Documentation on the django website where I learnt more about forms, CreateView, UpdateView and Delete View. Also plenty of documentation on linking views and URLs.</li>
    <li>Finally credits to slack, I could not have done this without looking at everyones advice there, knowing that everyone got the same issues really helped me believe I was not alone struggling with this project. Plenty of documenation and explanations</li>
</ul>

<h2>Self acknowledgement</h2>
<p>I am impressed at myself for actually getting this far, I managed to create a website that incorporates the basic CRUD functionality but I could have done better</p>
<p>Unfortunatly I ran out of time and was not able to create a more detailed README file as I could if I had more time. I managed to get the bare minimum but I feel like I could have done more deep testing and added more detail to screenshots giving a more detailed explanantion</p>
<p>My goal is to be able to write a well reported README document and manage my time better</p>