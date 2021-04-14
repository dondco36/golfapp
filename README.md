# Golf Stats App
Conor Dondale 12APR2021

## Project Overview
This is an app for goflers that would like to keep track of their statistics from each of their rounds.

### Features  

* Statistic of the Day
* User Profile
* Round/Statistic Search
* Add Round Statistics with notes

Additional Features:
* GOAL Setting
* Statistics Comparisons
* Graphical Output
* Create Group
* Join Group

Trackable statistics include, but are not limited to:    
* Score (Hole-by-Hole and/or Total)
* Fairway in Regulation (FIR)
* Green in Regulation (GIR)
* Putts
* Up and Down
* Sand Saves
* More statistics to come

### User Stories
"As a User, I want to see my statistics on the landing page."    

"As a User, I want be able to login and enter the **Date** and **Course** to view individual round statistics."    

"As a User, I want have the option to get a **Graphical Printout** of my stats as well as the percentages of each."    

"As a User, I want to be able to see **Comparisons** to see where my stats are compared to where my Goals are."    

"As a User, I want to be able to enter different **GOALS** to work on and refer to while practicing."  

### Functionality
* User create account or login
* Basic statistics on the homepage
​
* User Permissions:
    - Search for their rounds
    - Add statistics
    - Highlight GOALS
    - Post-Round notes
    
**Possible Features:**
* User Created Groups
    - Group Owner permissions:
        - Manage rounds, comments, and images
        - Manage moderators
​
    - Group Moderator permissions:
        - Manage rounds, comments, and images

### Models
​
* Rounds:
    - Score (Hole-by-Hole and/or Total)
    - Fairway in Regulation (FIR)
    - Green in Regulation (GIR)
    - Putts
    - Up and Down
    - Sand Saves
    - More statistics to come
​
* User Profile:
    - Name
    - Image
    - Favorite course
    - Best Round
    - Favorite Brand
​
**Additional Models:**
* Groups:
    - Name
    - Owner
    - Members


### Versions in Order

*Version 1*
* Create Django APP with REST Framework, API.
* Initial Database entry.
* User Profiles.

*Version 2*
* Landing Page.
* Login/Out Page.
* User Profiles with Statistics layout.

*Version 3*
* GOALS can be added to keep track of.
* The User will be able to see a **Graphical Representaion** of their statistics
* **Comparison Statistics** will be added as an option to for the User to compare against where they should be in accordance with their

*Version 4*
* Groups for Users
* Round and Statistic comparisons

*Version 5*
* Group competitions and MatchPlay Format tracker