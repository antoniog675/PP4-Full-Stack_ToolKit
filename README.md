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

<h2>Colours</h2>

<h2>Typegraphy</h2>
<p>fonts</p>
<p>font awesome icons</p>

<h2>Features</h2>
<p>index page gives a small intro to webpage, eye catching when users first land on it, register and sign in button for users that need to log in or need to register and account</p>
<p>Dissapears when users log in</p>
<p>explore page contains a list of all the drinks that have been posted, with the name of the drink, spirit, author name and when it was displayed, likes and comments</p>
<p>register page</p>
<p>login page</p>
<p>logout page</p>
<p>favourites page</p>

<h2>Languages</h2>
<p>Python</p>
<p>HTML</p>
<p>CSS</p>
<p>Javascript</p>

<h2>Technologies</h2>
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

<h2>Testing, bugs and fixed</h2>
<p>Testing</p>
<p>pep8 all files</p>
<p>HTML validator</p>
<p>CSS validator</p>
<h3>Manuel testing</h3>

<p>Solved Bugs</p>
<p>Unsolved Bugs</p>


<h2>Deployment</h2>

<h3>Creating the enviroment</h3>
<p>To deploy the project to heroku we first have to set 'DEBUG = False' rather than 'True'</p>

<p>And we have to add 'X_FRAME_OPTIONS = "SAMEORIGIN'" Under the debug</p>
<ul>
    <li>We will than go to the Herokuapp and go to settings and select 'Reveal Config Vars'</li>
    <li>Remove 'DISABLE_COLLECTSTATIC' from the config vars</li>
    <li>Go on 'Delpoy', scroll down and select 'Deploy Branch'</li>
</ul>

<h2>Credits</h2>

<p>Future features, drafts, virgin cocktails, category</p>